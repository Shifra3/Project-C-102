import os
import shutil

from_dir="C:/Users/shifr/Downloads/C102_assets-main/files"
to_dir="C:/Users/shifr/Downloads/C102_assets-main/files"

list_of_files=os.listdir(from_dir)
print(list_of_files)
#move all image files from files to image folder
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension=='':
        continue
    if extension in['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Image_Files"
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name
        #check if folder path exsist before moving else first create the folder then move it
        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("moving")
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving")