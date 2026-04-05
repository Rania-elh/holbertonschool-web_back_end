-- Prefix index on first character of name (speeds up LIKE 'x%' patterns)
CREATE INDEX idx_name_first ON names (name(1));
