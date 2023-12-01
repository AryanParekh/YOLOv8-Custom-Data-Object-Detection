from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(data='data.yaml', epochs=100, batch=64, imgsz=640, optimizer='Adam')