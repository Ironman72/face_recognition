#facial_recognition

import face_recognition

face = face_recognition.load_image_file('images/team2.jpeg')
face_enconding = face_recognition.face_encodings(face)

# print(face_enconding)
print(f'There are {len(face_enconding)} "Faces" In this image')