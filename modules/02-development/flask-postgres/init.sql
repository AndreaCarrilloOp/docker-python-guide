-- Optional sample data; run after the application creates the tasks table.
INSERT INTO tasks (title, description, completed, created_at) VALUES
('Learn Docker Compose', 'Explore service networking', false, CURRENT_TIMESTAMP),
('Implement CRUD API', 'Practice REST endpoints', false, CURRENT_TIMESTAMP);
