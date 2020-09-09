def merge_the_tools(string, k):

    while len(string) != 0:
        Ti = string[:k]
        Ui = ""
        for i in Ti:
            if i in Ui:
                continue
            else:
                Ui += i
        print(Ui)
        string = string[k:]
