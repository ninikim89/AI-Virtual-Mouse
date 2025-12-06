import cv2
import mediapipe as mp
import pyautogui
import math


cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    output = hands.process(rgb_frame)
    all_hands = output.multi_hand_landmarks

    if all_hands:
        for hand in all_hands:
            landmarks = hand.landmark
            
            # Get coordinates for Index (8) and Thumb (4)
            index_x = int(landmarks[8].x * frame_width)
            index_y = int(landmarks[8].y * frame_height)
            thumb_x = int(landmarks[4].x * frame_width)
            thumb_y = int(landmarks[4].y * frame_height)
            
            # Draw the Skeleton
            mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            
            # Move Mouse (Based on Index Finger)
            cursor_x = screen_width/frame_width * index_x
            cursor_y = screen_height/frame_height * index_y
            pyautogui.moveTo(cursor_x, cursor_y)
            
            # Calculate Distance
            distance = math.sqrt((index_y - thumb_y)**2 + (index_x - thumb_x)**2)
            
            # CLICK LOGIC
            # If distance is less than 50, we Click
            if distance < 50:
                # 1. Visual: Draw a GREEN circle and text
                cv2.circle(frame, (index_x, index_y), 15, (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, "CLICKING!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # 2. Action: Actually Click
                pyautogui.click()
            else:
                # Visual: Draw a RED circle (Not clicking)
                cv2.circle(frame, (index_x, index_y), 15, (0, 0, 255), cv2.FILLED)

    cv2.imshow('Virtual Mouse Application', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()

cv2.destroyAllWindows()
