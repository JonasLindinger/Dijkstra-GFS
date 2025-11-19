package LazyDijkstra_V1_1;

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
