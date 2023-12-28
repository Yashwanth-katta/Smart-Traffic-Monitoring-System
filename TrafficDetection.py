from imageai.Detection import ObjectDetection
import os
import cv2
import matplotlib.pyplot as plt


class TrafficDetection:
    @staticmethod
    def process(image):
        execution_path = os.getcwd()
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(os.path.join(execution_path, "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
        detector.loadModel()
        detections = detector.detectObjectsFromImage(input_image=os.path.join(image),
                                                     output_image_path=os.path.join("imagenew.jpg"))
        os.system("powershell -c imagenew.jpg")
        image = cv2.imread("imagenew.jpg")
        plt.axis("off")
        plt.imshow(image)
        plt.show()
        for eachObject in detections:
            print(eachObject["name"], " : ", eachObject["percentage_probability"])


if __name__ == "__main__":
    TrafficDetection.process('C:\\Users\\paras\\proj\\TrafficDet\\IMAGES\\4.jpg')
