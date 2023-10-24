WITH avg_votes AS (
    SELECT AVG(numVotes) AS average_votes
    FROM title_ratings
),
votes_ratings AS (
    SELECT tb.primaryTitle, tr.averageRating, tr.numVotes,
           (tr.numVotes / avg_votes.average_votes) * tr.averageRating AS ranking
    FROM title_ratings tr
    JOIN title_basics tb ON tr.tconst = tb.tconst 
    CROSS JOIN avg_votes
    WHERE tr.numVotes >= 100 
)
SELECT primaryTitle, numVotes, averageRating, ranking
FROM votes_ratings
ORDER BY ranking DESC
LIMIT 15;