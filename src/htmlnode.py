

class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
        #child methods will override this

    def props_to_html(self):
        # Create a list of formatted HTML attributes
        attributes = [f' {key}="{value}"' for key, value in self.props.items()]
        # Join the list into a single string
        return ''.join(attributes)

    def __repr__(self):
        return f"HTMLnode object has tag: <{self.tag}>"

    def __eq__(self, other):
        if not isinstance(other, HtmlNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)


class LeafNode(HtmlNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value")
        # Initialize the parent class with no children
        super().__init__(tag=tag, value=value, children=[], props=props)

    def add_child(self, child):
        raise Exception("LeafNode cannot have children")

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value  # Return raw text if no tag

        props_html = self.props_to_html() if self.props else ''
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode object has tag: <{self.tag}>, value: {self.value}"