import cv2
import os

def read_and_write_frames(filename, save_location, num_frames_to_save):
  vidcap = cv2.VideoCapture(filename) # read video file
  os.chdir(save_location) # go to save location

  success, frame=vidcap.read()
  frame_num = 0
  while success:
    if frame_num==num_frames_to_save:
      break
    success,frame = vidcap.read()
    cv2.imwrite("frame%d.jpg" % frame_num, frame)     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
    frame_num += 1
