import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExctractMarkdown(unittest.TestCase):
    def test_eq_image(self):
        text_1 = "This is text with a ![example image](https://example.com/image.png)"
        self.assertEqual(
            extract_markdown_images(text_1),
            [("example image", "https://example.com/image.png")]
        )

    def test_eq_images(self):
        text = "This is text with 2 images: ![example image](https://example.com/image.png) and another one: ![second image](https://example.org/pic.jpg)"
        self.assertEqual(
            extract_markdown_images(text),
            [("example image", "https://example.com/image.png"), ("second image", "https://example.org/pic.jpg")]
        )

    def test_empty_alt_text(self):
        text = "![](https://example.com/image.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [("", "https://example.com/image.png")]
        )

    def test_empty_url(self):
        text = "![missing_url]()"
        self.assertEqual(
            extract_markdown_images(text),
            [("missing_url", "")]
        )

    def test_invalid_markdown_image(self):
        text = "Here's some text [random](text)"
        self.assertEqual(
            extract_markdown_images(text),
            []
        )

    def test_eq_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_links(text),
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        )

    def test_empty_anchor_link(self):
        text = "This is a link with empty anchor[]()"
        self.assertEqual(
            extract_markdown_links(text),
            [("", "")]
        )

    def test_broken_link(self):
        text = "[broken](link"
        self.assertEqual(
            extract_markdown_links(text),
            []
        )