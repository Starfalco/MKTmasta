-- Runs as superuser (airflow) on container init
CREATE USER users WITH PASSWORD 'users';            -- Create app role
CREATE DATABASE users OWNER users;                  -- Create app DB owned by that role

\connect users                                      -- Switch to the app DB
ALTER SCHEMA public OWNER TO users;                 -- Make 'users' own the public schema
GRANT USAGE, CREATE ON SCHEMA public TO users;      -- Allow object creation in public

-- Default privileges for FUTURE objects created in public
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO users;    -- future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO users; -- future sequences


-- create table under 'users' ownership A TESTEEEEEEEEEER
CREATE EXTENSION IF NOT EXISTS pgcrypto;
SET ROLE users;

CREATE TABLE IF NOT EXISTS users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);