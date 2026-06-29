# import os

# base_folder = r"C:\Users\manal\Desktop\Lego Build Planner & inventory Optimizer\Lego Datasets"

# db_path = os.path.join(base_folder, "Users.db")

from pathlib import Path

project_root = Path(__file__).resolve().parent

databases = project_root / "databases"
datasets = project_root / "datasets"

# Datasets
sets_csv = datasets / "sets.csv"


# Databases
users_db = databases / "users.db"
sets_db = databases / "sets.db"

# Lego Selector 
lego_selector = project_root / "Lego_Set_Selector.py"