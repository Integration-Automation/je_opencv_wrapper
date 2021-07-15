import cv2
import numpy as np

'''
處理畫面更新 畫畫面等
'''


def create_canvas(Canvas_Property=(512, 512, 3)):
    # Default is create a black image
    return np.zeros(Canvas_Property, np.uint8)


class draw(object):
    """
    Canvas : The image where you want to draw the shapes
    color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
    thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
    lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv2.LINE_AA gives anti-aliased line which looks great for curves.

    Canvas：您要繪製形狀的圖像
    color：形狀的顏色。對於BGR，將其作為元組傳遞，例如：(255,0,0)對於藍色。對於灰度，只需傳遞標量值即可。
    厚度：線或圓等的粗細。如果對封閉的圖形（如圓）傳遞-1，它將填充形狀。默認厚度= 1
    lineType：線的類型，是否為8連接線，抗鋸齒線等。默認情況下，為8連接線。 cv2.LINE_AA給出抗鋸齒的線條，看起來非常適合曲線。
    """

    def __init__(self):
        self.canvas = create_canvas()
        self.clear_key = 'c'
        self.clear_flag = True

    def draw_line(self, Point1=(0, 0), Point2=(511, 511), Color=(255, 0, 0), Size=5):
        # Draw a diagonal blue line with thickness of 5 px
        self.canvas = cv2.line(self.canvas, Point1, Point2, Color, Size)

    def draw_rectangle(self, Point1=(384, 0), Point2=(510, 128), Color=(0, 255, 0), Size=3):
        self.canvas = cv2.rectangle(self.canvas, Point1, Point2, Color, Size)

    def draw_circle(self, Point=(447, 63), Radius=63, Color=(0, 0, 255), Size=-1):
        self.canvas = cv2.circle(self.canvas, Point, Radius, Color, Size)

    def draw_ellipse(self, Center_Point=(256, 256), Shaft_Lenth=(100, 50), Rotate_Angle=0, Start_Angle=0, End_Angle=180,
                     Color=255, Size=-1):
        self.canvas = cv2.ellipse(self.canvas, Center_Point, Shaft_Lenth, Rotate_Angle, Start_Angle, End_Angle, Color,
                                  Size)

    def draw_poly_gon(self, Points=np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32).reshape((-1, 1, 2)),
                      Color=(0, 255, 255)):
        # pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        self.canvas = cv2.polylines(self.canvas, [Points], True, Color)

    def draw_text(self, Text='OpenCV', Point=(10, 500), Font=cv2.FONT_HERSHEY_SIMPLEX, ForntSize=4,
                  Color=(255, 255, 255), Size=2, Line_Type=cv2.LINE_AA):
        cv2.putText(self.canvas, Text, Point, Font, ForntSize, Color, Size, Line_Type)

    def set_clear_key(self, clear_key):
        self.clear_key = clear_key

    def clear_canvas(self, clear_flag=True):
        self.clear_flag = clear_flag

    def show_canvas(self, canvas_name='Canvas', exit_key="q"):
        while True:
            cv2.imshow(canvas_name, self.canvas)
            key = cv2.waitKey(1) & 0xFF
            if key == ord(exit_key) or key == 27:
                break
            elif key == ord(self.clear_key) and self.clear_flag is True:
                self.canvas = create_canvas()

        cv2.destroyAllWindows()
