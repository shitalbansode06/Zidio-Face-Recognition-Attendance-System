import cv2
import pickle
import numpy as np
import os

# Ensure the 'data' directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Initialize video capture and face detector
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Check if the camera opened successfully
if not video.isOpened():
    print("Error: Could not open camera.")
    exit()

faces_data = []  # List to store the face images
i = 0  # Counter for frames
name = input("Enter Your Name: ")  # User input for the name

# Start capturing video frames
while True:
    ret, frame = video.read()  # Read a frame from the video
    
    # Check if frame is read correctly
    if not ret:
        print("Error: Could not read frame.")
        break  
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    faces = facedetect.detectMultiScale(gray, 1.3, 5)  # Detect faces in the frame

    
# Process each detected face
    for (x, y, w, h) in faces:
        # Crop and resize the detected face
        crop_img = frame[y:y+h, x:x+w]  
        resized_img = cv2.resize(crop_img, (50, 50))  
        
        # Add face data every 10 frames if less than 100 faces are collected
        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append(resized_img)
        
        i += 1  # Increment the frame counter
        
        # Display face count and draw rectangle around the face
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
    
    # Show the frame with face detection
    cv2.imshow("Frame", frame)
    
    # Break the loop if 'q' is pressed or 100 faces are collected
    k = cv2.waitKey(10)
    if k == ord('q') or len(faces_data) == 100:
        break

# Release the video capture object and close windows
video.release()
cv2.destroyAllWindows()

# Convert the list of faces into a numpy array
faces_data = np.asarray(faces_data)

# Ensure we have exactly 100 faces before reshaping
if len(faces_data) == 100:
    faces_data = faces_data.reshape(100, -1)
else:
    print(f"Error: Expected 100 faces, but got {len(faces_data)}")

# Handle name storage in 'names.pkl'
names_file = 'C:/Users/shaik/OneDrive/Desktop/zidio/data/names.pkl'
if 'names.pkl' not in os.listdir('data'):
    names = [name] * 100  # Create a list with the name repeated 100 times
    with open(names_file, 'wb') as f:
        pickle.dump(names, f)
else:
    # Load existing names and append the new ones
    with open(names_file, 'rb') as f:
        names = pickle.load(f)
    names += [name] * 100
    with open(names_file, 'wb') as f:
        pickle.dump(names, f)

# Handle face data storage in 'faces_data.pkl'
faces_data_file = 'C:/Users/shaik/OneDrive/Desktop/zidio/data/faces_data.pkl'
if 'faces_data.pkl' not in os.listdir('data'):
    with open(faces_data_file, 'wb') as f:
        pickle.dump(faces_data, f)
else:
    # Load existing face data and append the new ones
    with open(faces_data_file, 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
    with open(faces_data_file, 'wb')as f:
        pickle.dump(faces,f)