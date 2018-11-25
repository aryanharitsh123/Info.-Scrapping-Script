import json
import requests
import re

num = 1
r = requests.get("https://translate.sugarlabs.org/accounts/")
str_to_search = r.text
x = str_to_search.split("<table")[1].split("\n")[1:]
x = "\n".join(x).split("</table>")[0]
pattern=re.compile('<tr>(.*?)</tr>',re.DOTALL)
data = re.findall(pattern, x)
dat = {}
with open('data.json', 'a+', encoding='utf-8') as file:
	for x in data[2:]:
			#print(x)
			x = x.split("\n")
			dat['Username'] = x[2].strip()
			dat['Firstname'] = re.compile('<td>(.*?)</td>').search(x[4]).group(1)
			dat['Lastname'] = re.compile('<td>(.*?)</td>').search(x[4]).group(1).strip()
			json.dump(dat,file)
