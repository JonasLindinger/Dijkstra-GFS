package LazyDijkstra_V1;

public class VertexEntry {
    public Vertex vertex;
    public float value;

    public VertexEntry(Vertex vertex, float value) {
        this.vertex = vertex;
        this.value = value;
    }
}