# -*- coding:utf-8 -*-
# 유튜브에서 영상 가져오기

import cv2 
import pafy
import numpy as np

def rescale_frame(frame, scale):    # works for image, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def main():
    # print(cv2.__version__)
    # print(pafy.__version__)
    url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
    video = pafy.new(url)

    print('title = ', video.title)
    print('video.rating = ', video.rating)
    print('video.duration = ', video.duration)

    # KeyError: 'like_count' debuging
    # https://github.com/mps-youtube/pafy/pull/288

    best = video.getbest()
    print('best.resolution', best.resolution)

    cap=cv2.VideoCapture(best.url)
    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('frame_size =', frame_size)

    while(True):

        retval, frame = cap.read()
        if not retval:
            break
        frame_resized = rescale_frame(frame, scale=.5) # 비율 설정
        cv2.imshow('frame', frame_resized)
        
        vi = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 100)
        # kernel_filter2 = np.ones((100, 100), np.float32) / 10000
        # v_blurred2 = cv2. filter2D(gray, -1, kernel_filter2)
        # ret, thresh = cv2.threshold(gray, 176, 255, 0)
        # contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        # N = len(contours) - 1
        # contours = sorted(contours, key = cv2.contourArea, reverse=False)
        # for c in contours:
        #     hull = cv2.convexHull(c)
        #     cv2.drawContours(vi, [hull], 0, (0, 255, 0), 2)

        edges_resized = rescale_frame(vi, scale=.5)
        
        cv2.imshow('edges', edges_resized)

        key = cv2.waitKey(25)
        if key == 27: # Esc
                break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
