import json
import re
import os


def clear():
    for n in [219]:
        output = open('comments/chat' + str(n) + '.json', 'w+')
        output.write("")
        output.close()


clear()
for n in [219]:
    print(n)
    output = open('comments/chat' + str(n) + '.json', 'a+')
    output.write("[")
    with open('./res/chat' + str(n) + '.json', 'r',
              encoding='utf-8') as file:
        chat = json.load(file)
        i = 0
        for m in chat:
            if re.search('[a-zA-Z]', m['body'].replace('\n', ' ')):
                if i != 0:
                    output.write(",")
                json.dump(m, output)
                i += 1
    output.seek(output.tell() - 1, os.SEEK_SET)
    # output.truncate()
    output.write("]")
    output.close()
    file.close()
