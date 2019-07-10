import requests
import os
import simplejson

from dotenv import load_dotenv
load_dotenv()


def selectNewRandom(language):
    #building information necessary to make requests
    headers = {'Authorization' : os.getenv("AUTHKEY")}
    data = {'strategy' : 'random'}
    #making the request
    r = requests.post("https://www.codewars.com/api/v1/code-challenges/java/train", headers=headers, data=data)
    # parsing the json response 
    print r.status_code
    print r.content
    j = simplejson.loads(r.content)
    #ADD PARSEABLE PRINTOUT - USER CAN CHOOSE IF THEY WANT THIS TO BE CURRENT
    #building the correctly named folder
    folderBuild(j)
    #loading response to correct vars
    solutionTestCode = j['session']['exampleFixture']
    setupCode = j['session']['setup']

    #need to add language correct extension support opposed to it being static
    # writing the testing code to a file
        #finding the location of the word 'class'
    setupClassLoc = setupCode.find("class")
    solutionClassLoc = solutionTestCode.find("class")
    #finding the location of the first curly bracket '{'
    setupBracketLoc = setupCode.find("{")
    solutionBracketLoc = solutionTestCode.find("{")
    #between those two, I can find the class name
    #need to add language correct extension support opposed to it being static
    # finding the class name between the word 'class' and the bracket
    setupClassName = setupCode[setupClassLoc + 6 : setupBracketLoc - 1] + ".java"
    solutionClassName = solutionTestCode[solutionClassLoc + 6 : solutionBracketLoc - 1] + ".java"
    # making the userfile from the class name
    userFile = open(setupClassName, "w+")
    # writing the setup code
    userFile.write(setupCode)
    solutionTestFile = open(solutionClassName, "w+")
    solutionTestFile.write(solutionTestCode)

def selectNewTargeted(ID, language):
    #this method is for selecting the new kata to train
    # it needs to set it as a training kata on codewars
    # also needs to create a new folder with the right naming conventions
    r = requests.get("https://www.codewars.com/api/v1/code-chalenges/" + ID)
    # parsing the json
    j = simplejson.loads(r.content)
    # loading the json data to vars
    name = j['name']
    desc = j['description']
    # parsing the name and the difficulty
    name = "".join(name.split())
    diffNum = str(j['rank']['id'])
    # making the name of the directory out of those two vars
    dirName = diffNum[::-1] + name
    # making the directory and switching to it
    os.mkdir(dirName)
    os.chdir(dirName)
    # opening the file for writing
    f = open("README.MD", "w+")
    # writing the description to the file
    f.write(desc)

def folderBuild(j):
    # loading the json data to vars
    name = j['name']
    desc = j['description']
    # parsing the name and the difficulty
    name = "".join(name.split())
    diffNum = str(j['rank'])
    # making the name of the directory out of those two vars
    dirName = diffNum[::-1] + name
    # making the directory and switching to it
    os.mkdir(dirName)
    os.chdir(dirName)
    # opening the file for writing
    f = open("README.MD", "w+")
    # writing the description to the file
    f.write(desc)

selectNewRandom("java")

