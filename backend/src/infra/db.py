import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("Missing DATABASE_URL (check backend/.env and docker-compose env_file)")

# common ORM "blueprint" that all models inherit from
Base = declarative_base()

# Engine = the DB gateway + connection pool
engine = create_engine(DATABASE_URL)


# NEW: ensure the connected DB user has permissions on current and future tables in schema "public".
# - Grants on existing tables
# - Default privileges for tables created later
# - Uses current_user so it works for every developer
# with engine.begin() as conn:
#     conn.execute(text("""
#         DO $$
#         DECLARE
#             db_user text := current_user;
#         BEGIN
#             EXECUTE format('GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO %I;', db_user);
#             EXECUTE format('ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO %I;', db_user);
#         END $$;
#     """))


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# FastAPI DB dependency: "one request = one session".
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
