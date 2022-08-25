from xml.dom import minidom
import os
for x in os.listdir():
    file_name = x
    doc = minidom.parse(file_name)
    idno = doc.getElementsByTagName("image")
    limg = doc.getElementsByTagName("task")
    list1=[]
    name = doc.getElementsByTagName("size")[0]
    Last_frame = int(name.firstChild.data)
    print('last frame - ', (Last_frame))
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
    vinay = len(file_name)
    file_name = (file_name[:vinay-4]+".txt")
    with open(file_name, 'w') as f:
        f.write('file name -'+ file_name + '\n' )
        f.write('Number of frames 1 to'+ str(Last_frame) + '\n' )
        f.write("skipped frames - " + diff+ '\n')
        f.write('Total number of frames skipped - ' + x + '\n')