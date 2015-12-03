MATCH (u1:User {userID:?1})-[r1:RATED]->(m1:Movie)
RETURN m1.movieID AS `Movie ID`, m1.name AS `Movie Name`, r1.rating AS `Rating`
ORDER BY m1.movieID ASC
;