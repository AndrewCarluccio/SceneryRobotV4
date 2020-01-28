#SCENERY ROBOT V4 Firmware
#for UVA Stage Robotics Project
#Code Manager: Andy Carluccio - akclucc@gmail.com
#Programmers:
#Sai Raj

#Libraries
from roboclaw import Roboclaw #roboclaw library left adjancent to this module
import select
import sys


# address of the RoboClaw as set in Motion Studio
address = 128

# Creating the RoboClaw object, serial port and baudrate passed
roboclaw = Roboclaw("/dev/ttyS0", 115200)

# Starting communication with the RoboClaw hardware
roboclaw.Open()

#FUNCTIONS------------------------------------------------------

#Get cues from the server and save them to local memory
def pull_cues():
    return 1

#Takes movement parameters and calls on Roboclaw to complete
def drive(args):
    return 1

#Returns the encoder data for a particular motor
def get_encoder_data(enc_id):
    return 1

#Publish data to the server
def publish_data(page, data):
    return 1

#Generic function to stop the robot
def stop():
    roboclaw.ForwardM1(address, 0)
    roboclaw.ForwardM2(address, 0)

#Activate the current cue on deck, advance the rest, update previous, etc.
def go():
    return 1

#Trigger homing system to remove accumulated error (hardware support pending)
def home():
    return 1

#Reads an input file and sets up a server with ip information, etc.
def config_server(input_file):
    return 1

#Sets a particular SPI pin HIGH or LOW for external devices
def pin_mode(pin, val):
    return 1

#Execution loop
while(True):
    #For the sake of demo, a simple text-based control system:
    var = raw_input("Please Enter a drive command: ")
    print("You entered", var)
    words = var.split()
    print(words)
    if (words[0] == "forward"):
        if(words[1] == "1"):
            print("going forward")
            speed = int(words[2])
            roboclaw.ForwardM1(address, speed)
        elif(words[1] == "2"):
            speed = int(words[2])
            roboclaw.ForwardM2(address, speed)
        elif(words[1] == "all"):
            speed = int(words[2])
            roboclaw.ForwardM2(address, speed)
            roboclaw.ForwardM1(address, speed)
            
    elif(words[0] == "stop"):
        stop()

    elif(words[0] == "cue"):
        #SpeedAccelDeccelPositionM1(self,address,accel,speed,deccel,position,buffer)
        roboclaw.SpeedAccelDeccelPositionM1(address,words[1],words[2],words[3],words[4],words[5])
    #else:
        #print ("No data")

    




