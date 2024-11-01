import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.NORM)
        node2 = TextNode("This is a text node2", TextType.NORM)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.NORM)
        self.assertNotEqual(node, node2)

    def test_eq_false3(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.NORM)
        self.assertNotEqual(node, node2)

    def test_eq_false4(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORM)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITAL, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITAL, "www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a test", TextType.NORM, "www.stumbleupon.com")
        self.assertEqual(
            "TextNode(This is a test, normal, www.stumbleupon.com)", repr(
                node)
        )


if __name__ == "__main__":
    unittest.main()
