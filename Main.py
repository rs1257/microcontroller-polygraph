from GUI import initial
from csvhandler import writetofile
f = open('data.csv', 'w')
writetofile('yellow', 'red', 'breath', 'heart', 'conduct', 'temperature')
f.close()
f = open('interpolatedheart.csv', 'w')
f.close()
initial()