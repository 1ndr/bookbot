def find_word_count(file_content):
    content = file_content.split()
    return len(content)

def find_char_count(file_content):
    output = {}
    for char in file_content: 
        dict_char = char.lower()

        if dict_char in output: 
            output[dict_char] = output[dict_char] + 1
        else:
            output[dict_char] = 1

    return output

def sorted_on(items):
    return items["num"]

def my_sorted_dict(dic): 
    output = []
    for key, value in dic.items():
        output.append(
                {"char": key, 
                 "num": value
                 }
                )

    output.sort(reverse=True, key=sorted_on)

    return output


