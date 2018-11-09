import json

conf = None
with open('conf', 'r+') as fp:
    conf = json.load(fp)
    print(conf)
with open('conf','w+') as fp:
    conf['src'] = '12345'
    json.dump(conf, fp)
