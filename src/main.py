from textnode import TextNode
print('Hello World')


def main():
    test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test.__repr__())


main()
