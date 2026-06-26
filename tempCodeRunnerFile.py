base_folder = r"C:\Users\manal\Desktop\Lego Build Planner & inventory Optimizer\Lego Datasets"

# db_path = os.path.join(base_folder, "sets.db")
# csv_path = os.path.join(base_folder, "sets.csv")

# connect = sqlite3.connect(db_path)
# cursor = connect.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS sets (
#    set_num TEXT,
#    name TEXT,
#    year TEXT,
#    theme_id INTEGER,
#    num_parts INTEGER,
#    img_url TEXT
# )           
# """                
# )

# with open(csv_path, newline="", encoding="utf-8") as file:    
#     reader = csv.DictReader(file)
    
#     for row in reader: 
#         cursor.execute(
#             "INSERT INTO sets VALUES (?, ?, ?, ?, ?, ?)",
#             (
#                 row["set_num"], 
#                 row["name"], 
#                 row["year"], 
#                 row["theme_id"], 
#                 row["num_parts"], 
#                 row["img_url"])
#         )

# connect.commit()
# connect.close()

# cursor.execute("SELECT COUNT(*) FROM sets")
# print(cursor.fetchone())