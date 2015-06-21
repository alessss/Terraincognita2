from flask import Flask
import MySQLdb
import string



app = Flask(__name__)
@app.route('/api/v1.0/post_point', methods=['POST'])
def post_point():
    db = MySQLdb.connect(host="localhost", user="mayakmin", passwd="duYaa8ah", db="mayakmin_terraincognita", charset='utf8')
    cursor = db.cursor()
    point = {'lat':lat, 'lon':lon, 'counted':0}
    sql = """INSERT INTO usr_1(lat, lon, counted) VALUES {"lat":point[lat], "lon":point[lon], "counted":0}"""
    cursor.execute(sql)
    db.commit()
#@app.route('/')
#def index():
#    return "Hello, World!"
#
#if __name__ == '__main__':
    app.run(debug=True)