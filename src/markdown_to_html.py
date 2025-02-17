from split_delimiter import text_to_textnodes
from htmlnode import ParentNode
from blocks import markdown_to_blocks, block_to_block_type
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == "paragraph":
        return paragraph_to_html_node(block)
    if block_type == "heading":
        return heading_to_html_node(block)
    if block_type == "code":
        return code_to_html_node(block)
    if block_type == "ordered_list":
        return olist_to_html_node(block)
    if block_type == "unordered_list":
        return ulist_to_html_node(block)
    if block_type == "quote":
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    amount = 0
    for char in block:
        if char == '#':
            amount += 1
        else:
            break 
    text = block[amount + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{amount}", children)
    


def code_to_html_node(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    new_items = []
    for item in items:
        text = item[item.find('.') + 2:]
        children = text_to_children(text)
        new_items.append(ParentNode("li", children))
    return ParentNode("ol", new_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    new_items = []
    for line in items:
        text = line[2:]
        children = text_to_children(text)
        new_items.append(ParentNode("li", children))
    return ParentNode("ul", new_items)



def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        line = line.lstrip('>')
        line = line.lstrip()
        new_lines.append(line)
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)
