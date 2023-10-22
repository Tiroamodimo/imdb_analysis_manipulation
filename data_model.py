import logging
import os

import duckdb.duckdb


class DataModel:
    def __init__(self):
        self.queries_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'queries')

    @staticmethod
    def _get_query(file_path) -> str:
        try:
            with open(file_path, 'r') as file:
                query = file.read().replace('\n', ' ').strip()

        # if the file does not exist, return empty string
        except FileNotFoundError:
            message = 'The query file does not exist. Please check existing queries in the queries folder and pass the correct file name.'
            print(message)
            return ''
        else:
            return query

    def get_source_tables(self, db_connection):

        load_extensions_query = self._get_query(os.path.join(self.queries_dir, 'load_db_extensions.sql'))
        source_title_basics = self._get_query(os.path.join(self.queries_dir, 'source_title_basics.sql'))
        source_title_ratings = self._get_query(os.path.join(self.queries_dir, 'source_title_ratings.sql'))

        try:
            # ensure that the queries are not empty
            assert all([load_extensions_query != '', source_title_basics != '', source_title_ratings != ''])

            # run the queries
            db_connection.execute(load_extensions_query)
            db_connection.execute(source_title_basics)
            db_connection.execute(source_title_ratings)

        # if loading queries fails
        except AssertionError:
            message = 'The query file is empty / does not exist. Please check existing queries in the queries folder and pass the correct file name.'
            logging.exception(message)

        # executing the queries fails
        except duckdb.duckdb.DuckDBError as err:
            logging.exception(err)
