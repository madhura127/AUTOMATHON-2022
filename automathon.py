import numpy as np
import cv2

#matplotlib inline
from matplotlib import pyplot as plt

np.random.seed(42)

#Routine to fix 
def fixColor(image):
    return(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

video_stream = cv2.VideoCapture('people.mp4')

# Randomly select 30 frames
frameIds = video_stream.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)

# Store selected frames in an array
frames = []
for fid in frameIds:
    video_stream.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = video_stream.read()
    frames.append(frame)
    
video_stream.release()

# Calculate the median along the time axis
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
plt.imshow(fixColor(medianFrame))

grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)
plt.imshow(fixColor(grayMedianFrame))


text = "car"
color = (0, 0, 255)
thickness = 2
org = (00, 185)
fontScale = 1
font = cv2.FONT_HERSHEY_SIMPLEX




 
writer = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30,(640,480))

#Create a new video stream and get total frame count
video_stream = cv2.VideoCapture('people.mp4')
total_frames=video_stream.get(cv2.CAP_PROP_FRAME_COUNT)

frameCnt=0
while(frameCnt < total_frames-1):
    frameCnt+=1
    ret, frame = video_stream.read()

    # Convert current frame to grayscale
    gframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Calculate absolute difference of current frame and
    # the median frame
    dframe = cv2.absdiff(gframe, grayMedianFrame)
    
    # Gaussian
    # blurred = cv2.GaussianBlur(dframe, (7, 7), 0)
    blurred = cv2.medianBlur(dframe, 3)
    #Thresholding to binarise
    
    ret, tframe= cv2.threshold(blurred, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #Identifying contours from the threshold
    (cnts, _) = cv2.findContours(tframe.copy(), cv2.RETR_EXTERNAL, cv2 .CHAIN_APPROX_SIMPLE)
    
    cnts = np.array(cnts, dtype=object)
    areas = np.array([cv2.contourArea(cnt) for cnt in cnts])
    indices = areas > 1250
    cnts = cnts[indices]

    #For each contour draw the bounding bos
    for cnt in cnts:
        x,y,w,h = cv2.boundingRect(cnt)
         # Disregard items in the top of the picture
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cropped_img=frame[y:y+h,x:x+w]
        cv2.imwrite('C:/Users/User/Desktop/Automathon/people/'+str(frameCnt)+'.png',cropped_img)


    writer.write(cv2.resize(frame, (640,480)))
 
#Release video object
video_stream.release()
writer.release()