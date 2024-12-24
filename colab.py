"""import cv2
from google.colab import files

# Upload video
uploaded = files.upload()

# Get video filename (assume it's named 'video.mp4')
video_path = list(uploaded.keys())[0]

# Load the video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xmla')

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame.")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
    
    # Display result (using cv2_imshow since cv2.imshow doesn't work in Colab)
    from google.colab.patches import cv2_imshow
    cv2_imshow(frame)
    
    # Break loop (you can limit frames or stop after detection)
    break

cap.release()
cv2.destroyAllWindows()
"""