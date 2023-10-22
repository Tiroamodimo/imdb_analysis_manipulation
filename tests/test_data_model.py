import duckdb
import os
import unittest

import data_model

db_fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.db')


class TestDataModel(unittest.TestCase):

    def setUp(self) -> None:
        self.data_model = data_model.DataModel()
        self.db_connection = duckdb.connect("test.db")

    def tearDown(self) -> None:
        self.db_connection.close()
        os.remove("test.db")

    def test_given_valid_file_path_when_passed_to_get_query_return_expected_string(self):
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

    def test_given_invalid_file_path_when_passed_to_get_query_return_empty_string(self):
        # arrange
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_resources', 'fake_file.sql')
        assert not os.path.exists(file_path)

        expected_result = ''

        # act
        result = self.data_model._get_query(file_path)

        # assert
        self.assertEqual(expected_result, result)

    def test_given_valid_db_connection_when_passed_to_get_source_tables_return_expected_tables(self):
        # arrange
        expected_result = [('title_basics',), ('title_ratings',)]

        # act
        self.data_model.get_source_tables(self.db_connection)
        result = self.db_connection.execute("""
        SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE'
        """).fetchall()

        # assert
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
