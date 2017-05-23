f = open('text.txt','r')
a = ['41,51','42,50','41,42', '47,37', '52,42', '54,36']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('text.txt','w')
for line in lst:
    f.write(line)
f.close()