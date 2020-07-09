import cv2

class OpenCV_Video():

    def __init__(self):
        pass

    def Show_Video(self,Video,Video_Name='Video'):

        Cap=cv2.VideoCapture(Video)

        while True:
            ret , frame = Cap.read()
            if ret == True :
                cv2.imshow(Video_Name,frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                Cap.release()
                cv2.destroyAllWindows()
