from Feature_Detection import Feature_Detection
from Template_Detection import Template_Detection
from Feature import Feature

class OpenCV_Core():

    def __init__(self):
        try:
            self.Feature_Detection=Feature_Detection()
            self.Template_Detection=Template_Detection()
            self.Feature=Feature()
        except Exception as Errr:
            raise Errr