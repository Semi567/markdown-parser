def markdown_to_blocks(markdown):
    stripped_list_of_blocks = []
    list_of_blocks = markdown.split("\n\n")
    for el in list_of_blocks:
        if el == "":
            continue
        stripped_list_of_blocks.append(el.strip())
    return stripped_list_of_blocks