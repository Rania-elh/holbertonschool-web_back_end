-- Composite index: first character of name + full score
CREATE INDEX idx_name_first_score ON names (name(1), score);
