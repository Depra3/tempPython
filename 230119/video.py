import cv2
import numpy as np

video_path = '230119/data/archive/Background-Subtraction-Tutorial_merged.mp4'
cap = cv2.VideoCapture(cv2.samples.findFileOrKeep(video_path))
width = int(cap.get(3))
height = int(cap.get(4))

print(width, height)
                        # 경로
out = cv2.VideoWriter('./230119/data/Background_Subtraction_Tutorial_frame.mp4',
                     cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                     30, #프레임 속도
                     (width,height)) # 프레임 크기

# 그대로 적용 (이미지 처리 한 것과 영상 처리 하는 것이랑 큰 차이 없음)
backSub = cv2.createBackgroundSubtractorMOG2()

# 실행
while True: # local while True:
    ret, frame = cap.read() # 영상을 불러와서 이미지로 자동 변환
    
    # 영상 못 불러오면 자동으로 종료
    if frame is None: 
        break
        
    cv2.rectangle(frame, (10,2), (100,20), (255, 255, 255), -1) # 하나의 frame 2개를 띄우기 위한 작업
    cv2.imshow('Frame', frame)
    fgmask = backSub.apply(frame)
    cv2.imshow('FG Mask',fgmask)
    out.write(cv2.cvtColor(fgmask, cv2.COLOR_BGR2RGB))
    
    keyboard = cv2.waitKey(1) & 0xFF;
            # ESC 나 q 누르면 종료
    if(keyboard == 27) or (keyboard ==ord('q')):
        cv2.destroyAllWindows()
        break

# 전체 frame 종료시 전부 종료
cap.release()
out.release()
cv2.destroyAllWindows()