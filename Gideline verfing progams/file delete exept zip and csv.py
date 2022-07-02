import os
import time
import zipfile
cd = os.getcwd()
fn=[]
md=[]
xc=[]
xml_list=[]
files_to_del=[]
xlfil = open('qc_upload.csv', 'w')
#reads all folders
for root, dirs, files in os.walk(cd):
    for name in dirs:
        #print(os.path.join(root, name))
        md.append(os.path.join(root, name))

for fldr in md: # in each folder
    for root, dirs, files in os.walk(fldr):
        jj=os.path.split(fldr) # splits the folder name
        print(jj[1],"_______",files)
        xlfil.write(str(jj[1])+","+fldr+",")
        
        for x in files:
            print(x,"((((")
            #bx = os.path.split(x)
            #print(bx[1])
            xlfil.write(str(jj[1])+","+str(x[:-4])+",")
            
            if ".zip" in x[-4:]:
                print(type(x))
                x=os.path.join(root, x)
                zip_file = zipfile.ZipFile(x,'r')
                xc = zip_file.namelist()
                for fv in xc:
                    if ".xml" in fv:
                        xlfil.write(str(fv[:-4])+",")
                        pr=zip_file.getinfo(str(fv))
                        fs= int((int(pr.file_size))/1024)
                        print(fs)
                        xlfil.write(str(fs)+",")
                        xml_nm=fv[:-4]
                        zp_name=os.path.split(x)
                        if zp_name[1][-40:-4] == xml_nm:
                            xlfil.write("P"+",")
                        else:
                            xlfil.write("F"+",")

                        #print(zp_name[1][-40:-4],"<<<<<<<<<<<<>>>>>>>>>>>>")
                        
            #elif ".xml" in x[-4:]:
                #print(x)
            elif ".csv" in x[-4:]:
                print(x)
            else:
                files_to_del.append(os.path.join(root, x))

        xlfil.write('\n')
xlfil.close()
print("$$$$$$$$",files_to_del,"*************")
for dele in files_to_del:
    os.remove(dele)
