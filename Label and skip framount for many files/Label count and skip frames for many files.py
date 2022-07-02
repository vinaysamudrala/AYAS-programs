from xml.dom import minidom
import os

cd = os.getcwd()
fn=[]
md=[]
xlfil = open('dtextxl.csv', 'w')

for root, dirs, files in os.walk(cd):
    for name in dirs:
        print(os.path.join(root, name))
        md.append(os.path.join(root, name))

for fil in md:
    for root, dirs, files in os.walk(fil):
        for name in files:
            print(os.path.join(root, name))
            vinay=os.path.join(root, name)
            if ".xml" in vinay:
                fn.append(os.path.join(root, name))           

for xn in fn:
    file_name = xn
    doc = minidom.parse(file_name)
    idno = doc.getElementsByTagName("image")
    limg = doc.getElementsByTagName("task")
    list1=[]
    name = doc.getElementsByTagName("size")[0]
    Last_frame = int(name.firstChild.data)
    #print('last frame - ', (Last_frame))
    for image in idno:
        sid = image.getAttribute("id")
        sid=int(sid)
        list1.append(sid)

    vs1= open(str(file_name), 'r')
    sk1= vs1.read()
    CoList1 = sk1.split("\n")
    i=0
    j=0
    for pk in CoList1:
        if '</box>' in pk:
            i=i+1
        if '</points>' in pk:
            j=j+1

    print("*"*33, i , j, i+j)
    list2=[*range(Last_frame)]
    diff=list(set(list2)-set(list1))
    diff.sort()
    #print("skipped frames", diff)
    print('number of frames skipped', len(diff))
    x=str(len(diff))
    diff = str(diff)
    skp = len(file_name)
    fl_name = os.path.split(xn)
    fldr_name = os.path.split(str(fl_name[0]))
    print(fldr_name[1])
    k=str(fl_name[1])    
    '''
    file_name = (file_name[:vinay-4]+".txt")
    
    with open(file_name, 'w') as f:
        f.write('file name -'+ file_name + '\n' )
        f.write('Number of frames 1 to'+ str(Last_frame) + '\n' )
        f.write("skipped frames - " + diff+ '\n')
        f.write('Total number of frames skipped - ' + x + '\n')
        '''
    xlfil.write(str(fldr_name[1]) + ',' + k[:-4]+","+str(x) +","+str(i+j)+ "\n")
xlfil.close()