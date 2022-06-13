readdata = open('/Users/bmunna/Documents/GitHub/MunnaBujjiBabu_personal/Devnet/inheritance.py', 'r')
print(readdata.read())
readdata.close()

with open('/Users/bmunna/Documents/GitHub/MunnaBujjiBabu_personal/Devnet/classes.py', 'r') as readdata1:
    print(readdata1.read())

with open('/Users/bmunna/Documents/GitHub/MunnaBujjiBabu_personal/Devnet/junk.txt', 'r+') as readdata2:
    readdata2.write('\n new line added to file')
    print(readdata2.read())