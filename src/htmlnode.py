class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    # def props_to_html(self):
    #     if self.props is None:
    #         return ""
    #     result = ""
    #     for key, value in self.props.items():
    #         result += f' {key}="{value}"'
    #     return result

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode\ntag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}\n"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value)
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        if self.tag == "a":
            link = self.props_to_html()
            return f"<{self.tag}{link}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props=None)
        
    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("ParentNode must have a tag")
        if self.children is None or self.children == []:
            raise ValueError("ParentNode must have children")
        kids = ""
        for child in self.children:
            kids += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{kids}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        
