import base64
import os
import sys

#p = "{0}\{1}".format(os.getcwd(),sys.argv[1])
args = sys.argv
for i in range(1, len(args)):
    ifile = open("{0}\{1}".format(os.getcwd(),args[i]),'rb')
    print("{0}.{1}".format(os.path.splitext(args[i])[0],'b64'))
    out_file = open("{0}.{1}".format(os.path.splitext(args[i])[0],'b64'),'w')
    b64 = '<img style="max-width: 350px;" src="data:image/{0};base64, {1}" />'.format(os.path.splitext(args[i])[1][1:], base64.b64encode(ifile.read()).decode('utf-8'))
    out_file.write(b64)