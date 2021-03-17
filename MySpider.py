# -*- coding: utf-8 -*-
import re
import requests
res = [#'https://www.quora.com/Is-distance-education-good',
       #'https://www.quora.com/Is-there-any-future-to-distance-education',
       #'https://www.quora.com/Does-distance-learning-has-value',
       #'https://www.quora.com/Is-distance-learning-better-than-classroom-learning',
       #'https://www.quora.com/Why-is-online-college-education-a-horrible-waste-of-time',
       #'https://www.quora.com/Is-distance-learning-a-waste-of-time-and-effort',
       #'https://www.quora.com/What-is-your-opinion-about-online-courses',
       #'https://www.quora.com/Am-I-wasting-my-time-studying-online-courses',
       #'https://www.quora.com/Is-online-education-overrated'
        ]
response = requests.get('https://www.quora.com/Is-online-education-overrated')
f = open("words.txt", "a")
data = response.text
title = ' '.join(re.findall('<title>(.*?)</title>',data))
result_list = re.findall('"text": "(.*?)."',data)+re.findall(r'''\\\\\\"text\\\\\\": \\\\\\"(.*?).\\\\\\",''',data)
f.write('\n')
print(title)

for result in result_list:
    result = result.replace(r'\u2019', r"'")
    result = result.replace('\\\\\\', "")
    result = result.replace(r'/', "")
    result = result.replace(r'\n', "")
    result = result.replace('\\', "")
    result = result.replace(',', "")
    check = result.split()
    for ele in check:
        if '"modifiers": {"image": ' in ele or len(ele) >= 13:
            check.remove(ele)
    result = ' '.join(check)
    f.write(result+", "+title+"\n")
    print(result)

f.close()