from email.mime import image
import face_recognition


face = face_recognition.load_image_file('images/team2.jpeg')
face_loc = face_recognition.face_locations(face)

# print(face_loc)

print(f'There are {len(face_loc)} "Faces" In this image')