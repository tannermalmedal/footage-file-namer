import os
  
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
    counter += 1
    print(counter)
    os.rename(file, f'Losers #{counter}.mp4')

  

# for i in range(1,51):
#     directory = f'Losers #{i}'
#     path = os.path.join(parent_dir, directory)
#     os.mkdir(path)
#     print(directory)



#for every file
# for file in files:
#     curr_name = file.name.split('.') #split files by '.'

#     if curr_name[-1] == 'mkv': #if the last split segment is 'mkv' we know to delete this file
#         os.remove(file.path)