MATCH (m1:Movie {movieID:?1})
RETURN COUNT(m1) <> 0
;