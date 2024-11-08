import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_data = {"href": "https://www.google.com", "target": "_blank", }
        node = HTMLNode(props=test_data)
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(
            "HTMLNode(None, None, None, None)", repr(node)
        )

#    def test_children_is_list(self):
#        node = HTMLNode(children=['test data'])
#        pass

    def test_to_html_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
