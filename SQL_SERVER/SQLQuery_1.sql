SELECT DISTINCT P.Description as Product
FROM tProduct as P
WHERE P.Description is not NULL and P.Description <> ''
Order By P.Description ASC