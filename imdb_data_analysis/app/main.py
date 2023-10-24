import duckdb
import os
import streamlit as st

from data_model import DataModel

queries_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'queries')
db_fp = os.path.join(queries_dir, 'imdb.db')
db_connection = duckdb.connect(db_fp)

top_movies = DataModel() \
    .get_source_tables(db_connection, queries_dir) \
    .get_top_movies(db_connection, queries_dir)


st.write(top_movies)
