from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            list_of_nodes.append(node)
            continue
        processed_nodes = []
        fragments = node.text.split(delimiter)
        if len(fragments) % 2 == 0:
            raise ValueError("invalid markdown syntax")
        for i in range(len(fragments)):
            if fragments[i] == "":
                continue
            if i % 2 == 0:
                processed_nodes.append(TextNode(fragments[i], TextType.TEXT))
            else:
                processed_nodes.append(TextNode(fragments[i], text_type))
        list_of_nodes.extend(processed_nodes)
    return list_of_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        if not images:
            result.append(node)
            continue
        
        current_text = node.text
        for image_alt, image_link in images:
            sections = current_text.split(f"![{image_alt}]({image_link})", 1)

            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))

            result.append(TextNode(image_alt, TextType.IMAGE, image_link))

            current_text = sections[1]

        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))
    
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue
        
        current_text = node.text
        for link_alt, link in links:
            sections = current_text.split(f"[{link_alt}]({link})", 1)

            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))

            result.append(TextNode(link_alt, TextType.LINK, link))

            current_text = sections[1]

        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))
    
    return result

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes