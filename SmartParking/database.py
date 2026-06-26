import sqlite3

DATABASE = "smartparking.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS parking_spaces (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        space_number TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        parking_id INTEGER NOT NULL,
        reservation_date TEXT NOT NULL,
        reservation_time TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(parking_id) REFERENCES parking_spaces(id)
    )
    """)

    conn.commit()
    conn.close()


def insert_default_parking():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM parking_spaces")
    count = cursor.fetchone()[0]

    if count == 0:
        spaces = [
            ("A1", "Available"),
            ("A2", "Available"),
            ("A3", "Occupied"),
            ("A4", "Available"),
            ("B1", "Occupied"),
            ("B2", "Available"),
            ("B3", "Available"),
            ("B4", "Occupied"),
            ("C1", "Available"),
            ("C2", "Available"),
            ("C3", "Occupied"),
            ("C4", "Available")
        ]

        cursor.executemany(
            "INSERT INTO parking_spaces (space_number, status) VALUES (?, ?)",
            spaces
        )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    insert_default_parking()
    print("Database created successfully.")