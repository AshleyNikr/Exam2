def open_file(filename):
    # with open(filename) as file:
    #     print("File open")
    # print("File closed")

    # alternate solution:
    file = open(filename)
    print("File open")
    file.close()
    print("File closed")

if __name__ == "__main__":
    open_file("/data/alice.txt")