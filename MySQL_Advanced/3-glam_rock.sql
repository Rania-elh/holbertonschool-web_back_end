SELECT
    band_name,
    IF(split IS NULL OR split = 0, 2024, LEAST(split, 2024)) - formed AS lifespan
FROM metal_bands
WHERE TRIM(style) = 'Glam rock'
ORDER BY lifespan DESC, band_name ASC;
