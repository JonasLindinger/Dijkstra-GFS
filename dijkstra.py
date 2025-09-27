class Dijkstra():
    def __init__(self):
        pass

    def RunLazy(self, vertecies: list, startingVertexIndex: int):
        vertecies[startingVertexIndex].distance = 0
        priorityQueue: list = []
        priorityQueue.append((startingVertexIndex, 0)) # index, distance
        while len(priorityQueue) != 0:
            item = self.GetTheNearestItem(priorityQueue)
            priorityQueue.remove(item)
            index: int = item[0]
            # distance: float = item[1] <- no need for it
            vertecies[index].visited = True
            for edge in vertecies[index].outgoingEdges:
                edgeVertexIndex: int = vertecies.index(edge.to)
                if vertecies[edgeVertexIndex].visited: continue
                newDistance: float = vertecies[index].distance + edge.weight
                if newDistance < vertecies[edgeVertexIndex].distance:
                    vertecies[edgeVertexIndex].distance = newDistance
                    
                    vertexIndex: int = self.GetListIndexFromVertexIndexInList(priorityQueue, edgeVertexIndex)
                    if (vertexIndex != -1): # If we found it, remove it
                        priorityQueue.pop(vertexIndex)

                    # Add it
                    priorityQueue.append((edgeVertexIndex, newDistance))

    def GetListIndexFromVertexIndexInList(self, list: list, indexToSearchFor: int) -> int:
        for i in range(len(list)):
            if (list[i][0] == indexToSearchFor):
                return i
            
        return -1
        # Create list
        distances: list = []

        # Fill list
        for i in range(length):
            distances.append(float("inf")) # float("inf") -> infinity

        # Return list
        return distances
    
    def GetTheNearestItem(self, list: list):
        nearestDistance: float = float('inf')
        nearestItem = None

        for item in list:
            if item[1] < nearestDistance:
                nearestDistance = item[1]
                nearestItem = item

        return nearestItem