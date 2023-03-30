import cv2 
import numpy as np 

'''green = np.uint8([[[0, 255, 0]]])

# convert the color to HSV
hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

# Compute the lower and upper limits
lowerLimit = hsvGreen[0][0][0] - 10, 100, 100
upperLimit = hsvGreen[0][0][0] + 10, 255, 255

# display the lower and upper limits
print("Lower Limit:",lowerLimit)
print("Upper Limit", upperLimit)'''


#specify lower and upper boundaries for each color using code above
lower_red = np.array([-10, 100, 100])
upper_red = np.array([10, 255, 255])

lower_blue = np.array([110, 100, 100])
upper_blue = np.array([130, 255, 255])

lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])

def main(viedo_path):
    video_soure = cv2.VideoCapture(viedo_path)
    while video_soure.isOpened(): 
        ret, frame = video_soure.read() 
        
        #convert to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #make mask using coressponding boundaries
        red_mask = cv2.inRange(hsv, lower_red,upper_red)
        blue_mask = cv2.inRange(hsv, lower_blue,upper_blue)
        green_mask = cv2.inRange(hsv, lower_green,upper_green)
        yellow_mask = cv2.inRange(hsv, lower_yellow,upper_yellow)

        #assign contours to each color
        red_contours, hierarchy= cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        blue_contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        green_contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        yellow_contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        for ball in red_contours:
            #assign top left x, top left y, width, height
            x, y, w, h = cv2.boundingRect(ball)
            #build rectangle around the box using coordinates and RGB
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
        for ball in blue_contours:
            x, y, w, h = cv2.boundingRect(ball)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        for ball in green_contours:
            x, y, w, h = cv2.boundingRect(ball)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        for ball in yellow_contours:
            x, y, w, h = cv2.boundingRect(ball)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3)

        cv2.imshow('hsv balls', frame) 

        if cv2.waitKey(1) == ord('q'):
            break

    video_soure.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main('rgb_ball_720.mp4')

