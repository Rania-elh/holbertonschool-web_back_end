-- Total fans per country (sum of per-band fan counts), ranked descending
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
