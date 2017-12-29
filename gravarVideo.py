import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

#Definindo o codec e criando um objeto de VideoWriter
fourcc = cv.cv.CV_FOURCC(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        frame = cv.flip(frame,180) #Virar imagem em 180

        out.write(frame) #Gravando no arquivo
        
        cv.imshow('Video', frame) #Janela para exibir o video
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
