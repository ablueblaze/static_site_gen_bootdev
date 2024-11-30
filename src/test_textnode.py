import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_false3(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_false4(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.boot.dev")
        node2 = TextNode("This is a text node",
                         TextType.ITALIC, "www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a test", TextType.TEXT, "www.stumbleupon.com")
        self.assertEqual(
            "TextNode(This is a test, TextType.TEXT, www.stumbleupon.com)", repr(
                node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):

    # non-functioning test:
    #
    # def test_textnode_to_htmlnode_invalid_type(self):
    #     ''' pass a non-compatable TextType to the function
    #     '''
    #     node = TextNode('Test from the node', TextType.CAPS)
    #     with self.assertRaises(ValueError):
    #         text_node_to_html_node(node)
    #         # TextNode('Test from the node', TextType.CAPS)

    def test_textnode_to_htmlnode_text(self):
        ''' passing TextType.TEXT to text_node_to_html_node()
        '''
        node = text_node_to_html_node(
            TextNode('Test from the node', TextType.TEXT))
        self.assertEqual(None, node.tag)
        self.assertEqual('Test from the node', node.value)

    def test_textnode_to_htmlnode_bold(self):
        ''' passing TextType.BOLD to text_node_to_html_node()
        '''
        node = text_node_to_html_node(
            TextNode('Test from the node', TextType.BOLD))
        self.assertEqual('b', node.tag)
        self.assertEqual('Test from the node', node.value)

    def test_textnode_to_htmlnode_italic(self):
        ''' passing TextType.ITALIC to text_node_to_html_node()
        '''
        node = text_node_to_html_node(
            TextNode('Test from the node', TextType.ITALIC))
        self.assertEqual('i', node.tag)
        self.assertEqual('Test from the node', node.value)

    def test_textnode_to_htmlnode_code(self):
        ''' passing TextType.CODE to text_node_to_html_node()
        '''
        node = text_node_to_html_node(
            TextNode('Test from the node', TextType.CODE))
        self.assertEqual('code', node.tag)
        self.assertEqual('Test from the node', node.value)

    def test_textnode_to_htmlnode_link(self):
        ''' passing TextType.LINK to text_node_to_html_node()
        '''
        node = text_node_to_html_node(
            TextNode('Test from the node', TextType.LINK))
        self.assertEqual('a', node.tag)
        self.assertEqual('Test from the node', node.value)
        self.assertEqual('href', node.props)

    def test_textnode_to_htmlnode_image(self):
        ''' passing TextType.IMAGE to text_node_to_html_node()
        '''
        node = text_node_to_html_node(
            TextNode('Test from the node', TextType.IMAGE)
        )
        self.assertEqual(
            {'src': None, 'alt': 'Test from the node'}, node.props)


if __name__ == "__main__":
    unittest.main()
