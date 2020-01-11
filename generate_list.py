import json
import os
import pathlib

out = []
os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            jPath = os.path.join(root, file)
            with open(jPath, encoding='utf-8-sig') as f:
                jData = json.load(f)
                if type(jData) is dict and 'model' in jData and jData['model'].endswith('.moc'):
                    # n = file.replace('model', '').replace('json', '').strip('.').replace('.', '-')
                    # if len(n) == 0: n = root.strip('.')
                    out.append(pathlib.Path(jPath).as_posix())


with open('list.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=4)

print('Generated ' + str(len(out)) + ' items.')
