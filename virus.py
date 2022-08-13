import os

home = os.path.expanduser("~")
os.chdir(home)

for path, subdirs, files in os.walk(home):
	for file in files:
		print(os.path.join(path, file))
