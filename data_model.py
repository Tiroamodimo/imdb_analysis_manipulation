import os


class DataModel:
    def __init__(self):
        pass

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

    def get_tables(self, db_connection):
        pass
