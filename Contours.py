import cv2
import numpy as np

'''
What are contours?
Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. 
The contours are a useful tool for shape analysis and object detection and recognition.

For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
findContours function modifies the source image. 
So if you want source image even after finding contours, already store it to some other variables.
In OpenCV, finding contours is like finding white object from black background. 
So remember, object to be found should be white and background should be black.
'''
class Contours():

    def __init__(self):
        pass

    '''
    See, there are three arguments in cv2.findContours() function, 
    first one is source image, 
    second is contour retrieval mode, 
    third is contour approximation method. 
    And it outputs the image, contours and hierarchy. contours is a Python list of all the contours in the image. 
    Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
    '''

    def Contours_Binary_Image_All(self,Image,Mode=cv2.RETR_TREE,Start=127,End=255):
        imgray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, Start, End, 0)
        image, contours, hierarchy = cv2.findContours(thresh, Mode, cv2.CHAIN_APPROX_SIMPLE)
        return cv2.drawContours(Image, contours, -1, (0, 255, 0), 3)

    '''
    This is the third argument in cv2.findContours function. What does it denote actually?

    Above, we told that contours are the boundaries of a shape with same intensity. 
    It stores the (x,y) coordinates of the boundary of a shape. But does it store all the coordinates ? 
    That is specified by this contour approximation method.

    If you pass cv2.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we need all the points? 
    For eg, you found the contour of a straight line. 
    Do you need all the points on the line to represent that line? 
    No, we need just two end points of that line. 
    This is what cv2.CHAIN_APPROX_SIMPLE does. 
    It removes all redundant points and compresses the contour, thereby saving memory.
    '''

    def Contours_Binary_Image_One(self,Image,Mode=cv2.RETR_TREE,Start=127,End=255):
        imgray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, Start, End, 0)
        image, contours, hierarchy = cv2.findContours(thresh, Mode, cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[4]
        return cv2.drawContours(Image, [cnt], 0, (0, 255, 0), 3)

    '''
    1. Moments
    Image moments help you to calculate some features like center of mass of the object, area of the object etc.
    
    The function cv2.moments() gives a dictionary of all moment values calculated.
    
    From this moments, you can extract useful data like area, centroid etc
    
    M=cv2.moments(cnt)
    
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    
    '''
    def Moments(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        return cv2.moments(cnt)

    '''
    2. Contour Area
    Contour area is given by the function cv2.contourArea() or from moments, M[‘m00’].
    '''
    def Area(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        return cv2.contourArea(cnt)

    '''
    3. Contour Perimeter
    It is also called arc length. It can be found out using cv2.arcLength() function. 
    Second argument specify whether shape is a closed contour (if passed True), or just a curve.
    '''
    def Perimeter(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        return cv2.arcLength(cnt,True)

    '''
    4. Contour Approximation
    It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify. 
    It is an implementation of Douglas-Peucker algorithm. 
    Check the wikipedia page for algorithm and demonstration.
    '''
    def Approximation(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        epsilon = 0.1 * cv2.arcLength(cnt, True)
        return cv2.approxPolyDP(cnt, epsilon, True)

    '''
    5. Convex Hull
    Convex Hull will look similar to contour approximation, but it is not (Both may provide same results in some cases). 
    Here, cv2.convexHull() function checks a curve for convexity defects and corrects it. 
    Generally speaking, convex curves are the curves which are always bulged out, or at-least flat. 
    And if it is bulged inside, it is called convexity defects. 
    
    hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]
    
    Arguments details:
    points are the contours we pass into.
    hull is the output, normally we avoid it.
    clockwise : Orientation flag. If it is True, the output convex hull is oriented clockwise. 
    Otherwise, it is oriented counter-clockwise.
    returnPoints : By default, True. Then it returns the coordinates of the hull points. 
    If False, it returns the indices of contour points corresponding to the hull points.
    
    So to get a convex hull as in above image, following is sufficient:
    '''
    def Hull(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        return cv2.convexHull(cnt)

    '''
    6. Checking Convexity
    There is a function to check if a curve is convex or not, cv2.isContourConvex(). 
    It just return whether True or False. Not a big deal.
    '''

    def Convexity(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        return cv2.isContourConvex(cnt)

    '''
    7. Bounding Rectangle
    There are two types of bounding rectangles.

    7.a. Straight Bounding Rectangle
    It is a straight rectangle, it doesn’t consider the rotation of the object.
    So area of the bounding rectangle won’t be minimum. 
    It is found by the function cv2.boundingRect().

    Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height.
    '''
    def Straight_Bounding(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        x, y, w, h = cv2.boundingRect(cnt)
        return cv2.rectangle(Image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    '''
    7.b. Rotated Rectangle
    Here, bounding rectangle is drawn with minimum area, so it considers the rotation also. 
    The function used is cv2.minAreaRect(). 
    It returns a Box2D structure which contains following detals - ( top-left corner(x,y), (width, height), angle of rotation ). 
    But to draw this rectangle, we need 4 corners of the rectangle. 
    It is obtained by the function cv2.boxPoints()
    '''
    def Rotated(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        return cv2.drawContours(Image, [box], 0, (0, 0, 255), 2)

    '''
    8. Minimum Enclosing Circle
    Next we find the circumcircle of an object using the function cv2.minEnclosingCircle(). 
    It is a circle which completely covers the object with minimum area.
    '''
    def Minimum_Enclosing(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        return cv2.circle(Image, center, radius, (0, 255, 0), 2)

    '''
    9. Fitting an Ellipse
    Next one is to fit an ellipse to an object. 
    It returns the rotated rectangle in which the ellipse is inscribed.
    '''
    def Fitting_an_Ellipse(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        ellipse = cv2.fitEllipse(cnt)
        return cv2.ellipse(Image, ellipse, (0, 255, 0), 2)

    '''
    10. Fitting a Line
    Similarly we can fit a line to a set of points. 
    Below image contains a set of white points. 
    We can approximate a straight line to it.
    '''
    def Fitting_an_Line(self,Image,Start=127,End=255):
        ret, thresh = cv2.threshold(Image, Start, End, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        rows, cols = Image.shape[:2]
        [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
        lefty = int((-x * vy / vx) + y)
        righty = int(((cols - x) * vy / vx) + y)
        return cv2.line(Image, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)