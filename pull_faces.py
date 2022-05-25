import face_recognition
from PIL import Image


face = face_recognition.load_image_file('images/team1.jpeg')
face_enconding = face_recognition.face_encodings(face)


for faces in face_enconding:
    top,right,bottom,left = faces

    face_image = face[top:right,left:bottom]