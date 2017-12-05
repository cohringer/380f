from Functions import *
import cv2
import time
import easygopigo3 as easy
gpg=easy.EasyGoPiGo3()
ds=gpg.init_distance_sensor()
sv=gpg.init_servo()
s=-13 #servo correction
from picamera import PiCamera
from picamera.array import PiRGBArray
camera=PiCamera()

def interpreter():
    gpg.set_eye_color((255,255,255))
    index=3
    dest=0
    while dest==0:
        ans=numDots('filePath') #placeholder, it'll have to be taken in from the camera
        if ans==1:
            gpg.open_left_eye()
            time.sleep(.5)
            gpg.close_left_eye()
            gpg.turn_degrees(-90,True)
            gpg.drive_inches(12,True)
            gpg.turn_degrees(90,True)
            index-=1
        elif ans==2:
            open_right_eye()
            time.sleep(.5)
            close_right_eye()
            gpg.turn_degrees(-90,True)
            gpg.drive_inches(12,True)
            gpg.turn_degrees(90,True)
            index+=1
        else:
            dest=True
            gpg.set_eye_color((255,0,0))
            for i in index:
                gpg.open_left_eye()
                gpg.time.sleep(.5)
                gpg.close_left_eye()
            gpg.set_eye_color((0,0,255))
            for i in ans:
                gpg.open_left_eye()
                gpg.time.sleep(.5)
                gpg.close_left_eye()
            return ans

def maze():
    #Looks like the maze isn't solveable through wall following
    #Well, maybe if we treat the walls like obstacles we want to go around we can
    #Apparently this is a thing, Pledge's Alg.
    sv.rotate_servo(180+s) #point right
    while !dest:
        #have to rotate the servo back and forth to make sure it doesn't crash into a wall ahead of it
        d=ds.read_in()
        gpg.drive_inches(3) #can be changed
        dt+=3
        if d>7: #assume we're kinda near the middle of the course, change this value in testing
            gpg.turn_degrees(90,True) #always turn right
            
        #check the wikipedia article on maze solvers, basically once you get around an obstacle you pick an arbitrary direction to go in
        #We can also do bounds checking since we know the maze is 5x5
        
def destroy()
    dest1=0
    dest2=0
    dest3=0
    begin=True
    while dest1==0:
        #first waypoint
        if begin==True:
            gpg.drive_inches(12)
            gpg.turn_degrees(90,True)
            gpg.drive_inches(36)
            gpg.turn_degrees(-90,True)
            d=ds.read_in()
            begin=False
        if d<4: #Check to see if we're close enough to the folder
            camera.capture('folder.png')
            color=topColor('folder.png')
            BothBlink(color)
            dest1=1
        else: 
            gpg.drive_inches(1)
            d=ds.read_in()
    while dest2==0:
        #second waypoint
        #This is where we're most likely to hit obstacles, so let's implement some distance checking
        d=0
        gpg.turn_degrees(90,True)
        sv.rotate_servo(167)
        trav=0
        while ds.read_in()>5:
            if trav<12:
                gpg.drive_in(2)
                trav+=2
                trav1=0
            elif trav==12: #ensure one turn
                gpg.turn_degrees(90,True)
                trav+=1
            if trav1<36:
                gpg.drive_in(2)
                trav1+=2
                trav2=0
            elif trav1==36:
                gpg.turn_degrees(90,True)
                trav1+=1
                sv.rotate_servo(103)
            if trav2<12:
                gpg.drive_in(2)
                trav2+=2
            elif trav2==12:
                gpg.turn_degrees(90,True)
                trav2+=1
                break
        if d<4: #Check to see if we're close enough to the folder
            camera.capture('folder1.png')
            color=topColor('folder1.png')
            BothBlink(color)
            dest2=1
        else: 
            gpg.drive_inches(1)
            d=ds.read_in()
    jail=True #aka still have to be careful about obstacles
    while dest3==0:
        while jail:
            trav=0
            trav1=60 #won't trigger prematurely
            trav2=60
            while ds.read_in()>5:
                if trav==0:
                    gpg.turn_degrees(90,True)
                    sv.rotate_servo(13)
                    trav+=2
                elif trav<14 && trav!=0:
                    gpg.drive_in(2)
                    trav+=2
                elif trav==14:
                    gpg.turn(-90,True)
                    trav1=0
                    trav+=1
                if trav1<36:
                    gpg.drive_in(2)
                    trav1+=2
                elif trav1==36:
                    gpg.turn_degrees(-90,True)
                    trav2=0
                    trav1+=1
                if trav2<24:
                    gpg.drive_in(2)
                    trav2+=2
                elif trav2==24:
                    jail=False
                    break
        gpg.drive_in(12)
        gpg.turn_degrees(-90,True)
        gpg.drive_in(12)
        jail=True
        trav=0
        while jail:
            while ds.read_in()>5:
               if trav<24:
                    gpg.drive_in(2)
                    trav+=2
                elif trav==24:
                    gpg.turn_degrees(90,True)
                    jail=False
                    break
        gpg.drive_in(12)
        gpg.turn_degrees(90)
        camera.capture('folder1.png')
        d=ds.read_in()
        if d<4: #Check to see if we're close enough to the folder
            #insert something with the camera
            color=topColor('folder2.png')
            BothBlink(color)
            dest3=1
        else: 
            gpg.drive_inches(1)
            d=ds.read_in()
            
def Interpreter_1():#NOTES: need to add angle/spin corrections to everything that wasn't my test case
    sv.rotate_servo(90+ServoCorrection)
    First_Dist=MedianRead_mm()*mm2in
    correctiondist=First_Dist-24
    gpg.drive_inches(correctiondist)#lines up at 24 in
    gpg.drive_inches(24-16)#optimal picture taking distance
    camera.capture("Middle.png")
    MiddleCase=numDots("Middle.png")
    print(MiddleCase)
    if((MiddleCase>2) and (MiddleCase<7)):#this is the answer @index 3
            BothBlink(RGBred)
            BothBlink(RGBred)
            BothBlink(RGBred)
            for i in range(0,MiddleCase):
                    BothBlink(RGBblue)
    elif (MiddleCase==1):#answer lies to the left
            gpg.turn_degrees(-90+5,True)
            gpg.set_speed(300)
            gpg.drive_inches(28+2)#drive to the box at index 1. doesnt do it perfectly, had to add 2
            gpg.turn_degrees(90+10,True)#doesn't spin perfectly, had to adjust
            Second_Dist=MedianRead_mm()*mm2in
            correctiondist=Second_Dist-16
            gpg.drive_inches(correctiondist)
            camera.capture("Second.png")
            SecondCase=numDots("Second.png")
            print(SecondCase)
            if((SecondCase>2) and (SecondCase<7)):#this is the answer @index 1
                    BothBlink(RGBred)
                    for i in range(0,SecondCase):
                            BothBlink(RGBblue)
            elif (SecondCase==1):#answer lies to the left
                    gpg.turn_degrees(-90,True)
                    gpg.set_speed(300)
                    gpg.drive_inches(14+2)#drive to the box at index 0. doesnt do it perfectly, had to add 2
                    gpg.turn_degrees(90,True)
                    Second_Dist=MedianRead_mm()*mm2in
                    correctiondist=Second_Dist-16
                    gpg.drive_inches(correctiondist)
                    #arrived @ind 0
                    camera.capture("Third.png")
                    ThirdCase=numDots("Third.png")
                    print(ThirdCase)
                    #don't blink red, because index=0
                    for i in range(0,ThirdCase):
                            BothBlink(RGBblue)
            elif(SecondCase==2):#answer lies to the right
                    gpg.turn_degrees(90,True)
                    gpg.set_speed(300)
                    gpg.drive_inches(14+2)#drive to the box at index 2. doesnt do it perfectly, had to add 2
                    gpg.turn_degrees(-90,True)
                    Second_Dist=MedianRead_mm()*mm2in
                    correctiondist=Second_Dist-16
                    gpg.drive_inches(correctiondist)
                    #arrived @ind 2
                    camera.capture("Third.png")
                    ThirdCase=numDots("Third.png")
                    print(ThirdCase)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    for i in range(0,ThirdCase):
                            BothBlink(RGBblue)
    elif(MiddleCase==2):#answer lies to the right
            gpg.turn_degrees(90,True)
            gpg.set_speed(300)
            gpg.drive_inches(28+2)#drive to the box at index 5. doesnt do it perfectly, had to add 2
            gpg.turn_degrees(-90,True)
            Second_Dist=MedianRead_mm()*mm2in
            correctiondist=Second_Dist-16
            gpg.drive_inches(correctiondist)
            camera.capture("Second.png")
            SecondCase=numDots("Second.png")
            print(SecondCase)
            if((SecondCase>2) and (SecondCase<7)):#this is the answer @index 5
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    for i in range(0,SecondCase):
                            BothBlink(RGBblue)
            elif(SecondCase==1):#answer lies to the left
                    gpg.turn_degrees(-90,True)
                    gpg.set_speed(300)
                    gpg.drive_inches(14+2)#drive to the box at index 4. doesnt do it perfectly, had to add 2
                    gpg.turn_degrees(90,True)
                    Second_Dist=MedianRead_mm()*mm2in
                    correctiondist=Second_Dist-16
                    gpg.drive_inches(correctiondist)
                    #arrived @ind 4
                    camera.capture("Third.png")
                    ThirdCase=numDots("Third.png")
                    print(ThirdCase)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    for i in range(0,ThirdCase):
                            BothBlink(RGBblue)
            elif(SecondCase==2):#answer lies to the right
                    gpg.turn_degrees(90,True)
                    gpg.set_speed(300)
                    gpg.drive_inches(14+2)#drive to the box at index 6. doesnt do it perfectly, had to add 2
                    gpg.turn_degrees(-90,True)
                    Second_Dist=MedianRead_mm()*mm2in
                    correctiondist=Second_Dist-16
                    gpg.drive_inches(correctiondist)
                    #arrived @ind 6
                    camera.capture("Third.png")
                    ThirdCase=numDots("Third.png")
                    print(ThirdCase)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    BothBlink(RGBred)
                    for i in range(0,ThirdCase):
                            BothBlink(RGBblue)
    else:pass#retest, add code later-get closer, go left, go right? add condition(==0?)                            
def LeftWink(RGBval):#NOTE: for whatever reason, the open_right_eye method opens the left eye, and vice versa. these wink methods correct for that.
    gpg.set_right_eye_color(RGBval)
    gpg.open_right_eye()
    time.sleep(.5)
    gpg.close_right_eye()
    time.sleep(.5)
def RightWink(RGBval):
    gpg.set_left_eye_color(RGBval)
    gpg.open_left_eye()
    time.sleep(.5)
    gpg.close_left_eye()
    time.sleep(.5)
def BothBlink(RGBval):
    gpg.set_right_eye_color(RGBval)
    gpg.set_left_eye_color(RGBval)
    gpg.open_eyes()
    time.sleep(.5)
    gpg.close_eyes()
    time.sleep(.5)
def MedianRead_mm():#distance sensor is unreliable, use this to get more accurate measurements
    distances=[]
    for k in range(0,10):
            distances.append(ds.read_mm())
    mediandist=median(distances)
    return mediandist  
    