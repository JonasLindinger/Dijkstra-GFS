package LazyDijkstra_V2;

public class Programm {
    public static void main(String[] args) {
        Graph graph = GetGraphA();
        graph.RunLazyDijkstra(0);

        for (Vertex vertex : graph.GetShortestPath(graph.vertices.length - 1)) {
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