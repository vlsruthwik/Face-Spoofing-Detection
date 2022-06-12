import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot


cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(640,360,[20,50])

points = [22,23,24,26,110,157,158,159,160,161,130,243]
ratiolist = []
blinkstate = False

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img,draw=False)
    
    if faces:
        face = faces[0]
        # for id in points:
        #     cv2.circle(img,face[id],5,(255,0,0),cv2.FILLED)
    
        leftUP = face[159]
        leftDW = face[23]
        leftL = face[130]
        leftR = face[243]
        lenV = detector.findDistance(leftUP,leftDW)
        lenHZ = detector.findDistance(leftL,leftR)
        ratio = int((lenV[0]/lenHZ[0])*100)
        ratiolist.append(ratio)
        if len(ratiolist)>10: ratiolist.pop(0)
        ratioAvg = sum(ratiolist)/len(ratiolist)
        if ratioAvg<33:
            blinkstate=True
        if blinkstate:    
            cv2.putText(img,"Verified True",(50,100),cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

        # imgplt = plotY.update(ratioAvg)
        # cv2.imshow("Image Plot",imgplt)


    cv2.imshow("Image",img)
    cv2.waitKey(25)