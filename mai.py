from ultralytics import YOLO
import cv2
import math

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
"""
# Load YOLO model
model = YOLO("D:\\UVD MAJOR PROJECT\\UVD MAJOR PROJECT (1)\\runs\\detect\\train29\\weights\\best.pt")
classNames= ['With Helmet', 'Without Helmet']
"""



model = YOLO("yolov8n.pt")
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]



cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Webcam', 800, 600)  

while True:
    success, img = cap.read()

    
    if not success:
        print("Failed to read frame from the webcam.")
        break

    results = model(img, stream=True)

    
    for r in results:
        boxes = r.boxes

        for box in boxes:
            
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)


            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

    
    if img.shape[0] > 0 and img.shape[1] > 0:
        cv2.imshow('Webcam', img)

    
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()




