import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_print_info(self):
        node1 = HTMLNode(tag = "a", value = "Click here to see a chicken!", props = {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(
            node1.__repr__(),
            f"HTMLNode\ntag: a\nvalue: Click here to see a chicken!\nchildren: None\nprops: {{'href': 'https://www.google.com', 'target': '_blank'}}\n"
        )
    
    def test_get_props(self):
        node1 = HTMLNode(tag = "a", value = "Click here to see a chicken!", props = {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(
            node1.props_to_html(),
            f' href="https://www.google.com" target="_blank"'
        )

    def test_print_info_empty_object(self):
        node1 = HTMLNode()
        self.assertEqual(
            node1.__repr__(),
            f"HTMLNode\ntag: None\nvalue: None\nchildren: None\nprops: None\n"
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_leaf_value(self):
        node = LeafNode("p","This is a paragraph")
        self.assertEqual(
            node.tag,
            "p"
        )
        self.assertEqual(
            node.value,
            "This is a paragraph"
        )

        self.assertEqual(
            node.props,
            None
        )

    def test_leaf_to_html(self):
        node = LeafNode("p","This is a paragraph")
        self.assertEqual(
            node.to_html(),
            "<p>This is a paragraph</p>"
            )
    
    def test_leaf_to_html_link(self):
        node = LeafNode("a","This is a link", {"href":"https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">This is a link</a>'
        )
    
if __name__ == "__main__":
    unittest.main()