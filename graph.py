from main import *
from manim import *

class Graph():
    def __init__(self, vertices, edges):
        self.vertices: list = vertices
        self.edges: list = edges
        self.group: Group = self.generate_group(True)
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
            animations.append(Create(circle))
            animations.append(Write(text))
            graphGroup.add(visual)

        if showDistances:
            for vertex in self.vertices:
                distanceText = Text("∞", color=RED, font_size=20).move_to(vertex.visual[0].get_center() + DOWN * 0.25, aligned_edge=DOWN)
                vertex.visual.add(distanceText)
                scene.add(distanceText)
                graphGroup.add(distanceText)

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

        if showDistances:
            for vertex in self.vertices:
                distanceText = Text("∞", color=RED, font_size=20).move_to(vertex.visual[0].get_center() + DOWN * 0.25, aligned_edge=DOWN)
                vertex.visual.add(distanceText)
                graphGroup.add(distanceText)

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

        animations: list = []
        texts: list = []

        for vertex in self.vertices:
            transform, old_text, new_text = vertex.UpdateDistanceAndReturnAnimation(scene, vertex.distance, True)
            animations.append(transform)
            texts.append((old_text, new_text))

        scene.play(*animations, run_time=1)

        for old_text, new_text in texts:
            old_text.become(new_text)

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
            animations.append(vertex.ResetDistance(scene))

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
        vertecies[startingVertexIndex].UpdateDistance(scene, 0, liveUpdateVisuals)
        priorityQueue: list = []
        priorityQueue.append((startingVertexIndex, 0)) # index, distance

        while len(priorityQueue) != 0:
            item = self.GetTheNearestItem(priorityQueue)
            priorityQueue.remove(item)
            index: int = item[0]
            # distance: float = item[1]

            vertecies[index].visited = True
            for edge in vertecies[index].outgoingEdges:
                edgeVertexIndex: int = vertecies.index(edge.to)
                if vertecies[edgeVertexIndex].visited: continue
                newDistance: float = vertecies[index].distance + edge.weight
                if newDistance < vertecies[edgeVertexIndex].distance:
                    vertecies[edgeVertexIndex].previousVertex = vertecies[index]
                    vertecies[edgeVertexIndex].UpdateDistance(scene, newDistance, liveUpdateVisuals)
                    
                    vertexIndex: int = self.GetIndexFromFirstItemOfAToupleOfAList(priorityQueue, edgeVertexIndex)
                    if (vertexIndex != -1): # If we found it, remove it
                        priorityQueue.pop(vertexIndex)

                    # Add it
                    priorityQueue.append((edgeVertexIndex, newDistance))
    
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