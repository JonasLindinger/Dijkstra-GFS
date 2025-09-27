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

    # Lazy Dijkstra
    def RunLazy(self, vertecies: list, startingVertexIndex: int):
        visuals: list = []
        listStartingHeight: float = 3
        listXPosition: float = -5.5
        listItemPadding: float = 0.5

        vertecies[startingVertexIndex].distance = 0
        priorityQueue: list = []
        priorityQueue.append((startingVertexIndex, 0)) # index, distance

        # visuals
        self.UpdatePriorityQueueVisuals(priorityQueue, vertecies, visuals, listXPosition, listStartingHeight, listItemPadding)

        while len(priorityQueue) != 0:
            item = self.GetTheNearestItem(priorityQueue)
            priorityQueue.remove(item)
            index: int = item[0]
            # distance: float = item[1] <- no need for it

            # visuals
            self.UpdatePriorityQueueVisuals(priorityQueue, vertecies, visuals, listXPosition, listStartingHeight, listItemPadding)

            vertecies[index].visited = True
            self.HighlightVertex(vertecies[index])
            for edge in vertecies[index].outgoingEdges:
                edgeVertexIndex: int = vertecies.index(edge.to)
                if vertecies[edgeVertexIndex].visited: continue
                self.HighlightEdge(edge)
                newDistance: float = vertecies[index].distance + edge.weight
                if newDistance < vertecies[edgeVertexIndex].distance:
                    vertecies[edgeVertexIndex].distance = newDistance
                    
                    vertexIndex: int = self.GetIndexFromFirstItemOfAToupleOfAList(priorityQueue, edgeVertexIndex)
                    if (vertexIndex != -1): # If we found it, remove it
                        priorityQueue.pop(vertexIndex)

                        # visuals
                        self.UpdatePriorityQueueVisuals(priorityQueue, vertecies, visuals, listXPosition, listStartingHeight, listItemPadding)

                    # Add it
                    priorityQueue.append((edgeVertexIndex, newDistance))

                    # visuals
                    self.UpdatePriorityQueueVisuals(priorityQueue, vertecies, visuals, listXPosition, listStartingHeight, listItemPadding)
                self.UnhighlightEdge(edge)
            self.UnhighlightVertex(vertecies[index])

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

    def HighlightVertex(self, vertex: Vertex):
        circle: Circle = vertex.visual[0]
        text: Text = vertex.visual[1]
        animation: AnimationGroup = AnimationGroup(
            circle.animate.set_stroke(color=YELLOW),
            text.animate.set_color(color=WHITE)
        )

        self.play(animation)
    
    def UnhighlightVertex(self, vertex: Vertex):
        circle: Circle = vertex.visual[0]
        text: Text = vertex.visual[1]
        animation: AnimationGroup = AnimationGroup(
            circle.animate.set_stroke(color=RED),
            text.animate.set_color(color=RED)
        )

        self.play(animation)

    def HighlightEdge(self, edge: Edge):
        arrow: Circle = edge.visual[0]

        self.play(arrow.animate.set_stroke(color=YELLOW))

    def UnhighlightEdge(self, edge: Edge):
        arrow: Circle = edge.visual[0]

        self.play(arrow.animate.set_stroke(color=WHITE))

    # -- AI GENEREATED METHOD --
    def UpdatePriorityQueueVisuals(self, priorityQueue, vertecies, visuals,
                                   listXPosition, listStartingHeight, listItemPadding):
        # Sort the queue by distance (second item of tuple)
        sortedQueue = sorted(priorityQueue, key=lambda item: item[1])

        # Remove items that are not in the queue anymore
        for vIndex, text in visuals.copy():
            found = False
            for item in sortedQueue:
                if item[0] == vIndex:
                    found = True
                    break
            if not found:
                self.play(Unwrite(text))
                visuals.remove((vIndex, text))

        # Step 1: prepare animations for shifting
        animations = []

        # Step 2: check for new items
        for item in sortedQueue:
            index = item[0]
            distance = item[1]

            alreadyThere = False
            for vIndex, text in visuals:
                if vIndex == index:
                    alreadyThere = True
                    break

            # If it's a new item
            if not alreadyThere:
                # Find where it should go
                order = sortedQueue.index(item) + 1
                newPos = [listXPosition,
                          listStartingHeight - (listItemPadding * order),
                          0]

                # Special case: if it's at the top and something is already there
                if order == 1 and len(visuals) > 0:
                    shiftAnimations = []
                    for vIndex, text in visuals:
                        oldX, oldY, oldZ = text.get_center()
                        newY = oldY - listItemPadding
                        shiftAnimations.append(text.animate.move_to([oldX, newY, oldZ]))
                    if len(shiftAnimations) > 0:
                        self.play(*shiftAnimations)

                # Now write the new item
                newText = Text(
                    vertecies[index].name + " -> " + str(vertecies[index].distance),
                    font_size=30
                ).move_to(newPos)
                visuals.append((index, newText))
                self.play(Write(newText))

        # Step 3: Reorder everything according to sorted queue
        animations = []
        for order, item in enumerate(sortedQueue, start=1):
            index = item[0]
            for vIndex, text in visuals:
                if vIndex == index:
                    newPos = [listXPosition,
                              listStartingHeight - (listItemPadding * order),
                              0]
                    animations.append(text.animate.move_to(newPos))
        if len(animations) > 0:
            self.play(*animations)

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