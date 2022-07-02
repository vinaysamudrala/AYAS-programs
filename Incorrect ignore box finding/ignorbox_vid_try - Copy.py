from time import monotonic
from xml.dom import minidom
import os

file_name = str(os.listdir()[0])
doc = minidom.parse(file_name)
idno = doc.getElementsByTagName("track")
listoferrors =[]
for image in idno:
    sid = image.getAttribute("label")
    tsid = image.getAttribute("id")
    if 'Ignore Box' in sid:
        print(sid, tsid)
        uu = image.childNodes
        xc=(uu.length)
        xc=int((xc-1)/2)
        print(xc)
        for mno in range(int(xc)):
            if mno%2==0:
                #print(type(mno), mno)
                ce = image.childNodes[mno+1]
                x1= ce.getAttribute("xtl")
                x2=ce.getAttribute("xbr")
                y1=ce.getAttribute("ytl")
                y2=ce.getAttribute("ybr")
                fm=ce.getAttribute('frame')
                print(ce,x1,x2,y1,y2,"frm",fm)
                oc=ce.getAttribute('occluded')
                xl=float(x2)-float(x1)
                yl= float(y2)-float(y1)
                if (xl>40.0 or yl>40.0) and oc=='0':
                    size=(str(round(xl,2)) + " X " + str(round(yl,2)))
                    print(size)
                    listoferrors.append(size)
                    j=int(tsid)
                    j=str(j+1)
                    error_frame = ("   "+'frame number'+ '-'+fm + "   " + 'box number'+  '-' + j)
                    listoferrors.append(error_frame)
                    listoferrors.append('\n')
            else:
                continue
with open(file_name[0:-4] + '_ignore video box.txt', 'w') as f:
        f.write('file name -'+ file_name + '\n' )
        for vinay in listoferrors:
            f.write(vinay)