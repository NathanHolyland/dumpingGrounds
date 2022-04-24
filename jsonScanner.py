import json
import os

def scrapeElements(dict, elements):
    important_data = {}
    for i in dict:
        if i in elements:
            important_data[i] = dict[i]
        else:
            try:
                new_data = scrapeElements(dict[i], elements)
                if len(new_data) > 0:
                    important_data[i] = {}
                    for x in new_data:
                        important_data[i][x] = new_data[x]
                
            except TypeError:
                pass
    return important_data

dir = input("Enter Parent Folder Directory: ")

elements = []
closed = False
while not closed:
    print(f"enter \"stop\" to close")
    element_of_interest = input("Element: ")
    if element_of_interest == "stop":
        closed = True
    else:
        elements.append(element_of_interest)

dictionaries = {}
for filename in os.listdir(dir):
    if filename.endswith(".json"):
        with open(os.path.join(dir, filename)) as f:
            data = json.load(f)
            dictionaries[filename] = data

dataDict = {}
for data in dictionaries:
    important_data = scrapeElements(dictionaries[data], elements)
    dataDict[data] = important_data

for i in dataDict:
    print(f"{i} {dataDict[i]}")
    print("\n")


#    commit = input("Commit data to json file? Y|N ")
#    if commit.lower() == "y":
#        filename = input("enter appropriate file name: ")
#        print(dataDict)
#        with open(filename+".json", "w", encoding='utf-8') as file:
#            json_object = json.dumps(dataDict)
#            json.dump(json_object, file, ensure_ascii=False)