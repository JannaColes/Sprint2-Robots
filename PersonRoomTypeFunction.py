# Program Comments
# Written by:  Jennifer Oliver
# Date Written: August 7, 2023
# Program Description: Portion of code for person detection, location and rescue

# Function to enter a room
def Person_EnterRoom():
    # Sound clip "Fire, Fire, Fire" (add custom media file)
    media_ctrl.play_sound(rm_define.media_custom_audio_undefined)

    # Enter a room by moving the chassis straight x amount
    chassis_ctrl.move_with_distance(0, 2)
    print("Room successfully entered")


# Function to find and scan a marker/person
def Person_FindPersonMarker():
    # blink red until person found
    led_ctrl.set_flash(rm_define.armor_all, 2)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)

    # turns the gimbal in the angle to locate the marker
    gimbal_ctrl.pitch_ctrl(15)  # random number, need to adjust

    # moves robot to the right towards the marker
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    # move towards marker
    chassis_ctrl.move_with_distance(0, 1)  # random number, need to adjust

    # moves robot to the right to face the marker
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    # Enables vision detection for people
    vision_ctrl.enable_detection(rm_define.vision_detection_people)

    # sets vision detection distance
    vision_ctrl.set_marker_detection_distance(1)

    # Scan the marker
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)

    if vision_ctrl.check_condition(rm_define.cond_recognized_people):
        # turn to solid green once person is found (not sure how to turn this off...)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 127, 70, rm_define.effect_always_on)
        led_ctrl.set_top_led(rm_define.armor_top_all, 0, 127, 70, rm_define.effect_always_on)

        # play sound clip saying "Person found!" (replace with actual media content)
        media_ctrl.play_sound(rm_define.media_custom_audio_undefined, wait_for_complete_flag=True)

    # Disables vision detection
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    print("Person successfully located!")


# Function to bring person to safety (start point A)
def Person_RescuePerson():
    # Play siren sound while heading back to start (add custom media file)
    media_ctrl.play_sound(rm_define.media_custom_audio_undefined)

    # Turns robot towards the door
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    # Move to the door (Adjust values as needed)
    chassis_ctrl.move_with_distance(0, 0)

    # Turn 90 degrees to the left to face the door (Adjust values as needed)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, -90)

    # move out to the hallway (Adjust values as needed)
    chassis_ctrl.move_with_distance(0, 1.7)

    # Turn 90 degrees to the left to face the starting point (Adjust values as needed)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, -90)

    # Move down the hallway to starting point (Adjust values as needed)
    chassis_ctrl.move_with_distance(0, 0)

    # Turn 180 degrees to turn around to head back (Adjust values as needed)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    # Reset gimbal position (if needed)
    gimbal_ctrl.recenter()
    print("Person successfully rescued!")


# Function to return to the room where person was detected, maybe do the clap function here???
def Person_ReturnToRoom():
    # Return to the room in which the person was located
    TargetRoomList = ["C", "E", "G"]

    while True:
        TargetRoom = input("Enter the room letter: ").upper()

        if TargetRoom == "C":
            chassis_ctrl.move_with_distance(0, 0)  # Example values, adjust as needed
            print("Something")
        elif TargetRoom == "E":
            chassis_ctrl.move_with_distance(0, 0)  # Example values, adjust as needed
            print("Something")
        elif TargetRoom == "G":
            chassis_ctrl.move_with_distance(0, 0)  # Example values, adjust as needed
            print("Something")
        elif TargetRoom not in TargetRoomList:
            print("Error- Target room not a valid room")
        else:
            return TargetRoom
        print("Successfully returned to the room")


# Function that gets called once room type has been established
# Combines all previous functions into this one function
def PersonRoomType():
    # Enter the room
    Person_EnterRoom()

    # Find the person
    Person_FindPersonMarker()

    # Bring the person to the start position
    Person_RescuePerson()

    # Return to the front of the same door
    Person_ReturnToRoom()
    print("Operation Find and Rescue completed successfully!")
