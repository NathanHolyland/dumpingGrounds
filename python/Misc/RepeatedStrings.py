def repeatedStrings(string_length, data):
    string_dict = {}
    for line in data:
        for i in range(int(len(line) / string_length)):
            string = line[string_length * i:string_length * i + string_length]
            if string in string_dict:
                string_dict[string] += 1
            else:
                string_dict[string] = 1
    return string_dict
