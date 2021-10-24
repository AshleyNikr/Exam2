def open_file(filename):
    # with open(filename) as file:
    #     print("File open")
    # print("File closed")

    # alternate solution:
    file = open(filename)
    print("File open")
    file.close()
    print("File closed")

def odd_lines(filename):
    with open(filename) as file:
        i = 1
        for line in file:
            if i % 2 != 0:
                print(line)
            i += 1
    return i
if __name__ == "__main__":
    open_file("/data/alice.txt")
    print(odd_lines("/data/alice.txt"))