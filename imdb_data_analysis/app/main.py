import duckdb
import os
import streamlit as st

from data_model import DataModel

db_fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'imdb.db')
db_connection = duckdb.connect(db_fp)

top_movies = DataModel() \
    .get_source_tables(db_connection) \
    .get_top_movies(db_connection, )

st.write(top_movies)
