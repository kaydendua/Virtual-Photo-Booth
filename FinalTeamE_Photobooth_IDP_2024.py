import dlib
import cv2
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import math
from math import *
from math import hypot
import sys
import os
print("Welcome to 15Years@SST Photo Booth!")
print("Please be patient with the program, it may be slow at times.")
def main():
    #landmarks file
    p = "shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(p)
    detector = dlib.get_frontal_face_detector()

    # The coordinates to position the foreground image
    x_offset = 0  # X coordinate
    y_offset = 0   # Y coordinate

    # Open webcam
    print("Please place your (i)phone as far away as possible.")

    # Loads the camera
    # The looped try and except code will ensure that the camera loaded is the computer's
    # This is to prevent an error that occurs if there are too many devices nearby
    cam_check = 0
    while True:
        try:
            cap = cv2.VideoCapture(cam_check)
            _, frame = cap.read()
            rows, cols, _ = frame.shape
            break
        except:
            cam_check += 1

    background_list = ["Backgrounds_Folder/Students_Large_staircase_outside_robotics.jpeg",
                    "Backgrounds_Folder/Students_SST_Classroom_Whiteboard.jpeg",
                    "Backgrounds_Folder/Students_SST_Logo_Main_Entrance.jpeg",
                    "Backgrounds_Folder/Student_GreyWall.jpeg",
                    "Backgrounds_Folder/Student_Dropoff.jpeg",
                    #For students^(index 0 to 4)

                    "Backgrounds_Folder/IndustryPartners_SST_Exhibition_Room.jpeg",
                    "Backgrounds_Folder/IndustryPartners_SST_Logo_outside_GO.jpeg",
                    "Backgrounds_Folder/IndustryPartners_3D_Logo.jpeg",
                    #For industry partners^ (index 5 to 7)

                    "Backgrounds_Folder/Parents_SST_Ecopond.jpeg",
                    "Backgrounds_Folder/Students_SST_Logo_Main_Entrance.jpeg",
                    #For parents^ (index 8 to 9)

                    "Backgrounds_Folder/Staff_Electronics_Lab.jpeg",
                    "Backgrounds_Folder/Staff_Science_lab.jpeg",
                    "Backgrounds_Folder/Staff_SST_Info_Hub.jpeg",
                    #For staff^ (index 10 to 12)
                    
                    "Backgrounds_Folder/Casual_Beach.jpeg",
                    "Backgrounds_Folder/Casual_norway_attractions_house.jpeg",
                    "Backgrounds_Folder/Casual_BotanicGardens.jpeg",
                    "Backgrounds_Folder/Casual_GardensByTheBay1.jpeg",
                    "Backgrounds_Folder/Casual_GardensByTheBay2.jpeg",
                    "Backgrounds_Folder/Casual_Merlion.jpeg",
                    "Backgrounds_Folder/Casual_SG_Seashore.jpeg",
                    "Backgrounds_Folder/Casual_Sunset.jpeg"
                    #For casual^ (index 13 to 20)
    ]
    
    #foreground list contains a normal one and the others are related to house colours
    foreground_list = ["Foregrounds_Folder/Normal_Foreground_Outline.png",
                    "Foregrounds_Folder/Black_House_Banner_Outlines.png",
                    "Foregrounds_Folder/Blue_House_Banner_Outlines.png",
                    "Foregrounds_Folder/Green_House_Banner_Outlines.png",
                    "Foregrounds_Folder/Red_House_Banner_Outlines.png",
                    "Foregrounds_Folder/Yellow_House_Banner_Outlines.png"]
    
    #below are lists of suitable props decided by us for each group of audience
    students_head_prop_list = [
        "Head_props_Folder/SST_ACE_Cap.png",
        "Head_props_Folder/SST_DCB_Cap.png",
        "Head_props_Folder/SST_Hexagons_Cap.png",
        "Head_props_Folder/SST_House_Cap.png",
        "Head_props_Folder/SST_IDP_Cap.png",
        "Head_props_Folder/SST_Inc_Cap.png",
        "Head_props_Folder/SST_MUN_Cap.png",
        "Head_props_Folder/SST_PSB_Cap.png",
        "Head_props_Folder/SST_SC_Cap.png"
    ]
    staff_head_prop_list = [
        "Head_props_Folder/SST_Logo_Cap.png",
        "Head_props_Folder/Staff_Prop_1.png",
        "Head_props_Folder/Staff_Prop_2.png",
        "Head_props_Folder/Staff_Prop_3.png",
        "Head_props_Folder/Staff_Prop_4.png",
        "Head_props_Folder/Staff_Prop_5.png",
        "Head_props_Folder/Staff_Prop_6.png"
    ]

    industrypartners_head_prop_list = [
        "Head_props_Folder/SST_IDP_Cap.png",
        "Head_props_Folder/IndustryPartner_Prop_1.png",
        "Head_props_Folder/IndustryPartner_Prop_2.png",
        "Head_props_Folder/IndustryPartner_Prop_3.png",
        "Head_props_Folder/IndustryPartner_Prop_4.png",
        "Head_props_Folder/IndustryPartner_Prop_5.png",
        "Head_props_Folder/IndustryPartner_Prop_6.png"
    ]

    parents_head_prop_list = [
        "Head_props_Folder/SST_Logo_Cap.png",
        "Head_props_Folder/SST_PForSST_Cap.png"
    ]

    # casual head props
    casual_head_prop_list = [
        "Head_props_Folder/Casual_Bonefide.png",
        "Head_props_Folder/Casual_Lovely_Hat.png",
        "Head_props_Folder/Casual_Tophat.png",
        "Head_props_Folder/Casual_cap.png"
    ]
    
    # eye prop below
    sunglasses_list = ["Sunglasses_Folder/Sunglasses_1.png",
                       "Sunglasses_Folder/Sunglasses_2.png",
                       "Sunglasses_Folder/Sunglasses_3.png",
                       "Sunglasses_Folder/Sunglasses_4.png",
                       "Sunglasses_Folder/Sunglasses_5.png",
                       "Sunglasses_Folder/Sunglasses_6.png",
                       "Sunglasses_Folder/Sunglasses_7.png",
                       "Sunglasses_Folder/Sunglasses_8.png"]

    # The user now inputs the role that is suitable
    role_selection = ""
    print("")
    print("Select your role!")
    print("1 for Student; 2 for Industry Partner; 3 for Parent; 4 for Staff; 5 for Casual")
    while True:
        try:
            role_selection = int(input("Type in one of the numbers above as your desired role: "))
            if 1 <= role_selection <= 5:
                break
            else:
                print("Please enter a valid integer.")
                print("1 for Student; 2 for Industry Partner; 3 for Parent; 4 for Staff; 5 for Casual")
        except ValueError:
            print("Please enter a valid integer.")
            print("1 for Student; 2 for Industry Partner; 3 for Parent; 4 for Staff; 5 for Casual")
    
    # from the role, we assign the first suitable background for said role
    firs_background_selection = 0

    if role_selection == 1:
        role_selection = "Student" #has sunglasses
        first_background_selection = 0
    elif role_selection == 2:
        role_selection = "Industry Partner"
        first_background_selection = 3
    elif role_selection == 3:
        role_selection = "Parent" #has sunglasses
        first_background_selection = 5
    elif role_selection == 4:
        role_selection = "Staff" #has sunglasses
        first_background_selection = 7
    elif role_selection == 5:
        role_selection = "Casual" #has sunglasses
        first_background_selection = 10
    
    # afterwards, based on the role selection, we assign the correct pre-made list of props to corresponding role
    in_head_prop_list = []
    if role_selection == "Student":
        in_head_prop_list = students_head_prop_list
    elif role_selection == "Industry Partner":
        in_head_prop_list = industrypartners_head_prop_list
    elif role_selection == "Staff":
        in_head_prop_list = staff_head_prop_list
    elif role_selection == "Parent":
        in_head_prop_list = parents_head_prop_list
    elif role_selection == "Casual":
        in_head_prop_list = casual_head_prop_list

    # we will assign the props and foreground once the camera feed rolls, then the user can toggle between them.

    # Initialise SelfiSegmentation module
    seg = SelfiSegmentation()

    # print statements of instructions
    print("")
    print("《Instructions》")
    print("Press the 'a' and 'd' keys to switch BACKgrounds.")
    print("Press the 'b' and 'm' keys to switch FOREgrounds.")
    print("Press the 'q' and 'e' keys to switch HEAD props.")
    print("Press the arrow keys (←, →) to switch SUNGLASSES props.")

    # we have deemed that distinguished guests like industry partners would not want to have sunglasses as props.
    # therefore, based on the role selection, the snippet below assigns sunglasses or not
    sunglasses_option = False
    if role_selection != "Industry Partner":
        sunglasses_option = True
        print("Press 's' to TOGGLE SUNGLASSES.")

    print("Press 'H' to TOGGLE HEAD props.")
    print("Press the ESC key to select your ROLE again/ close the program.")
    print("Press the space key to take a photo!")
    print("")

    #angle detector
    def angle_trunc(a):
        while a < 0.0:
            a += pi * 2
        return a

    def getAngleBetweenPoints(xyog, xylandmark):
        deltaY = xylandmark[1] - xyog[1]
        deltaX = xylandmark[0] - xyog[0]
        return math.degrees(angle_trunc(atan2(deltaY, deltaX))) * -1

    #image rotator
    def rotate_image(image, angle):
        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        return result

    #midpoint
    def midpoint(point1, point2):
        x_mid = int((point1[0] + point2[0]) / 2)
        y_mid = int((point1[1] + point2[1]) / 2)
        return (x_mid, y_mid)
    
    # the next 4 user-defined functions facilitate the switching of backgrounds and the togggling of the sunglasses filter,
    # since only 3 out of 4 of our audience groups are given sunglasses. they will be called when the "a", "d"
    # or "s" (for sunglasses) is called [refer to line <>].
    # '/' switches the sunglasses filter
    # the parameter carries important information that is required as parameters for the UDF, video_play
    def bg_switch_student(key, bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection):
        if key == ord("a"):
            bg_sub_selection -= 1
            if 0 <= bg_sub_selection <= 4:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
            else:
                bg_sub_selection = 4
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("d"):
            bg_sub_selection += 1
            if 0 <= bg_sub_selection <= 4:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
            else:
                bg_sub_selection = 0
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("s"):
            if bg_func_sungl_op:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, False, bg_func_hat_op, sungl_sub_selection)
            else:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, True, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("/"):
            sungl_sub_selection += 1
            if sungl_sub_selection >= len(sunglasses_list):
                sungl_sub_selection = 0
            video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
    
    #only industry partners do not have acccess to sunglasses, hence it has one less parameter (i.e. bg_func_sungl_op)
    def bg_switch_ip(key, bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_hat_op):
        if key == ord("a"):
            bg_sub_selection -= 1
            if 5 <= bg_sub_selection <= 7:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, False, bg_func_hat_op, 0)
            else:
                bg_sub_selection = 7
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, False, bg_func_hat_op, 0)
        elif key == ord("d"):
            bg_sub_selection += 1
            if 5 <= bg_sub_selection <= 7:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, False, bg_func_hat_op, 0)
            else:
                bg_sub_selection = 5
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, False, bg_func_hat_op, 0)

    def bg_switch_staff(key, bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection):
        if key == ord("a"):
            bg_sub_selection -= 1
            if 10 <= bg_sub_selection <= 12:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
            else:
                bg_sub_selection = 12
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("d"):
            bg_sub_selection += 1
            if 10 <= bg_sub_selection <= 12:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
            else:
                bg_sub_selection = 10
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("s"):
            if bg_func_sungl_op:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, False, bg_func_hat_op, sungl_sub_selection)
            else:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, True, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("/"):
            sungl_sub_selection += 1
            if sungl_sub_selection >= len(sunglasses_list):
                sungl_sub_selection = 0
            video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)

    def bg_switch_parent(key, bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection):
        if key == ord("a"):
            bg_sub_selection -= 1
            if 8 <= bg_sub_selection <= 9:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
            else:
                bg_sub_selection = 9
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("d"):
            bg_sub_selection += 1
            if 8 <= bg_sub_selection <= 9:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
            else:
                bg_sub_selection = 8
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("s"):
            if bg_func_sungl_op:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, False, bg_func_hat_op, sungl_sub_selection)
            else:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, True, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("/"):
            sungl_sub_selection += 1
            if sungl_sub_selection >= len(sunglasses_list):
                sungl_sub_selection = 0
            video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
    
    def bg_switch_casual(key, bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection):
        if key == ord("a"):
            bg_sub_selection -= 1
            if 13 <= bg_sub_selection <= 20:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
            else:
                bg_sub_selection = 20
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("d"):
            bg_sub_selection += 1
            if 13 <= bg_sub_selection <= 20:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
            else:
                bg_sub_selection = 13
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("s"):
            if bg_func_sungl_op:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, False, bg_func_hat_op, sungl_sub_selection)
            else:
                video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, True, bg_func_hat_op, sungl_sub_selection)
        elif key == ord("/"):
            sungl_sub_selection += 1
            if sungl_sub_selection >= len(sunglasses_list):
                sungl_sub_selection = 0
            video_play(bg_sub_selection, fg_sub_selection, head_sub_selection, bg_func_sungl_op, bg_func_hat_op, sungl_sub_selection)
    
    # the UDF below is the primary function that executes all of the video output and filters
    def video_play(in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection):
        # reads the head props and background image
        in_head_prop = cv2.imread(in_head_prop_list[in_head_selection])
        in_sunglasses_prop = cv2.imread(sunglasses_list[in_sunglasses_selection])
        background_img = cv2.imread(background_list[in_bg_selection])
        # resizes the background image
        background_img = cv2.resize(background_img, (1920, 1080))
        
        while True:
            # reads a frame from the camera
            ret, frame = cap.read()
            if not ret:
                print("Failed to load camera. Please try again.")
                print("(This may have been intentional if you exited out of the code and inputted 'yes'.)")
                #if the camera fails, the code will terminate to prevent any crashes and errors from occurring
                sys.exit()

            # Background removal, after resizing the frame
            frame = cv2.resize(frame, (1920, 1080))
            frame = seg.removeBG(frame, background_img)

            # The next two lines creates a mask based on the dimensions of the frame
            rows, cols, _ = frame.shape
            mask = np.zeros((rows, cols), np.uint8)
        
            # Converting the image to grayscale
            mask.fill(0)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(frame)

            for face in faces:
                landmarks = predictor(gray_frame, face)

                #face coordinates are defined for the locations of the props
                #"nose"👃
                top_nose = (landmarks.part(29).x, landmarks.part(29).y)
                center_nose = (landmarks.part(30).x, landmarks.part(30).y)
                left_nose = (landmarks.part(31).x, landmarks.part(31).y)
                right_nose = (landmarks.part(35).x, landmarks.part(35).y)
                bottom_nose = (landmarks.part(33).x, landmarks.part(33).y)

                #"eyes"👀
                center_eyes = (landmarks.part(27).x, landmarks.part(27).y)

                #"chin"
                bottom_chin = (landmarks.part(8).x, landmarks.part(8).y)

                #"brow"
                right_brow = (landmarks.part(24).x, landmarks.part(24).y)
                left_brow = (landmarks.part(19).x, landmarks.part(19).y)
                center_brow = midpoint(left_brow, right_brow)

                # Distance between nose and parts of the face
                nose_to_eyes = int(hypot(center_nose[0] - center_eyes[0], center_nose[1] - center_eyes[1]))
                nose_to_hair = int(hypot(bottom_chin[0] - center_nose[0], bottom_chin[1] - center_nose[1]))
                brow_to_hairline = int(hypot(bottom_nose[0] - top_nose[0], bottom_nose[0] - top_nose[0]))     
                
                # Face angle ∠
                face_angle = getAngleBetweenPoints(top_nose, bottom_nose)
                placement_angle = face_angle + 90
                
                # Center hairline
                center_hairline = (int(center_brow[0] - brow_to_hairline * sin(math.radians(placement_angle))), int(center_brow[1] - brow_to_hairline * cos(math.radians(placement_angle))))
                
                # While the variables are named nose, the proportions here are for the face area
                nose_width = int(hypot(left_nose[0] - right_nose[0], left_nose[1] - right_nose[1]) * 1.7) * 3
                nose_height = int(nose_width * 0.77)

                # Eye proportions
                eyes_width = int(hypot(landmarks.part(36).x - landmarks.part(39).x, landmarks.part(19).x - landmarks.part(20).x) * 5.4)
                eyes_height = int(eyes_width * 0.51)
                
                # Calculate the position for the nose
                top_left_nose = (int(center_nose[0] - nose_width / 2), int(center_nose[1] - nose_height / 2))

                # Calculate the position for the eyes
                top_left_eyes = (int(center_nose[0] - eyes_width / 2), int(center_nose[1] - eyes_height / 2 - nose_to_eyes))
                
                # Calculate the position for the head
                top_left_head = (int(center_hairline[0] - eyes_width / 1.77), int(center_hairline[1] - nose_height / 1.0 - brow_to_hairline * cos(math.radians(placement_angle))))
                bottom_right_head = (int(center_hairline[0] + eyes_width / 1.77), int(center_hairline[1] + nose_height / 3.5 + brow_to_hairline * cos(math.radians(placement_angle))))

                # The trigonometric functions move the position of the hat such that it follows the user when they tilt their head, rather than rotating on the spot
                
                # Head proportions
                head_width = int(bottom_right_head[0] - top_left_head[0] - (eyes_width / 1.77) * sin(math.radians(placement_angle)))
                head_height = int((bottom_right_head[1] - top_left_head[1]) - (eyes_height / 2.5) * cos(math.radians(placement_angle)))

                # Note: many of the numbers in the proportions code were calculated through the aspect ratio of
                #the props, as well as trial and error

                # Placing sunglasses 🕶️
                if in_sunglasses == True:
                    sunglasses = rotate_image(in_sunglasses_prop, placement_angle) #rotate prop according to face
                    sunglasses = cv2.resize(sunglasses, (eyes_width, eyes_height)) #resize prop according to face

                    # The rest of the code in the if statement uses the mask to remove the image background
                    # Afterwards, it places the sunglasses on the face
                    filter_gray = cv2.cvtColor(sunglasses, cv2.COLOR_BGR2GRAY)  
                    eyes_area = frame[top_left_eyes[1]: top_left_eyes[1] + eyes_height, top_left_eyes[0]: top_left_eyes[0] + eyes_width]
                    _, mask = cv2.threshold(filter_gray, 25, 255, cv2.THRESH_BINARY_INV)

                    # The try and except statement prevents the code from crashing when there is no face detected
                    try:
                        mask_resized = cv2.resize(mask, (eyes_width, eyes_height))
                        eyes_area_no_eyes = cv2.bitwise_and(eyes_area, eyes_area, mask=mask_resized)
                        final = cv2.add(eyes_area_no_eyes, sunglasses)
                        frame[top_left_eyes[1]: top_left_eyes[1] + eyes_height, top_left_eyes[0]: top_left_eyes[0] + eyes_width] = final
                    except: True
                
                # placing hat (head) 🎩
                # The code works the same way as the sunglasses, except with hat proportions
                if in_hat == True:
                    hat = rotate_image(in_head_prop, placement_angle)
                    hat = cv2.resize(hat, (head_width, head_height))
                    filter_gray = cv2.cvtColor(hat, cv2.COLOR_BGR2GRAY)
                    
                    hat_area = frame[top_left_head[1]: top_left_head[1] + head_height, top_left_head[0]: top_left_head[0] + head_width]
                    
                    _, mask = cv2.threshold(filter_gray, 25, 255, cv2.THRESH_BINARY_INV)

                    try:
                        hat_area_no_hat = cv2.bitwise_and(hat_area, hat_area, mask=mask)
                        final = cv2.add(hat_area_no_hat, hat)
                        frame[top_left_head[1]: top_left_head[1] + head_height, top_left_head[0]: top_left_head[0] + head_width] = final
                    except: True
            
            # Applying the foreground
            foreground_final = cv2.imread(foreground_list[in_fg_selection], cv2.IMREAD_UNCHANGED)
            foreground_resized = cv2.resize(foreground_final, (frame.shape[1] - x_offset, frame.shape[0] - y_offset))
            for c in range(3):  # Looping over the RGB channels to ensure the pixels of both the foreground
                # and frame blend correctly
                frame[y_offset:y_offset + foreground_resized.shape[0], x_offset:x_offset + foreground_resized.shape[1], c] = \
                foreground_resized[:, :, c] * (foreground_resized[:, :, 3] / 255.0) + \
                frame[y_offset:y_offset+foreground_resized.shape[0], x_offset:x_offset + foreground_resized.shape[1], c] * \
                (1.0 - foreground_resized[:, :, 3] / 255.0)
            
            # Displaying the image
            cv2.imshow("15@SST Photo booth", frame)

            # waiting for key inputs (i.e. this reads the key inputs)
            k = cv2.waitKey(1) & 0xFF
            if k%256 == 32: # when the space bar is pressed, a screenshot is taken
                # Displaying the screenshot preview for the user to review
                preview_frame = frame
                cv2.imshow("Screenshot Preview", preview_frame)
                cv2.moveWindow("Screenshot Preview", 10, 50)  # Adjust the coordinates as needed
                cv2.waitKey(500)

                # The user then is asked whether to save the preview or not
                user_input = input("Do you want to save this photo? (yes/no): ")
                ss_counter = 0 # used for naming the screenshot files
                if user_input.lower() == 'yes':
                    ss_name = "screenshot_{}.png".format(ss_counter)
                    file_existence = os.path.exists(ss_name) # checks whether the name already exists
                    while file_existence:
                        # this increases the number on the "tag" (after the underscore) until the name of
                        # the file does not exist inside the folder
                        ss_counter += 1
                        ss_name = "screenshot_{}.png".format(ss_counter)
                        file_existence = os.path.exists(ss_name)
                    image_name = "screenshot_{}.png".format(ss_counter)
                    cv2.imwrite(image_name, preview_frame) # this writes the screenshot to the computer with the suitable name
                    print("Screenshot {} saved successfully.".format(ss_counter))
                
                cv2.destroyWindow("Screenshot Preview") # end of screenshot review process
            
            # the "a" and "d" keys control the backgrounds and "s" controls whether the sunglasses filter is enabled or disabled;
            # '/' switches the sunglasses filters
            elif k == ord("a") or k == ord("d") or k == ord("s") or k == ord("/"): # switches for backgrounds and sunglasses toggle (for 3 audience groups)
                # calls the corresponding function that will facilitate the two aforementioned purposes
                if role_selection == "Student":
                    bg_switch_student(k, in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
                elif role_selection == "Industry Partner":
                    bg_switch_ip(k, in_bg_selection, in_fg_selection, in_head_selection, in_hat)
                elif role_selection == "Staff":
                    bg_switch_staff(k, in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
                elif role_selection == "Parent":
                    bg_switch_parent(k, in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
                elif role_selection == "Casual":
                    bg_switch_casual(k, in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
            elif k == ord("h"): # 'h" toggles the head prop filter
                if in_hat == True:
                    in_hat = False
                    video_play(in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
                else:
                    in_hat = True
                    video_play(in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
            elif k == ord("q"): # 'q' toggles the HEAD props (i.e. index of in_head_prop_list + 1)
                in_head_selection += 1
                if in_head_selection >= len(in_head_prop_list):
                    in_head_selection = 0
                video_play(in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
            elif k == ord("e"): # 'e' toggles the HEAD props (i.e. index of in_head_prop_list - 1)
                in_head_selection -=1
                if in_head_selection < 0:
                    in_head_selection = len(in_head_prop_list) - 1
                video_play(in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
            elif k == ord("m"): # 'm' toggles the FOREGROUND (i.e. index of in_head_prop_list + 1)
                in_fg_selection += 1
                if in_fg_selection >= len(foreground_list):
                    in_fg_selection = 0
                video_play(in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
            elif k == ord("b"): # 'b' toggles the FOREGROUND (i.e. index of in_head_prop_list - 1)
                in_fg_selection -= 1
                if in_fg_selection >= len(foreground_list):
                    in_fg_selection = len(foreground_list)
                video_play(in_bg_selection, in_fg_selection, in_head_selection, in_sunglasses, in_hat, in_sunglasses_selection)
            elif k == 27: #ASCII 27 ⇒ Escape key; pressing the ESC key will prompt the user to whether to restart the program
                # for example, if the user chose the wrong role or the user just wants to close the program
                cv2.destroyAllWindows()
                cap.release()
                continue_input = input("Would you like to continue? (yes/no): ").lower()
                if continue_input == "yes":
                    main() # this line runs the program from the beginning again
                else:
                    print("Closing all windows.")
                    cv2.destroyAllWindows()
                    cap.release()
                    print("⚠️Please delete or rename the screenshots taken such that upon the next execution of this app,")
                    print("you can still save screenshots into your computer. ⭐ Thank you!")
                    break

    video_play(first_background_selection, 0, 0, sunglasses_option, True, 0)

main()
