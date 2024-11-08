class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # tag = A string representing an html tag
        # value = A string representing the actual value e.g. the text
        # children = A list of HTMLNode objects representing the children of this node
        # props = A dictionary of attributes of the HTML tag.
        #     example: {"href": "http://www.google.com"}
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if self.props is None:
            return ''
        result = ''
        for key in self.props.keys():
            result = result + f' {key}="{self.props[key]}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
