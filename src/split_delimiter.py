from textnode import TextType, TextNode

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
