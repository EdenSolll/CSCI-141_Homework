import matplotlib as plot

def read_word_file(filename):
    word_data = {}
    year_useage_data = {}
    with open(filename) as f:
        file_contents = f.read().strip()
        content_list = file_contents.split("\n")
        for i in content_list:
            year_useage_data[(int(i.split(",")[0]))] = [(int(i[1]))]
    return year_useage_data


print(read_word_file("very_short.txt"))
