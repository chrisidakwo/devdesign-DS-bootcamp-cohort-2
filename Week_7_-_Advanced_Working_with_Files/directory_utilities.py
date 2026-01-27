import os
from datetime import datetime
from pprint import pprint

def list_directory(path='.'):
    """List contents of a directory with details."""
    print(f"Contents of {os.path.abspath(path)}:")
    print(f"{'Name':<30} {'Size':<10} {'Modified':<20} {'Type':<10}")
    print("-" * 70)
    
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        size = os.path.getsize(full_path)
        mod_time = datetime.fromtimestamp(os.path.getmtime(full_path))
        item_type = "Directory" if os.path.isdir(full_path) else "File"
        
        print(f"{item:<30} {size:<10,} {mod_time.strftime('%Y-%m-%d %H:%M'):<20} {item_type:<10}")

list_directory("C://Users//ADMIN//Source//Data Science Bootcamp//Cohort 2")

