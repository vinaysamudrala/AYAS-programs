from xml.dom import minidom
import os
file_name = str(os.listdir()[0])
#file_name='4_77bc58f6-253d-4199-920d-2b868d1e0edb.zip (4).xml'
doc = minidom.parse(file_name)
idnos = doc.getElementsByTagName("box")
idno = doc.getElementsByTagName("image")
limg = doc.getElementsByTagName("task")
list1=[]
listoferrors =[]
for image in idnos:
    sid = image.getAttribute("label")
    if 'Ignore Box' in sid:
        x1=image.getAttribute("xtl")
        x2=image.getAttribute("xbr")
        y1=image.getAttribute("ytl")
        y2=image.getAttribute("ybr")
        xl=float(x2)-float(x1)
        yl= float(y2)-float(y1)
        if xl>40.0 or yl>40.0:
            size=(str(round(xl,2)) + " X " + str(round(yl,2)))
            print(size)
            listoferrors.append(size)
            j=image.parentNode.getAttribute('id')
            error_frame = ("   "+'frame number'+ '-' + j)
            listoferrors.append(error_frame)
            listoferrors.append('\n')

name = doc.getElementsByTagName("size")[0]
Last_frame = int(name.firstChild.data)
print('last frame 1- ', (Last_frame))
for image in idno:
    sid = image.getAttribute("id")
    sid=int(sid)
    list1.append(sid)
list2=[*range(Last_frame)]
diff=list(set(list2)-set(list1))
diff.sort()
print("skipped frames", diff)
print('number of frames skipped', len(diff))
x=str(len(diff))
diff = str(diff)
#file_name= file_name + "file"
vinay = len(file_name)
file_name = (file_name[:vinay-4]+".txt")
with open(file_name[0:-4] + "skip and ignore.txt", 'w') as f:
    f.write('file name -'+ file_name[0:-4]+  '\n' )
    f.write('Number of frames 1 to'+ str(Last_frame) + '\n' )
    f.write("skipped frames - " + diff+ '\n')
    f.write('Total number of frames skipped - ' + x + '\n'+"\n")
    for vinay in listoferrors:
        f.write(vinay)