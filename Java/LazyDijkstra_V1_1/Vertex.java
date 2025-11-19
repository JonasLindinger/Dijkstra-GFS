package LazyDijkstra_V1_1;

public class Vertex {
    public float distance = Float.POSITIVE_INFINITY;
    public boolean visited = false;
    public Edge[] outgoingEdges;
    public Vertex previousVertex;

    public Vertex() {
        
    }

    public void SetUp(Edge[] outgoingEdges) {
        this.outgoingEdges = outgoingEdges;
    }
}