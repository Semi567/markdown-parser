import unittest
from blocks import markdown_to_blocks, block_to_block_type

class TestBlocks(unittest.TestCase):
    #TEST MARKDOWN TO BLOCKS

    def test_markdown_to_blocks(self):
        markdown = """ # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                '# This is a heading', 
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ]
        )

    # TEST BLOCK_TO_BLOCK_TYPE

    def test_block_to_block_type_paragraph(self):
        markdown = "This is a simple paragraph"
        self.assertEqual(
            block_to_block_type(markdown),
            "paragraph"
        )

    def test_block_to_block_type_ordered_list(self):
        markdown = "1. This is first line\n2. This is second line"
        self.assertEqual(
            block_to_block_type(markdown),
            "ordered_list"
        )
    
    def test_block_to_block_type_unordered_list(self):
        markdown = "* This is first line\n* This is second line"
        self.assertEqual(
            block_to_block_type(markdown),
            "unordered_list"
        )
    
    def test_block_to_block_type_fake_list(self):
        markdown = "* This is first line\n- This is second line"
        self.assertEqual(
            block_to_block_type(markdown),
            "paragraph"
        )
    
    def test_block_to_block_type_heading(self):
        markdown = "# This is a simple paragraph"
        markdown_two = "## text"
        markdown_three = "####### fake"
        self.assertEqual(
            block_to_block_type(markdown),
            "heading"
        )
        self.assertEqual(
            block_to_block_type(markdown_two),
            "heading"
        )
        self.assertEqual(
            block_to_block_type(markdown_three),
            "paragraph"
        )
    
    def test_block_to_block_type_code(self):
        markdown = "``` This is a simple paragraph ```"
        markdown_two = "``` text"
        markdown_three = "``fake``"
        self.assertEqual(
            block_to_block_type(markdown),
            "code"
        )
        self.assertEqual(
            block_to_block_type(markdown_two),
            "paragraph"
        )
        self.assertEqual(
            block_to_block_type(markdown_three),
            "paragraph"
        )
    
    def test_block_to_block_type_quote(self):
        markdown = "> Line one\n> Line two"
        markdown_two = "> Line one\nLine two"
        markdown_three = "> Just one line"
        self.assertEqual(
            block_to_block_type(markdown),
            "quote"
        )
        self.assertEqual(
            block_to_block_type(markdown_two),
            "paragraph"
        )
        self.assertEqual(
            block_to_block_type(markdown_three),
            "quote"
        )