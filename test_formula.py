#http://gis-lab.info/qa/great-circles.html
import math

route = [{'lat': 53.23,'lon':27.77},
         {'lat': 53.24,'lon':27.76},
         {'lat': 53.25,'lon':27.75},
         {'lat': 53.25,'lon':27.73},
         {'lat': 53.27,'lon':27.74},
         {'lat': 53.26,'lon':27.73},
         {'lat': 53.24,'lon':27.77},
         {'lat': 53.23,'lon':27.78},
         {'lat': 53.22,'lon':27.80}]


def calc_azimuth_right_left(llat1,llong1,llat2,llong2):
    rad = 6372795
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


    azimutr = angledeg+90
    azimutl = angledeg-90
    if azimutr > 360:
        azimutr = azimutr - 360
    if azimutl <0:
        azimutl = azimutl + 360
    print str(angledeg) + 'angledeg'
    print str(azimutr) + 'azimutr'
    print str(azimutl) + 'azimutl'
    #http://gis-lab.info/forum/viewtopic.php?f=1&t=9874
    latr = llat1 + 500 * math.cos(azimutr * math.pi / 180) / (6371000 * math.pi / 180)
    lonr = llong1 + 500 * math.sin(azimutr * math.pi / 180) / math.cos(llat1 * math.pi / 180) / (6371000 * math.pi / 180)

    latl = llat1 + 500 * math.cos(azimutl * math.pi / 180) / (6371000 * math.pi / 180)
    lonl = llong1 + 500 * math.sin(azimutl * math.pi / 180) / math.cos(llat1 * math.pi / 180) / (6371000 * math.pi / 180)

    print 'left' + str(latl)+' '+str(lonl)
    print 'right' + str(latr)+' '+str(lonr)
    return(latr, lonr, latl, lonl)

#print calc_azimuth_right_left(53.917534443,27.7704913427,53.910025557,27.7620886573)
full_route = []
point = {}
i = 0
for point in route:
    a = route[i]
    b = route[i+1]
    print 'point' + ' ' +str(i+1)
    print calc_azimuth_right_left(a.get('lat'),a.get('lon'),b.get('lat'),b.get('lon'))
    i = i+1