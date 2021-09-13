max_len = 0

with open('./res/words.txt', 'r') as f:
    string = f.readline()[:-1]
    while string != '' or string != ' ':
        if len(string) > max_len:
            max_len = len(string)

print('max length: ', max_len)