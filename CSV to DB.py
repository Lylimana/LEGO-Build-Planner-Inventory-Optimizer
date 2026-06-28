import csv 
import sqlite3
from config import sets_csv, sets_db

with sqlite3.connect(sets_db) as connect:
    cursor = connect.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sets (
        set_num TEXT,
        name TEXT,
        year TEXT,
        theme_id INTEGER,
        num_parts INTEGER,
        img_url TEXT
        )           
        """                
    )

    with open(sets_csv, newline="", encoding="utf-8") as file:    
        reader = csv.DictReader(file)
        
        for row in reader: 
            cursor.execute(
                "INSERT INTO sets VALUES (?, ?, ?, ?, ?, ?)",
                (
                    row["set_num"], 
                    row["name"], 
                    row["year"], 
                    row["theme_id"], 
                    row["num_parts"], 
                    row["img_url"])
            )
        
cursor.execute("""
    UPDATE sets
    SET set_num = substr(set_num, 1, length(set_num) - 2)
""")

