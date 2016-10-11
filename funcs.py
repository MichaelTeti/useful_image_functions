import cv2
import os

def read_and_write_frames(filename, save_location, num_frames_to_save):
  """ Reads video file with name filename and saves the number of frames
   specified by num_frames_to_save at save_location. """
  
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
    
def read_image_files(im_height, im_width):
  """ Reads image files in the current directory, resizes them, then compiles
  them into one matrix, all_files"""
  num_files=len([name for name in os.listdir('.') if os.path.isfile(name)])
  all_files=np.zeros([im_height, im_width, num_files])
  directory=os.getcwd()
  a=os.listdir(directory)
  for i in range(num_files): 
    frame=cv2.cvtColor(imresize(cv2.imread(a[i]), [im_height, im_width]), cv2.COLOR_BGR2GRAY)
    all_files[:, :, i]=frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(10)==27:
      break
  return all_files
