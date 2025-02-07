import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_no_tag(self):
        node = LeafNode(value = "There is no tag")
        self.assertEqual(
            node.to_html(),
            "There is no tag"
        )

    def test_parent_node(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            ParentNode("p",[LeafNode(None, "I'm a child of a child"), LeafNode("b", "Same as me!")]),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )   
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b><p>I'm a child of a child<b>Same as me!</b></p>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
    def test_parent_node_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()