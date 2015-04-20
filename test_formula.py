#http://gis-lab.info/qa/great-circles.html
import math
 
rad = 6372795
llat1 = 53.91378
llong1 = 27.76629
llat2 = 53.91522
llong2 = 27.76258
lat1 = llat1*math.pi/180.
lat2 = llat2*math.pi/180.
long1 = llong1*math.pi/180.
long2 = llong2*math.pi/180.
cl1 = math.cos(lat1)
cl2 = math.cos(lat2)
sl1 = math.sin(lat1)
sl2 = math.sin(lat2)
delta = long2 - long1
cdelta = math.cos(delta)
sdelta = math.sin(delta)
y = math.sqrt(math.pow(cl2*sdelta,2)+math.pow(cl1*sl2-sl1*cl2*cdelta,2))
x = sl1*sl2+cl1*cl2*cdelta
ad = math.atan2(y,x)
dist = ad*rad
x = (cl1*sl2) - (sl1*cl2*cdelta)
y = sdelta*cl2
z = math.degrees(math.atan(-y/x))

if (x < 0):
    z = z+180.
 
z2 = (z+180.) % 360. - 180.
z2 = - math.radians(z2)
anglerad2 = z2 - ((2*math.pi)*math.floor((z2/(2*math.pi))) )
angledeg = (anglerad2*180.)/math.pi
 
print 'Distance >> %.0f' % dist, ' [meters]'
print 'Initial bearing >> ', angledeg, '[degrees]'