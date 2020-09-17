import json
import string
profanity = []
with open('/Users/hima/Desktop/list.txt', 'r') as f:
    for line in f:
        profanity.append(line.strip())
print(profanity)
with open('nums.json') as f:
    hours_json = json.load(f)
for word in profanity:
    for hour, txt in hours_json.items():
        for key, value in txt.items():
            key = key.replace(word, '')

with open('nums_screened.json', 'w+') as out_file:
    out = json.dumps(hours_json)
    out_file.write(out)

