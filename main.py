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

class FirstDemo(Scene):
    def construct(self):
        # Get the graph to display
        graph: Graph = self.GetGraph([2, 0, 0])

        self.DisplayGraph(graph)

        dijkstra: Dijkstra = Dijkstra()
        distances: list = dijkstra.RunLazy(graph.vertices, 0)

        result: str = ""
        i: int = 0
        for currentVertex in graph.vertices:
            result += currentVertex.name + " -> " + str(currentVertex.distance) + ", "
            i += 1
        text: Text = Text(result, font_size=20).move_to([0, -3, 0])
        self.play(Create(text))

        return

        # Algorithm starting
        startingVertex: Vertex = graph.vertices[0]
        startingVertex.distance = 0 # We are here -> distance = 0
        priorityQueue: list = []
        priorityQueue.append(startingVertex)

        # Algorithm visualisation
        vertexDisplays: list = []
        xCoordinate: float = -5.5
        startingHeight: float = 3
        yPadding: float = 0.5
        distancesText = Text("", font_size=20).move_to([0, -3, 0])
        self.add(distancesText)
        firstVertexText: Text = Text(startingVertex.name + " -> " + str(startingVertex.distance), font_size=30).move_to([xCoordinate, startingHeight, 0])
        vertexDisplays.append((startingVertex, firstVertexText))

        self.play(Write(firstVertexText))

        # Algorithm
        while len(priorityQueue) != 0:
            # Get the closest vertex
            closestVertex: Vertex = self.GetClosestVertex(priorityQueue)

            # Get index and mark as visited
            i: int = graph.vertices.index(closestVertex)
            graph.vertices[i].visited = True

            # Remove from queue
            # visual
            indexOfItemToPop: int = priorityQueue.index(closestVertex)
            for kvp in vertexDisplays:
                vertex: Vertex = kvp[0]
                if (vertex == priorityQueue[indexOfItemToPop]):
                    # Hide
                    text: Text = kvp[1]
                    self.play(Unwrite(text))
                    vertexDisplays.pop(vertexDisplays.index(kvp)) # remove the visual from list
                    break

            # algorithm
            priorityQueue.pop(indexOfItemToPop)

            currentVertex: Vertex = graph.vertices[i]
            for currentEdge in graph.vertices[i].connectedEdges:
                edge: Edge = currentEdge
                if (edge.to.visited): continue # Skip visited vertexes
                newDistance: float = currentVertex.distance + edge.weight
                if (newDistance < edge.to.distance): # Update the distance if we found a closer way
                    edge.to.distance = newDistance
                    priorityQueue.append(edge.to) # Append the new vertex

                    # visual
                    newText: Text = Text(edge.to.name + " -> " + str(edge.to.distance), font_size=30).move_to([xCoordinate, startingHeight - (yPadding * len(vertexDisplays)), 0])
                    vertexDisplays.append((edge.to, newText))

                    self.play(Write(newText)) 

            # Remove the old distances text first
            if text is not None:
                self.remove(text)

            # Create new distances text
            distances: str = ""
            for currentVertex in graph.vertices:
                distances += currentVertex.name + " -> " + str(currentVertex.distance) + ", "
            text: Text = Text(distances, font_size=20).move_to([0, -3, 0])
            self.play(Create(text))

                
    def GetClosestVertex(self, vertices: list) -> Vertex:
        nearestDistance: float = float('inf')
        nearestVertex = None

        for vertex in vertices:
            if vertex.distance < nearestDistance:
                nearestDistance = vertex.distance
                nearestVertex = vertex

        return nearestVertex

    
    def dump(self, graph):
        # OLD
        currentVertex: Vertex = graph.vertices[0]
        currentVertex.distance = 0 # We are here -> distance = 0
        previousVertex: Vertex = Vertex("None", [0, 0, 0], RED)

        while (True):
            # Check if we are finished
            if (currentVertex == graph.vertices[len(graph.vertices) - 1]):
                # We are finished because there is no other way to check.
                break

            # Highlight the first
            currentCircle: Circle = graph.vertices[0].visual[0]
            currentText: Text = graph.vertices[0].visual[1]
            previousCircle: Circle = previousVertex.visual[0]
            previousText: Text = previousVertex.visual[1]
            self.play(
                currentCircle.animate.set_fill(RED, opacity=0).set_stroke(YELLOW), 
                currentText.animate.set_color(WHITE),
                previousCircle.animate.set_fill(RED, opacity=0).set_stroke(RED), 
                previousText.animate.set_color(RED),
            )

            closestVertex: Vertex = None
            for connectedEdge in currentVertex.connectedEdges:
                edge: Edge = connectedEdge
                otherVertex: Vertex = None
                if (edge.vertexA == currentVertex):
                    # We come from vertexA so we want to use vertexA
                    otherVertex = edge.vertexB
                else:
                    # We come from vertexB so we want to use vertexB
                    otherVertex = edge.vertexA

                # Update the vertexes distance if the new distance is less than the old distance
                newDistance: float = currentVertex.distance + edge.weight
                if (otherVertex.distance > newDistance):
                    # Update the distance because we found a better way
                    otherVertex.distance = newDistance

                # Check and save the closest vertex
                if (closestVertex == None or closestVertex.distance > otherVertex.distance):
                    closestVertex = otherVertex
            
            # Update the newest Vertex for the next run
            previousVertex = currentVertex
            currentVertex = closestVertex

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