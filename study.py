import re
import csv

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
        lines = ""
        for line in file:
            line = line.strip()
            lines += line
        print(lines[::2], end="")

def average_words(filename):
    with open(filename) as file:
        avg = 0
        count = 0
        for line in file:
            words = re.findall("[a-zA-Z']+[']?", line)
            if len(words) > 0:
                avg += len(words)
                count += 1
        return avg / count

def field_count(csv_filename):
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        count = 0
        for row in csv_reader:
            count += len(row)
        return count

if __name__ == "__main__":
    # filename = "alice.txt"
    # open_file(filename)
    # print(odd_lines(filename))
    # even_letters(filename)
    # print(average_words(filename))
    print(field_count("grades_010.csv"))