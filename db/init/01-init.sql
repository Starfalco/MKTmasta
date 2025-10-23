-- Runs as superuser (airflow) on container init
CREATE USER users WITH PASSWORD 'users';
CREATE DATABASE users OWNER users;

\connect users
ALTER SCHEMA public OWNER TO users;
GRANT USAGE, CREATE ON SCHEMA public TO users;

-- Default privileges for FUTURE objects created in public
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO users;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO users;

CREATE EXTENSION IF NOT EXISTS pgcrypto;
SET ROLE users;

CREATE TABLE IF NOT EXISTS users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_name TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);