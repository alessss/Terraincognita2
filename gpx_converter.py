import time
from tiles_calculations import calc_square
import tiles_calculations
import argparse
import os

#parser = argparse.ArgumentParser(prog='PROG')
#parser.add_argument('--file', type = str)
#print parser
def file_worker(filename):
    file = open(filename, 'r')
    #file = open(parser.parse_args('--file'), 'r')
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
#           time.sleep(1)
    return track_list

def get_gpx_files(folder):
    #fold = os.walk(folder)
    gpx_names = []
    for d, dirs, files in os.walk(folder):
        print files
        filenames = files
        for i in filenames:
            if '.gpx' in i:
                gpx_names.append(i)
    return gpx_names

overall_square = 0
for i in get_gpx_files('D:\\Terra incognita\\'):
    overall_square = overall_square + tiles_calculations.calc_square(file_worker('D:\\Terra incognita\\'+i))
    print overall_square
