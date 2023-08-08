# Program Comments
# Written by:  Jennifer Oliver
# Date Written: August 7, 2023 -
# Program Description: Portion of code for Marker 1 function

# Function to move the gimbal and chassis 360 degrees in the opposite directions
# as well as play a custom sound clip, at Position F
def Marker1():
    # chassis to rotate 360 counter clockwise (may need adjusting)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, -360)

    # gimbal to rotate 360 clockwise
    gimbal_ctrl.yaw(360)

    # add a sound-clip of robot saying "I'm number 1!" ????
    media_ctrl.play_sound(rm_define.media_custom_audio_undefined)

    # Recenter ???
    gimbal_ctrl.recenter()

    # sleep to recenter chassis???
