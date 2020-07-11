from Feature_Detection import Feature_Detection
from Template_Detection import Template_Detection
from Feature import Feature
from Object_Tracking import Object_Tracking
from IO import IO
from Video import Video
from Draw import Draw
from Event import Event
from Basic_Image_Processing import Basic_Image_Processing
from UI import UI
from Image_Operations import Image_Operations
from FPS import FPS
from Thresholding import Thresholding
from Smoothing import Smoothing
from Morphological import Morphological
from Edge import Edge
from Gradients import Gradients
from Pyramids import Pyramids
from Contours import Contours

'''
主核心 從這裡選擇功能跟 import 
'''

class Core():

    def __init__(self):
        try:
            self.Feature_Detection=Feature_Detection()
            self.Template_Detection=Template_Detection()
            self.Feature=Feature()
            self.Object_Tracking=Object_Tracking()
            self.IO=IO()
            self.Video=Video()
            self.Draw=Draw()
            self.Event=Event()
            self.Basic_Image_Processing=Basic_Image_Processing()
            self.UI=UI()
            self.Image_Operations=Image_Operations()
            self.FPS=FPS()
            self.Thresholding=Thresholding()
            self.Smoothing=Smoothing()
            self.Morphological=Morphological()
            self.Edge=Edge()
            self.Gradients=Gradients()
            self.Pyramids=Pyramids()
            self.Contours=Contours()
        except Exception as Errr:
            raise Errr