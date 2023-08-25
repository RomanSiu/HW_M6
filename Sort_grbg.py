from pathlib import Path
from sys import argv

try:
    param = argv[1:]
except IndexError:
    print("Use path as a param")
    exit()

folder_list = ["archives", "videos", "images", "documents", "audio"]

param1 = " ".join(param)
path_grbg = Path(fr"{param1}")

def normalize(file_name):
    

def sorting(path):
    for file in path.iterdir():
        if file.is_dir() and not file.name in folder_list:
            sorting(file)
            file.rmdir()
            continue
        
       
sorting(path_grbg)