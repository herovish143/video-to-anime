import cv2
import os

if not os.path.exists('results'):
    os.makedirs('results')

cap = cv2.VideoCapture("sample.mp4")

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter('results/output.avi', fourcc, fps, (width, height))

for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()

    cartoon_image = cv2.stylization(frame, sigma_s= 120, sigma_r=0.20)

    cv2.imshow('Video Player', cartoon_image)
    video_writer.write(cartoon_image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
video_writer.release()