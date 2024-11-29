import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextType, TextNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_data = {"href": "https://www.google.com", "target": "_blank", }
        node = HTMLNode(props=test_data)
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"',
            node.props_to_html()
        )

    def test_values(self):
        node = HTMLNode("div", "check it mom!")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "check it mom!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(
            "HTMLNode(None, None, None, None)", repr(node)
        )

    def test_to_html_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    ####
    # Testing LeafNode:
    def test_LeafNode_value_none(self):
        """ returns a ValueError when "None" is passed in node.value
        """
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_LeafNode_tag_none(self):
        """ Checking if tag is None will return  the value as a string
        """
        test_value = "This is a paragraph of text."
        node = LeafNode(None, test_value)
        self.assertEqual("This is a paragraph of text.", node.to_html())

    def test_LeafNode_to_html(self):
        """ returns correct f string when given a basic tag and value
        """
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_LeafNode_props_to_html_leaf(self):
        """ returns correct f string when passed a prop
        """
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>', node.to_html()
        )

        ####
        # Testing ParentNode
    def test_parent_repr(self):
        """ returns all values of ParentNode using repr
        """
        node = ParentNode(
            "div",
            # None,
            [
                LeafNode("a", "dude, this is cool"),
                LeafNode(None, "Not cool dude!"),
                LeafNode("div", "Big bounce!")
            ]
        )
        self.assertEqual(
            "HTMLNode(div, None, [LeafNode(a, dude, this is cool, None), LeafNode(None, Not cool dude!, None), LeafNode(div, Big bounce!, None)], None)",
            repr(node)
        )

    def test_parent_primary_return(self):
        """ returns the resulting string if ParentNode is passed correct data
        """
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html()
        )

    def test_parent_with_props(self):
        """ return ParentNode if passed correct data including props
        """
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            '<p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
            node.to_html()
        )

    def test_parent_nested_with_props(self):
        """ return ParentNode if passed correct data including props
        Nested with ParentNodes
        """
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            '<p href="https://www.google.com"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
            node.to_html()
        )

    def test_parent_nested_with_props2(self):
        """ return ParentNode if passed correct data including props
        Nested with ParentNodes with props
        """
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                    {"href": "https://www.google.com"},
                ),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            '<p><p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
            node.to_html()
        )

    def test_parent_nested_parent(self):
        """ returns ParentNodes nested in ParentNodes (The Chaos!)
        """
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html()
        )

    ##### TextNode to HTMLNode function #####

    def test_textnode_to_htmlnode_no_type(self):
        '''pass a non-compatable TextType to the function
        '''
        with self.assertRaises(AttributeError):
            TextNode('test from the node', TextType.CAPS)

    def test_textnode_to_htmlnode_text(self):
        ''' passing TextType.TEXT to text_node_to_html_node()
        '''
        node = TextNode('Test from the node', TextType.TEXT)
        self.assertEqual('LeafNode(None, Test from the node, None)',
                         text_node_to_html_node(node).__repr__())

    def test_textnode_to_htmlnode_bold(self):
        ''' passing TextType.BOLD to text_node_to_html_node()
        '''
        node = TextNode('Test from the node', TextType.BOLD)
        self.assertEqual('LeafNode(b, Test from the node, None)',
                         text_node_to_html_node(node).__repr__())

    def test_textnode_to_htmlnode_italic(self):
        ''' passing TextType.ITALIC to text_node_to_html_node()
        '''
        node = TextNode('Test from the node', TextType.ITALIC)
        self.assertEqual('LeafNode(i, Test from the node, None)',
                         text_node_to_html_node(node).__repr__())

    def test_textnode_to_htmlnode_code(self):
        ''' passing TextType.CODE to text_node_to_html_node()
        '''
        node = TextNode('Test from the node', TextType.CODE)
        self.assertEqual('LeafNode(code, Test from the node, None)',
                         text_node_to_html_node(node).__repr__())

    def test_textnode_to_htmlnode_link(self):
        ''' passing TextType.LINK to text_node_to_html_node()
        '''
        node = TextNode('Test from the node', TextType.LINK)
        self.assertEqual('LeafNode(a, Test from the node, href)',
                         text_node_to_html_node(node).__repr__())

    def test_textnode_to_htmlnode_image(self):
        ''' passing TextType.IMAGE to text_node_to_html_node()
        '''
        node = TextNode('Test from the node', TextType.IMAGE)
        self.assertEqual("LeafNode(img, , {'src', 'alt'})",
                         text_node_to_html_node(node).__repr__())

# LeafNode(None, Test text one, None)
# LeafNode(b, Test text one, None)
# LeafNode(i, Test text one, None)
# LeafNode(code, Test text one, None)
# LeafNode(a, Test text one, href)
# LeafNode(img, None, {'src', 'alt'})


if __name__ == "__main__":
    unittest.main()
