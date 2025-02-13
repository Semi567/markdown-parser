import unittest
from split_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_image_simple(self):
        node = TextNode("This is text with an image ![alt text](image.jpg) and more text", TextType.TEXT)
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an image ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "image.jpg"),
                TextNode(" and more text", TextType.TEXT)
            ]
        )

    def test_split_nodes_image_multiple(self):
        node = TextNode(
            "![first](url1.jpg) then ![second](url2.jpg)",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("first", TextType.IMAGE, "url1.jpg"),
                TextNode(" then ", TextType.TEXT),
                TextNode("second", TextType.IMAGE, "url2.jpg")
            ]
        )

    def test_split_nodes_image_none(self):
        node = TextNode(
            "Just plain text without any images here",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_image([node]),
            [node]
        )

    def test_split_nodes_image_with_non_text_node(self):
        node = TextNode(
            "Some link text",
            TextType.LINK,
            "https://boot.dev"
        )
        self.assertEqual(
            split_nodes_image([node]),
            [node]
        )

    def test_split_nodes_link_single(self):
        node = TextNode(
            "This is text with a [link to boot.dev](https://boot.dev)",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link to boot.dev", TextType.LINK, "https://boot.dev")
            ]
        )
    
    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "This has [link1](url1) and [link2](url2) in it",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "url1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "url2"),
                TextNode(" in it", TextType.TEXT)
            ]
        )

    def test_split_nodes_link_no_links(self):
        node = TextNode(
            "Just plain text without any links",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_link([node]),
            [node]
        )

    def test_split_nodes_link_no_links(self):
        node = TextNode(
            "Just plain text without any links",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_link([node]),
            [node]
        )
    
    def test_split_nodes_link_no_text(self):
        node = TextNode(
            "Some link text",
            TextType.LINK,
            "https://boot.dev"
        )
        self.assertEqual(
            split_nodes_link([node]),
            [node]
        )

if __name__ == "__main__":
    unittest.main()
