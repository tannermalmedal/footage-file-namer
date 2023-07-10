import os
import shutil
  
# Parent Directory path
parent_dir = os.getcwd()

files = os.listdir(parent_dir)

# get input from user on what the most recent renamed video is
counter = int(input("What is the most recent number of vid renamed \n"))

# filter function
def keep_dates(file_name):
    if file_name[0] == '2':
        return True
    
    return False


# filter the files that arent dates (don't start with 2023-...-...)
files = list(filter(keep_dates, files))


# sort each file by it's modified time
files.sort(key = os.path.getctime)

# ensure this only happens for mp4 files
for file in files:
    counter += 1 #increment counter for each file
    directory = f'Losers #{counter}' #folder/dir name that file will go in
    path = os.path.join(parent_dir, directory) #create the full path
    os.mkdir(path) #make the directory in the path
    os.rename(file, f'Tanner #{counter}.mp4') #renaming the file
    shutil.move(f'Tanner #{counter}.mp4', path) #move file from 