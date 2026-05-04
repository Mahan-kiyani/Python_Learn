import json

def js_parse(js_str, keyd):
    j = json.loads(js_str)
    return j[keyd]

k = js_parse('{"a":2, "b":76}', 'a')
print(k)