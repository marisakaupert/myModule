

"""
import myModule
reload(myModule)
myModule.run()
"""

import logging
from collections import Counter
import maya.cmds as mc
import random as r
import time


import os
import functools
from PySide import QtGui, QtCore, QtUiTools
from shiboken import wrapInstance
import pyside_dynamic
import maya.cmds as mc 
import maya.OpenMayaUI as omui 


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def getMayaWindow():
    """ pointer to the maya main window  
    """
    ptr = omui.MQtUtil.mainWindow()
    if ptr :
        return wrapInstance(long(ptr), QtGui.QMainWindow)


def run():
    """  builds our UI
    """
    global win
    win = Homework(parent=getMayaWindow())
    win.show()

def stopwatch(func):

    def timed (*args, **kwargs):

        #start a timer
        timeStart = time.time()
        #run original function
        result = func(*args, **kwargs)

        #stop a timer
        timeEnd = time.time()
        elapsedTime = timeEnd - timeStart
        logger.debug("%2.2f sec" %(elapsedTime))
        #print the amount of time it took
        return result

    return timed





class Homework(QtGui.QDialog):
    """ This is the main class of this module """

    def __init__(self, parent=None):
        super(Homework,self).__init__(parent)

        self.greetingType = 'Hello!'

     # from pysideuic--------------------
        self.verticalLayoutWidget_2 = QtGui.QWidget()
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1041, 731))
        self.overallVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.overallVerticalLayout.setContentsMargins(6, 5, 5, 5)
        self.modelGeneratorVerticalLayout = QtGui.QVBoxLayout()
        self.modelGeneratorVerticalLayout.setContentsMargins(5, 5, 5, 5)
        self.modelGeneratorVerticalLayout.setContentsMargins(0, 0, 0, 0)

        self.robotPushButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.robotPushButton.setText("Make Robot")
        self.modelGeneratorVerticalLayout.addWidget(self.robotPushButton)

        self.spiralStairCasePushButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.spiralStairCasePushButton.setText("Make Staircases")
        self.modelGeneratorVerticalLayout.addWidget(self.spiralStairCasePushButton)

        self.randomizeModelsPushButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.randomizeModelsPushButton.setText("Make Random Models")
        self.modelGeneratorVerticalLayout.addWidget(self.randomizeModelsPushButton)

        self.robotDeployPushButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.robotDeployPushButton.setText("Make Robot Army")
        self.modelGeneratorVerticalLayout.addWidget(self.robotDeployPushButton)

        self.overallVerticalLayout.addLayout(self.modelGeneratorVerticalLayout)
        self.radioButtonHorizontalLayout = QtGui.QHBoxLayout()
        
        self.radioButtonHorizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.helloRadioButton = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.helloRadioButton.setText("Hello!")

        self.radioButtonHorizontalLayout.addWidget(self.helloRadioButton)
        self.howdyRadioButton = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.howdyRadioButton.setText("Howdy")

        self.radioButtonHorizontalLayout.addWidget(self.howdyRadioButton)
        self.greetingsRadioButton = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.greetingsRadioButton.setText("Greetings Earthling...")

        self.radioButtonHorizontalLayout.addWidget(self.greetingsRadioButton)
        self.overallVerticalLayout.addLayout(self.radioButtonHorizontalLayout)
        self.customGreetingHorizontalLayout = QtGui.QHBoxLayout()
        self.customGreetingHorizontalLayout.setContentsMargins(5, 5, 5, 5)

        self.customGreetingCheckBox = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.customGreetingCheckBox.setText("Make Custom Greeting:")
        self.customGreetingHorizontalLayout.addWidget(self.customGreetingCheckBox)
        self.customGreeetingLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)

        self.customGreetingHorizontalLayout.addWidget(self.customGreeetingLineEdit)
        self.overallVerticalLayout.addLayout(self.customGreetingHorizontalLayout)
        self.createGreetingPushButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.createGreetingPushButton.setText("Create Greeting")

        self.overallVerticalLayout.addWidget(self.createGreetingPushButton)
        self.mostCommonWordsHorizontalLayout = QtGui.QHBoxLayout()
        self.mostCommonWordsHorizontalLayout.setContentsMargins(5, 5, 5, 5)

        self.threeMostCommonWordsPushButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.threeMostCommonWordsPushButton.setText("Create Three Most Common Words")
        self.mostCommonWordsHorizontalLayout.addWidget(self.threeMostCommonWordsPushButton)

        self.textFileLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.textFileLabel.setText("File:")
        self.mostCommonWordsHorizontalLayout.addWidget(self.textFileLabel)

        self.browserLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.mostCommonWordsHorizontalLayout.addWidget(self.browserLineEdit)
        self.browserPushButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.browserPushButton.setText("...")

        self.mostCommonWordsHorizontalLayout.addWidget(self.browserPushButton)
        self.overallVerticalLayout.addLayout(self.mostCommonWordsHorizontalLayout)

        #many things you have to add
        self.makeConnections()
        self.setWindowTitle("Geometry Generator")
        self.setLayout(self.overallVerticalLayout)
        self.initStateOfUI()
        self.show()



    def makeConnections(self):
        """ connect events in the UI """
        self.robotPushButton.clicked.connect( self.makeRobot  )
        self.spiralStairCasePushButton.clicked.connect( 
            functools.partial(self.makeStairCase, 20 ) )

        self.randomizeModelsPushButton.clicked.connect(
            functools.partial(self.randomDeploy))

        self.robotDeployPushButton.clicked.connect(
            functools.partial(self.robotDeploy, 5, 5, 8))

        self.helloRadioButton.clicked.connect(
            functools.partial(self.radioChange, 'Hello!'))
        self.howdyRadioButton.clicked.connect(
            functools.partial(self.radioChange, 'Howdy'))
        self.greetingsRadioButton.clicked.connect(
            functools.partial(self.radioChange, 'Greetings Earthlings...'))

        self.customGreetingCheckBox.stateChanged.connect(
            self.customGreeetingLineEdit.setEnabled)

        self.createGreetingPushButton.clicked.connect( self.createGreeting )


        self.browserPushButton.clicked.connect(self.findTextFile)

        self.threeMostCommonWordsPushButton.clicked.connect(
            self.generateCommonWords)


    def initStateOfUI(self):
        """ sets state of UI """
        self.helloRadioButton.toggle()
        self.customGreeetingLineEdit.setEnabled(False)
        self.customGreeetingLineEdit.setPlaceholderText("Custom Greeting Here")

    def findTextFile(self):
        """ Browse to find a file """
        fileNames = None
        dialog = QtGui.QFileDialog(directory = os.path.dirname(__file__))
        if dialog.exec_():
            fileNames = dialog.selectedFiles()

        if fileNames:
            print(fileNames)
            self.browserLineEdit.setText(fileNames[0])

    def generateCommonWords(self):
        pathToFile = self.browserLineEdit.text()
        self.readFile(pathToFile)

    def radioChange(self, greetingType):
        self.greetingType = greetingType



    def createGreeting(self):

        finalGreeting = self.greetingType

        if self.customGreetingCheckBox.isChecked():
            # get a custom name
            customGreeting = self.customGreeetingLineEdit.text()

            if self.customGreeetingLineEdit.text() == "":
                print("Greeting Text: Hello!")

            elif customGreeting != "Custom Greeting Here":
                finalGreeting = customGreeting
                print("Greeting Text: {0}".format(finalGreeting))

        else:
            print("Greeting Text: {0}".format(finalGreeting))

    def getFilePath(self):
        dialog = QtGui.QFileDialog(self, directory=os.path.dirname(__file__))
        if dialog.exec_():
            fileNames = dialog.selectedFiles()

        print("File Name: {0}".format(fileNames))


    @stopwatch
    def makeRobot(self):
        """
        Function to model a robot.
        
        This function creates a robot out of primitive 
        geometry,then stores all of the geometry in 
        a master group.  
        """
        
        # TORSO
        torso = mc.polyPrism(ch=False, name="torso")
        mc.setAttr(torso[0] + ".translateY", 2.5)
        mc.setAttr(torso[0] + ".rotateY", -90)
        mc.setAttr(torso[0] + ".scale", 3, .92, 3)
        
        # HIPS
        hips = mc.polyCylinder(ch=False, name="hips")
        mc.setAttr(hips[0] + ".translateY", 1.53)
        mc.setAttr(hips[0] + ".scale", .85, .05, .85)
        
        # LEFT LEG
        leftLeg = mc.polyCylinder(ch=False, name="leftLeg")
        mc.setAttr(leftLeg[0] + ".translate", .5, 1, 0)
        mc.setAttr(leftLeg[0] + ".rotateZ", 20)
        mc.setAttr(leftLeg[0] + ".scale", .12, .6, .12)
        
        # LEFT ANKLE
        leftAnkle = mc.polyCylinder(ch=False, name="leftAnkle")
        mc.setAttr(leftAnkle[0] + ".translate", .67, .58, 0)
        mc.setAttr(leftAnkle[0] + ".rotateZ", 20)
        mc.setAttr(leftAnkle[0] + ".scale", .23, .23, .23)
        
        # LEFT FOOT
        leftFoot = mc.polySphere(ch=False, name="leftFoot")
        mc.setAttr(leftFoot[0] + ".translate", .80, .24, 0)
        mc.setAttr(leftFoot[0] + ".rotateZ", 20)
        mc.setAttr(leftFoot[0] + ".scale", .49, .49, .4)
        
        # RIGHT LEG
        rightLeg = mc.polyCylinder(ch=False, name="rightLeg")
        mc.setAttr(rightLeg[0] + ".translate", .5, 1, 0)
        mc.setAttr(rightLeg[0] + ".rotateZ", 20)
        mc.setAttr(rightLeg[0] + ".scale", .12, .6, .12)
        
        # RIGHT ANKLE
        rightAnkle = mc.polyCylinder(ch=False, name="rightAnkle")
        mc.setAttr(rightAnkle[0] + ".translate", .67, .58, 0)
        mc.setAttr(rightAnkle[0] + ".rotateZ", 20)
        mc.setAttr(rightAnkle[0] + ".scale", .23, .23, .23)
        
        # RIGHT FOOT
        rightFoot = mc.polySphere(ch=False, name="rightFoot")
        mc.setAttr(rightFoot[0] + ".translate", .80, .24, 0)
        mc.setAttr(rightFoot[0] + ".rotateZ", 20)
        mc.setAttr(rightFoot[0] + ".scale", .49, .49, .4)
        
        # CREATES A RIGHT LEG GROUP FOR ROTATION
        mc.select(d=True)
        
        rtLegGroup = mc.group(em=True, name="rtLegGroup")
        rightLeg = mc.parent(rightLeg[0], rtLegGroup)
        rightAnkle = mc.parent(rightAnkle[0], rtLegGroup)
        rightFoot = mc.parent(rightFoot[0], rtLegGroup)
        mc.setAttr(rtLegGroup + ".scaleX", -1.0)
        
        # DELETES RIGHT LEG GROUP
        rightLeg = mc.parent(rightLeg[0], world=True)
        rightAnkle = mc.parent(rightAnkle[0], world=True)
        rightFoot = mc.parent(rightFoot[0], world=True)
        mc.delete(rtLegGroup)
        
        # GEAR BOX
        gearBox = mc.polyCube(ch=False, name="gearBox")
        mc.setAttr(gearBox[0] + ".translate", .2, 2.8, 1.4)
        mc.setAttr(gearBox[0] + ".rotateY", 58)
        mc.setAttr(gearBox[0] + ".scale", .4, .4, .04)
        
        # LEFT ARM
        leftArm = mc.polyCylinder(ch=False, name="leftArm")
        mc.setAttr(leftArm[0] + ".translate", 1.89, 3, 0)
        mc.setAttr(leftArm[0] + ".rotateZ", 90)
        mc.setAttr(leftArm[0] + ".scale", .21, 1.2, .21)
        
        # RIGHT ARM
        rightArm = mc.polyCylinder(ch=False, name="rightArm")
        mc.setAttr(rightArm[0] + ".translate", -1.89, 3, 0)
        mc.setAttr(rightArm[0] + ".rotateZ", 90)
        mc.setAttr(rightArm[0] + ".scale", .21, 1.2, .21)
        
        #Left Shoulder
        leftShoulder = mc.polyTorus(ch=False, name="leftShoulder")
        mc.setAttr(leftShoulder[0] + ".translate", 1.2, 2.95, -0.08)
        mc.setAttr(leftShoulder[0] + ".rotate", -32, 0, 90)
        mc.setAttr(leftShoulder[0] + ".scale", .35, .35, .35)
        
        #Right Shoulder
        rightShoulder = mc.polyTorus(ch=False, name="rightShoulder")
        mc.setAttr(rightShoulder[0] + ".translate", -1.2, 2.95, -0.08)
        mc.setAttr(rightShoulder[0] + ".rotate", -32, 0, -90)
        mc.setAttr(rightShoulder[0] + ".scale", .35, .35, .35)
        
        # LEFT HAND
        leftHand = mc.polySphere(ch=False, name="leftHand")
        mc.setAttr(leftHand[0] + ".translate", 3, 2.95, 0)
        mc.setAttr(leftHand[0] + ".scale", .4, .4, .4)
        
        # RIGHT HAND
        rightHand = mc.polySphere(ch=False, name="rightHand")
        mc.setAttr(rightHand[0] + ".translate", -3, 2.95, 0)
        mc.setAttr(rightHand[0] + ".scale", .4, .4, .4)
        
        # NECK
        neck = mc.polyCube(ch=False, name = "neck")
        mc.setAttr(neck[0] + ".translateY", 3.4)
        mc.setAttr(neck[0] + ".scale", .6, .5, .6)
        
        # HEAD
        head = mc.polyCube(ch=False, name = "head")
        mc.setAttr(head[0] + ".translate", 0, 4.5, 0.2)
        mc.setAttr(head[0] + ".scale", 2.9, 1.8, 2.8)
        
        # HEAD WIRE
        headWire = mc.polyCylinder(ch=False, name="headWire")
        mc.setAttr(headWire[0] + ".translateY", 5.7)
        mc.setAttr(headWire[0] + ".scale", .12, .5, .12)
        
        # HEAD TOP
        headTop = mc.polySphere(ch=False, name="headTop")
        mc.setAttr(headTop[0] + ".translateY", 6.35)
        mc.setAttr(headTop[0] + ".scale", .55, .55, .55)
        
        # LEFT EYE
        leftEye = mc.polyCylinder(ch=False, name="leftEye")
        mc.setAttr(leftEye[0] + ".translate", .8, 4.9, 1.57)
        mc.setAttr(leftEye[0] + ".rotateX", 90)
        mc.setAttr(leftEye[0] + ".scale", .4, .2, .4)
        
        # RIGHT EYE
        rightEye = mc.polyCylinder(ch=False, name="rightEye")
        mc.setAttr(rightEye[0] + ".translate", -0.8, 4.9, 1.57)
        mc.setAttr(rightEye[0] + ".rotateX", 90)
        mc.setAttr(rightEye[0] + ".scale", .4, .2, .4)
        
        # MOUTH
        mouth = mc.polyCube(ch=False, name="mouth")
        mc.setAttr(mouth[0] + ".translate", 0, 4.35, 1.57)
        mc.setAttr(mouth[0] + ".scale", 1, .3, .3)
        
        # PUTS ALL PARTS INTO A LIST
        bodyParts = [torso, hips, leftLeg, leftAnkle, leftFoot, rightLeg, rightAnkle,
                    rightFoot, gearBox, leftArm, leftShoulder, leftHand, rightArm,
                    rightShoulder, rightHand,neck, head, headWire, headTop, leftEye,
                    rightEye, mouth]
        
        # CREATES THE EMPTY MASTER GROUP
        mc.select(d=True)
        robotGroup = mc.group(em=True, name="robotGroup{0}".format(1))
        
        
        # PARENTS EACH BODY PART TO THE MASTER GROUP
        for obj in bodyParts:
            parts = mc.parent(obj, robotGroup)
        
        return robotGroup


    @stopwatch
    def makeStairCase(self, numSteps, settings=None):
        """
        Function to create a spiral staircase.
        
        This function creates a spiral staircase using
        the main settings below, then parenting all geometry 
        in a group to set rotation, and finally storing 
        everything in a master group.  
        """
        
        # SETTINGS
        settings = {'degrees': 20,
        'spread': 5,
        'stepHeight': 0.5,
        'stepLength': 1.4,
        'stepName': 'spiral' 
        }

        # GET THE ROTATION
        ro = settings.get("degrees")
        
        # GET THE SPREAD
        spread = settings.get("spread") 
        
        # GET THE HEIGHT
        height = settings.get("stepHeight")
        
        # GET THE LENGTH
        length = settings.get("stepLength")
        
        # GET THE NAME
        name = settings.get("stepName")
        
        # CREATES EMPTY MASTER GROUP
        mc.select(d=True)
        stairGroup = mc.group(em=True, name="stairGroup{0}".format(1))
        # numSteps = int(r.random()*(stepMaximum-stepMinimum))
        
        # CREATES A LOOP TO MAKE EACH INDIVIDUAL STAIR
        for x in range(numSteps):
            cube,cubeHist = mc.polyCube(n=name + "{0}".format(x+1))
            mc.setAttr(cube + ".translateZ", 2)
            mc.setAttr(cube + ".scale", length,height,spread)
            
            # CREATES AN EMPTY GROUP THEN PARENTS EACH STAIR TO THE GROUP
            mc.select(d=True)
            spiralGroup = [mc.group(em=True, name="spiralGroup{0}".format(x+1))]
            cube = mc.parent(cube, spiralGroup)
                
            # IF X > 0, THEN EACH STAIR MOVES UP AND ROTATES TO CREATE THE SPIRAL EFFECT
            if x > 0:
                mc.setAttr(spiralGroup[0] + ".translateY", x*0.5)
                mc.setAttr(spiralGroup[0] + ".rotateY", x*ro)
           
           
            # PARENTS ALL OF THE SPIRALGROUPS INTO THE MASTER GROUP
            for obj in spiralGroup:
                mc.parent(obj, stairGroup)
            
        return stairGroup
        return spiralGroup

    @stopwatch
    def randomDeploy(self,numOfRandomModels=None, stepMinimum=20, stepMaximum=90):
        """ 
        Function randomly makes staircases or robots 
        depending on the user's number.

        This function calls the makeRobot() and makeStairCases() 
        functions to randomly generate either models and place 
        them randomly in space. 
        """ 

        # SETS THE ROBOT AND STAIRCASE COUNT TO 0
        robots = 0
        stairs = 0


        #INSTANTIATES numOfRandomModels
        numOfRandomModels = int(r.random()*(stepMaximum-stepMinimum))

        # RANDOMIZES THE NUMBER OF STAIRCASES AND MODELS MADE 
        for i in range(numOfRandomModels):
            selector = int(r.random() * 2)
            randX = int(r.uniform(-50, 50) )
            randY = int(r.uniform(-50, 50)  )
            randZ = int(r.uniform(-50, 50)  )
            
            # CREATES ROBOTS, FINDS ALL THE GROUPS AND RANDOMIZES POSITION
            if selector == 0:
                robotMaker = self.makeRobot()
                robots += 1
                mc.setAttr("{0}.translate".format(robotMaker), randX,randY,randZ)
                
            # CREATES STAIRS, FINDS ALL THE GROUPS AND RANDOMIZES POSITION
            else:
                numSteps = int(r.random()*(stepMaximum-stepMinimum))
                stairGroupMaker = self.makeStairCase(numSteps)
                stairs += 1
                mc.setAttr("{0}.translate".format(stairGroupMaker), randX,randY,randZ)


    @stopwatch
    def robotDeploy(self,row,column,increment):
        """ 
        Function to create an army of robots.

        Creates robots in rows and columns based on the two 
        input parameters. The increment argument spaces
        the robots out. This project was fun, so I made this
        extra function. :) 
        """

        robots = 0

        # INITIAL POSITION OF X AND Z
        x = -5
        z = -10

        # MAKES ROWS AND COLUMNS OF KILLER ROBOTS
        for i in range(row):
            for j in range(column):
                army = self.makeRobot()
                robots += 1
                mc.select("robotGroup{0}".format(robots), ne=True)
                mc.setAttr("{0}.translate".format(army), x,0,z)
                z += increment
            x += increment
            z = -10


    def readFile(self,inFile=None):
        """ Function that reads a file and adds them to a list.
        
        This function specifically reads a file (In this case, Einstein's creedo) and adds
        it to a master list, which is then easier to count and manipulate. This also calls and uses the other
        functions needed to make the text curves and polygons. 
        """

        text = []
        punctuationChars = [".", ",", "\n", "!", ";", ":",'\"']
        with open(inFile, 'r') as fin:
            for line in fin:
                for punc in punctuationChars:
                    line = line.replace(punc, "")
                chunks = line.split(" ")
                for item in chunks:
                    if item != '':
                        text.append(item)
                
        mostCommon = self.countWords(text, 3)
        print(mostCommon)
            
        words = self.makeWords(mostCommon)
        return(words)   
        
    def countWords(self,text, n):
        """ Function to count the words and order them from most common to least common.
        
        Using the collections class in Maya, this easily counts the msot used words in the 
        text and stores them into tuples. 
        """
        return(Counter(text).most_common(n)) 
        
    def makeWords(self,mostCommon,font='Comic Sans MS'):
        """ Function to make the text curves of the three most common words
        
        Function to go through the list of the most common used words 
        and order them from greatest to least, the most common starting on top. 
        """

        for i in range(0,len(mostCommon)):
            curves = mc.textCurves(n="word{0}".format(1), f=font, t=mostCommon[i][0], ch=True)
            mc.setAttr(curves[0] + ".translateY", (len(mostCommon)-i) * 0.5)
            mc.select(ne=True)
            mc.planarSrf(n="Trim Char {0}".format(curves), ko=False, d=1, po=1)
            
            

