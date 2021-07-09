import cv2

'''
計算及更改執行效率
'''


def get_fps(function):
    time1 = cv2.getTickCount()
    function()
    time2 = cv2.getTickCount()
    return (time2 - time1) / cv2.getTickFrequency()


'''
Many of the OpenCV functions are optimized using SSE2, AVX etc. 
It contains unoptimized code also.
So if our system support these features, we should exploit them (almost all modern day processors support them).
It is enabled by default while compiling. So OpenCV runs the optimized code if it is enabled, else it runs the unoptimized code.
You can use cv2.useOptimized() to check if it is enabled/disabled and cv2.setUseOptimized() to enable/disable it.
Let’s see a simple example.
'''


def set_optimized():
    cv2.setUseOptimized(not cv2.useOptimized())
