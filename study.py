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

def even_letters(filename):
    with open(filename) as file:
        for line in file:
            line = line.strip()
            print(line[::2], end="")


if __name__ == "__main__":
    filename = "alice.txt"
    # open_file(filename)
    # print(odd_lines(filename))
    even_letters(filename)