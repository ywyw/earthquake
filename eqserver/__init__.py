# imports
from flask import Flask,jsonify,request,make_response,render_template
#import happybase
import json
import StringIO
import random # random integer generator
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

#connection = happybase.Connection()
#connection.open()
#t = connection.table('hbase_test2')
#print connection.tables()

# Creates our application.
app = Flask(__name__)
@app.route('/textbox')
def my_form():
    return render_template("request.html")

@app.route('/')
def hello_world():
	return 'Hello World!'

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    }
]

@app.route('/plot.png')
def plot():
    fig = Figure()
    print "ok"
    f=open('numbymag.tsv')
    
    axis = fig.add_subplot(1, 1, 1)
    #xs = range(100)
    #ys = [random.randint(1, 50) for x in xs]
    xs = [-1,0,1,2,3,4,5,6,7,8,9]
    ys = [617,51148,64243,120267,159628,267216,63973,6605,1707,82,5]
    print "ok2" 
    axis.plot(xs, ys)
    fig.suptitle('Number of earthquakes per magnitude', fontsize=20)
    #axis.xlabel("magnitude")
    #axis.ylabel("number")
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    params = str(request.args.get('magnitude',None))
    mintime = str(request.args.get('mintime',None))
    maxtime = str(request.args.get('maxtime',None))
    #ten = t.scan(limit=10)
    #tenlist = list(ten)
    filterstr = "SingleColumnValueFilter ('b','mag',=,'regexstring:%s$')" % params
    ans = t.scan(row_start=mintime,row_stop=maxtime,filter=filterstr,limit=10)
    anslist = list(ans)
    print len(anslist)
    print t.row("-107383963000")
    #print str(anslist)
    testlist = [
        {'param': "foo", 'val': 2},
        {'param': 'bar', 'val': 10}
    ]
    return jsonify( { 'earthquakes': anslist } )
    #return PrettyPrinter.pformat(ans)

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify( { 'task': task } ), 201

# Development configuration settings
# WARNING - these should not be used in production
app.config.from_pyfile('settings/development.cfg')

# Production configuration settings
# To have these override your development settings,
# you'll need to set your environment variable to
# the file path:
# export PRODUCTION_SETTINGS=/path/to/settings.cfg
app.config.from_envvar('PRODUCTION_SETTINGS', silent=True)

# Application DEBUG - should be True in development
# and False in production
app.debug = app.config["DEBUG"]

# DATABASE SETTINGS
host = app.config["DATABASE_HOST"]
port = app.config["DATABASE_PORT"]
user = app.config["DATABASE_USER"]
passwd = app.config["DATABASE_PASSWORD"]
db = app.config["DATABASE_DB"]

from app import views
