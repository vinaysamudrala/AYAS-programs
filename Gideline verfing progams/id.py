import xml.etree.ElementTree as ET
import os
import zipfile

cd = os.getcwd()
fn=[]
md=[]
xc=[]
xml_list=[]
files_with_error=[]
xlfil = open('qc_0pid.csv', 'w')
#reads all folders
for root, dirs, files in os.walk(cd):
    for name in dirs:
        md.append(os.path.join(root, name))

for fldr in md:                     # walks in each folder
    for root, dirs, files in os.walk(fldr):
        jj=os.path.split(fldr)      # splits the folder name and file name
        
        for x in files:             # walks in each file            
            if ".zip" in x[-4:]:    #finds if their are any ZIP files in files list
                x=os.path.join(root, x)
                zip_file = zipfile.ZipFile(x,'r')
                xc = zip_file.namelist()
                for fv in xc:
                    if ".xml" in fv:  #finds if their are any XML files in ZIP File
                        xlfil.write(str(fv[:-4])+",")
                        pr=zip_file.getinfo(str(fv))
                        fs= int((int(pr.file_size))/1024)
                        print(fs)
                        try:
                            zip_file.extract(fv, "temp")
                        except:
                            files_with_error.append(fv)
                            continue

for root, dirs, files in os.walk(cd):
    for name in files:
        if ".xml" in name:
            xml_list.append(os.path.join(root, name))

for fn in xml_list:
    tree = ET.parse(fn)
    root = tree.getroot()
    list_of_errors=[]

    for xx in root.iter("image"):
        for x in xx.iter('attribute'):
            try:
                idno=int(x.text)
                if idno==0:
                    list_of_errors.append(xx.attrib['id'])
            except:
                continue
    xlfil.write(str(fn)+",")
    for er in list_of_errors:
        xlfil.write(str(er)+",")
    xlfil.write("\n")
    print(list_of_errors)
xlfil.close()