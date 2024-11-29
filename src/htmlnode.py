# for jank testing only
from textnode import TextNode, TextType


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # tag = A string representing an html tag
        # value = A string representing the actual value e.g. the text
        # children = A list of HTMLNode objects representing the children of this node
        # props = A dictionary of attributes of the HTML tag.
        #     example: {"href": "http://www.google.com"}
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if self.props is None:
            return ''
        result = ''
        for key in self.props.keys():
            result = result + f' {key}="{self.props[key]}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    # def __init__(self, tag=None, value=None, children=None, props=None):
    def __init__(self, tag, value, props=None):
        # super().__init__(tag, value, None, props)
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode, value is None")
        if self.tag is None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode, No tag passed")
        if self.children is None:
            raise ValueError("ParentNode, No children passed")
        result_string = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            result_string = result_string + f"{child.to_html()}"
            # f"{LeafNode(child.tag, child.value).to_html()}"
        return result_string + f"</{self.tag}>"

    def __repl__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"


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
            return LeafNode('img', '', {'src', 'alt'})
    raise Exception("TextType not valid")

# Test to show how it works


def test_text_node_to_html_node(text_node):
    print('Debug>>> text_node.value: ', text_node.text_type.value)
    if text_node.text_type.value == 'bold':
        return True
    return False


'''Testing outputs of text_node_to_html_node
node_text = TextNode('Test text one', TextType.TEXT)
node_bold = TextNode('Test text one', TextType.BOLD)
node_italic = TextNode('Test text one', TextType.ITALIC)
node_code = TextNode('Test text one', TextType.CODE)
node_link = TextNode('Test text one', TextType.LINK)
node_image = TextNode('Test text one', TextType.IMAGE)

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
'''
