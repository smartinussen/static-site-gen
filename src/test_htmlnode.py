import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode("html", "body")
        node2 = HtmlNode("html", "body")
        self.assertEqual(node, node2)
        node3 = HtmlNode("a", "div")
        node4 = HtmlNode("h1", "div", None)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Hello, world!</a>'
        )

if __name__ == "__main__":
    unittest.main()