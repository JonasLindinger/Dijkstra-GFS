package LazyDijkstra_V3;

public class Edge {
    public float weight;
    public Vertex start;
    public Vertex to;

    public Edge(Vertex start, Vertex to, float weight) {
        this.start =  start;
        this.to = to;
        this.weight = weight;
    }
}
