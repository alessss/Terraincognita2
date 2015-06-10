import time
from tiles_calculations import calc_square
import tiles_calculations
import os

def file_worker(filename):# transfers coordinates from *.jpx file
    file = open(filename, 'r')
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
    return track_list

def get_gpx_files(folder):
    gpx_names = []
    for d, dirs, files in os.walk(folder):
        print files
        filenames = files
        for i in filenames:
            if '.gpx' in i:
                gpx_names.append(i)
    return gpx_names


