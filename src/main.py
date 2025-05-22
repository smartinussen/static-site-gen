from textnode import TextNode, TextType
print("Hello World")

def main():
    test_node = TextNode("Hello World", TextType.BOLD, "https://www.google.com")
    print(test_node)
main()