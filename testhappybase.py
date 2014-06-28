import happybase

conn = happybase.Connection('localhost',port=8888)
t = happybase.table('hbase_test')
row = t.row('http://comcat.cr.usgs.gov/earthquakes/eventpage/atlas19600229234000')
print conn.tables()
#print row
