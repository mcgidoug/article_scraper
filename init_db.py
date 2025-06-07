import sqlite3

conn = sqlite3.connect("scraper_data.db")
cursor = conn.cursor()

cursor.execute(
             """
             CREATE TABLE IF NOT EXISTS articles (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               url TEXT UNIQUE,
               author TEXT,
               date TEXT,
               content TEXT
            )
            """
)

conn.commit()
conn.close()
