from Functions import *
import cv2
import time
import easygopigo3 as easy
gpg=easy.EasyGoPiGo3()
ds=gpg.init_distance_sensor()
sv=gpg.init_servo()
s=-13 #servo correction

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
            #insert something with the camera
            color=topColor('folder1')
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
            #Insert something about the camera
            color=topColor('folder2.png')
            BothBlink(color)
            dest2=1
        else: 
            gpg.drive_inches(1)
            d=ds.read_in()
        
        
def BothBlink(RGBval):
    gpg.set_right_eye_color(RGBval)
    gpg.set_left_eye_color(RGBval)
    gpg.open_eyes()
    time.sleep(.5)
    gpg.close_eyes()
    time.sleep(.5)
        
    
    