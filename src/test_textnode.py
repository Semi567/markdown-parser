import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_again(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://google.com")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("Just a normal text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.value,
            "Just a normal text"
        )
        self.assertEqual(
            html_node.tag,
            None
        )

    def test_italic(self):
        node = TextNode("This is an italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.value,
            "This is an italic text"
        )
        self.assertEqual(
            html_node.tag,
            "i"
        )

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.tag, 
            "img"
        )
        self.assertEqual(
            html_node.value, 
            ""
        )
        self.assertEqual(
            html_node.props,
            {"src": "https://www.google.com", "alt": "This is an image"},
        )

    def test_link(self):
        node = TextNode("This is a link to somewhere special", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.tag,
            "a"
        )
        self.assertEqual(
            html_node.value,
            "This is a link to somewhere special"
        )
        self.assertEqual(
            html_node.props,
            {'href': 'https://www.google.com'}
        )

    def test_bold(self):
        node = TextNode("This is a bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.value,
            "This is a bold text"
        )
        self.assertEqual(
            html_node.tag,
            "b"
        )

    def test_code(self):
        node = TextNode("This is a code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.value,
            "This is a code"
        )
        self.assertEqual(
            html_node.tag,
            "code"
        )

    def test_wrong_type(self):
        node = TextNode("This be a wrong type t'ing", "oops")
        with self.assertRaises(Exception):
            html_node = text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()