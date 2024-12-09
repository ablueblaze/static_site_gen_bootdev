from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    parsed_nodes = []
    for node in old_nodes:
        # print("Debug>>> for loop: ", node.text)
        # print("Debug>>> for loop split point: ", node.text.split(delimiter))
        split_node = node.text.split(delimiter)
        for split in split_node:
            pass

    return parsed_nodes


# Testing area
node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

print("Debug>>> node: ", node)
print("Debug>>> new_nodes: ", new_nodes)
