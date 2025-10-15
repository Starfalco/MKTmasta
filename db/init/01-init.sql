-- Create a regular database role (login) named 'users' with its password.
CREATE USER users WITH PASSWORD 'users';

-- Create the 'users' database and set 'users' as its owner (not a superuser).
CREATE DATABASE users OWNER users;

-- Grant full privileges on the 'users' database to the 'users' role (connect/create).
GRANT ALL PRIVILEGES ON DATABASE users TO users;
