import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print_info(self):
        node1 = HTMLNode(tag = "a", value = "Click here to see a chicken!", props = {"href": "https://www.google.com","target": "_blank"})
        node2 = HTMLNode(tag = "p", children = [node1], value = "Oh no")
        print(node1)
        print(node2)
    
    def test_get_props(self):
        node1 = HTMLNode(tag = "a", value = "Click here to see a chicken!", props = {"href": "https://www.google.com","target": "_blank"})
        print(node1.props_to_html())

    def test_print_info_empty_object(self):
        node1 = HTMLNode()
        print(node1)

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
    
if __name__ == "__main__":
    unittest.main()