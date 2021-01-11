import requests

link = open('list.txt', 'r')
link = link.read().strip().split('\n')
none = True

for i in link:
	content = requests.get(i)
	if "hrs" in content.text:
		print(i, end='')
		print(" has new chapter")
		none = False

if none:
	print("No new chapter today, feelsbadman...")