#Import the opencv library
import cv2
import face_recognition
#Define a video capture object
vid = cv2.VideoCapture(0)
img = cv2.imread('/Users/neevgrover/Desktop/Screen Shot 2022-10-23 at 1.44.51 PM.png',1)
known_encoding = face_recognition.face_encodings(img)[0]
while(True):
    #Capture the video frame by frame
    _, frame = vid.read()
    #Display the resulting frame
    cv2.imshow('frame', frame)
    unknown_encoding = face_recognition.face_encodings(frame)
    for k in unknown_encoding:
        results = face_recognition.compare_faces([known_encoding], k,0.4)
        if True in results:
            print("Neev found")
        else:
            print("Could not find Neev")
    #The "q" button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()