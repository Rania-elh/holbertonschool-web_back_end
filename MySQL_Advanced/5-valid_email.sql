-- Reset valid_email when the email address is updated to a new value
DELIMITER $$

CREATE TRIGGER reset_valid_email_on_email_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
