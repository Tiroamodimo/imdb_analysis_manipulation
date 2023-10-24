import duckdb
import os
import unittest

from imdb_data_analysis.app import data_model


class TestDataModel(unittest.TestCase):

    def setUp(self) -> None:
        self.queries_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_resources',
                                        'test_case_queries')
        self.data_dir = os.path.join(os.path.join(self.queries_dir, 'imdb_sample_data'))
        self.db_fp = os.path.join(self.data_dir, 'test.db')

        self.data_model = data_model.DataModel()
        self.db_connection = duckdb.connect(self.db_fp)

    def tearDown(self) -> None:
        self.db_connection.close()
        os.remove(self.db_fp)

    def test_given_valid_file_path_when_passed_to_get_query_then_return_expected_string(self):
        # arrange
        file_path_1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_resources',
                                   'test_query_1.sql')
        file_path_2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_resources',
                                   'test_query_2.sql')
        assert all([os.path.exists(file_path_1), os.path.exists(file_path_2)])

        expected_result_1 = 'select * from NON_EXISTING_TABLE;'
        expected_result_2 = 'insert into NOTHING.NON_EXISTING_TABLE select * from NON_EXISTING_TABLE;'

        # act
        result_1 = self.data_model._get_query(file_path_1)
        result_2 = self.data_model._get_query(file_path_2)

        # assert
        self.assertEqual(expected_result_1, result_1)
        self.assertEqual(expected_result_2, result_2)

    def test_given_invalid_file_path_when_passed_to_get_query_then_return_empty_string(self):
        # arrange
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_resources', 'fake_file.sql')
        assert not os.path.exists(file_path)

        expected_result = ''

        # act
        result = self.data_model._get_query(file_path)

        # assert
        self.assertEqual(expected_result, result)

    def test_given_valid_db_connection_when_passed_to_get_source_tables_then_return_expected_tables(self):
        # arrange
        expected_result = [('title_basics',), ('title_ratings',)]

        # act
        self.data_model.get_source_tables(self.db_connection, self.queries_dir)
        result = self.db_connection.execute("""
        SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE'
        """).fetchall()

        # assert
        self.assertEqual(expected_result, result)

    def test_given_valid_db_and_db_connection_when_passed_to_get_top_movies_then_return_expected_result(self):
        # arrange
        expected_columns = ['primaryTitle', 'numVotes', 'averageRating', 'ranking']
        expected_row_count = 15

        os.chdir(self.data_dir)
        self.db_connection.execute("""
        CREATE OR REPLACE TABLE title_basics AS
        SELECT tconst, primaryTitle
        FROM read_csv('title.basics.tsv.gz', delim='\t', header=true, nullstr='\\N', quote='',
        columns={'tconst': 'VARCHAR', 'titleType': 'VARCHAR', 'primaryTitle': 'VARCHAR', 'originalTitle': 'VARCHAR', 'isAdult': 'VARCHAR', 'startYear': 'VARCHAR', 'endYear': 'INTEGER', 'runtimeMinutes': 'VARCHAR', 'genres': 'VARCHAR'},
        ignore_errors=true, parallel=false);    
        """)
        self.db_connection.execute("""
        CREATE OR REPLACE TABLE title_ratings AS
        SELECT *
        FROM read_csv('title.ratings.tsv.gz', delim='\t', header=true, nullstr='\\N', quote='',
        columns={'tconst': 'VARCHAR', 'averageRating': 'REAL', 'numVotes': 'INTEGER'}, ignore_errors=true, parallel=false);
        """)

        # act
        result = self.data_model.get_top_movies(self.db_connection, self.queries_dir)

        result_columns = list(result.columns)
        result_row_count = len(result)

        # assert
        self.assertEqual(expected_columns, result_columns)
        self.assertEqual(expected_row_count, result_row_count)


if __name__ == '__main__':
    unittest.main()
