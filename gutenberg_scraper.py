# from os import listdir
import os
import json
files = []
for r, d, f in os.walk('/Users/giros/Desktop/gutenberg-dammit-files/books'):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
with open('gutenberg-metadata.json') as f:
    meta = json.load(f)
meta_len = len(meta)



months = ['January', 'February', 'March', 'April',\
     'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
days = ['0th', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', \
    '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th',\
     '18th', '19th', '20th', '21th', '22th', '23th', '24th', '25th', '26th',\
     '27th', '28th', '29th', '30th', '31st']
ordinal_days = ['first','second','third','fourth','fifth','sixth', \
    'seventh', 'eighth', 'ninth','tenth','eleventh','twelfth','thirteenth', 'fourteenth', 'fifteenth', 'sixteenth','seventeenth', 'eighteenth', 'nineteenth','twentieth',\
    'twenty-first','twenty-second','twenty-third','twenty-fourth','thirtieth', 'thirty-first']
seconds = [' zero ', '  one  ', ' two ', ' three ', ' four ', ' five ', ' six ', ' seven ', ' eight ', ' nine ']
tens = [ ' ten ',' twenty ', ' thirty ', ' forty ', ' fifty ', ' sixty ']
hours = [ '  one  ', ' two ', ' three ', ' four ', ' five ', ' six ', ' seven ', ' eight ', ' nine ', ' ten ',' eleven ', ' twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteenth']
nums = [' ' + str(i) + ' ' for i in range(0, 61)]
def search(words):
    words_json = {}
    for word in words:
        found = 0
        words_json[word] = {}
        for file_name in files:
            # print(file_name)
            if(found > 100): 
                break
            with open(file_name, 'r') as read_obj:
                # Read all lines in the file one by one
                print(file_name)
                bottom = file_name.rfind('/')
                top = file_name.find('.')
                if(bottom == -1 or top == -1 or bottom + 1 >=  len(file_name)) :
                   book_name = 'temp'
                elif(top >= meta_len or bottom >= meta_len):
                    book_name = file_name[bottom : top]
                else:
                    try:
                        book_name = meta[int(file_name[bottom + 1 : top])]['Title']
                    except:
                        book_name = 'temp'
                if(type(book_name) == list):
                    book_name  = book_name[0]
                print(book_name)
                for line in read_obj:
                   
                    # For each line, check if line contains the string
                    if word in line:
                        found += 1
                        print(found)
                        if(found > 100): break
                        words_json[word][book_name] = line
    return words_json


# months_json = search(months)
# with open('months.json', 'w+') as f:
#     out = json.dumps(months_json)
#     f.write(out)
# days_json = search(days)
# with open('days.json', 'w+') as f:
#     out = json.dumps(days_json)
#     f.write(out)

# ordinal_days_json = search(ordinal_days)
# with open('ordinal_days.json', 'w+') as f:
#     out = json.dumps(ordinal_days_json)
#     f.write(out)
nums_json = search(nums)
with open('nums.json', 'w+') as f:
    out = json.dumps(nums_json)
    f.write(out)
    # json.dump(seconds_json, f, ensure_ascii=False)