-- Recompute and persist a user's average correction score
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users u
    SET u.average_score = IFNULL((
        SELECT AVG(c.score)
        FROM corrections c
        WHERE c.user_id = u.id
    ), 0)
    WHERE u.id = user_id;
END$$

DELIMITER ;
