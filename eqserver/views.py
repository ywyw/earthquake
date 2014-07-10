from app import app, host, port, user, passwd, db
from app.helpers.database import con_db
from flask import Flask,jsonify,request,make_response,render_template
import happybase
import json
import StringIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import csv
import pprint
import ast

# To create a database connection, add the following
# within your view functions:
# con = con_db(host, port, user, passwd, db)

connection = happybase.Connection()
connection.open()
t = connection.table('hbase_eqsgrid')
t2 = connection.table('hbase_eqsgrid2')

# ROUTING/VIEW FUNCTIONS
@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')

@app.route('/home')
def home():
    # Renders home.html.
    return render_template('home.html')

@app.route('/slides')
def about():
    # Renders slides.html.
    return render_template('slides.html')

@app.route('/author')
def contact():
    # Renders author.html.
    return render_template('author.html')

@app.route('/earthquake/api2', methods = ['GET'])
def get_tasks2():
    # index by magnitude and time range, reset unix time to 0 at 1900 instead of 1970
    # left padding takes care of HBase lexicographical ordering
    magni = str(request.args.get('magnitude',None))
    mintime = (request.args.get('mintime',None))
    maxtime = (request.args.get('maxtime',None))
    if (mintime is not None):
        mintime = str(long(mintime)+2208988800000).zfill(13)
    if (maxtime is not None):
        maxtime = str(long(maxtime)+2208988800000).zfill(13)
    startstr = magni+"_"+str(mintime)
    stopstr = magni+"_"+str(maxtime)
    # return at maximum 10 earthquakes
    ans = t2.scan(row_start=startstr,row_stop=stopstr,limit=10)
    anslist = dict(ans)
    # final answer prints column family and double quote strings, which we don't want
    replaced = str(anslist).replace("a:","").replace("\"","")
    repeval= ast.literal_eval(replaced)
    return jsonify(**repeval)

@app.route('/earthquake/mag.png')
def plotmag():
    return plot('numbymag.tsv','Number of earthquakes per magnitude')

@app.route('/earthquake/numbyyear.png')
def numbyyear():
    return plot('numbyyear.tsv','Number of earthquakes per year')

@app.route('/earthquake/magbyyear.png')
def magbyyear():
    return plot('magbyyear.tsv','Avg magnitude per year')

@app.route('/earthquake/vorticity.png')
def vorticity():
    return plot('vorticity.tsv','Average abs vorticity per magnitude')

@app.route('/earthquake/strainmag.png')
def strainmag():
    return plot('strainmag.tsv','Average abs strain mag per magnitude')

@app.route('/earthquake/sunrise.png')
def sunrise():
    return plot('sunrisefl.tsv','Earthquakes per fraction of day from sunrise')

@app.route('/earthquake/sunset.png')
def sunset():
    return plot('sunsetfl.tsv','Earthquakes per fraction of day from sunset')

@app.route('/earthquake/moonphase.png')
def moonphase():
    return plot('moonphasefl.tsv','Earthquakes per fraction of moon illumination')

@app.route('/earthquake/damagecost.png')
def damagecost():
    return plot('totdambyyear.tsv','Average earthquake damage (mil) per year')

@app.route('/earthquake/deaths.png')
def deaths():
    return plot('totdeathbyyear.tsv','Average earthquake deaths per year')

# dynamically rendered plots that read off tsv files and returns a png response
def plot(filename,plottitle):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    with open(filename) as tsv:
        data = [(float(x), float(y)) for x, y in csv.reader(tsv, delimiter = '\t')]
        xs, ys = zip(*data)
    axis.plot(xs, ys) 
    fig.suptitle(plottitle, fontsize=20)
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/earthquake/index.html')
def realindex():
    return render_template('realindex.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
