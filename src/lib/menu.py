class MenuUI:

    def __init__(self, options):
        self.options = options
        pass

    def showHeader(self):
        print("\nSelcet an option: \n")
        for index, item in enumerate(self.options):
            print(index + 1, item["title"], "\n")

        print(self.lastIndex(), "Exit from Application", "\n")

    def lastIndex(self):
        return len(self.options) + 1

    def render(self):
        while True is True:
            try:
                self.showHeader()
                print("\n===================\n")
                index = int(input("Choose an option: "))
                print("\n")
                if index == self.lastIndex():
                    break
                option = self.options[index - 1]
                option["handler"]()
            except Exception as e:
                print("Something went wrong, please try again.", e)
