import operator


class ReadiedFile:
    def __init__(self, filename):
        self.filename = filename
        self.strings = 0
        self.content = ''
        with open(self.filename, 'r', encoding='utf-8') as file:
            count = 0
            for line in file:
                count += 1
                self.content += line
            self.strings = count
            # self.content = file.read()   - не пойму, почему так не работает, пришлось построчно читать


def file_compare(file_list):
    sorted_list = sorted(file_list, key=operator.attrgetter('strings'))
    out_data = ''
    for sorted_file in sorted_list:
        out_data += sorted_file.filename
        out_data += '\n'
        out_data += str(sorted_file.strings)
        out_data += '\n'
        out_data += sorted_file.content

    with open('out.txt', 'w', encoding='utf-8') as file:
        file.write(out_data)

file1 = ReadiedFile("1.txt")
#print(file1.filename, file1.strings, file1.content)
file2 = ReadiedFile("2.txt")
file3 = ReadiedFile("3.txt")

file_compare([file1, file2, file3])

