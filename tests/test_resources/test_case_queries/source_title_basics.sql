CREATE OR REPLACE TABLE title_basics AS
SELECT tconst, primaryTitle
FROM read_csv('title.basics.tsv.gz', delim='\t', header=true, nullstr='\\N', quote='',
columns={'tconst': 'VARCHAR', 'titleType': 'VARCHAR', 'primaryTitle': 'VARCHAR', 'originalTitle': 'VARCHAR', 'isAdult': 'INTEGER', 'startYear': 'INTEGER', 'endYear': 'INTEGER', 'runtimeMinutes': 'INTEGER', 'genres': 'VARCHAR'},
ignore_errors=true, parallel=false);
