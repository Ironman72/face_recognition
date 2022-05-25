import face_recognition
#Base image or Known Image
tony_stark = face_recognition.load_image_file('known/cap.jpeg')
tony_encodings = face_recognition.face_encodings(tony_stark)[0]

#Unknown image or FINDING Image
unknown_image = face_recognition.load_image_file('unknown/cap.jpeg')
unknown_encodings = face_recognition.face_encodings(unknown_image)[0]

result = face_recognition.compare_faces([tony_encodings],unknown_encodings)

if result[0]:
    print('This is Captain America')
else:
    print('This is not Captain America')