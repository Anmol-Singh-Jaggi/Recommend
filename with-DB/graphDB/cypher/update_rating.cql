MATCH (u1:User {userID:?1}), (m1:Movie {movieID:?2})
MERGE (u1)-[r1:RATED]-(m1)
SET r1.rating=?3
;