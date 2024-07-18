-- SQLite
SELECT endpoint_reasons.*
FROM endpoint_reasons
JOIN endpoints ON endpoint_reasons.endpoint_id = endpoints.id
WHERE endpoints.active = 'true';