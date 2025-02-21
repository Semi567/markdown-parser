import os
import shutil
from page_generator import generate_page



def copy_static(source = "static", destination = "public"):
        
    # delete the destination directory if it exists
    if os.path.exists(destination):
        shutil.rmtree(destination)
        
    os.mkdir(destination) # create destination directory
        
    files = os.listdir(source) # create a list of files in source directory

    # loop over files in the list
    for element in files:
        if os.path.isfile(os.path.join(source, element)): # if elements is a file, copy it to destination folder
            source_path = os.path.join(source, element)
            destination_path = os.path.join(destination, element)
            # print(f"Copying {source_path} to {destination_path}")
            shutil.copy(source_path, destination_path)
            
        else:   # if element is a directory, recursively call the function on it
            # print(f"Processing directory: {element}")
            copy_static(source = os.path.join(source, element), destination= os.path.join(destination, element))

def main():
    copy_static()
    generate_page(from_path="content/index.md", template_path="template.html", dest_path="public/index.html")

main()
