from htmlnode import LeafNode
from enum import Enum


class TextType(Enum):
    """Note: Sets a predefined list of items that can be used
    in the TextNode class as valid text types.
    In essence restricting the development side of things.
    """
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        """returns a string representation of the TextNode object.
        It should look like this:
            TextNode(TEXT, TEXT_TYPE, URL)
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type.value:
        case 'text':
            return LeafNode(None, text_node.text)
        case 'bold':
            return LeafNode('b', text_node.text)
        case 'italic':
            return LeafNode('i', text_node.text)
        case 'code':
            return LeafNode('code', text_node.text)
        case 'link':
            return LeafNode('a', text_node.text, 'href')
        case 'image':
            return LeafNode(
                'img', '', {'src': text_node.url, 'alt': text_node.text}
            )
    raise ValueError(f"Invalid text_type: {text_node.text_type}")


'''
Debuging leftovers:



print('Debug>>> node_image.props: ', node_image.props)

text_node = TextNode('Test text one', TextType.IMAGE)
leaf_node = text_node_to_html_node(text_node)
print('Debug>>> text_node_to_html_node output "image": ',
      leaf_node)
print('Debug>>> leaf_node.tag: ', leaf_node.tag)
print('Debug>>> leaf_node.value: ', leaf_node.value)
print('Debug>>> leaf_node.props: ', leaf_node.props)

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text, 'href')
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            'img', '', {'src': text_node.url, 'alt': text_node.text}
        )
    raise ValueError(f"Invalid TextType: {text_node.text_type}")

# Test to show how it works


def test_text_node_to_html_node(text_node):
    print('Debug>>> text_node.value: ', text_node.text_type.value)
    if text_node.text_type.value == 'bold':
        return True
    return False


# Testing outputs of text_node_to_html_node
node_text = TextNode('Test text one', TextType.TEXT)
node_bold = TextNode('Test text one', TextType.BOLD)
node_italic = TextNode('Test text one', TextType.ITALIC)
node_code = TextNode('Test text one', TextType.CODE)
node_link = TextNode('Test text one', TextType.LINK)
node_image = TextNode('Test text one', TextType.IMAGE)
node_caps = TextNode('Test text one', TextType.CAPS)


# print('Debug>>> text_node_to_html_node: ', test_text_node_to_html_node(node))
print('Debug>>> text_node_to_html_node output "text": ',
      text_node_to_html_node(node_text))
print('Debug>>> text_node_to_html_node output "bold": ',
      text_node_to_html_node(node_bold))
print('Debug>>> text_node_to_html_node output "italic": ',
      text_node_to_html_node(node_italic))
print('Debug>>> text_node_to_html_node output "code": ',
      text_node_to_html_node(node_code))
print('Debug>>> text_node_to_html_node output "link": ',
      text_node_to_html_node(node_link))
print('Debug>>> text_node_to_html_node output "image": ',
      text_node_to_html_node(node_image))
print('Debug>>> text_node_to_html_node output "image": ',
      text_node_to_html_node(node_caps))
'''
