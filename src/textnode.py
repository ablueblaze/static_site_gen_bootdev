from enum import Enum


class TextType(Enum):
    NORM = "normal"
    BOLD = "bold"
    ITAL = "italic"
    CODE = "code"
    LINK = "link"
    IMAG = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        # returns a string representation of the TextNode object.
        # It should look like this:
        #     TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
