import plotly.plotly as py
import plotly.graph_objs as go

matrix = [[0 for x in xrange(75)] for y in xrange(75)]

f = open('text.txt')
for line in f:
    if line == "" or line == '\n':
        continue
    k = line.split(',')
    x = int(k[1])
    y = int(k[0])

    matrix[x-2][y-2] += 1
    matrix[x-1][y-2] += 1
    matrix[x][y-2] += 1
    matrix[x+1][y-2] += 1
    matrix[x+2][y-2] += 1

    matrix[x-2][y-1] += 1
    matrix[x-1][y-1] += 1
    matrix[x][y-1] += 1
    matrix[x+1][y-1] += 1
    matrix[x+2][y-1] += 1

    matrix[x-2][y] += 1
    matrix[x-1][y] += 1
    matrix[x+1][y] += 1
    matrix[x+2][y] += 1

    matrix[x-2][y+1] += 1
    matrix[x-1][y+1] += 1
    matrix[x][y+1] += 1
    matrix[x+1][y+1] += 1
    matrix[x+2][y-2] += 1

    matrix[x-2][y+2] += 1
    matrix[x-1][y+2] += 1
    matrix[x][y+2] += 1
    matrix[x+1][y+2] += 1
    matrix[x+2][y+2] += 1

trace = go.Heatmap(z=matrix) 
data=[trace]
py.iplot(data, filename='basic-heatmap')    