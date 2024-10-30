from enum import Enum


class TextType(Enum):
    NORM = "normal"
    BOLD = "bold"
    ITAL = "italic"
    CODE = "code"
    LINK = "link"
    IMAG = "image"


class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        # self.text_type = TextType(text_type)
        self.text_type = text_type
        self.url = url

    def __eq__(self, node1, node2):
        # returns True if all of the properties of two TextNode objects are equal.
        if node1.values() == node2.values():
            return True

    def __repr__(self):
        # returns a string representation of the TextNode object. It should look like this:
        # TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
