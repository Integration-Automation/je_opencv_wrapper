import cv2

class OpenCV_IO:

    def __init__(self):
        pass

    def Read_Image(self,Image,Flag=1):
        return cv2.imread(Image,Flag)

    def Show_Image(self,Image,Window_Name='Image'):
        cv2.imshow(Window_Name,Image)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def Output_Image(self,Image,File_Name='Image'):
        cv2.imwrite(File_Name,Image)
