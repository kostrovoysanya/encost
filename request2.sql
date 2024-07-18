-- SQLite
SELECT endpoints.id, endpoints.name, COUNT(endpoint_reasons.id) AS downtime_reasons_count
FROM endpoints
LEFT JOIN endpoint_reasons ON endpoints.id = endpoint_reasons.endpoint_id
WHERE endpoints.active = 'false'
GROUP BY endpoints.id, endpoints.name;