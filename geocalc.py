import math, cmath

longtitude_degree_length_km = 111.1

def calc_lat_length(latitude):
    #print 'radians =' + str(math.radians(latitude))
    #print 'cos =' + str(cmath.cos(math.radians(latitude)))
    #print 'radian' + str(math.radians(5.7295))
    latitude_degree_length_km = abs((111.3) * abs(cmath.cos(math.radians(latitude))))
# dont know why inaccurate
    return latitude_degree_length_km

def calc_lat_lon_change(latitude, latitude_previous, longtitude, longtitude_previous):
    latitude_move = (latitude_previous - latitude) * calc_lat_length(latitude)
    longtitude_move = (longtitude_previous - longtitude) * longtitude_degree_length_km
    return (latitude_move, longtitude_move)

#def define_moving_angle(latitude,longtitude)
#print calc_lat_length(90)


print calc_lat_lon_change(53.91251,53.91278,27.77017,27.76944)







