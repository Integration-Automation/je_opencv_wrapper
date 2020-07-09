from Feature_Detection import Feature_Detection

class OpenCV_Core():

    def __init__(self):
        try:
            self.Feature_Detection=Feature_Detection()
        except Exception as Errr:
            raise Errr