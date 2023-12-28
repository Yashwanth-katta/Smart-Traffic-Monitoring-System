from imageai.Detection import ObjectDetection
import datetime
import os


class TrafficDetection2:
    def addSecs(tm, secs):
        fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
        fulldate = fulldate + datetime.timedelta(seconds=secs)
        return fulldate.time()
    @staticmethod
    def process():
        execution_path = os.getcwd()
        print(execution_path)
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(os.path.join(execution_path, "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
        detector.loadModel()
        d = {}
        su = 0
        for var in range(1, 5):
            print("IMAGES/" + str(var) + ".jpg")
            detections = detector.detectObjectsFromImage(input_image=os.path.join("IMAGES/" + str(var) + ".jpg"),
                                                         output_image_path=os.path.join(
                                                             "IMAGES/" + "out" + str(var) + ".jpg"))
            c = 0
            for eachObject in detections:
                # print(eachObject["name"], " : ", eachObject["percentage_probability"])
                c = c + 1
            su += c
            d[var] = c
        print(su)
        a = datetime.datetime.now().time()
        f = open('res.txt', 'w')
        for var in d:
            print(d[var])
            b = TrafficDetection2.addSecs(a, 30)
            a = str(a)
            a = a[0:8]
            t = int((d[var]/su)*200)+10
            f.write("Signal" + str(var) + " :" + str(a) + "-" + str(b) + " : " + str(d[var]) + "\n")
            f.write("Signal" + str(var) + " : "+ str(t) +" : \n\n")
            a = b
        f.close()


if __name__ == "__main__":
    TrafficDetection2.process()
