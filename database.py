"""
Database module for CodePet.

Provides SQLite database access with singleton pattern for persistent storage
of tasks, user profile, and pet state.
"""

import sqlite3
from pathlib import Path
from typing import Optional
from platformdirs import user_data_dir


class Database:
    """Singleton database manager for CodePet."""

    _instance: Optional['Database'] = None
    _connection: Optional[sqlite3.Connection] = None

    def __new__(cls) -> 'Database':
        """Ensure only one instance of Database exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize database connection if not already connected."""
        if self._connection is None:
            self._connect()
            self._create_tables()

    def _get_db_path(self) -> Path:
        """Get the database file path in user data directory."""
        data_dir = Path(user_data_dir("CodePet", "CodePet"))
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir / "codepet.db"

    def _connect(self) -> None:
        """Establish database connection with WAL mode."""
        db_path = self._get_db_path()
        self._connection = sqlite3.connect(str(db_path), check_same_thread=False)
        self._connection.row_factory = sqlite3.Row

        # Enable WAL mode for better concurrent access
        self._connection.execute("PRAGMA journal_mode=WAL")
        self._connection.execute("PRAGMA foreign_keys=ON")

    def _create_tables(self) -> None:
        """Create database tables if they don't exist."""
        cursor = self._connection.cursor()

        # Tasks table with parent_id for subtasks
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                completed INTEGER DEFAULT 0,
                xp_value INTEGER DEFAULT 10,
                parent_id INTEGER DEFAULT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP DEFAULT NULL,
                FOREIGN KEY (parent_id) REFERENCES tasks(id) ON DELETE CASCADE
            )
        """)

        # User profile table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_profile (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                username TEXT DEFAULT 'User',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Pet state table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pet_state (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                name TEXT DEFAULT 'Pet',
                level INTEGER DEFAULT 1,
                current_xp INTEGER DEFAULT 0,
                evolution_stage TEXT DEFAULT 'egg',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self._connection.commit()

        # Initialize default records if they don't exist
        self._initialize_defaults()

    def _initialize_defaults(self) -> None:
        """Create default user profile and pet state if they don't exist."""
        cursor = self._connection.cursor()

        # Check and insert default user profile
        cursor.execute("SELECT COUNT(*) FROM user_profile")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO user_profile (id, username) VALUES (1, 'User')")

        # Check and insert default pet state
        cursor.execute("SELECT COUNT(*) FROM pet_state")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO pet_state (id, name, level, current_xp, evolution_stage) "
                "VALUES (1, 'Pet', 1, 0, 'egg')"
            )

        self._connection.commit()

    @property
    def connection(self) -> sqlite3.Connection:
        """Get the database connection."""
        return self._connection

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a query and return the cursor."""
        return self._connection.execute(query, params)

    def commit(self) -> None:
        """Commit the current transaction."""
        self._connection.commit()

    def close(self) -> None:
        """Close the database connection."""
        if self._connection:
            self._connection.close()
            Database._connection = None
            Database._instance = None


def get_database() -> Database:
    """Get the database singleton instance."""
    return Database()
