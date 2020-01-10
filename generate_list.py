import json
import os

out = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            jpath = root + '\\' + file
            with open(jpath, encoding='utf-8-sig') as f:
                jdata = json.load(f)
                if type(jdata) is dict and 'model' in jdata and jdata['model'].endswith('.moc'):
                    # n = file.replace('model', '').replace('json', '').strip('.').replace('.', '-')
                    # if len(n) == 0: n = root.strip('.')
                    out.append(jpath)


with open('list.json', 'w', encoding='utf-8') as f:
    json.dump(out, f)

print('Generated ' + str(len(out)) + ' items.')
