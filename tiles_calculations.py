import math
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)

def num2deg(xtile, ytile, zoom):
  n = 2.0 ** zoom
  lon_deg = xtile / n * 360.0 - 180.0
  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
  lat_deg = math.degrees(lat_rad)
  return (lat_deg, lon_deg)

def distance_calculator(llat1,llong1,llat2,llong2):
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
    return dist

def calc_corners(x,y,zoom):
    NWlat, NWlon = num2deg(x, y, zoom)
    SWlat, SWlon = num2deg(x, y+1, zoom)
    NElat, NElon = num2deg(x+1, y, zoom)
    SElat, SElon = num2deg(x+1, y+1, zoom)
    NWNE = distance_calculator(NWlat, NWlon, NElat, NElon)
    SWSE = distance_calculator(SWlat, SWlon, SElat, SElon)
    NWSW = distance_calculator(NWlat, NWlon, SWlat, SWlon)
    NESE = distance_calculator(NElat, NElon, SElat, SElon)
    print NWNE, SWSE, NWSW, NESE

    print 'distance_difference'
    print NWNE - SWSE #distance difference
    print 'square NORTH'
    print NWSW * NWNE
    print 'square SOUTH'
    print SWSE * NWSW
    print 'square_difference'
    print (NWSW * NWNE) - (SWSE * NWSW)


print calc_corners(77580, 65535, 17)

print deg2num(53.23432,24.54323, 12)