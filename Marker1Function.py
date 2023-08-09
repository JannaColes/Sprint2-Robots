# Program Comments
# Written by:  Jennifer Oliver
# Date Written: August 9, 2023 -
# Program Description: Portion of code for Marker 1 function (Branch 1)


# Function to move the gimbal and chassis 360 degrees in the opposite directions at Position F
def Marker1():
    # chassis to rotate 360 counter clockwise (may need adjusting)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 360)
    print("Chassis 360 rotation complete")

    # gimbal to rotate 360 clockwise
    gimbal_ctrl.yaw(360)
    print("Gimbal 360 rotation complete")

    # add a sound-clip of robot saying "I'm number 1!" ????
    # media_ctrl.play_sound(rm_define.media_custom_audio_undefined)

    # Recenter ???
    gimbal_ctrl.recenter()
    print("Gimbal re-centered")

    # sleep to recenter chassis???
