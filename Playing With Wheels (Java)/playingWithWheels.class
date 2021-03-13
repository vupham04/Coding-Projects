import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class PlayingWithWheels {
	
	int start;
	int dest;
	ArrayList<Integer> invalid;
	CS232DirectedAdjacencyListGraph<Integer, Integer> graph;
	
	public PlayingWithWheels() {
		start = -1;
		dest = -1;
		invalid = new ArrayList<Integer>();
		graph = new CS232DirectedAdjacencyListGraph<Integer, Integer>(10000);
	}
	
    public static void main(String[] args) {
        PlayingWithWheels pww = new PlayingWithWheels();
        pww.readInput();
        pww.createGraph();
        pww.solve();
    }
    
    public void readInput() {
    	Scanner scr = new Scanner(System.in);
    	start = scr.nextInt();
    	dest = scr.nextInt();
    	while(scr.hasNextInt()) {
    		invalid.add(scr.nextInt());
    	}
    	scr.close();
    }
    
    public void createGraph() {
    	for(int i=0;i<10000;i++) {
    		int[] neighbors = findNeighbors(i);
    		for(int k=0;k<8;k++) {
    			graph.addEdge(neighbors[k], i, 0);
    			graph.addEdge(i, neighbors[k], 0);
    		}
    	}
    	
    	for(Integer inv: invalid) {
    		int[] invalidNeighbors = findNeighbors(inv);
    		for(int g=0;g<8;g++) {
    			graph.removeEdge(invalidNeighbors[g], inv);
    			graph.removeEdge(inv, invalidNeighbors[g]);
    		}
    	}
    	
    }
    
    private int[] findNeighbors(int num) {
    	int[] neighbors = new int[8];
    	int fourth = num%10;
    	int third = (num/10)%10;
    	int second = (num/100)%10;
    	int first = (num/1000)%10;
    	
    	neighbors[0] = createNumber((first+1)%10, second, third, fourth);
    	neighbors[1] = createNumber((first+10-1)%10, second, third, fourth);
    	neighbors[2] = createNumber(first, (second+1)%10, third, fourth);
    	neighbors[3] = createNumber(first, (second+10-1)%10, third, fourth);
    	neighbors[4] = createNumber(first, second, (third+1)%10, fourth);
    	neighbors[5] = createNumber(first, second, (third+10-1)%10, fourth);
    	neighbors[6] = createNumber(first, second, third, (fourth+1)%10);
    	neighbors[7] = createNumber(first, second, third, (fourth+10-1)%10);
    	return neighbors;
    }
    
    private int createNumber(int first, int second, int third, int fourth) {
    	return first*1000+second*100+third*10+fourth;
    }
    
    public void solve() {
    	if(start==dest) {
    		System.out.println(0);
    		return;
    	} else {
    		for(int i=0;i<10000;i++) {
    			graph.setVertexMark(i, -1);
    		}
    		Queue<Integer> queue = new LinkedList<>();
    		queue.add(start);
    		graph.setVertexMark(start,0);
    		
    		while(!queue.isEmpty()) {
    			int vertex = queue.poll();
    			ArrayList<Integer> neighbors = graph.getNeighbors(vertex);
    			for(int neighbor :neighbors) {
    				if(neighbor == dest) {
    					System.out.println(graph.getVertexMark(vertex)+1);
    					return;
    				} else if(graph.getVertexMark(neighbor)==-1) {
    					graph.setVertexMark(neighbor, graph.getVertexMark(vertex)+1);
    					queue.add(neighbor);
    				}
    			}
    		}
    		System.out.println(-1);
    	}
    }
    
    
}

class CS232DirectedAdjacencyListGraph<V, E> {
	
	/**
	 * Constant for marking vertices as unvisitied.
	 */
	public static final int UNVISITED = 0;

	/**
	 * Constant for marking vertices as visited.
	 */
	public static final int VISITED = 1;
	
	
	protected V[] vertexObjects;
	protected int[] vertexMarks;

	protected int numEdges;
	
	protected LinkedList<Edge<E>>[] edgeLists;

	/**
	 * Construct a new AdjacencyListGraph with the specified number of vertices.
	 * 
	 * @param numVertices
	 *            the number of vertices in the graph.
	 */
	public CS232DirectedAdjacencyListGraph(int numVertices) {
		vertexObjects = (V[]) new Object[numVertices];
		vertexMarks = new int[numVertices];
		numEdges = 0;

		edgeLists = (LinkedList<Edge<E>>[]) new LinkedList<?>[numVertices];
		for (int i = 0; i < edgeLists.length; i++) {
			edgeLists[i] = new LinkedList<Edge<E>>();
		}
	}

	/*
	 * Helper method that gets the Edge object associated with an edge.
	 */
	private Edge<E> getEdgeObject(int v1, int v2) {
		// Use an iterator to search the list of edges for v1
		LinkedList<Edge<E>> list = edgeLists[v1];
		Iterator<Edge<E>> it = list.iterator();
		while (it.hasNext()) {
			Edge<E> edge = it.next();
			if (edge.equals(new Edge<E>(v1, v2, null))) {
				// found it.
				return edge;
			}
		}
		// Edge is not in the graph.
		return null;
	}

	public int getVertexMark(int v) {
		checkVertex(v);
		return vertexMarks[v];
	}

	public void setVertexMark(int v, int mark) {
		checkVertex(v);
		vertexMarks[v] = mark;
	}
	
	public void addEdge(int v1, int v2, E value) {
		checkVertices(v1, v2);

		if (v1 == v2) {
			throw new IllegalArgumentException(
					"Self-edges are not allowed: v1 cannot equal v2.");
		}

		if (value == null) {
			throw new IllegalArgumentException("Edge value cannot be null.");
		}

		Edge<E> edge = getEdgeObject(v1, v2);
		if (edge != null) {
			// edge is already in the graph, just replace its value.
			edge.edgeObject = value;
		} else {
			// edge not in the graph.
			// Add the edge to the list for v1.
			edgeLists[v1].add(new Edge<E>(v1, v2, value));
			numEdges++;
		}
	}

	/**
	 * {@inheritDoc}
	 */
	public E getEdge(int v1, int v2) {
		checkVertices(v1, v2);

		Edge<E> edge = getEdgeObject(v1, v2);
		if (edge != null) {
			// edge is in the graph.
			return edge.edgeObject;
		} else {
			// edge not in the graph.
			return null;
		}
	}

	/**
	 * {@inheritDoc}
	 */
	public E removeEdge(int v1, int v2) {
		checkVertices(v1, v2);

		// Use an iterator to search the list of edges for v1
		LinkedList<Edge<E>> list = edgeLists[v1];
		Iterator<Edge<E>> it = list.iterator();
		while (it.hasNext()) {
			Edge<E> edge = it.next();
			if (edge.equals(new Edge<E>(v1, v2, null))) {
				// found it, so use the iterator to remove it.
				it.remove();
				numEdges--;
				return edge.edgeObject;
			}
		}

		// edge not in the list, so also not in the graph.
		return null;
	}
	
	/**
	 * Helper method to check if a pair of vertices are both valid.
	 * 
	 * @param v1
	 *            one vertex
	 * @param v2
	 *            another vertex
	 * @throws IllegalArgumentException
	 *             if either of the vertices is not valid.
	 */
	protected void checkVertices(int v1, int v2) {
		checkVertex(v1);
		checkVertex(v2);
	}

	
	public ArrayList<Integer> getNeighbors(int v) {
		checkVertex(v);

		ArrayList<Integer> neighbors = new ArrayList<Integer>();

		// Use an iterator to get all of the edges departing v
		LinkedList<Edge<E>> list = edgeLists[v];
		Iterator<Edge<E>> it = list.iterator();
		while (it.hasNext()) {
			neighbors.add(it.next().endVertex);
		}

		return neighbors;
	}
	
	/**
	 * Helper method to check if a vertex is valid.
	 * 
	 * @param v
	 *            the vertex
	 * @throws IllegalArgumentException
	 *             if the specified vertex is not valid.
	 */
	protected void checkVertex(int v) {
		if (v < 0 || v >= numVertices()) {
			throw new IllegalArgumentException("Invalid vertex: " + v);
		}
	}
	
	public int numVertices() {
		return vertexObjects.length;
	}

	
	public int numEdges() {
		return numEdges;
	}

	/**
	 * Get the in degree of vertex v.
	 * 
	 * @param v
	 *            the vertex of which to compute the in degree.
	 * @return the in degree of vertex v.
	 */
	public int inDegree(int v) {
		checkVertex(v);

		int in = 0;
		
		/*
		 * For every vertex, vi, go through the list of edges leaving vi looking
		 * for an edge going to vertex v...
		 */
		for (int vi = 0; vi < numVertices(); vi++) {
			LinkedList<Edge<E>> edgesLeavingVi = edgeLists[vi];
			Iterator<Edge<E>> it = edgesLeavingVi.iterator();
			boolean foundEdgeToV = false;
			while (it.hasNext() && !foundEdgeToV) {
				if (it.next().endVertex == v) {
					in++;
					/*
					 * Can only have a single edge from vi to v so once we find
					 * one, there is no need to go though the rest of the edges
					 * leaving vi.
					 */
					foundEdgeToV = true;
				}
			}
		}

		return in;
	}

	/**
	 * Class used to hold the information about each edge in the graph.
	 */
	protected static class Edge<E> {
		public E edgeObject;
		public int startVertex; // not strictly necessary, but seems nice.
		public int endVertex;

		public Edge(int sv, int ev, E obj) {
			edgeObject = obj;
			startVertex = sv;
			endVertex = ev;
		}

		/*
		 * Check if two edges are equal in a directed graph.
		 */
		public boolean equals(Edge<E> e) {
			return (startVertex == e.startVertex && endVertex == e.endVertex);
		}
	}
}