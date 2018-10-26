import os
filenameout="IPAddressesCopy.txt"
os.system('sed -i "$ d" {0}'.format(filenameout))
