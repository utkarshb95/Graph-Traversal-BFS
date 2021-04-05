import sys
import re
import linecache as lc

GRAPH_FILE_NAME = sys.argv[1]
OUTPUT_FILE_NAME = sys.argv[2]
queuenode = []
ajm = []
mydict = {"color":"v1", "visited":"v2", "parentnode":"v3", "direction":"v4"}

# To get number of rows and columns
rc = lc.getline(GRAPH_FILE_NAME,1)
y = rc.split()
r = int(y[0])
c = int(y[1])
print("Size of the maze is ", r, " x ", c)

# To create graph from text file
with open(GRAPH_FILE_NAME) as file:
	next(file)
	graph = [line for line in file]
open(OUTPUT_FILE_NAME, 'w').close()

# To add nodes to the queue
def addnodes():
	nodeclr = ajm[queuenode[0][0]][queuenode[0][1]]["color"]
	nodecol = queuenode[0][1]
	noderow = queuenode[0][0]
	nodedir = ajm[queuenode[0][0]][queuenode[0][1]]["direction"]
	i = 0
	j = 0

	if (nodedir == "N"):
		i = noderow
		while (i >= 0):
			if (ajm[i][nodecol]["color"] != nodeclr and ajm[i][nodecol]["visited"] == 0):
				queuenode.append((i,nodecol))
				ajm[i][nodecol]["visited"] = 1
				ajm[i][nodecol]["parentnode"] = (noderow, nodecol)
			i = i-1
	
	elif (nodedir == "NE"):
		i = noderow
		j = nodecol
		while  (i >= 0 and j < c):
			if (ajm[i][j]["color"] != nodeclr and ajm[i][j]["visited"] == 0):
				queuenode.append((i,j))
				ajm[i][j]["visited"] = 1
				ajm[i][j]["parentnode"] = (noderow, nodecol)
			i = i-1
			j = j+1

	elif (nodedir == "E"):
		i = nodecol
		while  (i < c):
			if (ajm[noderow][i]["color"] != nodeclr and ajm[noderow][i]["visited"] == 0):
				queuenode.append((noderow,i))
				ajm[noderow][i]["visited"] = 1
				ajm[noderow][i]["parentnode"] = (noderow, nodecol)
			i = i+1

	elif (nodedir == "SE"):
		i = noderow
		j = nodecol
		while  (i < r and j < c):
			if (ajm[i][j]["color"] != nodeclr and ajm[i][j]["visited"] == 0):
				queuenode.append((i,j))
				ajm[i][j]["visited"] = 1
				ajm[i][j]["parentnode"] = (noderow, nodecol)
			i = i+1
			j = j+1

	elif (nodedir == "S"):
		i = noderow
		while  (i < r):
			if (ajm[i][nodecol]["color"] != nodeclr and ajm[i][nodecol]["visited"] == 0):
				queuenode.append((i,nodecol))
				ajm[i][nodecol]["visited"] = 1
				ajm[i][nodecol]["parentnode"] = (noderow, nodecol)
			i = i+1

	elif (nodedir == "SW"):
		i = noderow
		j = nodecol
		while  (i < r and j >= 0):
			if (ajm[i][j]["color"] != nodeclr and ajm[i][j]["visited"] == 0):
				queuenode.append((i,j))
				ajm[i][j]["visited"] = 1
				ajm[i][j]["parentnode"] = (noderow, nodecol)
			i = i+1
			j = j-1

	elif (nodedir == "W"):
		i = nodecol
		while  (i >= 0):
			if (ajm[noderow][i]["color"] != nodeclr and ajm[noderow][i]["visited"] == 0):
				queuenode.append((noderow,i))
				ajm[noderow][i]["visited"] = 1
				ajm[noderow][i]["parentnode"] = (noderow, nodecol)
			i = i-1

	elif (nodedir == "NW"):
		i = noderow
		j = nodecol
		while  (i >= 0 and j >= 0):
			if (ajm[i][j]["color"] != nodeclr and ajm[i][j]["visited"] == 0):
				queuenode.append((i,j))
				ajm[i][j]["visited"] = 1
				ajm[i][j]["parentnode"] = (noderow, nodecol)
			i = i-1
			j = j-1
	elif (nodedir == "O"):
		print("Bullseye reached. Yay!")

# To print the path
def printPath():
        i = r-1
        j = c-1
        path = []

        while True:
            parentRow = ajm[i][j]["parentnode"][0]
            parentColumn = ajm[i][j]["parentnode"][1]
            tempRow = i - ajm[i][j]["parentnode"][0]
            tempColumn = j - ajm[i][j]["parentnode"][1]

            if(ajm[parentRow][parentColumn]["direction"][0] == 'S'):
                path.append(tuple([ajm[parentRow][parentColumn]["direction"], tempRow]))
            elif(ajm[parentRow][parentColumn]["direction"][0] == 'N'):
                path.append(tuple([ajm[parentRow][parentColumn]["direction"], (tempRow * -1)]))
            elif(ajm[parentRow][parentColumn]["direction"][0] == 'E'):
                path.append(tuple([ajm[parentRow][parentColumn]["direction"], tempColumn]))
            elif(ajm[parentRow][parentColumn]["direction"][0] == 'W'):
                path.append(tuple([ajm[parentRow][parentColumn]["direction"], (tempColumn * -1)]))

            i = parentRow
            j = parentColumn

            if(i != 0 or j != 0):
                continue
            else:
            	break
        print("Number of nodes traversed is ", len(path))
        x = len(path) - 1
        while x >= 0:
        	with open(OUTPUT_FILE_NAME, "a") as f:
        		print(f"{path[x][1]}{path[x][0]}", end=" ", file=f)
        	x = x - 1


# To create a mulidimensional list of dictionaries as adjacency matrix
for j in range(len(graph)):
	lst = graph[j]
	i = 0
	x = []
	while(i < len(lst)):
		if(lst[i] == 'R' or lst[i] == 'B'):
			mydict["color"] = lst[i]
			mydict["visited"] = 0
			mydict["parentnode"] = (0,0)
			if(lst[i+3] != ' '):
				mydict["direction"] = lst[i+2:i+4]
				i = i+3
			else:
				mydict["direction"] = lst[i+2:i+3]
				i = i+2
			x.append(mydict.copy())
		elif(lst[i] == 'O'):
			mydict["color"] = lst[i]
			mydict["visited"] = 0
			mydict["parentnode"] = (0,0)
			mydict["direction"] = lst[i]
			x.append(mydict.copy())
		i += 1
	ajm.append(x)

# To perform BFS
queuenode.append((0,0))
while(queuenode != []):
	ajm[queuenode[0][0]][queuenode[0][1]]["visited"] = 1
	addnodes()
	queuenode.pop(0)

printPath()