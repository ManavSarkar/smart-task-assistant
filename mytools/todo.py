import sqlite3

# --- SQLite To-Do Storage ---
conn = sqlite3.connect("todos.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL
    )
""")
conn.commit()

def add_todo(item: str):
    """
    Adds a new to-do item to the database.

    Args:
        item (str): The to-do item to be added.

    Returns:
        str: A confirmation message indicating the item was added and the total number of items in the list.

    Raises:
        sqlite3.DatabaseError: If there is an issue with the database operation.
    """
    cursor.execute("INSERT INTO todos (item) VALUES (?)", (item,))
    conn.commit()
    count = cursor.execute("SELECT COUNT(*) FROM todos").fetchone()[0]
    return f"Added to-do: '{item}'. You now have {count} items in your list."


def list_todos():
    """
    Fetches and lists all to-do items from the database.

    This function retrieves all to-do items stored in the database and formats 
    them into a numbered list. If no items are found, it returns a message 
    indicating that the to-do list is empty.

    Returns:
        str: A formatted string containing the list of to-do items or a message 
        indicating that the to-do list is empty.
    """
    cursor.execute("SELECT id, item FROM todos")
    rows = cursor.fetchall()
    if not rows:
        return "Your to-do list is empty."
    return "Your to-dos:\n" + "\n".join(f"{row[0]}. {row[1]}" for row in rows)
