stringpart = ""
stb = ["A","B","C","D","E","F","G","H","I"]
for f in stb:
    for i in range(12):
        stringpart = stringpart + '"{}'.format(f) + '{}"'.format(i)+ ","
print(stringpart)