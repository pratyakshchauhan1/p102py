import os
import shutil
fromdir = "C:/Users/praty/Downloads"
todir = "C:/Users/praty/OneDrive/Desktop/python/c102/dowloadedimages"
listoffiles = os.listdir(fromdir)
###print(listoffiles)
for filename in listoffiles:
    name,extension = os.path.splitext(filename)
    ##print(name)
    ##print(extension)
    if extension == '':
        continue
    if extension in ['.doc','.pdf','.docx','.ppt','.pptx']:
        path1 = fromdir+'/'+filename
        path2 = todir+'/'+"document_files"
        path3 = todir+'/'+"document_files"+'/'+filename
        ##print(path1)     
        ##print(path3)  
        if os.path.exists(path2):
            print("file is moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("file is moving")
            shutil.move(path1,path3)