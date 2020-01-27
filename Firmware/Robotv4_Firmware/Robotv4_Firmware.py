# Complete example of using the RoboClaw library
#import the relevant code from the RoboClaw library

from roboclaw import RoboClaw

# address of the RoboClaw as set in Motion Studio

address = 0x128

# Creating the RoboClaw object, serial port and baudrate passed

roboclaw = RoboClaw(“/dev/ttyS0”, 115200)

# Starting communication with the RoboClaw hardware

roboclaw.Open()

# Start motor 1 in the forward direction at half speed

roboclaw.ForwardM1(address, 63)
