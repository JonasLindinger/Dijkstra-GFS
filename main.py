from manim import *
from vertex import *
from edge import *
from graph import *

class GFS(Scene):
    def construct(self):
        # Run both parts in sequence
        self.Intro()
        self.WhatIs()
        self.Lazy()
        self.LazyOptimizations()
        self.EagerDijkstra()
        self.ShowLimitations()

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
        self.second = Text("2. Lazy Dijkstra").scale(.5).move_to([-6.5, 1.5, 0], aligned_edge=LEFT)
        self.third  = Text("3. Lazy Dijkstra Optimierungen").scale(.5).move_to([-6.5, 1, 0], aligned_edge=LEFT)
        self.fourth = Text("4. Eager Dijkstra").scale(.5).move_to([-6.5, 0.5, 0], aligned_edge=LEFT)
        self.fifth  = Text("5. Limitierungen").scale(.5).move_to([-6.5, 0, 0], aligned_edge=LEFT)

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
        self.wait(2)
        self.play(Write(country), run_time=1)
        self.wait(2)
        self.play(Write(award), run_time=1)

        hidePersonalInfo: AnimationGroup = AnimationGroup(
            FadeOut(img, run_time=1),
            Unwrite(name, run_time=1),
            Unwrite(country, run_time=1),
            Unwrite(award, run_time=1),
        )

        self.wait(2)
        self.play(hidePersonalInfo, run_time=1)
        self.wait(2)
        
        self.demo_graph = self.GetGraphA([0, 0, 0], True)
        self.demo_graph.write(self, True)
        self.wait(2)
        self.demo_graph.highlight_solution(self)

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

        self.demo_graph.resetVisuals(self)
        self.wait(2)
        self.demo_graph.solveWithLazy(self, True)
        self.wait(2)

        self.play(self.demo_graph.group.animate.shift(DOWN * 10))

        self.showLazyV1UML()
        self.showLazyV1JavaCode()
        self.priorityQueue()

        self.wait(2)

        self.play(self.demo_graph.group.animate.shift(UP * 10))

        self.wait(2)
        self.demo_graph.resetVisuals(self)
        self.demo_graph.solveWithLazy(self, True)
        self.wait(2)
        self.demo_graph.highlight_solution(self)
        self.wait(2)

        self.play(self.demo_graph.group.animate.shift(DOWN * 10))

        self.showLazyV1_1UML()
        self.showLazyV1_1JavaCode()
        self.showGetShortestPathJavaCode()

        self.play(self.demo_graph.group.animate.shift(UP * 10))

        self.wait(1)

    def LazyOptimizations(self):
        new_text = Text("Lazy Dijkstra Optimierungen").move_to([-6.5, 3, 0], aligned_edge=LEFT).scale(1.0)
        new_underline = Underline(new_text, buff=0)

        self.play(
            Transform(self.first, new_text),
            Transform(self.underline, new_underline),
            run_time=1,
        )

        self.remove(new_text)        
        self.remove(new_underline)

        self.wait(2)

        self.play(self.demo_graph.group.animate.shift(DOWN * 10), self.first.animate.shift(UP * 3), self.underline.animate.shift(UP * 3))

        self.wait(2)

        self.showLazyV2JavaCode()

        self.wait(2)

        self.play(self.first.animate.shift(DOWN * 3), self.underline.animate.shift(DOWN * 3))
        self.demo_graph_2 = self.GetGraphB([0, 0, 0], True)
        self.demo_graph_2.write(self, True)
        self.demo_graph_2.solveWithLazy(self, True)
        self.demo_graph_2.highlight_solution(self)

        self.play(self.demo_graph_2.group.animate.shift(DOWN * 10), self.first.animate.shift(UP * 3), self.underline.animate.shift(UP * 3))

        self.showLazyV3JavaCode()

        self.demo_graph_2.resetVisuals(self)

        self.play(self.demo_graph_2.group.animate.shift(UP * 10), self.first.animate.shift(DOWN * 3), self.underline.animate.shift(DOWN * 3))

        self.demo_graph_2.solveWithOptimizedLazy(self, True)
        self.play(self.demo_graph_2.group.animate.shift(DOWN * 10))

        self.wait(2)

    def EagerDijkstra(self):
        new_text = Text("Eager Dijkstra").move_to([-6.5, 3, 0], aligned_edge=LEFT).scale(1.0)
        new_underline = Underline(new_text, buff=0)

        self.play(
            Transform(self.first, new_text),
            Transform(self.underline, new_underline),
            run_time=1,
        )

        self.remove(new_text)        
        self.remove(new_underline)

        self.wait(2)

        change = Text("Priority Queue -> Indexed Priority Queue").scale(.5).move_to([-6.5, 2, 0], aligned_edge=LEFT)

        self.play(Write(change))

        self.wait(2)

        self.play(Unwrite(change))

        f1 = lambda x: 1
        f2 = lambda x: x
        f3 = lambda x: np.log2(x)

        axes_small = Axes(
            x_range=[1, 10, 1],
            y_range=[0, 10, 1],
            x_length=12,
            y_length=5,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 0.35)

        labels_small = axes_small.get_axis_labels("Elements", "Operations")

        g1_small = axes_small.plot(f1, color=BLUE)
        g2_small = axes_small.plot(f2, color=YELLOW)
        g3_small = axes_small.plot(f3, color=RED)

        g1_label = Text("O(1)", color=BLUE, font_size=18).move_to([-2, -3.6, 0], aligned_edge=LEFT)
        g2_label = Text("O(n)", color=YELLOW, font_size=18).move_to([0, -3.6, 0], aligned_edge=LEFT)
        g3_label = Text("O(log(n))", color=RED, font_size=18).move_to([2, -3.6, 0], aligned_edge=LEFT)

        labels = VGroup(g1_label, g2_label, g3_label)

        self.play(Write(axes_small), Write(labels_small))
        self.wait(2)
        self.play(Write(g1_small), Write(g1_label))
        self.wait(2)
        self.play(Write(g2_small), Write(g2_label))
        self.wait(2)
        self.play(Write(g3_small), Write(g3_label))

        group_small = VGroup(axes_small, labels_small, g1_small, g2_small, g3_small)

        self.wait(1)

        axes_large = Axes(
            x_range=[1, 1000, 200],
            y_range=[0, 1000, 200],
            x_length=12,
            y_length=5,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 0.35)
        
        labels_large = axes_large.get_axis_labels("Elements", "Operations")

        g1_large = axes_large.plot(f1, color=BLUE)
        g2_large = axes_large.plot(f2, color=YELLOW)
        g3_large = axes_large.plot(f3, color=RED)

        group_large = VGroup(axes_large, labels_large, g1_large, g2_large, g3_large)

        self.play(Transform(group_small, group_large), run_time=3)

        self.wait(2)

        self.play(Unwrite(group_small), Unwrite(labels))

        self.wait(2)

    def ShowLimitations(self):
        new_text = Text("Dijkstra Limitierungen").move_to([-6.5, 3, 0], aligned_edge=LEFT).scale(1.0)
        new_underline = Underline(new_text, buff=0)

        self.play(
            Transform(self.first, new_text),
            Transform(self.underline, new_underline),
            run_time=1,
        )

        self.remove(new_text)        
        self.remove(new_underline)

        self.demo_graph_3 = self.GetGraphC([0, 0, 0], True)
        self.demo_graph_3.write(self, True)
        self.wait(2)
        self.demo_graph_3.solveWithLazy(self, False)
        self.demo_graph_3.highlight_solution(self)

        self.wait(2)

    def priorityQueue(self):
        rect: VGroup = VGroup(Rectangle(height=1, width=1, fill_opacity=0, color=RED), Text("1"))
        r1: VGroup = VGroup(Rectangle(height=1, width=1, fill_opacity=0), Text("1"))
        r2: VGroup = VGroup(Rectangle(height=1, width=1, fill_opacity=0), Text("2"))
        r3: VGroup = VGroup(Rectangle(height=1, width=1, fill_opacity=0), Text("3"))
        r4: VGroup = VGroup(Rectangle(height=1, width=1, fill_opacity=0), Text("4"))
        r5: VGroup = VGroup(Rectangle(height=1, width=1, fill_opacity=0), Text("5"))

        self.play(Write(rect))

        group: VGroup = VGroup(
            r1,
            r2,
            r3,
            r4,
            r5,
        )
        rects: VGroup = VGroup(
            r1[0],
            r2[0],
            r3[0],
            r4[0],
            r5[0],
        )

        group.arrange()
        rects.set_color_by_gradient(RED, ORANGE, YELLOW_C, PURE_GREEN)

        self.play(ReplacementTransform(rect, group))

        self.wait(1)

        self.play(r1.animate.shift(LEFT * 20))
        group.remove(r1)
        rects.remove(r1[0])
        self.play(group.animate.arrange())
        self.play(rects.animate.set_color_by_gradient(RED, ORANGE, YELLOW_C, PURE_GREEN))

        r1.move_to([0, 0, 0])
        r1.shift(RIGHT * 4)
        self.play(Write(r1))
        self.play(group.animate.arrange())

        self.play(
            r2.animate.shift(UP * 1.2),
            r3.animate.shift(UP * 1.2),
            r4.animate.shift(UP * 1.2),
            r5.animate.shift(UP * 1.2),
        )
        self.play(r1.animate.next_to(r2, LEFT + (DOWN * 1.2)))
        
        group.remove(r1)
        group.insert(0, r1)
        rects.remove(r1[0])
        rects.insert(0, r1[0])

        self.play(group.animate.arrange())
        self.play(rects.animate.set_color_by_gradient(RED, ORANGE, YELLOW_C, PURE_GREEN))

        self.wait(1)

        # Show content per entry
        animations: list = []
        for r in group:
            content: Rectangle = Rectangle(height=1, width=1, fill_opacity=1, color=GRAY).next_to(r[0], DOWN)
            r.add(content)
            animations.append(Write(content))

        self.play(*animations)
        self.play(group.animate.arrange())

        # Turn into binary tree
        c1 = VGroup(Circle(0.5), Text("1")).shift(UP * 2)
        c2 = VGroup(Circle(0.5), Text("2")).shift(UP * 0 + LEFT * 1.5)
        c3 = VGroup(Circle(0.5), Text("3")).shift(UP * 0 + RIGHT * 1.5)
        c4 = VGroup(Circle(0.5), Text("4")).shift(DOWN * 2 + LEFT * 2.25)
        c5 = VGroup(Circle(0.5), Text("5")).shift(DOWN * 2 + LEFT * 0.75)

        l1 = self.GetLine(c1[0], c2[0], GRAY)
        l2 = self.GetLine(c1[0], c3[0], GRAY)
        l3 = self.GetLine(c2[0], c4[0], GRAY)
        l4 = self.GetLine(c2[0], c5[0], GRAY)

        circles: VGroup = VGroup(
            c1,
            c2,
            c3,
            c4,
            c5,
            l1,
            l2,
            l3,
            l4,
        )

        self.play(ReplacementTransform(group, circles))

        self.wait(2)

        # extract min
        self.play(c1.animate.shift(UP * 10))

        # rebalance
        self.play(c2[0].animate.set_color(YELLOW))
        self.play(c2[0].animate.set_color(RED))
        self.play(c3[0].animate.set_color(YELLOW))
        self.play(c3[0].animate.set_color(RED))
        self.play(c2.animate.move_to([0, 2, 0]))
        self.play(c4[0].animate.set_color(YELLOW))
        self.play(c4[0].animate.set_color(RED))
        self.play(c5[0].animate.set_color(YELLOW))
        self.play(c5[0].animate.set_color(RED))
        self.play(c4.animate.move_to([-1.5, 0, 0]), FadeOut(l3))

        self.wait(1)

        c1.move_to([2, -2, 0])
        self.play(Write(c1))
        self.play(
            c1.animate.move_to([-2.25, -2, 0]),
            Write(l3),
        )
        self.play(c1[0].animate.set_color(YELLOW))
        self.play(c4[0].animate.set_color(YELLOW))
        self.play(
            c1.animate.move_to(c4.get_center()),
            c4.animate.move_to(c1.get_center()),
        )
        self.play(c4[0].animate.set_color(RED))
        self.play(c2[0].animate.set_color(YELLOW))
        self.play(
            c1[0].animate.set_color(RED),
            c2[0].animate.set_color(RED),
            c1.animate.move_to(c2.get_center()),
            c2.animate.move_to(c1.get_center()),
        )
        self.play(
            c1[0].animate.set_color(RED),
            c2[0].animate.set_color(RED),
        )

        self.play(FadeOut(circles))

        self.wait(1)

    def GetLine(self, c1: Circle, c2: Circle, color) -> Line:
        # direction from c1 → c2
        direction = c2.get_center() - c1.get_center()

        # compute touching points
        start = c1.get_center() + direction / np.linalg.norm(direction) * c1.radius
        end   = c2.get_center() - direction / np.linalg.norm(direction) * c2.radius

        line = Line(start, end, color=color)

        return line

    def showLazyV1UML(self):
        # Partly AI Generated
        # Load the SVG (adjust the path as needed)
        svg = SVGMobject("Lazy Dijkstra v1.svg")
        svg.set_width(12).center().shift(DOWN * 0.5)

        # Just show it — no animation
        self.play(Write(svg))

        self.wait(1)

        self.play(Unwrite(svg))

    def showLazyV1_1UML(self):
        # Partly AI Generated
        # Load the SVG (adjust the path as needed)
        svg = SVGMobject("Lazy Dijkstra v1.svg")
        svg.set_width(12).center().shift(DOWN * 0.5)

        # Just show it — no animation
        self.play(Write(svg))

        self.wait(1)

        # Partly AI Generated
        # Load the SVG (adjust the path as needed)
        new_svg = SVGMobject("Lazy Dijkstra v1.1.svg")
        new_svg.set_width(12).center().shift(DOWN * 0.5)

        # Just show it — no animation
        self.play(FadeOut(svg), FadeIn(new_svg), rate_func=linear)

        self.wait(1)

        self.play(Unwrite(new_svg))

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
        PriorityQueue<VertexEntry> priorityQueue = new PriorityQueue<>(
            (a, b) -> Float.compare(a.value, b.value)
        );

        Vertex startingVertex = vertices[startingVertexIndex];

        startingVertex.distance = 0;
        priorityQueue.add(new VertexEntry(startingVertex, startingVertex.distance));

        while (!priorityQueue.isEmpty()) {
            VertexEntry vertexEntry = priorityQueue.poll();

            vertexEntry.vertex.visited = true;

            for (Edge edge : vertexEntry.vertex.outgoingEdges) {
                Vertex neighbor = edge.to;

                if (neighbor.visited) continue;

                float newDistance = vertexEntry.vertex.distance + edge.weight;

                if (newDistance < neighbor.distance) {
                    neighbor.distance = newDistance;

                    priorityQueue.add(new VertexEntry(neighbor, neighbor.distance));
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
        graph_rendered_code.shift(DOWN * 0.6).shift(RIGHT * 2.5);
    
        self.play(Write(graph_rendered_code), run_time=1)
        self.wait(1)
        self.play(FadeOut(graph_rendered_code), run_time=0.5)
        self.wait(1)

    def showLazyV1_1JavaCode(self):
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
        ).shift(DOWN * 0.5)
        vertex_rendered_code.width = 10
    
        self.play(
            Write(vertex_rendered_code),
            run_time=1
        )
        
        self.wait(1)

        new_vertexCode = '''public class Vertex {
    public float distance = Float.POSITIVE_INFINITY;
    public boolean visited = false;
    public Edge[] outgoingEdges;
    public Vertex previousVertex;

    public Vertex() {
        
    }

    public void SetUp(Edge[] outgoingEdges) {
        this.outgoingEdges = outgoingEdges;
    }
}'''
        new_vertex_rendered_code = Code(
            code_string=new_vertexCode,
            tab_width=10,
            language="Java",
            background="window",  # optional: "rectangle", "window", None
        ).shift(DOWN * 0.5)
        new_vertex_rendered_code.width = 10

        self.play(FadeOut(vertex_rendered_code), FadeIn(new_vertex_rendered_code),  run_time=1, rate_func=linear)

        self.wait(1)
        
        self.play(FadeOut(new_vertex_rendered_code))

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
        PriorityQueue<VertexEntry> priorityQueue = new PriorityQueue<>(
            (a, b) -> Float.compare(a.value, b.value)
        );

        Vertex startingVertex = vertices[startingVertexIndex];

        startingVertex.distance = 0;
        priorityQueue.add(new VertexEntry(startingVertex, startingVertex.distance));

        while (!priorityQueue.isEmpty()) {
            VertexEntry vertexEntry = priorityQueue.poll();

            vertexEntry.vertex.visited = true;

            for (Edge edge : vertexEntry.vertex.outgoingEdges) {
                Vertex neighbor = edge.to;

                if (neighbor.visited) continue;

                float newDistance = vertexEntry.vertex.distance + edge.weight;

                if (newDistance < neighbor.distance) {
                    neighbor.distance = newDistance;


                    priorityQueue.add(new VertexEntry(neighbor, neighbor.distance));
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
        graph_rendered_code.shift(DOWN * 0.6).shift(RIGHT * 2.5);

        self.play(Write(graph_rendered_code))
    
        self.wait(1)

        new_graphCode = '''import java.util.PriorityQueue;

    public class Graph {
        public Vertex[] vertices;
        public Edge[] edges;

        public Graph(Vertex[] vertices, Edge[] edges) {
            this.vertices = vertices;
            this.edges = edges;
        }
        
        public void RunLazyDijkstra(int startingVertexIndex) {
            PriorityQueue<VertexEntry> priorityQueue = new PriorityQueue<>(
                (a, b) -> Float.compare(a.value, b.value)
            );

            Vertex startingVertex = vertices[startingVertexIndex];

            startingVertex.distance = 0;
            priorityQueue.add(new VertexEntry(startingVertex, startingVertex.distance));

            while (!priorityQueue.isEmpty()) {
                VertexEntry vertexEntry = priorityQueue.poll();

                vertexEntry.vertex.visited = true;

                for (Edge edge : vertexEntry.vertex.outgoingEdges) {
                    Vertex neighbor = edge.to;

                    if (neighbor.visited) continue;

                    float newDistance = vertexEntry.vertex.distance + edge.weight;

                    if (newDistance < neighbor.distance) {
                        neighbor.distance = newDistance;
                        neighbor.previousVertex = vertexEntry.vertex;

                        priorityQueue.add(new VertexEntry(neighbor, neighbor.distance));
                    }
                }
            }
        }
    }
    '''
        new_graph_rendered_code = Code(
            code_string=new_graphCode,
            tab_width=10,
            language="Java",
            background="window",  # optional: "rectangle", "window", None
        ).scale(0.5)
        new_graph_rendered_code.width = 9
        new_graph_rendered_code.shift(DOWN * 0.6).shift(RIGHT * 2.5);
    
        self.play(FadeOut(graph_rendered_code), FadeIn(new_graph_rendered_code), run_time=1, rate_fun=linear)

        self.wait(1)

        self.play(FadeOut(new_graph_rendered_code))

    def showGetShortestPathJavaCode(self):
        shortestPathCode = '''public Vertex[] GetShortestPath(int endingVertexIndex) {
        List<Vertex> path = new ArrayList<>();
        
        if (vertices[endingVertexIndex].distance == Float.POSITIVE_INFINITY) {
            System.out.println("Run Dijkstra first!");
            return new Vertex[0];
        }

        Vertex currentVertex = vertices[endingVertexIndex];
        while (currentVertex != null) {
            path.add(currentVertex);
            currentVertex = currentVertex.previousVertex;
        }

        path = path.reversed();

        return path.toArray(new Vertex[0]);
    }
'''
        shortestPath_rendered_code = Code(
            code_string=shortestPathCode,
            tab_width=10,
            language="Java",
            background="window",  # optional: "rectangle", "window", None
        ).scale(0.5)
        shortestPath_rendered_code.width = 9

        self.play(Write(shortestPath_rendered_code))
    
        self.wait(1)

        self.play(FadeOut(shortestPath_rendered_code))

    def showLazyV2JavaCode(self):
        graphCode = '''import java.util.PriorityQueue;

    public class Graph {
        public Vertex[] vertices;
        public Edge[] edges;

        public Graph(Vertex[] vertices, Edge[] edges) {
            this.vertices = vertices;
            this.edges = edges;
        }
        
        public void RunLazyDijkstra(int startingVertexIndex) {
            PriorityQueue<VertexEntry> priorityQueue = new PriorityQueue<>(
                (a, b) -> Float.compare(a.value, b.value)
            );

            Vertex startingVertex = vertices[startingVertexIndex];

            startingVertex.distance = 0;
            priorityQueue.add(new VertexEntry(startingVertex, startingVertex.distance));

            while (!priorityQueue.isEmpty()) {
                VertexEntry vertexEntry = priorityQueue.poll();

                vertexEntry.vertex.visited = true;

                


                for (Edge edge : vertexEntry.vertex.outgoingEdges) {
                    Vertex neighbor = edge.to;

                    if (neighbor.visited) continue;

                    float newDistance = vertexEntry.vertex.distance + edge.weight;

                    if (newDistance < neighbor.distance) {
                        neighbor.distance = newDistance;
                        neighbor.previousVertex = vertexEntry.vertex;

                        priorityQueue.add(new VertexEntry(neighbor, neighbor.distance));
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
        graph_rendered_code.width = 12
        graph_rendered_code.shift(DOWN * 1.9)

        self.play(Write(graph_rendered_code))
    
        self.wait(1)

        new_graphCode = '''import java.util.PriorityQueue;

public class Graph {
    public Vertex[] vertices;
    public Edge[] edges;

    public Graph(Vertex[] vertices, Edge[] edges) {
        this.vertices = vertices;
        this.edges = edges;
    }
    
    public void RunLazyDijkstra(int startingVertexIndex) {
        PriorityQueue<VertexEntry> priorityQueue = new PriorityQueue<>(
            (a, b) -> Float.compare(a.value, b.value)
        );

        Vertex startingVertex = vertices[startingVertexIndex];

        startingVertex.distance = 0;
        priorityQueue.add(new VertexEntry(startingVertex, startingVertex.distance));

        while (!priorityQueue.isEmpty()) {
            VertexEntry vertexEntry = priorityQueue.poll();

            vertexEntry.vertex.visited = true;

            if (vertexEntry.vertex.distance < vertexEntry.value)
                continue;

            for (Edge edge : vertexEntry.vertex.outgoingEdges) {
                Vertex neighbor = edge.to;

                if (neighbor.visited) continue;

                float newDistance = vertexEntry.vertex.distance + edge.weight;

                if (newDistance < neighbor.distance) {
                    neighbor.distance = newDistance;
                    neighbor.previousVertex = vertexEntry.vertex;

                    priorityQueue.add(new VertexEntry(neighbor, neighbor.distance));
                }
            }
        }
    }
}
    '''
        new_graph_rendered_code = Code(
            code_string=new_graphCode,
            tab_width=10,
            language="Java",
            background="window",  # optional: "rectangle", "window", None
        ).scale(0.5)
        new_graph_rendered_code.height = graph_rendered_code.height
        new_graph_rendered_code.shift(DOWN * 1.9)
    
        self.play(FadeOut(graph_rendered_code), FadeIn(new_graph_rendered_code), run_time=1, rate_fun=linear)

        self.wait(2)

        self.play(FadeOut(new_graph_rendered_code))

    def showLazyV3JavaCode(self):
        graphCode = '''import java.util.PriorityQueue;

public class Graph {
    public Vertex[] vertices;
    public Edge[] edges;

    public Graph(Vertex[] vertices, Edge[] edges) {
        this.vertices = vertices;
        this.edges = edges;
    }
    
    public void RunLazyDijkstra(int startingVertexIndex) {
        PriorityQueue<VertexEntry> priorityQueue = new PriorityQueue<>(
            (a, b) -> Float.compare(a.value, b.value)
        );

        Vertex startingVertex = vertices[startingVertexIndex];

        startingVertex.distance = 0;
        priorityQueue.add(new VertexEntry(startingVertex, startingVertex.distance));

        while (!priorityQueue.isEmpty()) {
            VertexEntry vertexEntry = priorityQueue.poll();

            vertexEntry.vertex.visited = true;

            if (vertexEntry.vertex.distance < vertexEntry.value)
                continue;

            for (Edge edge : vertexEntry.vertex.outgoingEdges) {
                Vertex neighbor = edge.to;

                if (neighbor.visited) continue;

                float newDistance = vertexEntry.vertex.distance + edge.weight;

                if (newDistance < neighbor.distance) {
                    neighbor.distance = newDistance;
                    neighbor.previousVertex = vertexEntry.vertex;

                    priorityQueue.add(new VertexEntry(neighbor, neighbor.distance));
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
        graph_rendered_code.width = 12
        graph_rendered_code.shift(DOWN * 2)

        self.play(Write(graph_rendered_code))
        
        self.wait(1)

        new_graphCode = '''import java.util.PriorityQueue;

public class Graph {
    public Vertex[] vertices;
    public Edge[] edges;

    public Graph(Vertex[] vertices, Edge[] edges) {
        this.vertices = vertices;
        this.edges = edges;
    }
    
    public void RunLazyDijkstra(int startingVertexIndex, int endingVertexIndex) {
        PriorityQueue<VertexEntry> priorityQueue = new PriorityQueue<>(
            (a, b) -> Float.compare(a.value, b.value)
        );

        Vertex startingVertex = vertices[startingVertexIndex];
        Vertex endingVertex = vertices[endingVertexIndex];

        startingVertex.distance = 0;
        priorityQueue.add(new VertexEntry(startingVertex, startingVertex.distance));

        while (!priorityQueue.isEmpty()) {
            VertexEntry vertexEntry = priorityQueue.poll();

            vertexEntry.vertex.visited = true;

            if (vertexEntry.vertex.distance < vertexEntry.value)
                continue;

            for (Edge edge : vertexEntry.vertex.outgoingEdges) {
                Vertex neighbor = edge.to;

                if (neighbor.visited) continue;

                float newDistance = vertexEntry.vertex.distance + edge.weight;

                if (newDistance < neighbor.distance) {
                    neighbor.distance = newDistance;
                    neighbor.previousVertex = vertexEntry.vertex;

                    priorityQueue.add(new VertexEntry(neighbor, neighbor.distance));
                }
            }

            if (vertexEntry.vertex == endingVertex) return;
        }
    }
}
    '''
        new_graph_rendered_code = Code(
            code_string=new_graphCode,
            tab_width=10,
            language="Java",
            background="window",  # optional: "rectangle", "window", None
        ).scale(0.5)
        new_graph_rendered_code.height = graph_rendered_code.height
        new_graph_rendered_code.shift(DOWN * 2)
    
        self.play(FadeOut(graph_rendered_code), FadeIn(new_graph_rendered_code), run_time=1, rate_fun=linear)
        self.wait(2)
        self.play(new_graph_rendered_code.animate.shift(UP * 4))

        self.wait(2)

        self.play(FadeOut(new_graph_rendered_code))

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
    
    def GetGraphB(self, position, showDistances: bool) -> Graph:
        # Create all vertices
        vStart: Vertex = Vertex("S", self.LocalToWorldPosition(position, [-4, 0, 0]), WHITE, showDistances)
        vA: Vertex = Vertex("A", self.LocalToWorldPosition(position, [-2, 2, 0]), WHITE, showDistances)
        vB: Vertex = Vertex("B", self.LocalToWorldPosition(position, [-2, -2, 0]), WHITE, showDistances)
        vC: Vertex = Vertex("C", self.LocalToWorldPosition(position, [0, 0, 0]), WHITE, showDistances)
        vD: Vertex = Vertex("D", self.LocalToWorldPosition(position, [-4, -3, 0]), WHITE, showDistances)
        vE: Vertex = Vertex("E", self.LocalToWorldPosition(position, [3, -3, 0]), WHITE, showDistances)
        vTarget: Vertex = Vertex("Z", self.LocalToWorldPosition(position, [3, 0, 0]), WHITE, showDistances)

        # Create all edges
        startToA: Edge = Edge(vStart, vA, 4, color=LIGHT_GRAY)
        startToB: Edge = Edge(vStart, vB, 1, color=LIGHT_GRAY)
        bToA: Edge = Edge(vB, vA, 2, color=LIGHT_GRAY)
        bToC: Edge = Edge(vB, vC, 5, color=LIGHT_GRAY)
        aToC: Edge = Edge(vA, vC, 1, color=LIGHT_GRAY)
        startToD: Edge = Edge(vStart, vD, 100, color=LIGHT_GRAY)
        dToE: Edge = Edge(vD, vE, 1, color=LIGHT_GRAY)
        eToTarget: Edge = Edge(vE, vTarget, 1, color=LIGHT_GRAY)
        cToTarget: Edge = Edge(vC, vTarget, 3, color=LIGHT_GRAY)

        # Create the array
        vertices: list = [vStart, vA, vB, vC, vD, vE, vTarget]
        edges: list = [startToA, startToB, bToA, bToC, aToC, cToTarget, startToD, dToE, eToTarget]

        # Create the graph
        graph: Graph = Graph(vertices, edges)

        return graph
    
    def GetGraphC(self, position, showDistances: bool) -> Graph:
        # Create all vertices
        vStart: Vertex = Vertex("S", self.LocalToWorldPosition(position, [-4, 0, 0]), WHITE, showDistances)
        vA: Vertex = Vertex("A", self.LocalToWorldPosition(position, [-2, 2, 0]), WHITE, showDistances)
        vB: Vertex = Vertex("B", self.LocalToWorldPosition(position, [-2, -2, 0]), WHITE, showDistances)
        vC: Vertex = Vertex("C", self.LocalToWorldPosition(position, [0, 0, 0]), WHITE, showDistances)
        vD: Vertex = Vertex("D", self.LocalToWorldPosition(position, [-4, -3, 0]), WHITE, showDistances)
        vE: Vertex = Vertex("E", self.LocalToWorldPosition(position, [3, -3, 0]), WHITE, showDistances)
        vTarget: Vertex = Vertex("Z", self.LocalToWorldPosition(position, [3, 0, 0]), WHITE, showDistances)

        # Create all edges
        startToA: Edge = Edge(vStart, vA, 4, color=LIGHT_GRAY)
        startToB: Edge = Edge(vStart, vB, 1, color=LIGHT_GRAY)
        bToA: Edge = Edge(vB, vA, 2, color=LIGHT_GRAY)
        bToC: Edge = Edge(vB, vC, 5, color=LIGHT_GRAY)
        aToC: Edge = Edge(vA, vC, 1, color=LIGHT_GRAY)
        startToD: Edge = Edge(vStart, vD, 100, color=LIGHT_GRAY)
        dToE: Edge = Edge(vD, vE, -100, color=LIGHT_GRAY)
        eToTarget: Edge = Edge(vE, vTarget, 1, color=LIGHT_GRAY)
        cToTarget: Edge = Edge(vC, vTarget, 3, color=LIGHT_GRAY)

        # Create the array
        vertices: list = [vStart, vA, vB, vC, vD, vE, vTarget]
        edges: list = [startToA, startToB, bToA, bToC, aToC, cToTarget, startToD, dToE, eToTarget]

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