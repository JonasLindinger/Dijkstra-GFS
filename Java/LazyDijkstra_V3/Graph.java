package LazyDijkstra_V3;

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
    
    public void RunLazyDijkstra(int startingVertexIndex, int endingVertexIndex) { // Added endingVertexIndex for stopping early
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
                continue; // We have found a better way to this vertex

            // Foreach edge in outgoing edges
            for (Edge edge : vertexEntry.vertex.outgoingEdges) {
                Vertex neighbor = edge.to;

                if (neighbor.visited) continue;

                float newDistance = vertexEntry.vertex.distance + edge.weight;

                // Check if this is a better way
                if (newDistance < neighbor.distance) {
                    neighbor.distance = newDistance;
                    neighbor.previousVertex = vertexEntry.vertex;

                    // Add. This can create duplicates. but is O(log(n)) which is better than O(n).
                    priorityQueue.add(new VertexEntry(neighbor, neighbor.distance));
                }
            }

            if (vertexEntry.vertex == endingVertex) return; // Check if we are at the ending of the vertex
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