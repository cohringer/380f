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
        
        
    
    