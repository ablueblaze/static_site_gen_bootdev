import unittest

from md_to_html_utilities import split_nodes_delimiter
from textnode import TextType, TextNode


class TestMdToHtmlUtility(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        '''Basic functionality of split_nodes_delimiter
        '''
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes
        )


if __name__ == "__main__":
    unittest.main()
