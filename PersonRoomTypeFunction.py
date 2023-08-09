# Program Comments
# Written by:  Jennifer Oliver
# Date Written: August 8, 2023 
# Program Description: Portion of code for person detection, location and rescue (Branch 1)


# Function to re-center the robot
def Person_ResetFunction():
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 0)
    print("Gimbal successfully re-centered!")


# Function to enter a room
def Person_EnterRoom():
    # Sound clip "To the rescue!" (add custom media file)
    # custom_audio_file_path = "voice-changer-2023-08-09.mp3"
    # media_ctrl.play_sound(custom_audio_file_path)
    # media_ctrl.play_sound(rm_define.media_custom_audio_, "voice-changer-2023-08-09.mp3")  # Not sure if this is right

    # Enter a room by moving the chassis straight x amount
    chassis_ctrl.move_with_distance(0, 2.6)
    print("Room successfully entered")


# Function to find and scan a marker/person
def Person_FindPersonRoomC():
    # blink red until person found
    led_ctrl.set_flash(rm_define.armor_all, 2)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_flash)

    # turns the gimbal in the angle to locate the person
    gimbal_ctrl.pitch_ctrl(15)

    # moves robot to the right towards the person
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    # move towards person
    chassis_ctrl.move_with_distance(0, 2.11)

    # moves robot to the right to face the person
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    # Enables vision detection for people
    vision_ctrl.enable_detection(rm_define.vision_detection_people)

    # sets vision detection distance
    vision_ctrl.set_marker_detection_distance(1)

    # Scan for person
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)

    # Recognized Person
    vision_ctrl.check_condition(rm_define.cond_recognized_people)
    print("Person successfully located!")

    # Disables vision detection
    vision_ctrl.disable_detection(rm_define.vision_detection_people)

    # turn to solid green once person is found
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_always_on)

    # play sound clip saying "Person found!" (replace with actual media content)
    # custom_audio_file_path2 = "voice-changer-2023-08-09-11-14.mp3"
    # media_ctrl.play_sound(custom_audio_file_path2, wait_for_complete_flag=True)
    # # media_ctrl.play_sound(rm_define.media_custom_audio_undefined, wait_for_complete_flag=True)


# Function to find and scan a marker/person
def Person_FindPersonRoomE():
    # blink red until person found
    led_ctrl.set_flash(rm_define.armor_all, 2)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_flash)

    # turns the gimbal in the angle to locate the marker
    gimbal_ctrl.pitch_ctrl(15)

    # turns robot to the right
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    # move towards person
    chassis_ctrl.move_with_distance(0, 0.15)

    # turns robot to the left
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    # move towards person
    chassis_ctrl.move_with_distance(0, 0.47)

    # turns robot to the right
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    # moves robot towards person
    chassis_ctrl.move_with_distance(0, 1.19)

    # Enables vision detection for people
    vision_ctrl.enable_detection(rm_define.vision_detection_people)

    # sets vision detection distance
    vision_ctrl.set_marker_detection_distance(1)  # should this be person marker?

    # Scan the marker
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)

    # Recognized Person
    vision_ctrl.check_condition(rm_define.cond_recognized_people)
    print("Person successfully located!")

    # Disables vision detection
    vision_ctrl.disable_detection(rm_define.vision_detection_people)

    # turn to solid green once person is found (not sure how to turn this off...)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_always_on)

    # play sound clip saying "Person found!" (replace with actual media content)
    # custom_audio_file_path2 = "voice-changer-2023-08-09-11-14.mp3"
    # media_ctrl.play_sound(custom_audio_file_path2, wait_for_complete_flag=True)
    # # media_ctrl.play_sound(rm_define.media_custom_audio_undefined, wait_for_complete_flag=True)


# Function to bring person to safety (start point A)
def Person_RescuePersonRoomC():
    # Play siren sound while heading back to start (add custom media file)
    # media_ctrl.play_sound(rm_define.media_custom_audio_undefined)

    # Turns robot right
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    # Move to the door
    chassis_ctrl.move_with_distance(0, 2.11)

    # Turn 90 degrees to the left to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    # move out to the hallway (Adjust values as needed)
    chassis_ctrl.move_with_distance(0, 2.6)

    # Turn 90 degrees to the left to face the starting point
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    # Move down the hallway to starting point (Adjust values as needed)
    # Total move - 14.73
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.73)
    print("Person successfully rescued!")

    # Reset gimbal position (if needed)
    gimbal_ctrl.recenter()
    print("Gimbal successfully re-centered!")


# Function to bring person to safety (start point A)
def Person_RescuePersonRoomE():
    # Play siren sound while heading back to start (add custom media file)
    # media_ctrl.play_sound(rm_define.media_custom_audio_undefined)

    # Turns robot around
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    # Moves robot to the door
    chassis_ctrl.move_with_distance(0, 1.19)

    # Turns 90 degrees to the left
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    # Moves robot to the door
    chassis_ctrl.move_with_distance(0, 1.19)  # place holder values)

    # Turns 90 degrees to the right
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    # Moves robot to the door
    chassis_ctrl.move_with_distance(0, 1.19)  # place holder values)

    # Turns 90 degrees to the left
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    # move out to the hallway (Adjust values as needed)
    chassis_ctrl.move_with_distance(0, 2.6)

    # Turn 90 degrees to the left to face the starting point (Adjust values as needed)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    # Move down the hallway to starting point (Adjust values as needed)
    # Total move - 25.25
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, .25)
    rint("Person successfully rescued!")

    # Reset gimbal position (if needed)
    gimbal_ctrl.recenter()
    print("Gimbal successfully re-centered!")


# Function to return to infront of room c
def Person_ReturnToRoomC():
    # Total move - 14.73
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.73)
    print("Back to Room C")


# Function to return to infront of room E
def Person_ReturnToRoomE():
    # Total move - 25.25
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, .25)
    print("Back to Room E")


# MAIN FUNCTION: that gets called once room type has been established
# Combines all previous functions into this one function
def PersonRoomCType3():
    # Re-center Robot
    Person_ResetFunction()

    # Enter the room
    Person_EnterRoom()

    # Find the person
    Person_FindPersonRoomC()

    # Bring the person to the start position
    Person_RescuePersonRoomC()

    # Return to the front of the same door
    Person_ReturnToRoomC()
    # print("Operation Find and Rescue completed successfully!")


def PersonRoomEType3():
    # Re-center Robot
    Person_ResetFunction()

    # Enter the room
    Person_EnterRoom()

    # Find the person
    Person_FindPersonRoomE()

    # Bring the person to the start position
    Person_RescuePersonRoomE()

    # Return to the front of the same door
    Person_ReturnToRoomE()
    # print("Operation Find and Rescue completed successfully!")

# Call the necessary function:
# PersonRoomCType3()
# PersonRoomEType3()
