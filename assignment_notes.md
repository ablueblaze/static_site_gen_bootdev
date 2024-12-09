# Assignment notes for static site builder

## Current Assignment:

### Assignment

- Create a new function (I put this in a new code file, but you can organize your code as you please):
```python
def split_nodes_delimiter(old_nodes, delimiter, text_type):
```
It takes a list of "old nodes", a delimiter, and a text type. It should return a new list of nodes, where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax. For example, given the following input:
```python
node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
```
It returns:
```python
[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
]
```
The beauty of this function is that it will take care of inline code, bold, and italic text, all in one! The logic is identical, the delimiter and matching text_type are the only thing that changes, e.g. ** for bold, * for italic, and a backtick for code. Also, because it operates on an input list, we can call it multiple times to handle different types of delimiters. The order in which you check for different delimiters matters, which actually simplifies implementation.

- Write a bunch of tests. Be sure to test various types of delimiters.
- Run and submit the tests from the root of the project.

