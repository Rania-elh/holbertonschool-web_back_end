-- Glam rock bands ranked by longevity (years) up to 2024
SELECT
    band_name,
    IFNULL(NULLIF(`split`, 0), 2024) - formed AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
