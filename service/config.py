"""
Global Configuration for Application
"""
import os


# Get configuration from environment
# Default to a local SQLite database so the service can run without
# requiring a PostgreSQL server.  CI pipelines override this with the
# appropriate value when needed.
DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///development.db")

# Build DATABASE_URI from other environment variables if provided and no
# explicit DATABASE_URI was set
if DATABASE_URI == "sqlite:///development.db":
    database_user = os.getenv("DATABASE_USER")
    if database_user:
        database_password = os.getenv("DATABASE_PASSWORD", "postgres")
        database_name = os.getenv("DATABASE_NAME", "postgres")
        database_host = os.getenv("DATABASE_HOST", "localhost")
        DATABASE_URI = (
            f"postgresql://{database_user}:{database_password}@"
            f"{database_host}:5432/{database_name}"
        )

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret for session management
SECRET_KEY = os.getenv("SECRET_KEY", "s3cr3t-key-shhhh")
