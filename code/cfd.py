import numpy as np
import os, sys

from IPython import get_ipython
get_ipython().magic('reset -sf')

import QuickSort as QS

####################################################################

pointsFile = open("Mesh/points","r")
facesFile = open("Mesh/faces","r")
ownersFile = open("Mesh/owner","r")
neighbourFile = open("Mesh/neighbour","r")
boundaryFile = open("Mesh/boundary",'r')

####################################################################

#Reading number of points in space
line = pointsFile.readline()

# skipping through the 1st (
pointsFile.readline()


x = int(line)
####################################################################
#Total number of nodes
totalPoints = x
####################################################################

# Reading the lines from file
lines = pointsFile.readlines()

# Read only the points
strpoints = lines[0:x]

#manipulation of strings to remove unwanted characters
for i in range(0, len(strpoints)):
      strpoints[i]=strpoints[i].replace("(","")
      strpoints[i]=strpoints[i].replace(")","")
      strpoints[i]=strpoints[i].replace("\n","")
      strpoints[i] = strpoints[i].split(" ")

# initializing the points list
points = [[0 for i in range(3)] for j in range(x)]

# converting the points from string to float
for i in range(0,x):
    for j in range(0,len(strpoints[i])):
        points[i][j] = float(strpoints[i][j])

####################################################################


#Reading number of faces in space
line = facesFile.readline()

# skipping through the 1st (
facesFile.readline()


x = int(line)

####################################################################
# storing the total faces in the mesh
totalFaces = x
####################################################################

# Reading the lines from file
lines = facesFile.readlines()

# Read only the faces
strfaces = lines[0:x]

for i in range(0, len(strfaces)):
      strfaces[i]=strfaces[i].replace("("," ")
      strfaces[i]=strfaces[i].replace(")","")
      strfaces[i]=strfaces[i].replace("\n","")
      strfaces[i] = strfaces[i].split(" ")

#Initializing the face list (Needs to be imporved)
faces = [[0 for i in range(5)] for j in range(x)]

#Converting string to int
for i in range(0,x):
    for j in range(0,len(strfaces[i])):
        faces[i][j] = int(strfaces[i][j])

####################################################################

#Reading number of Onwers the face
line = ownersFile.readline()

# skipping through the 1st (
ownersFile.readline()


x = int(line)

# Reading the lines from file
lines = ownersFile.readlines()

# Read only the Owners
strOwner = lines[0:x]

for i in range(0, len(strOwner)):
      strOwner[i]=strOwner[i].replace("("," ")
      strOwner[i]=strOwner[i].replace(")","")
      strOwner[i]=strOwner[i].replace("\n","")
      strOwner[i] = strOwner[i].split(" ")

#Initializing Owners list
owners = [0 for i in range(x)]

for i in range(0,x):
    owners[i] = int(strOwner[i][0])

####################################################################

#Reading number of Neighbours for faces
line = neighbourFile.readline()


# skipping through the 1st (
neighbourFile.readline()


x = int(line)

####################################################################
#Total number of internal faces = faces with neighbours
internalFaces = x
####################################################################


  # Reading the lines from file
lines = neighbourFile.readlines()

# Read only the Neighbours
strNeighbour = lines[0:x]

for i in range(0, len(strNeighbour)):
      strNeighbour[i]=strNeighbour[i].replace("("," ")
      strNeighbour[i]=strNeighbour[i].replace(")","")
      strNeighbour[i]=strNeighbour[i].replace("\n","")
      strNeighbour[i] = strNeighbour[i].split(" ")

#Initializing the neighbour list
neighbours = [0 for i in range(x)]

#converting string to int
for i in range(0,x):
    neighbours[i] = int(strNeighbour[i][0])

####################################################################

totalBoundaryFaces = totalFaces - internalFaces

####################################################################

line = boundaryFile.readline()

x = int(line)

BoundaryPatches = x

#Initializing the neighbour list
boundaryName = [" " for i in range(x)]
boundaryType = [" " for i in range(x)]
boundarynFaces =[0 for i in range(x)]
boundaryStart =[0 for i in range(x)]


i = 0
ReadName = 0
ReadType = 0
ReadnFaces = 0
ReadStart = 0

while i<x:
    line = boundaryFile.readline()
    line = line.split()
    for word in line:
        word = word.replace(";","")
        if word =="(" or word == "}":
            ReadName = 1
            continue
        if ReadName == 1:
            boundaryName[i] = word
            ReadName = 0
            ReadnFaces = 1
            continue
        if word == "empty" or word =="patch" or word == "wall" :
            boundaryType[i] = word
            ReadType = 0
        if word == "nFaces" and ReadnFaces == 1:
            ReadnFaces = 2
            continue
        if ReadnFaces == 2:
            boundarynFaces[i] = int(word)
            ReadnFaces = 0
            ReadStart = 1
        if word == "startFace" and ReadStart == 1:
            ReadStart = 2
            continue
        if ReadStart == 2:
            boundaryStart[i] = int(word)
            ReadStart = 0
            i+=1


#####################################################################
## Cell Formation

FacesC = [[0 for i in range (0,2)]for j in range (0, totalFaces)]
for i in range (0,totalFaces):
    FacesC[i][0] = owners[i]
    FacesC[i][1] = i


FacesC = QS.quickSort(FacesC,0,(totalFaces-1))


nCells = FacesC[-1][0] + 1
NeiC = [[0 for i in range (0,2)]for j in range (0, internalFaces)]
for i in range (0,internalFaces):
    NeiC[i][0] = neighbours[i]
    NeiC[i][1] = i



NeiC = QS.quickSort(NeiC,0,(internalFaces-1))

###########################################################
# Surface Normal And Area calc

SF = [[0.0 for i in range(0,3)] for i in range(0,len(faces))]
Area = [0.0 for i in range (0,totalFaces)]

for i in range(0,totalFaces):

    Sx = Sy = Sz = 0

    for j in range(2,len(faces[i])-1):

        Sx = Sx + 0.5*((points[faces[i][j+1]][1] - points[faces[i][1]][1])*(points[faces[i][j]][2] - points[faces[i][1]][2])-((points[faces[i][j+1]][2] - points[faces[i][1]][2])*(points[faces[i][j]][1] - points[faces[i][1]][1])))
        Sy = Sy + 0.5*((points[faces[i][j+1]][2] - points[faces[i][1]][2])*(points[faces[i][j]][0] - points[faces[i][1]][0])-((points[faces[i][j+1]][0] - points[faces[i][1]][0])*(points[faces[i][j]][2] - points[faces[i][1]][2])))
        Sz = Sz + 0.5*((points[faces[i][j+1]][0] - points[faces[i][1]][0])*(points[faces[i][j]][1] - points[faces[i][1]][1])-((points[faces[i][j+1]][1] - points[faces[i][1]][1])*(points[faces[i][j]][0] - points[faces[i][1]][0])))

    SF[i] = [Sx,Sy,Sz]

    Area[i] = (Sx**2 + Sy**2 + Sz**2)**0.5

######################################################################
## Cell CG, Centroid and Volume

CG = [[0 for i in range(0,3)]for i in range(0,nCells)]

Centroid = [[0 for i in range(0,3)]for i in range(0,nCells)]

jOwn = iOwn = 0
jNei = iNei = 0

Volume = [0.0 for i in range(0,nCells)]

for i in range(0,nCells):

    Vx = Vy = Vz = n = CGx = CGy = CGz = 0

    while jOwn != totalFaces  and FacesC[jOwn][0] == i :

        for j in range(1,len(faces[FacesC[jOwn][1]])):

            CGx += points[faces[FacesC[jOwn][1]][j]][0]
            CGy += points[faces[FacesC[jOwn][1]][j]][1]
            CGz += points[faces[FacesC[jOwn][1]][j]][2]

            n += 1

        jOwn += 1

    while jNei != internalFaces and NeiC[jNei][0] == i:

        for j in range(1,len(faces[FacesC[jNei][1]])):

            CGx += points[faces[NeiC[jNei][1]][j]][0]
            CGy += points[faces[NeiC[jNei][1]][j]][1]
            CGz += points[faces[NeiC[jNei][1]][j]][2]
            n += 1

        jNei += 1

    CG[i] = [CGx/n,CGy/n,CGz/n]


    while iOwn != totalFaces  and FacesC[iOwn][0] == i :

        Sx = Sy = Sz = 0
        CGx = CGy = CGz = CEx = CEy = CEz = 0

        for j in range(2,(faces[FacesC[iOwn][1]][0])):

            CGx = (points[faces[FacesC[iOwn][1]][j+1]][0] + points[faces[FacesC[iOwn][1]][j]][0] + points[faces[FacesC[iOwn][1]][1]][0])/3
            CGy = (points[faces[FacesC[iOwn][1]][j+1]][1] + points[faces[FacesC[iOwn][1]][j]][1] + points[faces[FacesC[iOwn][1]][1]][1])/3
            CGz = (points[faces[FacesC[iOwn][1]][j+1]][2] + points[faces[FacesC[iOwn][1]][j]][2] + points[faces[FacesC[iOwn][1]][1]][2])/3

            Sx = Sx + 0.5*((points[faces[FacesC[iOwn][1]][j+1]][1] - points[faces[FacesC[iOwn][1]][1]][1])*(points[faces[FacesC[iOwn][1]][j]][2] - points[faces[FacesC[iOwn][1]][1]][2])-((points[faces[FacesC[iOwn][1]][j+1]][2] - points[faces[FacesC[iOwn][1]][1]][2])*(points[faces[FacesC[iOwn][1]][j]][1] - points[faces[FacesC[iOwn][1]][1]][1])))
            Sy = Sy + 0.5*((points[faces[FacesC[iOwn][1]][j+1]][2] - points[faces[FacesC[iOwn][1]][1]][2])*(points[faces[FacesC[iOwn][1]][j]][0] - points[faces[FacesC[iOwn][1]][1]][0])-((points[faces[FacesC[iOwn][1]][j+1]][0] - points[faces[FacesC[iOwn][1]][1]][0])*(points[faces[FacesC[iOwn][1]][j]][2] - points[faces[FacesC[iOwn][1]][1]][2])))
            Sz = Sz + 0.5*((points[faces[FacesC[iOwn][1]][j+1]][0] - points[faces[FacesC[iOwn][1]][1]][0])*(points[faces[FacesC[iOwn][1]][j]][1] - points[faces[FacesC[iOwn][1]][1]][1])-((points[faces[FacesC[iOwn][1]][j+1]][1] - points[faces[FacesC[iOwn][1]][1]][1])*(points[faces[FacesC[iOwn][1]][j]][0] - points[faces[FacesC[iOwn][1]][1]][0])))

            Vec = (CG[i][0] - points[faces[FacesC[iOwn][1]][1]][0])*(Sx) + (CG[i][1]-points[faces[FacesC[iOwn][1]][1]][1])*Sy + (CG[i][2]-points[faces[FacesC[iOwn][1]][1]][2])*Sz

            BArea = (Sx**2 + Sy**2 + Sz**2)**0.5

            CEx += 0.75*CGx + 0.25*(CG[i][0] - CGx)
            CEy += 0.75*CGy + 0.25*(CG[i][1] - CGy)
            CEz += 0.75*CGz + 0.25*(CG[i][2] - CGz)

            Vol = Vec*BArea/3

            Vx += CEx*Vol
            Vy += CEy*Vol
            Vz += CEz*Vol

            Volume[i] += Vol

        iOwn += 1

    while iNei != internalFaces and NeiC[iNei][0] == i:

        Sx = Sy = Sz = 0
        CGx = CGy = CGz = CEx = CEy = CEz = 0

        for j in range(2,len(faces[NeiC[iNei][1]])-1):

            CGx = (points[faces[NeiC[iNei][1]][j+1]][0] + points[faces[NeiC[iNei][1]][j]][0] + points[faces[NeiC[iNei][1]][1]][0])/3
            CGy = (points[faces[NeiC[iNei][1]][j+1]][1] + points[faces[NeiC[iNei][1]][j]][1] + points[faces[NeiC[iNei][1]][1]][1])/3
            CGz = (points[faces[NeiC[iNei][1]][j+1]][2] + points[faces[NeiC[iNei][1]][j]][2] + points[faces[NeiC[iNei][1]][1]][2])/3


            Sx = Sx + 0.5*((points[faces[NeiC[iNei][1]][j+1]][1] - points[faces[NeiC[iNei][1]][1]][1])*(points[faces[NeiC[iNei][1]][j]][2] - points[faces[NeiC[iNei][1]][1]][2])-((points[faces[NeiC[iNei][1]][j+1]][2] - points[faces[NeiC[iNei][1]][1]][2])*(points[faces[NeiC[iNei][1]][j]][1] - points[faces[NeiC[iNei][1]][1]][1])))
            Sy = Sy + 0.5*((points[faces[NeiC[iNei][1]][j+1]][2] - points[faces[NeiC[iNei][1]][1]][2])*(points[faces[NeiC[iNei][1]][j]][0] - points[faces[NeiC[iNei][1]][1]][0])-((points[faces[NeiC[iNei][1]][j+1]][0] - points[faces[NeiC[iNei][1]][1]][0])*(points[faces[NeiC[iNei][1]][j]][2] - points[faces[NeiC[iNei][1]][1]][2])))
            Sz = Sz + 0.5*((points[faces[NeiC[iNei][1]][j+1]][0] - points[faces[NeiC[iNei][1]][1]][0])*(points[faces[NeiC[iNei][1]][j]][1] - points[faces[NeiC[iNei][1]][1]][1])-((points[faces[NeiC[iNei][1]][j+1]][1] - points[faces[NeiC[iNei][1]][1]][1])*(points[faces[NeiC[iNei][1]][j]][0] - points[faces[NeiC[iNei][1]][1]][0])))

            Vec = (CG[i][0]-points[faces[NeiC[iNei][1]][1]][0])*(Sx) + (CG[i][1]-points[faces[NeiC[iNei][1]][1]][1])*Sy + (CG[i][2]-points[faces[NeiC[iNei][1]][1]][2])*Sz

            BArea = (Sx**2 + Sy**2 + Sz**2)**0.5

            CEx += 0.75*CGx + 0.25*(CG[i][0] - CGx)
            CEy += 0.75*CGy + 0.25*(CG[i][1] - CGy)
            CEz += 0.75*CGz + 0.25*(CG[i][2] - CGz)

            Vol = (-1)*Vec*BArea/3

            Vx += CEx*Vol
            Vy += CEy*Vol
            Vz += CEz*Vol

            Volume[i] += Vol

        iNei += 1

    CEx = Vx/Volume[i]
    CEy = Vy/Volume[i]
    CEz = Vz/Volume[i]

    Centroid[i] = [Vx/Volume[i],Vy/Volume[i],Vz/Volume[i]]

#######################################################################
