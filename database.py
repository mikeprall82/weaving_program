import sqlite3

# Database file location
DB_FILE = "weaving_program.db"

def connect_db():
    """Connect to the SQLite database and create tables if they don't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create Patterns table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patterns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            shafts INTEGER NOT NULL,
            treadles INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create Threading table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS threading (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pattern_id INTEGER,
            thread_number INTEGER,
            shaft INTEGER,
            FOREIGN KEY (pattern_id) REFERENCES patterns (id) ON DELETE CASCADE
        )
    ''')

    # Create Treadling table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS treadling (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pattern_id INTEGER,
            treadle_number INTEGER,
            shaft INTEGER,
            FOREIGN KEY (pattern_id) REFERENCES patterns (id) ON DELETE CASCADE
        )
    ''')

    # Create Tie-up table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tieups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pattern_id INTEGER,
            treadle INTEGER,
            shaft INTEGER,
            FOREIGN KEY (pattern_id) REFERENCES patterns (id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

def get_patterns():
    """Retrieve all patterns from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patterns')
    patterns = cursor.fetchall()
    conn.close()
    return patterns

def add_pattern(name, shafts, treadles):
    """Add a new weaving pattern to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patterns (name, shafts, treadles)
        VALUES (?, ?, ?)
    ''', (name, shafts, treadles))
    conn.commit()
    conn.close()
    print(f"Pattern '{name}' added successfully!")

def update_pattern(pattern_id, name, shafts, treadles):
    """Update an existing pattern in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE patterns
        SET name = ?, shafts = ?, treadles = ?
        WHERE id = ?
    ''', (name, shafts, treadles, pattern_id))
    conn.commit()
    conn.close()
    print(f"Pattern ID {pattern_id} updated successfully!")

def delete_pattern(pattern_id):
    """Delete a pattern from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM patterns WHERE id = ?', (pattern_id,))
    conn.commit()
    conn.close()
    print(f"Pattern ID {pattern_id} deleted successfully!")

def add_threading(pattern_id, thread_number, shaft):
    """Add a threading entry for a pattern."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO threading (pattern_id, thread_number, shaft)
        VALUES (?, ?, ?)
    ''', (pattern_id, thread_number, shaft))
    conn.commit()
    conn.close()

def add_treadling(pattern_id, treadle_number, shaft):
    """Add a treadling entry for a pattern."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO treadling (pattern_id, treadle_number, shaft)
        VALUES (?, ?, ?)
    ''', (pattern_id, treadle_number, shaft))
    conn.commit()
    conn.close()

def add_tieup(pattern_id, treadle, shaft):
    """Add a tie-up entry linking treadles to shafts."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tieups (pattern_id, treadle, shaft)
        VALUES (?, ?, ?)
    ''', (pattern_id, treadle, shaft))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    connect_db()
    print("Database setup complete!")
