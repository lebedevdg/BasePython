    def greet_names(names):
        # never change in place!!
        # for name in names:
        #     print("Hello", name.title())
        while names:
            name = names.pop()
            print("Hello", name.title())

        # return None


    names = ["sam", "ann", "nick", "john"]
    print("names:", names)
    greet_names(names)
    print("names:", names)