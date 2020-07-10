import cv2
class Event():

    '''
    Event:
    [
    'EVENT_FLAG_ALTKEY',
    'EVENT_FLAG_CTRLKEY',
    'EVENT_FLAG_LBUTTON',
    'EVENT_FLAG_MBUTTON',
    'EVENT_FLAG_RBUTTON',
    'EVENT_FLAG_SHIFTKEY',
    'EVENT_LBUTTONDBLCLK',
    'EVENT_LBUTTONDOWN',
    'EVENT_LBUTTONUP',
    'EVENT_MBUTTONDBLCLK',
    'EVENT_MBUTTONDOWN',
    'EVENT_MBUTTONUP',
    'EVENT_MOUSEHWHEEL',
    'EVENT_MOUSEMOVE',
    'EVENT_MOUSEWHEEL',
    'EVENT_RBUTTONDBLCLK',
    'EVENT_RBUTTONDOWN',
    'EVENT_RBUTTONUP'
      ]

    '''


    def __init__(self):
        self.ALTKEY_Event=self.Default_Event
        self.CTRLKEY_Event = self.Default_Event
        self.LBUTTON_Event = self.Default_Event
        self.MBUTTON_Event = self.Default_Event
        self.RBUTTON_Event = self.Default_Event
        self.SHIFTKEY_Event = self.Default_Event
        self.LBUTTONDBLCLK_Event = self.Default_Event
        self.LBUTTONDOWN_Event = self.Default_Event
        self.LBUTTONUP_Event = self.Default_Event
        self.MBUTTONDBLCLK_Event = self.Default_Event
        self.MBUTTONDOWN_Event = self.Default_Event
        self.MBUTTONUP_Event = self.Default_Event
        self.MOUSEHWHEEL_Event = self.Default_Event
        self.MOUSEMOVE_Event = self.Default_Event
        self.MOUSEWHEEL_Event = self.Default_Event
        self.RBUTTONDBLCLK_Event = self.Default_Event
        self.RBUTTONDOWN_Event = self.Default_Event
        self.RBUTTONUP_Event = self.Default_Event


    '''
    回調都會送五個參數
    def draw_circle(event,x,y,flag,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(a.Draw.Canvas,(x,y),100,(255,0,0),-1)
    '''

    def Default_Event(self):
        pass

    def Set_ALTKEY_Event(self,Event):
        self.ALTKEY_Event=Event

    def ALTKEY_Event(self):
        self.ALTKEY_Event()

    def Set_CTRLKEY_Event(self,Event):
        self.CTRLKEY_Event=Event

    def CTRLKEY_Event(self):
        self.CTRLKEY_Event()

    def Set_LBUTTON_Event(self,Event):
        self.LBUTTON_Event=Event

    def LBUTTON_Event(self):
        self.LBUTTON_Event()

    def Set_MBUTTON_Event(self,Event):
        self.MBUTTON_Event=Event

    def MBUTTON_Event(self):
        self.MBUTTON_Event()

    def Set_RBUTTON_Event(self,Event):
        self.RBUTTON_Event=Event

    def RBUTTON_Event(self):
        self.RBUTTON_Event()

    def Set_SHIFTKEY_Event(self,Event):
        self.SHIFTKEY_Event=Event

    def SHIFTKEY_Event(self):
        self.SHIFTKEY_Event()

    def Set_LBUTTONDBLCLK_Event(self,Event):
        self.LBUTTONDBLCLK_Event=Event

    def LBUTTONDBLCLK_Event(self):
        self.LBUTTONDBLCLK_Event()

    def Set_LBUTTONDOWN_Event(self,Event):
        self.LBUTTONDOWN_Event=Event

    def LBUTTONUP_Event(self):
        self.LBUTTONUP_Event()

    def Set_LBUTTONUP_Event(self,Event):
        self.LBUTTONUP_Event=Event

    def Set_MBUTTONDBLCLK_Event(self,Event):
        self.MBUTTONDBLCLK_Event=Event

    def MBUTTONDBLCLK_Event(self):
        self.MBUTTONDBLCLK_Event()

    def Set_MBUTTONDOWN_Event(self,Event):
        self.MBUTTONDOWN_Event=Event

    def MBUTTONDOWN_Event(self):
        self.MBUTTONDOWN_Event()

    def Set_MBUTTONUP_Event(self,Event):
        self.MBUTTONUP_Event=Event

    def MBUTTONUP_Event(self):
        self.MBUTTONUP_Event()

    def Set_MOUSEHWHEEL_Event(self,Event):
        self.MOUSEHWHEEL_Event=Event

    def MOUSEHWHEEL_Event(self):
        self.MOUSEHWHEEL_Event()

    def Set_MOUSEMOVE_Event(self,Event):
        self.MOUSEMOVE_Event=Event

    def MOUSEMOVE_Event(self):
        self.MOUSEMOVE_Event()

    def Set_MOUSEWHEEL_Event(self,Event):
        self.MOUSEWHEEL_Event=Event

    def MOUSEWHEEL_Event(self):
        self.MOUSEWHEEL_Event()

    def Set_RBUTTONDBLCLK_Event(self,Event):
        self.RBUTTONDBLCLK_Event=Event

    def RBUTTONDBLCLK_Event(self):
        self.RBUTTONDBLCLK_Event()

    def Set_RBUTTONDOWN_Event(self,Event):
        self.RBUTTONDOWN_Event=Event

    def RBUTTONDOWN_Event(self):
        self.RBUTTONDOWN_Event()

    def Set_RBUTTONUP_Event(self,Event):
        self.RBUTTONUP_Event=Event

    def RBUTTONUP_Event(self):
        self.RBUTTONUP_Event()


    def Events(self):
        return [i for i in dir(cv2) if 'EVENT' in i]

    def Set_Event(self,event,x,y,flags,param):

        if event == cv2.EVENT_FLAG_ALTKEY:
            self.ALTKEY_Event()

        elif event == cv2.EVENT_FLAG_CTRLKEY:
            self.CTRLKEY_Event()

        elif event == cv2.EVENT_FLAG_LBUTTON:
            self.LBUTTON_Event()

        elif event == cv2.EVENT_FLAG_MBUTTON:
            self.MBUTTON_Event()

        elif event == cv2.EVENT_FLAG_RBUTTON:
            self.RBUTTON_Event()

        elif event == cv2.EVENT_FLAG_SHIFTKEY:
            self.SHIFTKEY_Event()

        elif event == cv2.EVENT_LBUTTONDBLCLK:
            self.LBUTTONDBLCLK_Event()

        elif event == cv2.EVENT_LBUTTONDOWN:
            self.LBUTTONDOWN_Event()

        elif event == cv2.EVENT_LBUTTONUP:
            self.LBUTTONUP_Event()

        elif event == cv2.EVENT_MBUTTONDBLCLK:
            self.MBUTTONDBLCLK_Event()

        elif event == cv2.EVENT_MBUTTONDOWN:
            self.MBUTTONDOWN_Event()

        elif event == cv2.EVENT_MBUTTONUP:
            self.MBUTTONUP_Event()

        elif event == cv2.EVENT_MOUSEHWHEEL:
            self.MOUSEHWHEEL_Event()

        elif event == cv2.EVENT_MOUSEMOVE:
            self.MOUSEMOVE_Event()

        elif event == cv2.EVENT_MOUSEWHEEL:
            self.MOUSEHWHEEL_Event()

        elif event == cv2.EVENT_RBUTTONDBLCLK:
            self.RBUTTONDBLCLK_Event()

        elif event == cv2.EVENT_RBUTTONDOWN:
            self.RBUTTONDOWN_Event()

        elif event == cv2.EVENT_RBUTTONUP:
            self.RBUTTONUP_Event()


    def Set_Callback_Event(self,Window_Name):
        cv2.namedWindow(Window_Name)
        cv2.setMouseCallback(Window_Name,self.Set_Event)

    def Set_Callback_Function(self,Window_Name,Job_Function):
        cv2.namedWindow(Window_Name)
        cv2.setMouseCallback(Window_Name,Job_Function)
