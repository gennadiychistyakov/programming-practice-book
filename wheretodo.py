import os

def fileProcessing(filename):
	comments, f = [], open(filename, "r")
	for str in f.readlines():
		if str.startswith("<!-- TODO:") or str.startswith("<!--TODO:"):
			comments.append(str.strip())
	if comments:
		print(filename + "\n" + "\n".join(comments) + "\n")
	f.close()

for path, dirs, filenames in os.walk(os.getcwd()):
	for x in filter(lambda x: os.path.splitext(x)[1] == ".md", filenames):
		fileProcessing(os.path.join(path, x))