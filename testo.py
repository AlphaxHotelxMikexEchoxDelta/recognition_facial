import cv2
import face_recognition


capture = cv2.VideoCapture(0)


while True:

    ret, frame = capture.read()
    rgb_frame = frame[:,:,::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "LeBoss"

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    #cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

print(frame[0:5])
print(rgb_frame[0:5])

capture.release()
cv2.destroyAllWindows()