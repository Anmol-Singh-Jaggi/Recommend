MATCH (m1:Movie {movieID:'?1'})
RETURN count(m1);
