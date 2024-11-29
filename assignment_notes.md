# Assignment notes for static site builder

## Current Assignment:

### Write a function:
```python
def text_node_to_html_node(text_node):
```
- It should handle each type of the TextType enum. If it gets a TextNode that is none of those types, it should raise an exception.

- TextType.TEXT: This should become a LeafNode with no tag, just a raw text value.
- TextType.BOLD: This should become a LeafNode with a "b" tag and the text
- TextType.ITALIC: "i" tag, text
- TextType.CODE: "code" tag, text
- TextType.LINK: "a" tag, anchor text, and "href" prop
- TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)

- Add some tests.
- Run and submit the tests from the root of the project.

ERROR: test_textnode_to_htmlnode_no_type (test_htmlnode.TestHTMLNode)
pass a None TextType to the function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/blaze/Workspace/github.com/ablueblaze/static_site_gen_bootdev/src/test_htmlnode.py", line 203, in test_textnode_to_htmlnode_no_type
    node = TextNode('test from the node', TextType.CAPS)
  File "/usr/lib/python3.10/enum.py", line 437, in __getattr__
    raise AttributeError(name) from None
AttributeError: CAPS
