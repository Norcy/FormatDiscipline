import os
import os.path
import sys
path = ""
if (len(sys.argv) >= 2):
	path = sys.argv[1]
if (path == ""):
	path = os.getcwd()

print("目标目录：%s" %(path))

for root, dirs, files in os.walk(path):
	for name in files:
		if (name.endswith(".h") or name.endswith(".m")):
			localpath = root + '/' + name
			print(localpath)
			os.system("clang-format -i %s -style=File" %(localpath))

print("格式化结束")