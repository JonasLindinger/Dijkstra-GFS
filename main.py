from manim import *
from vertex import *
from edge import *
from graph import *
from dijkstra import *
import random

class GFS(Scene):
    def construct(self):
        # Run both parts in sequence
        self.Intro()
        self.WhatIs()
        # self.basics()
        # self.shortestPathProblem()

    def Intro(self):
        # Topic title
        self.title = Text("Dijkstra Algorithmus").scale(1.5)
        self.play(Write(self.title, run_time=2))
        self.wait(1)

        self.play(self.title.animate.scale(0.7).move_to([-6.5, 3, 0], aligned_edge=LEFT))
        self.underline = Underline(self.title, buff=0)
        self.play(Write(self.underline, run_time=0.5))

        # Gliederung
        self.first  = Text("1. Was ist der Dijkstra Algorithmus?").scale(.5).move_to([-6.5, 2, 0], aligned_edge=LEFT)
        self.second = Text("2. Das Problem des kürzesten Weges.").scale(.5).move_to([-6.5, 1.5, 0], aligned_edge=LEFT)
        self.third  = Text("3. Was ist der Dijkstra Algorithmus?").scale(.5).move_to([-6.5, 1, 0], aligned_edge=LEFT)
        self.fourth = Text("4. Wo wird der Dijkstra Algorithmus genutzt?").scale(.5).move_to([-6.5, 0.5, 0], aligned_edge=LEFT)
        self.fifth  = Text("5. Wie funktioniert der Lazy Dijkstra Algorithmus?").scale(.5).move_to([-6.5, 0, 0], aligned_edge=LEFT)

        self.play(
            Write(self.first, run_time=1), Write(self.second, run_time=1),
            Write(self.third, run_time=1), Write(self.fourth, run_time=1), Write(self.fifth, run_time=1)
        )
        self.wait(2)

    def WhatIs(self):
        new_text = Text("Was ist der Dijkstra Algorithmus?").move_to([-6.5, 3, 0], aligned_edge=LEFT).scale(1.0)
        new_underline = Underline(new_text, buff=0)

        # Animate text morph
        self.play(
            Unwrite(self.title),
            Unwrite(self.underline),
            Unwrite(self.second),
            Unwrite(self.third),
            Unwrite(self.fourth),
            Unwrite(self.fifth),
            Transform(self.first, new_text),
            Write(new_underline),
            run_time=1
        )

        # Update references
        self.first = new_text
        self.underline = new_underline

        # Show Edsger Dijkstra infos
        img = ImageMobject("Edsger_Dijkstra.jpg") # https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Edsger_Wybe_Dijkstra.jpg/250px-Edsger_Wybe_Dijkstra.jpg
        img.scale(2)
        self.play(FadeIn(img))
        self.play(img.animate.scale(0.6).to_edge(UL).shift(DOWN))

        name = Text("Edsger W. Dijkstra (1930 - 2002)", font_size=24).next_to(img, RIGHT, buff=0.3).shift(UP)
        country = Text("Niederländer", font_size=24).next_to(img, RIGHT, buff=0.3).shift(UP * 0.5)
        award = Text("Turing Award (1972)", font_size=24).next_to(img, RIGHT, buff=0.3)
    
        self.play(Write(name), run_time=1)
        self.wait(0.5)
        self.play(Write(country), run_time=1)
        self.wait(0.5)
        self.play(Write(award), run_time=1)

        hidePersonalInfo: AnimationGroup = AnimationGroup(
            FadeOut(img, run_time=1),
            Unwrite(name, run_time=1),
            Unwrite(country, run_time=1),
            Unwrite(award, run_time=1),
        )

        self.wait(1)
        self.play(hidePersonalInfo, run_time=1)
        
        demo_graph = self.GetGraphA([0, 0, 0], True)
        demo_graph.write(self, True)
        self.wait(1)
        demo_graph.highlight_solution(self)

    def basics(self):
        # Animate menu removal and title change
        self.basicsText = Text("Grundlagen").scale(1.5).scale(0.7).move_to([-6.5, 3, 0], aligned_edge=LEFT)
        self.basicsTextUnderline = Underline(self.basicsText, buff=0)

        self.play(
            Unwrite(self.first, run_time=0.75), Unwrite(self.second, run_time=0.75),
            Unwrite(self.third, run_time=0.75), Unwrite(self.fourth, run_time=0.75), Unwrite(self.fifth, run_time=0.75),
            Transform(self.title, self.basicsText, run_time=1),
            Transform(self.underline, self.basicsTextUnderline, run_time=1),
        )

        self.wait(1)

        graph: Graph = self.GetGraphA([0, 0, 0], False)

        self.graphGroup: Group = self.DisplayGraph(graph, False)

        vertexText: Text = Text("Vertex (sg), Vertices (pl)", color=RED).scale(.5).move_to([-6.5, 2, 0], aligned_edge=LEFT)
        self.graphGroup.add(vertexText)
        self.animations.clear()
        
        for vertex in graph.vertices:
            circle: Circle = vertex.visual[0]
            name: Text = vertex.visual[1]
            self.animations.append(circle.animate.set_color(RED))
            self.animations.append(name.animate.set_color(RED))
        
        self.animations.append(Write(vertexText))

        self.play(*self.animations)

        edgeText: Text = Text("Edge (sg), Edges (pl)", color=GREEN).scale(.5).move_to([-6.5, 1.5, 0], aligned_edge=LEFT)
        self.graphGroup.add(edgeText)
        self.animations.clear()
        
        for edge in graph.edges:
            arrow: Arrow = edge.visual[0]
            self.animations.append(arrow.animate.set_fill(GREEN))
            self.animations.append(arrow.animate.set_color(GREEN))

        self.animations.append(Write(edgeText))

        self.play(*self.animations)
        
        self.animations.clear()

        self.wait(2)

    def shortestPathProblem(self):
        # Animate transition
        self.sppText = Text("Das Problem des kürzesten Weges.").scale(1.5).scale(0.7).move_to([-6.5, 3, 0], aligned_edge=LEFT)
        self.sppTextUnderline = Underline(self.sppText, buff=0)

        dot: Dot = Dot([0, 0, 0], 0, color=ORANGE)

        self.play(
            ReplacementTransform(self.graphGroup, dot),
            ReplacementTransform(self.basicsText, self.sppText),
            ReplacementTransform(self.basicsTextUnderline, self.sppTextUnderline),
        )

        self.wait(1)

        # Todo: fix text overlap

    def GetGraphA(self, position, showDistances: bool) -> Graph:
        # Create all vertices
        vStart: Vertex = Vertex("S", self.LocalToWorldPosition(position, [-4, 0, 0]), WHITE, showDistances)
        vA: Vertex = Vertex("A", self.LocalToWorldPosition(position, [-2, 2, 0]), WHITE, showDistances)
        vB: Vertex = Vertex("B", self.LocalToWorldPosition(position, [-2, -2, 0]), WHITE, showDistances)
        vC: Vertex = Vertex("C", self.LocalToWorldPosition(position, [0, 0, 0]), WHITE, showDistances)
        vTarget: Vertex = Vertex("Z", self.LocalToWorldPosition(position, [3, 0, 0]), WHITE, showDistances)

        # Create all edges
        startToA: Edge = Edge(vStart, vA, 4, color=LIGHT_GRAY)
        startToB: Edge = Edge(vStart, vB, 1, color=LIGHT_GRAY)
        bToA: Edge = Edge(vB, vA, 2, color=LIGHT_GRAY)
        bToC: Edge = Edge(vB, vC, 5, color=LIGHT_GRAY)
        aToC: Edge = Edge(vA, vC, 1, color=LIGHT_GRAY)
        cToTarget: Edge = Edge(vC, vTarget, 3, color=LIGHT_GRAY)

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

class CodeExample(Scene):
    def construct(self):
        code = '''class Dijkstra():
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
    
    def GetTheNearestItem(self, list: list):
        nearestDistance: float = float('inf')
        nearestItem = None

        for item in list:
            if item[1] < nearestDistance:
                nearestDistance = item[1]
                nearestItem = item

        return nearestItem'''

        rendered_code = Code(
            code_string=code,
            tab_width=6,
            language="Python",
            background="window",  # optional: "rectangle", "window", None
        ).scale(0.5)

        self.play(Write(rendered_code))
        self.wait(2)

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
        self.ShowDistance(vertecies[startingVertexIndex])

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
                    self.ShowDistance(vertecies[edgeVertexIndex])
                    
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
                 
            self.MarkVertexAsVisited(vertecies[index])

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

    # (Un)Highlighting vertices and edges
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
            circle.animate.set_stroke(color=WHITE),
            text.animate.set_color(color=WHITE)
        )

        self.play(animation)

    def HighlightEdge(self, edge: Edge):
        arrow: Circle = edge.visual[0]

        self.play(arrow.animate.set_stroke(color=YELLOW).set_fill(color=YELLOW))

    def UnhighlightEdge(self, edge: Edge):
        arrow: Circle = edge.visual[0]

        self.play(arrow.animate.set_stroke(color=LIGHT_GRAY).set_fill(color=LIGHT_GRAY))

    # Markings
    def MarkVertexAsVisited(self, vertex: Vertex):
        circle: Circle = vertex.visual[0]
        text: Text = vertex.visual[1]
        animation: AnimationGroup = AnimationGroup(
            circle.animate.set_stroke(color=GREEN),
            text.animate.set_color(color=GREEN)
        )

        self.play(animation)

    # Distance
    def ShowDistance(self, vertex: Vertex):
        distance: Text = vertex.visual[2]

        self.play(Unwrite(distance))

        vertex.visual.remove(distance)

        newDistanceText = Text(str(vertex.distance), color=RED, font_size=16).move_to(distance.get_center())
        newDistanceText.move_to(vertex.visual[0].get_center() + DOWN * 0.25, aligned_edge=DOWN)
        self.play(ReplacementTransform(distance, newDistanceText))
        vertex.visual.add(newDistanceText)

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
                ).move_to(newPos, aligned_edge=DOWN)
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

        for vertex in graph.vertices:
            distanceText = Text("∞", color=RED, font_size=20).move_to(vertex.visual[0].get_center() + DOWN * 0.25, aligned_edge=DOWN)
            vertex.visual.add(distanceText)
            self.add(distanceText)


        # Add every edge to the animations
        for edge in graph.edges:
            arrow = edge.visual
            animations.append(Write(arrow))

        # Display
        self.play(*animations)

    def GetGraph(self, position) -> Graph:
        # Create all vertices
        vStart: Vertex = Vertex("S", self.LocalToWorldPosition(position, [-3, 0, 0]), color=WHITE)
        vA: Vertex = Vertex("A", self.LocalToWorldPosition(position, [-1.5, 1.5, 0]), color=WHITE)
        vB: Vertex = Vertex("B", self.LocalToWorldPosition(position, [-1.5, -1.5, 0]), color=WHITE)
        vC: Vertex = Vertex("C", self.LocalToWorldPosition(position, [0, 0, 0]), color=WHITE)
        vTarget: Vertex = Vertex("Z", self.LocalToWorldPosition(position, [3, 0, 0]), color=WHITE)

        # Create all edges
        startToA: Edge = Edge(vStart, vA, 4, color=LIGHT_GRAY)
        startToB: Edge = Edge(vStart, vB, 1, color=LIGHT_GRAY)
        bToA: Edge = Edge(vB, vA, 2, color=LIGHT_GRAY)
        bToC: Edge = Edge(vB, vC, 5, color=LIGHT_GRAY)
        aToC: Edge = Edge(vA, vC, 1, color=LIGHT_GRAY)
        cToTarget: Edge = Edge(vC, vTarget, 3, color=LIGHT_GRAY)

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

# -- AI Generated class --
class UMLClassBox(VGroup):
    def __init__(self, class_name, attributes=None, methods=None, **kwargs):
        super().__init__(**kwargs)

        attributes = attributes or []
        methods = methods or []

        # Text sections
        name_text = Text(class_name, weight=BOLD).scale(0.5)
        attr_text = VGroup(*[Text(a).scale(0.4) for a in attributes]).arrange(DOWN, aligned_edge=LEFT)
        meth_text = VGroup(*[Text(m).scale(0.4) for m in methods]).arrange(DOWN, aligned_edge=LEFT)

        # Rectangles
        name_box = SurroundingRectangle(name_text, buff=0.2)
        attr_box = SurroundingRectangle(attr_text, buff=0.2) if attr_text else Rectangle(width=name_box.width, height=0.3)
        meth_box = SurroundingRectangle(meth_text, buff=0.2) if meth_text else Rectangle(width=name_box.width, height=0.3)

        # Align widths
        max_width = max(name_box.width, attr_box.width, meth_box.width)
        for box in [name_box, attr_box, meth_box]:
            box.stretch_to_fit_width(max_width)

        # Stack vertically
        boxes = VGroup(name_box, attr_box, meth_box).arrange(DOWN, buff=0)
        texts = VGroup(name_text, attr_text, meth_text).arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        self.add(boxes, texts)
        self.boxes = boxes
        self.texts = texts

# -- AI Generated class --
class UMLDiagram(Scene):
    def construct(self):
        # Create classes
        base_class = UMLClassBox("Animal", attributes=["+ name: str", "+ age: int"], methods=["+ eat()", "+ sleep()"])
        derived_class = UMLClassBox("Dog", attributes=["+ breed: str"], methods=["+ bark()"])

        # Position them
        base_class.to_edge(UP)
        derived_class.next_to(base_class, DOWN, buff=2)

        # Inheritance arrow
        arrow = Arrow(start=derived_class.get_top(), end=base_class.get_bottom(), buff=0.1)

        # Animate
        self.play(FadeIn(base_class))
        self.play(FadeIn(derived_class))
        self.play(Create(arrow))
        self.wait(2)