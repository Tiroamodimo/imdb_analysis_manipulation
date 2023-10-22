-- Load title ratings table
CREATE OR REPLACE TABLE title_ratings AS
SELECT * -- optimize
FROM read_csv('https://datasets.imdbws.com/title.ratings.tsv.gz', delim='\t', header=true, nullstr='\\N', quote='',
columns={'tconst': 'VARCHAR', 'averageRating': 'REAL', 'numVotes': 'INTEGER'}, ignore_errors=true);

-- Load title basics table
CREATE OR REPLACE TABLE title_basics AS
SELECT * -- optimize
FROM read_csv('https://datasets.imdbws.com/title.basics.tsv.gz', delim='\t', header=true, nullstr='\\N', quote='',
columns={'tconst': 'VARCHAR', 'titleType': 'VARCHAR', 'primaryTitle': 'VARCHAR', 'originalTitle': 'VARCHAR', 'isAdult': 'INTEGER', 'startYear': 'INTEGER', 'endYear': 'INTEGER', 'runtimeMinutes': 'INTEGER', 'genres': 'VARCHAR'}, ignore_errors=true);

