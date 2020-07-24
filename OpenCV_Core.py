import datetime

from Feature_Detection import Feature_Detection
from Template_Detection import Template_Detection
from Feature import Feature
from Object_Tracking import Object_Tracking
from OpenCV_IO import OpenCV_IO
from OpenCV_Video import OpenCV_Video
from Draw import Draw
from Event import Event

class OpenCV_Core():

    def __init__(self):
        try:
            self.Feature_Detection=Feature_Detection()
            self.Template_Detection=Template_Detection()
            self.Feature=Feature()
            self.Object_Tracking=Object_Tracking()
            self.OpenCV_IO=OpenCV_IO()
            self.OpenCV_Video=OpenCV_Video()
            self.Draw=Draw()
            self.Event=Event()
        except Exception as Errr:
            raise Errr
        print(datetime.datetime.now(),self.__class__,'Ready',sep=' ')