class Dijkstra():
    def __init__(self):
        pass

    def Run(self, vertecies: list, startingVertexIndex: int) -> list:
        verteciesCount: int = len(vertecies)
        visited: list = self.CreateVisitedList(verteciesCount)
        distances: list = self.CreateDistanceList(verteciesCount)
        distances[startingVertexIndex] = 0
        priorityQueue: list = []
        priorityQueue.append((startingVertexIndex, 0)) # index, distance
        while len(priorityQueue) != 0:
            item = self.GetTheNearestItem(priorityQueue)
            priorityQueue.remove(item)
            index: int = item[0]
            # distance: float = item[1] <- no need for it
            visited[index] = True
            for edge in vertecies[index].outgoingEdges:
                edgeVertexIndex: int = vertecies.index(edge.to)
                if visited[edgeVertexIndex]: continue
                newDistance: float = distances[index] + edge.weight
                if newDistance < distances[edgeVertexIndex]:
                    distances[edgeVertexIndex] = newDistance
                    
                    vertexIndex: int = self.GetListIndexFromVertexIndexInList(priorityQueue, edgeVertexIndex)
                    if (vertexIndex != -1): # If we found it, remove it
                        priorityQueue.pop(vertexIndex)

                    # Add it
                    priorityQueue.append((edgeVertexIndex, newDistance))
        
        return distances

    def GetListIndexFromVertexIndexInList(self, list: list, indexToSearchFor: int) -> int:
        for i in range(len(list)):
            if (list[i][0] == indexToSearchFor):
                return i
            
        return -1

    def CreateVisitedList(self, length: int) -> list:
        # Create list
        visited: list = []

        # Fill list
        for i in range(length):
            visited.append(False)

        # Return list
        return visited
    
    def CreateDistanceList(self, length: int) -> list:
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