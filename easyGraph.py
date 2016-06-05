__author__ = 'Austin'
#https://www.reddit.com/r/dailyprogrammer/comments/4ijtrt/20160509_challenge_266_easy_basic_graph/

#open up file to read from
matrix = open("matrix.txt", 'r')
numNodes = int(matrix.readline())
degree = [0]*(numNodes + 1)
matrixMap = [[0]*(numNodes + 1)]*(numNodes + 1)
matrixMap = []
for p in range(0, numNodes):
    matrixMap.append([0 for i in range(0,numNodes)])

#cycling through the file to discover the edges
for line in matrix:
    temp = line.split(' ')
    degree[int(temp[0])] += 1
    degree[int(temp[1])] += 1
    matrixMap[int(temp[0])-1][int(temp[1])-1] = 1
    matrixMap[int(temp[1])-1][int(temp[0])-1] = 1

for i in range(1, numNodes + 1):
    print "node " + str(i) + " has degree " + str(degree[i])

print str(matrixMap)