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
