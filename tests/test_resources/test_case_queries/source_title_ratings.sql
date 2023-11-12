CREATE OR REPLACE TABLE title_ratings AS
SELECT *
FROM read_csv('title.ratings.tsv.gz', delim='\t', header=true, nullstr='\\N', quote='',
columns={'tconst': 'VARCHAR', 'averageRating': 'REAL', 'numVotes': 'INTEGER'}, ignore_errors=true, parallel=false);
