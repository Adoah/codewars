import datetime
import os
import sys

now = datetime.datetime.now()

print str(now)

print "current location:", os.getcwd()

print str(sys.argv)

os.chdir(os.getcwd() + "/" + sys.argv[1])

print os.getcwd()

f = open("README.MD", "r+")
content = f.read()
f.seek(0, 0)
f.write("COMPLETED ON: " + str(now) + '\n\n' + content)

f.close()
