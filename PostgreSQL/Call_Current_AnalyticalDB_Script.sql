SELECT table_name, current_database()
FROM information_schema.tables
WHERE table_schema = 'public';


