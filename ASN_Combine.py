import os
import shutil
import time
print '*************************'
print '****** ASN Merge ********'
print '*************************'
print '\nStarting ASN Merge...'
time.sleep(3)
print 'Waiting for files...'
Archive = "E:\ASN\Archive"
while 1:
    os.chdir("E:\ASN")
    for files in os.listdir("."):
        if files.endswith(".856"):
            if files != "ASN.856":
                ASN_856 = open("C:\ASN_Gentran\ASN.856", "a")
                print 'Merging {}'.format(files)
                f = open(files, "r")
                ASN_856.write(f.read())
                f.close()
                shutil.move(files, os.path.join(Archive, files))
                ASN_856.close()
    time.sleep(15)
