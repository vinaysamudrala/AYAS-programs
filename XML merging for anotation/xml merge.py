import os
file_names = (os.listdir()[0:2])
print(file_names)
vs1= open(str(file_names[0]), 'r')
vs2= open(str(file_names[1]), 'r')
sk1= vs1.read()
sk2= vs2.read()
CoList1 = sk1.split("\n") 
CoList2 = sk2.split("\n")
vinay = CoList2.index('  </meta>')
vinay = vinay +1
print(vinay)
with open('merged.xml','w') as secondfile:
    for line in CoList1[0:len(CoList1)-1]:      
            secondfile.write(line)
            secondfile.write('\n')
    for line in CoList2[vinay:]:      
            secondfile.write(line)
            secondfile.write('\n')