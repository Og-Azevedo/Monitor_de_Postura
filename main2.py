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

# CERTO
# width: 0.20781370997428894
# height: 0.27708548307418823

#ERRADO
# width: 0.18490871787071228
# height: 0.24654525518417358

# label_id: 0
# score: 0.8415176272392273
# location_data {
#   format: RELATIVE_BOUNDING_BOX
#   relative_bounding_box {
#     xmin: 0.31571871042251587
#     ymin: 0.35041677951812744
#     width: 0.22377753257751465
#     height: 0.2983705401420593
#   }
#   relative_keypoints {
#     x: 0.3434287905693054
#     y: 0.4289180636405945
#   }
#   relative_keypoints {
#     x: 0.4066750109195709
#     y: 0.418102502822876
#   }
#   relative_keypoints {
#     x: 0.33405348658561707
#     y: 0.48086947202682495
#   }
#   relative_keypoints {
#     x: 0.35693106055259705
#     y: 0.5530667901039124
#   }
#   relative_keypoints {
#     x: 0.37146955728530884
#     y: 0.47282445430755615
#   }
#   relative_keypoints {
#     x: 0.5326547622680664
#     y: 0.4576878547668457
#   }
# }