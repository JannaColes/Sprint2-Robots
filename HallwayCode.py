
# Define Functions before start() function

def ResetPoint():
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 0)



# Starting Point (A)
# Initialize all required settings such as speed, frequency, quantity and more
# Function for starting program, settings, timer,
def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(60)
    gimbal_ctrl.yaw_ctrl(250)
    gimbal_ctrl.pitch_ctrl(15)
    chassis_ctrl.set_rotate_speed(30)
    chassis_ctrl.set_trans_speed(0.5)

    # Reset Function
    ResetPoint()

    # Function to get to obstacle course
    # Move from Point A to Beginning Point B
    chassis_ctrl.move_with_distance(0, 5.69)

# B Point
# Function for obstacle course
# Function to reset
ResetPoint()
# Function to move from end of B to the first room, C point
chassis_ctrl.move_with_distance(0,5)
chassis_ctrl.move_with_distance(0,1.5)
# Total Move - 6.5 m


# C Point
# # Turn chassis 90 degrees
chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
# # Enter room
chassis_ctrl.move_with_distance(0,1.7)


# Function for room 1, if statement for room type,
# # Function - type 1 - fire
# # Function - type 2 - poison
# # Function - type 3 - search and rescue person
# # Function to leave room, return to C point
chassis_ctrl.move_with_distance(0,1.7)
chassis_ctrl.rotate_with_degree(rm_define.clockwise, -90)
# # Function to move from C point to D point

# D point
# # Reset function
# Function to go to E point

# E point
# # Turn chassis 90 degrees
# # Enter Room

# Function for room 2, if statement for room type,
# # Function - type 1 - fire
# # Function - type 2 - poison
# # Function - type 3 - search and rescue person
# # Function to leave room, return to E point
# # Function to move from E point to F point

# F Point
# Scan wall, read marker on wall, if statement
# # Function - marker 1 - do something with chassis and gimbal
# # Function - marker 2 - do something with the LED lights
# # Function - marker 3 - do something with both
# # Function to move from F point to G point

# G Point
# # Turn chassis 90 degrees
# # Enter Room

# Function for room 3, if statement for room type,
# # Function - type 2 - poison
# # Function to move from G point to H point

# H Point
# # Reset Function
# # Function to turn around
# # Function to move from H point to D point

# D Point
# # Reset Function
# # Do something cool Function
# # Final Reset Function
# # Function to return to A point

# A Point
# # Victory Dance