import os
import shutil
from pathlib import Path
from page_generator import generate_pages_recursive

# Get the directory where the script is running from
script_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to reach the root directory
root_dir = os.path.dirname(script_dir)

def copy_static(source="static", destination="public"):
    # Convert to absolute paths
    source_abs = os.path.join(root_dir, source)
    destination_abs = os.path.join(root_dir, destination)
    
    # Rest of your function stays similar but uses the absolute paths
    if os.path.exists(destination_abs):
        shutil.rmtree(destination_abs)
        
    os.makedirs(destination_abs, exist_ok=True)
        
    if not os.path.exists(source_abs):
        return

    for item in os.listdir(source_abs):
        source_path = os.path.join(source_abs, item)
        dest_path = os.path.join(destination_abs, item)
        
        if os.path.isfile(source_path):
            # Copy the file
            shutil.copy2(source_path, dest_path)
        else:
            # Recursively copy the directory
            copy_static(os.path.join(source, item), os.path.join(destination, item))

def main():
    # Create public directory
    public_dir = os.path.join(root_dir, "public")
    os.makedirs(public_dir, exist_ok=True)
    
    # Copy static files
    copy_static()
    
    # Generate all pages
    content_dir = os.path.join(root_dir, "content")
    template_path = os.path.join(root_dir, "template.html")
    public_dir = os.path.join(root_dir, "public")
    
    # Call your generate_pages_recursive function with these paths
    generate_pages_recursive(content_dir, template_path, public_dir)


main()
