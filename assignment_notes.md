# Assignment notes for static site builder

## Current Assignment:
Parent nodes

### Create another child class of the HTMLNode called ParentNode. Its constructor should differ from the parent class in that:
- The tag and children arguments are not optional
- It doesn't take a value argument
- props is optional
- (the exact opposite of the LeafNode class)

### Add a .to_html method.
- If the object doesn't have a tag, raise a ValueError.
- If there are no children, raise a ValueError with a different message.
- Otherwise, return a string representing the HTML tag of the node and its children. This should be a recursive method (each recursion being called on a nested child node). I iterated over all the children and called to_html on each, concatenating the results and injecting them between the opening and closing tags of the parent.

For example, this node and its children:
```python
node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

node.to_html()
```
Should convert to:
```HTML
<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>
```

Don't worry about indentation or pretty-printing. (When pretty-printed it would look like this):
```HTML
<p>
    <b>Bold text</b>
    Normal text
    <i>italic text</i>
    Normal text
</p>
```

Most editors can be configured to auto-format HTML on save, so we don't need to worry about implementing that in our code.

I wrote many tests for this class. I recommend you do the same, there is a lot of room for error. Test all the edge cases you can think of, including nesting ParentNode objects inside of one another, multiple children, and no children.

Once you're happy that everything is working as intended, run and submit the tests from the root of the project.

