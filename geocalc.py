import math, cmath

longtitude_degree_length_km = 111.1

def calc_lat_length(latitude):
    #print 'radians =' + str(math.radians(latitude))
    #print 'cos =' + str(cmath.cos(math.radians(latitude)))
    #print 'radian' + str(math.radians(5.7295))
    latitude_degree_length_km = abs((111.3) * abs(cmath.cos(math.radians(latitude))))
# dont know why inaccurate
    return latitude_degree_length_km

def calc_lat_lon_change_distance_angle(latitude, latitude_previous, longtitude, longtitude_previous):
    latitude_move = (latitude_previous - latitude) * calc_lat_length(latitude)
    longtitude_move = (longtitude_previous - longtitude) * longtitude_degree_length_km
    distance = math.sqrt(latitude_move*latitude_move+longtitude_move*longtitude_move)
    beta = math.acos(latitude_move/distance)
    return (latitude_move, longtitude_move, distance,beta)




print calc_lat_lon_change_distance_angle(53.91378,53.91522,27.76629,27.76258)
print calc_lat_lon_change_distance_angle(53.91378,53.91522,27.76629,27.76258)






