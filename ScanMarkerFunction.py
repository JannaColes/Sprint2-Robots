# Program Comments
# Written by:  Jennifer Oliver
# Date Written: August 7, 2023 -
# Program Description: Portion of code for marker scanning

# Function to scan and identify the marker in order to perform actions
def ScanMarker():
    # Enable vision detection for marker
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)

    # sets vision detection distance
    vision_ctrl.set_marker_detection_distance(1)

    # Scan the marker
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)

    if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one):
        # Call function for Marker 1
        Marker1()
        print("Marker 1 complete ")
    elif vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two):
        # Call function for Marker 2
        print("Marker 2 complete ")
    elif vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three):
        # Call function for Marker 3
        print("Marker 3 complete ")

    # Disable vision detection for marker
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
