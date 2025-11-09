from manim import *
from vertex import *
from edge import *
from graph import *
from dijkstra import *

class GFS(Scene):
    def construct(self):
        # Run both parts in sequence
        self.Intro()
        self.WhatIs()
        self.Lazy()

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

        self.play(
            Unwrite(self.title),
            Unwrite(self.second),
            Unwrite(self.third),
            Unwrite(self.fourth),
            Unwrite(self.fifth),
            Transform(self.first, new_text),            
            Transform(self.underline, new_underline),
            run_time=1
        )

        self.remove(new_text)
        self.remove(new_underline)

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
        
        self.demo_graph = self.GetGraphA([0, 0, 0], True)
        self.demo_graph.write(self, True)
        self.wait(1)
        self.demo_graph.highlight_solution(self)

        self.play(self.demo_graph.group.animate.shift(DOWN * 10))

    def Lazy(self):
        new_text = Text("Lazy Dijkstra").move_to([-6.5, 3, 0], aligned_edge=LEFT).scale(1.0)
        new_underline = Underline(new_text, buff=0)

        self.play(
            Transform(self.first, new_text),
            Transform(self.underline, new_underline),
            run_time=1,
        )

        self.remove(new_text)        
        self.remove(new_underline)

        self.showLazyV1UML()
        self.showLazyV1JavaCode();

        self.play(self.demo_graph.group.animate.shift(UP * 10))

        self.demo_graph.resetVisuals(self)

        self.demo_graph.solve(self, True)
        self.demo_graph.highlight_solution(self)

        self.play(self.demo_graph.group.animate.shift(DOWN * 10))

        self.wait(1)

        self.showLazyV1_1UML()

        self.wait(1)

    def showLazyV1UML(self):
        # Partly AI Generated
        # Load the SVG (adjust the path as needed)
        svg = SVGMobject("Lazy Dijkstra v1.svg")
        svg.set_width(12).center().shift(DOWN * 0.1)

        # Just show it — no animation
        self.play(Write(svg))

        self.wait(1)

        self.play(Unwrite(svg))

    def showLazyV1_1UML(self):
        # Partly AI Generated
        # Load the SVG (adjust the path as needed)
        svg = SVGMobject("Lazy Dijkstra v1.1.svg")
        svg.set_width(12).center().shift(DOWN * 0.1)

        # Just show it — no animation
        self.play(Write(svg))

        self.wait(1)

        self.play(Unwrite(svg))

    def showLazyV1JavaCode(self):
        vertexCode = '''public class Vertex {
    public float distance = Float.POSITIVE_INFINITY;
    public boolean visited = false;
    public Edge[] outgoingEdges;

    public Vertex() {
        
    }

    public void SetUp(Edge[] outgoingEdges) {
        this.outgoingEdges = outgoingEdges;
    }
}'''
        vertex_rendered_code = Code(
            code_string=vertexCode,
            tab_width=10,
            language="Java",
            background="window",  # optional: "rectangle", "window", None
        ).shift(LEFT * 3.5)
        vertex_rendered_code.height = 3

        edgeCode = '''public class Edge {
    public float weight;
    public Vertex start;
    public Vertex to;

    public Edge(Vertex start, Vertex to, float weight) {
        this.start =  start;
        this.to = to;
        this.weight = weight;
    }
}
'''
        edge_rendered_code = Code(
            code_string=edgeCode,
            tab_width=10,
            language="Java",
            background="window",  # optional: "rectangle", "window", None
        ).shift(RIGHT * 3.5)
        edge_rendered_code.height = 3

        self.play(
            Write(vertex_rendered_code),            
            Write(edge_rendered_code),
            run_time=1
        )
        self.wait(2)
        self.play(
            FadeOut(vertex_rendered_code),            
            FadeOut(edge_rendered_code),
            run_time=0.5
        )

        programmCode = '''public class Programm {
    public static void main(String[] args) {
        Graph graph = GetGraphA();
        graph.RunLazyDijkstra(0);

        for (Vertex vertex : graph.vertices) {
            System.out.println(vertex.distance);
        }
    }    

    private static Graph GetGraphA() {
        Vertex start = new Vertex();
        Vertex a = new Vertex();
        Vertex b = new Vertex();
        Vertex c = new Vertex();
        Vertex target = new Vertex();

        Edge SA = new Edge(start, a, 4);        
        Edge SB = new Edge(start, b, 1);
        Edge BA = new Edge(b, a, 2);
        Edge BC = new Edge(b, c, 5);
        Edge AC = new Edge(a, c, 1);
        Edge CT = new Edge(c, target, 3);

        start.SetUp(new Edge[] { SA, SB });        
        a.SetUp(new Edge[] { AC });
        b.SetUp(new Edge[] { BA, BC });
        c.SetUp(new Edge[] { CT });
        target.SetUp(new Edge[] { });

        Vertex[] vertices = new Vertex[] {
            start,
            a, 
            b, 
            c, 
            target
        };

        Edge[] edges = new Edge[] {
            SA,
            SB,
            BA,
            BC,
            AC,
            CT
        };

        Graph graph = new Graph(vertices, edges);

        return graph;
    }
}
'''
        programm_rendered_code = Code(
            code_string=programmCode,
            tab_width=10,
            language="Java",
            background="window",  # optional: "rectangle", "window", None
        ).scale(0.5)
        programm_rendered_code.width = 8
        programm_rendered_code.shift(DOWN * 5).shift(RIGHT * 2);

        self.play(Write(programm_rendered_code), run_time=1)
        self.wait(1)
        self.play(programm_rendered_code.animate.shift(UP * 8.25), run_time=2)
        self.wait(1)
        self.play(FadeOut(programm_rendered_code), run_time=0.5)
        self.wait(1)

        graphCode = '''import java.util.PriorityQueue;

public class Graph {
    public Vertex[] vertices;
    public Edge[] edges;

    public Graph(Vertex[] vertices, Edge[] edges) {
        this.vertices = vertices;
        this.edges = edges;
    }
    
    public void RunLazyDijkstra(int startingVertexIndex) {
        PriorityQueue<Vertex> priorityQueue = new PriorityQueue<>(
            (a, b) -> Float.compare(a.distance, b.distance)
        );

        Vertex startingVertex = vertices[startingVertexIndex];

        startingVertex.distance = 0;
        priorityQueue.add(startingVertex);

        while (!priorityQueue.isEmpty()) {
            Vertex vertex = priorityQueue.poll();

            vertex.visited = true;

            for (Edge edge : vertex.outgoingEdges) {
                Vertex neighbor = edge.to;

                if (neighbor.visited) continue;

                float newDistance = vertex.distance + edge.weight;

                if (newDistance < neighbor.distance) {
                    neighbor.distance = newDistance;

                    priorityQueue.remove(neighbor);

                    priorityQueue.add(neighbor);
                }
            }
        }
    }
}
'''
        graph_rendered_code = Code(
            code_string=graphCode,
            tab_width=10,
            language="Java",
            background="window",  # optional: "rectangle", "window", None
        ).scale(0.5)
        graph_rendered_code.width = 9
        graph_rendered_code.shift(DOWN * 2.5).shift(RIGHT * 2.5);
    
        self.play(Write(graph_rendered_code), run_time=1)
        self.wait(1)
        self.play(graph_rendered_code.animate.shift(UP * 2.75), run_time=2)
        self.wait(1)
        self.play(FadeOut(graph_rendered_code), run_time=0.5)
        self.wait(1)

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