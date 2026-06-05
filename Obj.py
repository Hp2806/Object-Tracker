import cv2
import numpy as np

def main():
 cap = cv2.VideoCapture(0)

 if not cap.isOpened():
 print("Could not open webcam!")
 return

 lower_blue = np.array([90, 100, 100])
 upper_blue = np.array([130, 255, 255])

 while True:
 ret, frame = cap.read()

 if not ret:
 break

 # Flip frame (optional)
 frame = cv2.flip(frame, 1)

 # Convert BGR to HSV
 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 # Create mask
 mask = cv2.inRange(hsv, lower_blue, upper_blue)

 # Remove noise
 kernel = np.ones((5, 5), np.uint8)
 mask = cv2.erode(mask, kernel, iterations=1)
 mask = cv2.dilate(mask, kernel, iterations=2)

 # Find contours
 contours, _ = cv2.findContours(
 mask,
 cv2.RETR_EXTERNAL,
 cv2.CHAIN_APPROX_SIMPLE
 )

 hashtag#print("Contours found:", len(contours))

 for contour in contours:
 area = cv2.contourArea(contour)

 if area > 50:
 x, y, w, h = cv2.boundingRect(contour)

 cv2.rectangle(
 frame,
 (x, y),
 (x + w, y + h),
 (0, 255, 0),
 2
 )

 cv2.putText(
 frame,
 "Blue Object",
 (x, y - 10),
 cv2.FONT_HERSHEY_SIMPLEX,
 0.6,
 (0, 255, 0),
 2
 )

 cv2.imshow("Object Tracking", frame)
 hashtag#cv2.imshow("Mask", mask)

 key = cv2.waitKey(1) & 0xFF

 if key == ord('q'):
 break

 cap.release()
 cv2.destroyAllWindows()

if __name__ == "__main__":
 main()
