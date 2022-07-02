import os
import time
import zipfile
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
            fn.append(os.path.join(root, name))
            if ".zip" in vinay:
                ti_c = os.path.getmtime(vinay)
                zip_file = zipfile.ZipFile(vinay,'r')
                xc = len(zip_file.namelist())

                c_ti = time.ctime(ti_c)
                fl_name = os.path.split(vinay)
                fldr_name = os.path.split(str(fl_name[0]))
                print(fldr_name[1])
                k=str(fl_name[1])
                '''
                fn1p = list(k)
                print("****", vinay)
                for root, dirs, filess in os.walk(vinay):
                    print(os.path.join(root, filess))
                    '''
                xlfil.write(str(c_ti) + "," + str(fldr_name[1]) + ',' + k +','+ k[:19] + "," +k[19:54]+","+str(xc)+ "\n")
xlfil.close()