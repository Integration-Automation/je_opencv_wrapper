import cv2
import numpy as np

'''
處理畫面更新 畫畫面等
'''

class Draw():

    '''
    Canvas : The image where you want to draw the shapes
    color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
    thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
    lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv2.LINE_AA gives anti-aliased line which looks great for curves.

    Canvas：您要繪製形狀的圖像
    color：形狀的顏色。對於BGR，將其作為元組傳遞，例如：(255,0,0)對於藍色。對於灰度，只需傳遞標量值即可。
    厚度：線或圓等的粗細。如果對封閉的圖形（如圓）傳遞-1，它將填充形狀。默認厚度= 1
    lineType：線的類型，是否為8連接線，抗鋸齒線等。默認情況下，為8連接線。 cv2.LINE_AA給出抗鋸齒的線條，看起來非常適合曲線。
    '''

    def __init__(self):
        self.Canvas=self.Create_Canvas()
        self.Clear_Key='c'
        self.Clear_Flag=True

    def Create_Canvas(self):
        # Create a black image
        return np.zeros((512, 512, 3), np.uint8)

    def Draw_Line(self):
        # Draw a diagonal blue line with thickness of 5 px
        self.Canvas = cv2.line(self.Canvas, (0, 0), (511, 511), (255, 0, 0), 5)

    def Draw_Retangle(self):
        self.Canvas = cv2.rectangle(self.Canvas, (384, 0), (510, 128), (0, 255, 0), 3)

    def Draw_Circle(self):
        self.Canvas = cv2.circle(self.Canvas, (447, 63), 63, (0, 0, 255), -1)

    def Draw_Ellipse(self):
        self.Canvas = cv2.ellipse(self.Canvas, (256, 256), (100, 50), 0, 0, 180, 255, -1)

    def Draw_PolyGon(self):
        pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        self.Canvas = cv2.polylines(self.Canvas, [pts], True, (0, 255, 255))

    def Draw_Text(self,Text='OpenCV'):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(self.Canvas, Text, (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

    def Clear_Canvas(self,Clear_Flag=True):
        self.Clear_Flag=Clear_Flag

    def Show_Canvas(self,Canvas_Name='Canvas'):
        while (1):
            cv2.imshow(Canvas_Name, self.Canvas)

            Key= cv2.waitKey(1) & 0xFF

            if Key == ord('q') or Key == 27:
                break

            elif Key == ord(self.Clear_Key) and self.Clear_Flag == True:
                self.Canvas=self.Create_Canvas()

        cv2.destroyAllWindows()