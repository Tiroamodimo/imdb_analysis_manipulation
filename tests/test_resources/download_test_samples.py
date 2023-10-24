import os
from os import path as os_path
from shutil import rmtree

test_resources_dir = os_path.dirname(os_path.abspath(__file__))
sample_data_dir = os_path.join(test_resources_dir, 'test_case_queries/imdb_sample_data')

LINKS_TO_TEST_DATA = [
    ('https://datasets.imdbws.com/title.basics.tsv.gz', os_path.join(sample_data_dir, 'title.basics.tsv.gz')),
    ('https://datasets.imdbws.com/title.ratings.tsv.gz', os_path.join(sample_data_dir, 'title.ratings.tsv.gz'))
]


def main():
    if os_path.exists(sample_data_dir):
        rmtree(sample_data_dir)
    os.mkdir(sample_data_dir)

    for link, file_path in LINKS_TO_TEST_DATA:
        os.system(f'wget {link} -O {file_path}')


if __name__ == '__main__':
    main()
