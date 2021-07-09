import cv2

'''
負責處理事件
'''


class cv_event(object):
    """
    event:
    [
    'event_FLAG_ALTKEY',
    'event_FLAG_CTRLKEY',
    'event_FLAG_LBUTTON',
    'event_FLAG_MBUTTON',
    'event_FLAG_RBUTTON',
    'event_FLAG_SHIFTKEY',
    'event_LBUTTONDBLCLK',
    'event_LBUTTONDOWN',
    'event_LBUTTONUP',
    'event_MBUTTONDBLCLK',
    'event_MBUTTONDOWN',
    'event_MBUTTONUP',
    'event_MOUSEHWHEEL',
    'event_MOUSEMOVE',
    'event_MOUSEWHEEL',
    'event_RBUTTONDBLCLK',
    'event_RBUTTONDOWN',
    'event_RBUTTONUP'
      ]

    """

    def __init__(self):
        self.ALTKEY_event = self.default_event
        self.CTRLKEY_event = self.default_event
        self.LBUTTON_event = self.default_event
        self.MBUTTON_event = self.default_event
        self.RBUTTON_event = self.default_event
        self.SHIFTKEY_event = self.default_event
        self.LBUTTONDBLCLK_event = self.default_event
        self.LBUTTONDOWN_event = self.default_event
        self.LBUTTONUP_event = self.default_event
        self.MBUTTONDBLCLK_event = self.default_event
        self.MBUTTONDOWN_event = self.default_event
        self.MBUTTONUP_event = self.default_event
        self.MOUSEHWHEEL_event = self.default_event
        self.MOUSEMOVE_event = self.default_event
        self.MOUSEWHEEL_event = self.default_event
        self.RBUTTONDBLCLK_event = self.default_event
        self.RBUTTONDOWN_event = self.default_event
        self.RBUTTONUP_event = self.default_event

    '''
    回調都會送五個參數
    def draw_circle(event,x,y,flag,param):
        if event == cv2.event_LBUTTONDBLCLK:
            cv2.circle(a.Draw.Canvas,(x,y),100,(255,0,0),-1)
    '''

    def default_event(self):
        pass

    def set_altkey_event(self, event):
        self.ALTKEY_event = event

    def altkey_event(self):
        self.ALTKEY_event()

    def Set_CTRLKEY_event(self, event):
        self.CTRLKEY_event = event

    def CTRLKEY_event(self):
        self.CTRLKEY_event()

    def Set_LBUTTON_event(self, event):
        self.LBUTTON_event = event

    def LBUTTON_event(self):
        self.LBUTTON_event()

    def Set_MBUTTON_event(self, event):
        self.MBUTTON_event = event

    def MBUTTON_event(self):
        self.MBUTTON_event()

    def Set_RBUTTON_event(self, event):
        self.RBUTTON_event = event

    def RBUTTON_event(self):
        self.RBUTTON_event()

    def Set_SHIFTKEY_event(self, event):
        self.SHIFTKEY_event = event

    def SHIFTKEY_event(self):
        self.SHIFTKEY_event()

    def Set_LBUTTONDBLCLK_event(self, event):
        self.LBUTTONDBLCLK_event = event

    def LBUTTONDBLCLK_event(self):
        self.LBUTTONDBLCLK_event()

    def Set_LBUTTONDOWN_event(self, event):
        self.LBUTTONDOWN_event = event

    def LBUTTONUP_event(self):
        self.LBUTTONUP_event()

    def Set_LBUTTONUP_event(self, event):
        self.LBUTTONUP_event = event

    def Set_MBUTTONDBLCLK_event(self, event):
        self.MBUTTONDBLCLK_event = event

    def MBUTTONDBLCLK_event(self):
        self.MBUTTONDBLCLK_event()

    def Set_MBUTTONDOWN_event(self, event):
        self.MBUTTONDOWN_event = event

    def MBUTTONDOWN_event(self):
        self.MBUTTONDOWN_event()

    def Set_MBUTTONUP_event(self, event):
        self.MBUTTONUP_event = event

    def MBUTTONUP_event(self):
        self.MBUTTONUP_event()

    def Set_MOUSEHWHEEL_event(self, event):
        self.MOUSEHWHEEL_event = event

    def MOUSEHWHEEL_event(self):
        self.MOUSEHWHEEL_event()

    def Set_MOUSEMOVE_event(self, event):
        self.MOUSEMOVE_event = event

    def MOUSEMOVE_event(self):
        self.MOUSEMOVE_event()

    def Set_MOUSEWHEEL_event(self, event):
        self.MOUSEWHEEL_event = event

    def MOUSEWHEEL_event(self):
        self.MOUSEWHEEL_event()

    def Set_RBUTTONDBLCLK_event(self, event):
        self.RBUTTONDBLCLK_event = event

    def RBUTTONDBLCLK_event(self):
        self.RBUTTONDBLCLK_event()

    def Set_RBUTTONDOWN_event(self, event):
        self.RBUTTONDOWN_event = event

    def RBUTTONDOWN_event(self):
        self.RBUTTONDOWN_event()

    def Set_RBUTTONUP_event(self, event):
        self.RBUTTONUP_event = event

    def RBUTTONUP_event(self):
        self.RBUTTONUP_event()

    def events(self):
        return [i for i in dir(cv2) if 'event' in i]

    def set_event(self, event, x, y, flags, param):

        if event == cv2.event_FLAG_ALTKEY:
            self.ALTKEY_event()

        elif event == cv2.event_FLAG_CTRLKEY:
            self.CTRLKEY_event()

        elif event == cv2.event_FLAG_LBUTTON:
            self.LBUTTON_event()

        elif event == cv2.event_FLAG_MBUTTON:
            self.MBUTTON_event()

        elif event == cv2.event_FLAG_RBUTTON:
            self.RBUTTON_event()

        elif event == cv2.event_FLAG_SHIFTKEY:
            self.SHIFTKEY_event()

        elif event == cv2.event_LBUTTONDBLCLK:
            self.LBUTTONDBLCLK_event()

        elif event == cv2.event_LBUTTONDOWN:
            self.LBUTTONDOWN_event()

        elif event == cv2.event_LBUTTONUP:
            self.LBUTTONUP_event()

        elif event == cv2.event_MBUTTONDBLCLK:
            self.MBUTTONDBLCLK_event()

        elif event == cv2.event_MBUTTONDOWN:
            self.MBUTTONDOWN_event()

        elif event == cv2.event_MBUTTONUP:
            self.MBUTTONUP_event()

        elif event == cv2.event_MOUSEHWHEEL:
            self.MOUSEHWHEEL_event()

        elif event == cv2.event_MOUSEMOVE:
            self.MOUSEMOVE_event()

        elif event == cv2.event_MOUSEWHEEL:
            self.MOUSEHWHEEL_event()

        elif event == cv2.event_RBUTTONDBLCLK:
            self.RBUTTONDBLCLK_event()

        elif event == cv2.event_RBUTTONDOWN:
            self.RBUTTONDOWN_event()

        elif event == cv2.event_RBUTTONUP:
            self.RBUTTONUP_event()

    def set_callback_event(self, Window_Name):
        cv2.setMouseCallback(Window_Name, self.set_event)

    def set_callback_function(self, Window_Name, Job_Function):
        cv2.setMouseCallback(Window_Name, Job_Function)
