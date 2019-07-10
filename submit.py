import requests
import os
import simplejson

from dotenv import load_dotenv
load_dotenv()

# auth

headers = {'Authorization' : os.getenv("AUTHKEY")}

r = requests.get("https://www.codewars.com/api/v1/code-challenges/valid-braces")

print headers

print os.getenv("AUTHKEY")

print r.status_code
result = r.json()
print r.json()

j = simplejson.loads(r.content)

print j['description']
print 
print j['name']
name = j['name']

name = "".join(name.split())
print name
print j['rank']['id']
diffNum = str(j['rank']['id'])
dirName = diffNum[::-1] + name

print dirName
try:
    os.mkdir(dirName)
except OSError, e:
    if e.errno != os.errno.EEXIST:
        raise
    pass

os.chdir(dirName)
print os.getcwd()

f = open("README.MD", "w+")
f.write(j['description'])


#trialing new code
data = {'strategy' : 'default'}

r = requests.post("https://www.codewars.com/api/v1/code-challenges/java/train", headers=headers, data=data)

# print r.json()

j = simplejson.loads(r.content)

print j['session']['setup']
print j['session']['exampleFixture']

SolutionTestCode = j['session']['exampleFixture']
setupCode = j['session']['setup']

testFile = open("SolutionTest.java", "w+")
testFile.write(SolutionTestCode)

classLoc = setupCode.find("class")
bracketPos = setupCode.find("{")

className = setupCode[classLoc + 6:bracketPos - 1] + ".java"
print "CLASS NAME IS: " + className

userFile = open(className, "w+")
userFile.write(setupCode)
# need to auto gen a main method that will run the solution test file
print j['session']



