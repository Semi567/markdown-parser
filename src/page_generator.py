from markdown_to_html import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    result = ""
    for line in lines:
        if line.startswith("# "):
            result = line[2:].strip()
            break
    if result == "":
        raise Exception("There's no h1 header in markdown file")
    return result

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()

    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok = True)

    with open(dest_path, mode ='w') as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
     for item in os.listdir(dir_path_content):
         # Get the full path of the current item
        item_path = os.path.join(dir_path_content, item)

        # Now we need to check if it's a file or directory
        if os.path.isfile(item_path):
            # If it's a file, check if it's a markdown file
            if item.endswith('.md'):
                # Create the destination path with same structure but in dest_dir_path
                relative_path = os.path.relpath(item_path, dir_path_content)
                # We get the directory part and join it to dest_dir_path
                dest_dir = os.path.join(dest_dir_path, os.path.dirname(relative_path))
                # Make sure this directory exists
                os.makedirs(dest_dir, exist_ok=True)
                # Create the destination file path
                dest_file = os.path.join(dest_dir, os.path.basename(item_path).replace('.md', '.html'))

                # Generate the HTML file
                generate_page(item_path, template_path, dest_file)

        elif os.path.isdir(item_path):
            # If it's a directory, create the corresponding directory in the destination
            new_dest_dir = os.path.join(dest_dir_path, item)
            os.makedirs(new_dest_dir, exist_ok=True)
                
            # Recursively process this directory
            generate_pages_recursive(item_path, template_path, new_dest_dir)
            
