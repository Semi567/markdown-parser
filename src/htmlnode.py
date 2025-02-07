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
        if self.value is None or self.value == "":
            raise ValueError("LeafNode must have a value.")
        if self.tag is None or self.tag == "":
            return self.value
        if self.tag == "a":
            link = self.props_to_html()
            return f"<{self.tag}{link}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
        
