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

得到特徵 並畫出輪廓區域
'''

'''
See, there are three arguments in cv2.findContours() function, 
first one is source image, 
second is contour retrieval mode, 
third is contour approximation method. 
And it outputs the image, contours and hierarchy. contours is a Python list of all the contours in the image. 
Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
'''


def contours_binary_image_all(image, Mode=cv2.RETR_TREE, start=127, end=255):
    image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image_array, start, end, 0)
    image, contours, hierarchy = cv2.findContours(thresh, Mode, cv2.CHAIN_APPROX_SIMPLE)
    return cv2.drawContours(image, contours, -1, (0, 255, 0), 3)


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


def contours_binary_image(image, Mode=cv2.RETR_TREE, start=127, end=255):
    image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image_array, start, end, 0)
    image, contours, hierarchy = cv2.findContours(thresh, Mode, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[4]
    return cv2.drawContours(image, [cnt], 0, (0, 255, 0), 3)


'''
1. Moments
image moments help you to calculate some features like center of mass of the object, area of the object etc.

The function cv2.moments() gives a dictionary of all moment values calculated.

From this moments, you can extract useful data like area, centroid etc

M=cv2.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

'''


def moments(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    return cv2.moments(cnt)


'''
2. Contour Area
Contour area is given by the function cv2.contourArea() or from moments, M[‘m00’].
'''


def area(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    return cv2.contourArea(cnt)


'''
3. Contour Perimeter
It is also called arc length. It can be found out using cv2.arcLength() function. 
Second argument specify whether shape is a closed contour (if passed True), or just a curve.
'''


def perimeter(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    return cv2.arcLength(cnt, True)


'''
4. Contour Approximation
It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify. 
It is an implementation of Douglas-Peucker algorithm. 
Check the wikipedia page for algorithm and demonstration.
'''


def approximation(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
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


def hull(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    return cv2.convexHull(cnt)


'''
6. Checking Convexity
There is a function to check if a curve is convex or not, cv2.isContourConvex(). 
It just return whether True or False. Not a big deal.
'''


def convexity(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
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


def straight_bounding(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    x, y, w, h = cv2.boundingRect(cnt)
    return cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


'''
7.b. Rotated Rectangle
Here, bounding rectangle is drawn with minimum area, so it considers the rotation also. 
The function used is cv2.minAreaRect(). 
It returns a Box2D structure which contains following detals - ( top-left corner(x,y), (width, height), angle of rotation ). 
But to draw this rectangle, we need 4 corners of the rectangle. 
It is obtained by the function cv2.boxPoints()
'''


def rotated(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    return cv2.drawContours(image, [box], 0, (0, 0, 255), 2)


'''
8. Minimum Enclosing Circle
Next we find the circumcircle of an object using the function cv2.minEnclosingCircle(). 
It is a circle which completely covers the object with minimum area.
'''


def minimum_enclosing(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    return cv2.circle(image, center, radius, (0, 255, 0), 2)


'''
9. Fitting a Line
Similarly we can fit a line to a set of points. 
Below image contains a set of white points. 
We can approximate a straight line to it.
'''


def fitting_an_line(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    rows, cols = image.shape[:2]
    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    return cv2.line(image, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)


'''
1. Aspect Ratio
It is the ratio of width to height of bounding rect of the object.
長寬比
'''


def aspect_ratio(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    x, y, w, h = cv2.boundingRect(cnt)
    return float(w) / h


'''
2. Extent
Extent is the ratio of contour area to bounding rectangle area.
範圍
'''


def extent(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    extent_area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    rect_area = w * h
    return float(extent_area) / rect_area


'''
3. Solidity
Solidity is the ratio of contour area to its convex hull area.
堅固度是輪廓面積與其凸包面積的比率。
'''


def solidity(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    solidity_area = cv2.contourArea(cnt)
    solidity_hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(solidity_hull)
    return float(solidity_area) / hull_area


'''
4. Equivalent Diameter
Equivalent Diameter is the diameter of the circle whose area is same as the contour area.
等效直徑
'''


def equivalent_diameter(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    equivalent_diameter_area = cv2.contourArea(cnt)
    return np.sqrt(4 * equivalent_diameter_area / np.pi)


'''
5. Orientation
Orientation is the angle at which object is directed. 
Following method also gives the Major Axis and Minor Axis lengths.
'''


def orientation(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    return cv2.fitEllipse(cnt)


'''
6. Mask and Pixel Points
In some cases, we may need all the points which comprises that object
'''


def mask_and_pixel_points(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    mask = np.zeros(thresh.shape, np.uint8)
    cv2.drawContours(mask, [cnt], 0, 255, -1)
    return np.transpose(np.nonzero(mask))
    # pixelpoints = cv2.findNonZero(mask)


'''
Here, two methods, one using Numpy functions, next one using OpenCV function (last commented line) are given to do the same.
Results are also same, but with a slight difference. 
Numpy gives coordinates in (row, column) format, while OpenCV gives coordinates in (x,y) format. 
So basically the answers will be interchanged. Note that, row = x and column = y.
在這裡，給出了兩種方法，一種使用Numpy函數，另一種使用OpenCV函數（最後註釋的行）執行相同的操作。
結果也相同，但略有不同。Numpy以（行，列）格式給出坐標，而OpenCV以（x，y）格式給出坐標。
因此，基本上答案是可以互換的。
! 注意，row = x，column = y
'''

'''
7. Maximum Value, Minimum Value and their locations
We can find these parameters using a mask image.
'''


def value_locations(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    mask = np.zeros(thresh.shape, np.uint8)
    return cv2.minMaxLoc(thresh, mask=mask)


'''
8. Mean Color or Mean Intensity
Here, we can find the average color of an object. 
Or it can be average intensity of the object in grayscale mode. 
We again use the same mask to do it.
'''


def intensity(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    mask = np.zeros(thresh.shape, np.uint8)
    return cv2.mean(image, mask=mask)


'''
9. Extreme Points
Extreme Points means topmost, bottommost, rightmost and leftmost points of the object.
'''


def extreme(image, start=127, end=255):
    ret, thresh = cv2.threshold(image, start, end, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
    topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
    bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
    return leftmost, rightmost, topmost, bottommost


'''
It returns an array where each row contains these values
[ start point, end point, farthest point, approximate distance to farthest point ].
We can visualize it using an image. We draw a line joining start point and end point, then draw a circle at the farthest point. 
Remember first three values returned are indices of cnt. So we have to bring those values from cnt.
'''


def convexity_defects(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 2, 1)
    cnt = contours[0]
    convexity_defects_hull = cv2.convexHull(cnt, returnPoints=False)
    return cv2.convexityDefects(cnt, convexity_defects_hull)


'''
OpenCV comes with a function cv2.matchShapes() which enables us to compare two shapes, 
or two contours and returns a metric showing the similarity. The lower the result, the better match it is. 
It is calculated based on the hu-moment values. Different measurement methods are explained in the docs.
'''


def match_shapes(image1, image2):
    ret, thresh = cv2.threshold(image1, 127, 255, 0)
    ret, thresh2 = cv2.threshold(image2, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 2, 1)
    cnt1 = contours[0]
    contours, hierarchy = cv2.findContours(thresh2, 2, 1)
    cnt2 = contours[0]
    return cv2.matchShapes(cnt1, cnt2, 1, 0.0)
