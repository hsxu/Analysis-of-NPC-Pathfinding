import plotly.plotly as py
import plotly.graph_objs as go

matrix = [[0 for x in xrange(70)] for y in xrange(70)]

f = open('text.txt')
for line in f:
    if line == "":
        continue
    k = line.split(',')
    x = int(k[1])
    y = int(k[0])
    matrix[x][y] += 1

trace = go.Heatmap(z=matrix) 
data=[trace]
py.iplot(data, filename='basic-heatmap')    