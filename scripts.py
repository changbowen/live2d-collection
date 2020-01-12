import os
import json

def gen_model_json_from_textures():
    with open('index.json.bak') as f:
        j = json.load(f)
        for t in os.listdir('textures'):
            j['textures'] = ['textures/' + t]
            with open(os.path.splitext(t)[0] + '.json', 'w') as ff:
                json.dump(j, ff)

def get_model_json(path, callback):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.json'):
                jPath = os.path.join(root, file)
                with open(jPath, encoding='utf-8-sig') as fo:
                    jData = json.load(fo)
                    if type(jData) is dict and 'model' in jData and jData['model'].endswith('.moc'):
                        callback(jPath, jData)

def add_hit_areas_to_model_json(path, data):
    if 'hit_areas' not in data and 'hit_areas_custom' not in data:
        print('No hit areas found: ' + path)
        data['hit_areas_custom'] = {
            "head_x": [-0.35, 0.6],
            "head_y": [0.19, -0.2],
            "body_x": [-0.3, -0.25],
            "body_y": [0.3, -0.9]
        }
        # data['motions']['flick_head'] = data['motions'].pop('thanking')
        with open(path, 'w', encoding='utf-8') as fs:
            json.dump(data, fs)

# os.chdir('33')
# add_hit_areas_to_model_json('.')
get_model_json('.', add_hit_areas_to_model_json)

pass
# j['hit_areas_custom'] = {
#     "head_x": [-0.35, 0.6],
#     "head_y": [0.19, -0.2],
#     "body_x": [-0.3, -0.25],
#     "body_y": [0.3, -0.9]
# }