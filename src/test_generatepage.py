import unittest
from page_generator import extract_title

class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):   # multiple h1 headers, h1 is not the first line, extra whitespace
        markdown = """Title
## Stuff etc
# Proper h1 header   
*Something in italic*
# Oh no"""
        self.assertEqual(
            "Proper h1 header",
            extract_title(markdown)
        )

    def test_extract_title_no_h1(self):
        markdown = """## first line
Second line"""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "There's no h1 header in markdown file")

    def test_extract_title_first_line(self):
        markdown = """# This is first h1
Second line
# Another h1"""
        self.assertEqual(
            "This is first h1",
            extract_title(markdown)
        )
