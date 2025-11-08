from main import *
from manim import *
from vertex import *

class Graph():
    def __init__(self, vertices, edges):
        self.vertices: list = vertices
        self.edges: list = edges
        self.group: Group = Group()
        self.displayed_distances = False

    # Creating and displaying the graph
    def write(self, scene: Scene, showDistances: bool) -> Group:
        graphGroup: Group = self.group

        # Create animation list
        animations = []

        # Add every vertex to the animations
        for vertex in self.vertices:
            visual = vertex.visual
            circle = visual[0]  # Circle
            text = visual[1]    # Text
            distance = visual[2]
            animations.append(Create(circle))
            animations.append(Write(text))
            animations.append(Write(distance))
            graphGroup.add(visual)

        # Add every edge to the animations
        for edge in self.edges:
            arrow = edge.visual
            animations.append(Write(arrow))
            graphGroup.add(arrow)

        # Display
        scene.play(*animations)

        self.group = graphGroup
        self.displayed_distances = showDistances

        return self.group
    
    def generate_group(self, showDistances: bool) -> Group:
        graphGroup: Group = Group()

        # Add every vertex to the animations
        for vertex in self.vertices:
            visual = vertex.visual
            graphGroup.add(visual)

        # Add every edge to the animations
        for edge in self.edges:
            arrow = edge.visual
        graphGroup.add(arrow)

        self.group = graphGroup
        self.displayed_distances = showDistances

        return self.group 

    def solve(self, scene: Scene, liveUpdateVisuals: bool):
        if self.group == None:
            self.write(scene, True)

        self.RunLazy(scene, self.vertices, 0, liveUpdateVisuals)

    def highlight_solution(self, scene: Scene):
        if self.group == None:
            self.write(scene, True)

        startingVertexIndex: int = 0 # We assume, that the starting vertex is the first item in the vertecies
        endingVertexIndex: int = len(self.vertices) - 1 # -1 makes it an index. We assume, that the ending vertex is at the end
        path: list = self.GetShortestPath(scene, self.vertices, startingVertexIndex, endingVertexIndex)

        for vertex in self.vertices:
            tracker: ValueTracker = vertex.UpdateDistanceAndReturnAnimation(vertex.distance, True)
            tracker.set_value(vertex.distance)

        for i in range(len(path)):
            vertex: Vertex = path[i]
            self.HighlightVertex(scene, vertex, 0.1)

            if i < len(path) - 1:
                nextVertex: Vertex = path[i + 1]
                edge: Edge = self.GetEdge(vertex, nextVertex)
                self.HighlightEdge(scene, edge, 0.1)

    def resetVisuals(self, scene: Scene):
        animations: list = []

        for vertex in self.vertices:
            tracker: ValueTracker = vertex.ResetDistance()
            tracker.set_value(vertex.distance)
            #animations.append(tracker.set_value(vertex.distance))

        for vertex in self.vertices:
            circle: Circle = vertex.visual[0]
            text: Text = vertex.visual[1]
            animations.append(circle.animate.set_stroke(color=WHITE))            
            animations.append(text.animate.set_stroke(color=WHITE))

        for edge in self.edges:
            arrow: Circle = edge.visual[0]
            animations.append(arrow.animate.set_stroke(color=WHITE).set_fill(color=WHITE))

        scene.play(*animations, run_time=1)

    def GetEdge(self, start: Vertex, to: Vertex) -> Edge:
        for edge in start.outgoingEdges:
            if edge.to == to:
                return edge
            
        return None

    # (Un)Highlighting vertices and edges
    def HighlightVertex(self, scene: Scene, vertex: Vertex, run_time: float):
        circle: Circle = vertex.visual[0]
        text: Text = vertex.visual[1]
        animation: AnimationGroup = AnimationGroup(
            circle.animate.set_stroke(color=YELLOW),
            text.animate.set_color(color=WHITE)
        )

        scene.play(animation, run_time=run_time)
    
    def UnhighlightVertex(self, scene: Scene, vertex: Vertex, run_time: float):
        circle: Circle = vertex.visual[0]
        text: Text = vertex.visual[1]
        animation: AnimationGroup = AnimationGroup(
            circle.animate.set_stroke(color=WHITE),
            text.animate.set_color(color=WHITE)
        )

        scene.play(animation, run_time=run_time)

    def HighlightEdge(self, scene: Scene, edge: Edge, run_time: float):
        arrow: Circle = edge.visual[0]

        scene.play(arrow.animate.set_stroke(color=YELLOW).set_fill(color=YELLOW), run_time=run_time)

    def UnhighlightEdge(self, scene: Scene, edge: Edge, run_time: float):
        arrow: Circle = edge.visual[0]

        scene.play(arrow.animate.set_stroke(color=LIGHT_GRAY).set_fill(color=LIGHT_GRAY), run_time=run_time)

    # Lazy Dijkstra
    def RunLazy(self, scene: Scene, vertecies: list, startingVertexIndex: int, liveUpdateVisuals):
        # 1. Init variables 

        # 1.1. Set the starting vertex to a distance of 0 
        vertecies[startingVertexIndex].UpdateDistance(scene, 0, liveUpdateVisuals)

        # 1.2.Create the priotity queue and append the startingVertex
        priorityQueue: list = []
        priorityQueue.append((startingVertexIndex, 0)) # index, distance

        # While the priority Queue isn't empty
        while len(priorityQueue) != 0:
            # 2.1. Get nearest vertex from the priority queue and remove the item from the list
            item = self.GetTheNearestItem(priorityQueue)
            priorityQueue.remove(item)

            # 2.2. Get the index of the vertex in the vertecies list
            index: int = item[0]
            # distance: float = item[1]

            # 2.3. Mark the vertex as visited
            vertecies[index].visited = True

            # Visuals
            if (liveUpdateVisuals):
                self.HighlightVertex(scene, vertecies[index], 0.5)

            # Go through every outgoing edge of this vertex
            for edge in vertecies[index].outgoingEdges:
                # 3.1. Get the index of the vbertex the edge points at.
                edgeVertexIndex: int = vertecies.index(edge.to)

                # If the vertex is visited, skip it
                if vertecies[edgeVertexIndex].visited: continue

                # Visuals
                if (liveUpdateVisuals):
                    self.HighlightEdge(scene, edge, 0.5)

                # 3.2. Calculate the distance if we went to the vertex vie the current vertex of the edge it points at.
                newDistance: float = vertecies[index].distance + edge.weight

                # If the distance if less then the old distance (default is infinity), update it.
                if newDistance < vertecies[edgeVertexIndex].distance:
                    # 4.1. Update distance and mark the vertexes previousVertex to the current Vertex to later find the shortest path.
                    vertecies[edgeVertexIndex].previousVertex = vertecies[index]
                    vertecies[edgeVertexIndex].UpdateDistance(scene, newDistance, liveUpdateVisuals)
                    
                    # 4.2 When the vertex the edge points to, is in our list, remove it.
                    vertexIndex: int = self.GetIndexFromFirstItemOfAToupleOfAList(priorityQueue, edgeVertexIndex)
                    if (vertexIndex != -1): # If we found it, remove it
                        priorityQueue.pop(vertexIndex)

                    # 4.3 Add the vertex the edge points to, to the priority queue
                    priorityQueue.append((edgeVertexIndex, newDistance))

                    # Visuals
                    if (liveUpdateVisuals):
                        self.UnhighlightEdge(scene, edge, 0.5)

            # Visuals
            if (liveUpdateVisuals):
                self.UnhighlightVertex(scene, vertecies[index], 0.5)
    
    # Returns a list from the starting node to the end node that contains every vertex which is part of the shortest path.
    def GetShortestPath(self, scene: Scene, vertecies: list, startingVertexIndex: int, endingVertexIndex) -> list:
        self.RunLazy(scene, self.vertices, startingVertexIndex, False)
        path: list =  []

        # Check if we got to the ending vertex
        if vertecies[endingVertexIndex].distance == float("inf"): return path

        currentVertex: Vertex = vertecies[endingVertexIndex]
        while currentVertex is not None:
            path.append(currentVertex)
            currentVertex = currentVertex.previousVertex
        
        # This makes the path start at the starting vertex and end at the ending vertex
        path.reverse()

        return path
    
    # Returns the shortest distance between two vertecies
    def GetShortestDistance(self, scene: Scene, vertecies: list, startingVertexIndex: int, endingVertexIndex) -> float:
        self.RunLazy(scene, self.vertices, startingVertexIndex, False)
        shortestDistance: float = float("inf")

        # Check if we got to the ending vertex
        if vertecies[endingVertexIndex].distance == float("inf"): return shortestDistance

        shortestDistance = vertecies[endingVertexIndex].distance
        return shortestDistance

    def GetTheNearestItem(self, list: list):
        nearestDistance: float = float('inf')
        nearestItem = None

        for item in list:
            if item[1] < nearestDistance:
                nearestDistance = item[1]
                nearestItem = item

        return nearestItem

    def GetIndexFromFirstItemOfAToupleOfAList(self, list: list, item):
        for i in range(len(list)):
            if (list[i][0] == item):
                return i
            
        return -1