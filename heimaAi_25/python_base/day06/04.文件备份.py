
targetF = open("./files/b.txt","rb")
fileData = targetF.readlines()

writeF = open("./files/D.txt","wb")

for line in fileData:
    writeF.write(line)

writeF.close()
targetF.close()