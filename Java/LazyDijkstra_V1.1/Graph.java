import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

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

            // Foreach edge in outgoing edges
            for (Edge edge : vertex.outgoingEdges) {
                Vertex neighbor = edge.to;

                if (neighbor.visited) continue;

                float newDistance = vertex.distance + edge.weight;

                // Check if this is a better way
                if (newDistance < neighbor.distance) {
                    neighbor.distance = newDistance;
                    neighbor.previousVertex = vertex;

                    // If the vertex is already in the queue, remove it
                    priorityQueue.remove(neighbor); // This is O(n)...!

                    // Add
                    priorityQueue.add(neighbor);
                }
            }
        }
    }

    public Vertex[] GetShortestPath(int endingVertexIndex) {
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

        path = path.reversed(); // O(1) : )

        return path.toArray(new Vertex[0]);
    }
}