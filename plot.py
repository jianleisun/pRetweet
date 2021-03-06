from sklearn import linear_model
import numpy as np
import MySQLdb as mdb
import plotly.plotly as ply
from plotly.graph_objs import *

ply.sign_in('rathodsachin20', 'z83geaui8i')

N=7

def plot():
    try:
        con = mdb.connect('localhost', 'xsiena', 'xsiena', 'pretweet');

        cur = con.cursor()
        cur.execute("Select retweet_count, followers_count from tweets where retweet_count>0 order by followers_count desc")

        rows = cur.fetchall()
        #print len(rows)
        px = np.empty((0,1))
        py = np.empty((0,1))
        #p = np.zeros(7)
        #p = np.array([1,1,1,1,1,1,1])
        #p = np.array([1,1,1,1,1,1])
        #p = np.ones(6)
        #print p
        xlist = []
        ylist = []
        for row in rows:
            #print row
            #arr = np.array([i for i in row[6:]])
            #print arr
            #px = np.append(px, row[7])
            #py = np.append(py, row[6])
            xlist.append(row[1])
            ylist.append(row[0])
            #p = np.concatenate((p, arr), axis=0)

        px = np.asarray(xlist, dtype=int)
        py = np.asarray(ylist, dtype=int)

        for i in xrange(100):
            print px[i], ":", py[i]
        data = Data([Histogram( x=px, y=py )])
        layout = Layout(title='#Followers and retweets', xaxis=XAxis(title='#followers' ), yaxis=YAxis( title='#retweets') )
        fig = Figure(data=data, layout=layout)

        plot_url = ply.plot(fig, filename='horizontal-histogram')


    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
    finally:        
        if con:    
            con.close()


if __name__ == "__main__":
    plot()
