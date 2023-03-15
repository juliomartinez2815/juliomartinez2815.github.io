import os
import shutil
path='C:\My Web Sites\proyecto_final\www.classcentral.com'
count = 0
count_file =0
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith((".html", ".htm")):
            count+=1
            original_path = root+'\\'+name
            new_path = r"C:\My Web Sites\all_html\\"+name
            shutil.copyfile(original_path, new_path)
    # print(dirs)