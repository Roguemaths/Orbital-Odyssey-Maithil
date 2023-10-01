import cv2
import numpy as np

# Function to find the red cross and draw a dot on it
def find_and_draw_red_cross(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Threshold the frame to get only red colors
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Find contours in the red mask
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours and find the largest one (assuming it's the red cross)
    max_area = 0
    red_cross_coords = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            # Get the centroid of the contour
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                red_cross_coords = (cX, cY)

    # Draw a red dot on the frame at the red cross coordinates
    if red_cross_coords:
        cv2.circle(frame, red_cross_coords, 5, (0, 0, 255), -1)
        print(f'Red Cross Coordinates: {red_cross_coords}')

    return frame

# Open the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, you can change it if you have multiple cameras

while cap.isOpened():
    # Read a frame from the camera
    ret, frame = cap.read()

    # Resize the frame to a smaller size for faster processing
    resized_frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    # Find and draw the red cross on the resized frame
    frame_with_red_cross = find_and_draw_red_cross(resized_frame)

    # Display the frame with the red dot
    cv2.imshow('Red dot Detection', frame_with_red_cross)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
