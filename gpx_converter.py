import time
from tiles_calculations import calc_square
import tiles_calculations
__author__ = 'a_makarevich'
file = open('D:\Terra incognita\long_gpx.gpx', 'r')
track_list = []
track_dict = {}
for line in file:
    if '<trkpt' in line:
        lat_start = line.find('"')
        lat_end = line.find('"',lat_start+1)
        lat = line[lat_start+1:lat_end]
        lon_start = line.find('"', lat_end+1)
        lon_end = line.find('"',lon_start+1)
        lon = line[lon_start+1:lon_end]
        track_dict = {'lat': lat, 'lon': lon}
        track_list.append(track_dict)
#        time.sleep(1)
print tiles_calculations.calc_square(track_list)