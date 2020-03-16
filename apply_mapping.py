""" genere un json à partir du mapping fourni
    Le mapping doit respecter le format du json d'exemple
    voir exemple_analyse.py pour générer la liste des champs du json.
"""

def del_comment(s):
    """ FIXME traiter les cas particuliers """
    return  (s.split("#"))[0].strip()



mapping = {}
with open("mapping.txt", "r") as mapping_f:
    for line in mapping_f:
        del_comment(line)
        if len(line)==0:
            continue
        (cerfa_key, json_path) = [s.strip() for s in line.split(":")]
        mapping[cerfa_key] = json_path

cerfa = {}
with open("export_cerfa.txt", "r") as cerfa_f:
    for line in cerfa_f:
        del_comment(line)
        if len(line)==0:
            continue
        (cerfa_key, cerfa_value) = [s.strip() for s in line.split("=")]
        cerfa[cerfa_key] = cerfa_value

def ajoute(data, path, value):
    path[0]

# génération des données contenues dans le cerfa
data = None
for (key, value) in cerfa.items():
    ajoute(data, mapping[key], value)