import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

height_ok = 0.34

while True:
    #ler as infos da webcam
    verificador, frame = webcam.read()

    if not verificador: #conseguiu ler a webcam
        break

    lista_rostos = reconhecedor_rostos.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            width_live = round(rosto.location_data.relative_bounding_box.xmin, 2)
            height_live = round(rosto.location_data.relative_bounding_box.ymin,2)
            print(round(height_live,2))

            if height_live > 0.45 :
                print('Corriga postura 🟥🟥🟥')
            else:
                print('Postura correta 🟢🟢🟢')

            desenho.draw_detection(frame, rosto)

    cv2.imshow('Rostos webcam', frame)



    if cv2.waitKey(500) == 27:
        break


webcam.release()
cv2.destroyAllWindows()

