import unittest
from markdown_to_html import *

class TestExctractMarkdown(unittest.TestCase):
    
    def test_markdown_to_html_node(self):
        markdown = """# Title

This is a paragraph with **bold** text.

* List item 1
* List item 2

> A quote block
> with multiple lines
"""
        html_node = markdown_to_html_node(markdown)
        assert html_node.tag == "div"
        assert len(html_node.children) == 4  # title, paragraph, list, quote
        assert html_node.children[0].tag == "h1"
        assert html_node.children[1].tag == "p"
        assert html_node.children[2].tag == "ul"
        assert html_node.children[3].tag == "blockquote"

    def test_markdown_to_html_olist(self):
        markdown = """1. First item
2. Second item
3. Third item"""
        html_node = olist_to_html_node(markdown)
        assert html_node.tag == "ol"
        assert len(html_node.children) == 3
        assert html_node.children[0].tag == "li"
        assert html_node.children[1].children[0].value == "Second item"
        