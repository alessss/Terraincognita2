from gpx_converter import get_gpx_files
import tiles_calculations
from gpx_converter import file_worker

overall_square = 0
for i in get_gpx_files('D:\\Terra incognita\\'):
    overall_square = overall_square + tiles_calculations.calc_square(file_worker('D:\\Terra incognita\\'+i))
    print 'file' + ' ' + i + ' ' + 'processed'
    print overall_square
    print "% of land visited"
    print (overall_square/510072000)*100