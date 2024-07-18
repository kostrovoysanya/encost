-- SQLite
SELECT endpoints.id, endpoints.name, endpoint_reasons.reason_hierarchy, COUNT(endpoint_reasons.id) AS power_outage_count
FROM endpoints
JOIN endpoint_reasons ON endpoints.id = endpoint_reasons.endpoint_id
WHERE endpoints.active = 'true' AND endpoint_reasons.reason_name = 'Перебои напряжения'
GROUP BY endpoints.id, endpoints.name, endpoint_reasons.reason_hierarchy;


