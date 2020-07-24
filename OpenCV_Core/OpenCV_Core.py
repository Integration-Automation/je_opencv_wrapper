import datetime

from Models.Feature_Detection import Feature_Detection
from Models.Template_Detection import Template_Detection
from Models.Feature import Feature
from Models.Object_Tracking import Object_Tracking
from Models.IO import IO
from Models.Video import Video
from Models.Draw import Draw
from Models.Event import Event
from Models.Basic_Image_Processing import Basic_Image_Processing
from Models.UI import UI
from Models.Image_Operations import Image_Operations
from Models.FPS import FPS
from Models.Thresholding import Thresholding
from Models.Smoothing import Smoothing
from Models.Morphological import Morphological
from Models.Edge import Edge
from Models.Gradients import Gradients
from Models.Pyramids import Pyramids
from Models.Contours import Contours
from Models.Fourier import Fourier
from Models.Histograms import Histograms
from Models.Hough_Line import Hough_Line
'''
主核心 從這裡選擇功能跟 import 
'''

class OpenCV_Core():

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
            self.Fourier = Fourier()
            self.Histograms=Histograms()
            self.Hough_Line=Hough_Line()
        except Exception as Errr:
            raise Errr
        print(datetime.datetime.now(),self.__class__,'Ready',sep=' ')