from manim import *
from vertex import *
from edge import *
from graph import *
from dijkstra import *

class DijkstraIntro(Scene):
    def construct(self):
        # Show topic
        title: Text = Text("Dijkstra Algorithmus").scale(1.5)
        self.play(Write(title, run_time=2))
        
        titleAnimation: AnimationGroup = AnimationGroup(
            title.animate
            .scale(0.7)
            .move_to([-3.2, 3, 0]),
        )

        self.play(titleAnimation)

        underline: Underline = Underline(title, buff=0)

        self.play(Write(underline, run_time=.5))

        # Show content
        first: Text = Text("1. Was macht der Dijkstra Algorithmus?").scale(.5).move_to([-3.2, 2, 0])

        contentGroup: AnimationGroup = AnimationGroup(
            Write(first, run_time=1),
        )

        self.play(contentGroup)
        self.wait(5)

class LazyDijkstra(Scene):
    def construct(self):
        # Get the graph to display
        graph: Graph = self.GetGraph([2, 0, 0])

        self.DisplayGraph(graph)

        self.RunLazy(graph.vertices, 0)

        result: str = ""
        i: int = 0
        for currentVertex in graph.vertices:
            result += currentVertex.name + " -> " + str(currentVertex.distance) + ", "
            i += 1
        text: Text = Text(result, font_size=20).move_to([0, -3, 0])
        self.play(Create(text))

    # Lazy Dijkstra
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
    
    def GetTheNearestItem(self, list: list):
        nearestDistance: float = float('inf')
        nearestItem = None

        for item in list:
            if item[1] < nearestDistance:
                nearestDistance = item[1]
                nearestItem = item

        return nearestItem

    # Creating and displaying the graph
    def DisplayGraph(self, graph: Graph):
        # Create animation list
        animations = []

        # Add every vertex to the animations
        for vertex in graph.vertices:
            visual = vertex.visual
            circle = visual[0]  # Circle
            text = visual[1]    # Text
            animations.append(Create(circle))
            animations.append(Write(text))

        # Add every edge to the animations
        for edge in graph.edges:
            arrow = edge.visual
            animations.append(Write(arrow))

        # Display
        self.play(*animations)

    def GetGraph(self, position) -> Graph:
        # Create all vertices
        vStart: Vertex = Vertex("S", self.LocalToWorldPosition(position, [-3, 0, 0]), color=RED)
        vA: Vertex = Vertex("A", self.LocalToWorldPosition(position, [-1.5, 1.5, 0]), color=RED)
        vB: Vertex = Vertex("B", self.LocalToWorldPosition(position, [-1.5, -1.5, 0]), color=RED)
        vC: Vertex = Vertex("C", self.LocalToWorldPosition(position, [0, 0, 0]), color=RED)
        vTarget: Vertex = Vertex("Z", self.LocalToWorldPosition(position, [3, 0, 0]), color=RED)

        # Create all edges
        startToA: Edge = Edge(vStart, vA, 4, color=WHITE)
        startToB: Edge = Edge(vStart, vB, 1, color=WHITE)
        bToA: Edge = Edge(vB, vA, 2, color=WHITE)
        bToC: Edge = Edge(vB, vC, 5, color=WHITE)
        aToC: Edge = Edge(vA, vC, 1, color=WHITE)
        cToTarget: Edge = Edge(vC, vTarget, 3, color=WHITE)

        # Create the array
        vertices: list = [vStart, vA, vB, vC, vTarget]
        edges: list = [startToA, startToB, bToA, bToC, aToC, cToTarget]

        # Create the graph
        graph: Graph = Graph(vertices, edges)

        return graph
    
    def LocalToWorldPosition(self, worldPosition: list, localPosition: list) -> list:
        newWorldPosition: list = [
            worldPosition[0] + localPosition[0],
            worldPosition[1] + localPosition[1],
            worldPosition[2] + localPosition[2],
        ]
        return newWorldPosition