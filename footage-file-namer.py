import os
import shutil
import subprocess
import time
  
# Parent Directory path
parent_dir = os.path.dirname(os.path.realpath(__file__))

files = os.listdir(parent_dir)

print(parent_dir)
print(files)
print(os.path.join(parent_dir, 'Losers 14124124'))



# get input from user on what the most recent renamed video is
counter = int(input("What is the most recent number of vid renamed \n"))

# filter function
def keep_dates(file_name):
    if file_name[0] == '2':
        return True
    
    return False


# filter the files that arent dates (don't start with 2023-...-...)
files = list(filter(keep_dates, files))
print(files)


# sort each file by it's modified time
sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(parent_dir, x)))

# ensure this only happens for mp4 files
for file in sorted_files:
    
    counter += 1 #increment counter for each file
    directory = f'Losers #{counter}' #folder/dir name that file will go in
    path = os.path.join(parent_dir, directory) #create the full path
    os.mkdir(path) #make the directory in the path

    # Provide the full path for the file while renaming and moving
    full_file_path = os.path.join(parent_dir, file)
    new_file_name = f'Tanner #{counter}.mp4'
    new_file_path = os.path.join(path, new_file_name)

    os.rename(full_file_path, new_file_path)  # renaming the file and moving it to new path

# Inform the user that the file operations are completed
print("File operations completed.")

# Open a new command prompt to keep it open after the script execution
subprocess.call("cmd /k", shell=True)

