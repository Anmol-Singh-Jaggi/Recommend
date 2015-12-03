MATCH (u1:User {userID:?1})
RETURN COUNT(u1) <> 0
;