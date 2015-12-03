MATCH (m1:Movie)
RETURN m1.movieID AS `Movie ID`, m1.name AS `Movie Name`
ORDER BY m1.movieID ASC
;