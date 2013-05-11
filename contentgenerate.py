import os

def fileProcessing(filename):
	global content
	f = open(filename, "r")
	for str in f.readlines():
		if str.startswith("#") and "{" in str:
			str = (lambda func: lambda v: func(func, v))(lambda f, s: s if not s.startswith("#") else f(f, s[1:]))(str).strip()
			str = "[" + str[:str.rfind("{")].strip() + "]" + str[str.rfind("{"):]
			content.append(str.replace("{", "(").replace("}", ")"))
	f.close()

content = []
for path, dirs, filenames in os.walk(os.getcwd()):
	for x in filter(lambda x: os.path.splitext(x)[1] == ".md", filenames):
		fileProcessing(os.path.join(path, x))
content.sort(key = lambda str: "!!!" if "#introduce" in str else str)
print("\\\n".join(content))