import json

f_exemple = open("exemple.json","r")
exemple = json.load(f_exemple)
f_exemple.close()

paths = []
def analyse(data, path=""):
    if type(data) is list:
        if len(data) > 1:
            del data[1:]
        analyse(data[0], f"{path}[0]")
    elif type(data) is dict:
        for key, value in data.items():
            analyse(value, f"{path}['{key}']")
    else:
        paths.append(path)

analyse(exemple)

f_paths = open("liste_champs_json.txt","w")
for path in paths:
    f_paths.write(path + '\n')
f_paths.close()

f_ex_simple = open("exemple_simple.json", "w")
json.dump(exemple, f_ex_simple, indent = 4)
f_ex_simple.close()