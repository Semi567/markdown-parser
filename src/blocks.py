def markdown_to_blocks(markdown):
    stripped_list_of_blocks = []
    list_of_blocks = markdown.split("\n\n")
    for el in list_of_blocks:
        if el == "":
            continue
        stripped_list_of_blocks.append(el.strip())
    return stripped_list_of_blocks

def block_to_block_type(block):
    if (block.startswith('# ') 
        or block.startswith('## ') 
        or block.startswith('### ') 
        or block.startswith('#### ') 
        or block.startswith('##### ')
        or block.startswith('###### ')):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            if line.startswith(">"):
                continue
            else:
                return "paragraph"
        return "quote"
    elif block.startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if line.startswith("- "):
                continue
            else:
                return "paragraph"
        return "unordered_list"
    elif block.startswith("* "):
        lines = block.split("\n")
        for line in lines:
            if line.startswith("* "):
                continue
            else:
                return "paragraph"
        return "unordered_list"
    elif block.startswith("1. "):
        lines = block.split("\n")
        i = 1
        for line in lines:
            if line.startswith(f"{i}. "):
                i += 1
                continue
            else:
                return "paragraph"
        return "ordered_list"
    else:
        return "paragraph"