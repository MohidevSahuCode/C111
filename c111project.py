import os
import shutil

list_files = os.listdir("C:/Users/mohid/OneDrive/Desktop/P")
print(list_files)

destination = "C:/Users/mohid/OneDrive/Desktop/Practice"
source = "C:/Users/mohid/OneDrive/Desktop/P"

shifting = shutil.move(source,destination)