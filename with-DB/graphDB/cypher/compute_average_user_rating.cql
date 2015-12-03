MATCH (u:User {userID:?1})-[r:RATED]->(m:Movie)
WITH u, COUNT(r) as rating_count, SUM(r.rating) as rating_sum
SET u.avg_rating = rating_sum/(rating_count*1.0)
// RETURN u, rating_sum, rating_count, u.avg_rating ORDER BY u.userID ASC
;