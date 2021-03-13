import java.io.*;
import java.util.*;

public class Huffman {
    
    private ArrayList<String> input;
    private String[] huffmanCode;
    private int[] frequency;
    private static String command = "";
    private Node tree;
    
    
    public Huffman() {
        input = new ArrayList<String>();
        frequency = new int[126];
        tree = null;
        huffmanCode = new String[126];
    }
    
    public void frequency() {
        frequency[9] = input.size()-1;
        for(String s: input) {
            char[] stringArray = s.toCharArray();
            for(char ch: stringArray) {
                int num = ch;
                frequency[num-1]++;
            }
        }
    }
    
    public void printFrequency() {
        for(int i=0;i<126;i++) {
            if(frequency[i]==0) {
                continue;
            } else if(i==9) {
                System.out.println ("\\n:"+frequency[i]);
            } else if(i==8) {
                System.out.println("\\t:"+frequency[i]);
            } else {
                char ch = (char) (i+1);
                System.out.println(ch+":"+ frequency[i]);
            }
        }
    }
    
    public void buildTree() {
        PriorityQueue<Node> tempQueue = new PriorityQueue<>();
        for(int i=0;i<126;i++) {
            if(frequency[i]==0) {
                continue;
            }
            Node tempNode = new Node((char)(i+1), frequency[i]);
            tempQueue.add(tempNode);
        }
        while(tempQueue.size()>1) {
            Node nodeOne = tempQueue.poll();
            Node nodeTwo = tempQueue.poll();
            char smallerValue = (char) Math.min(nodeOne.value, nodeTwo.value);
            Node mergeNode = new Node(smallerValue, nodeOne.key+nodeTwo.key);
            mergeNode.right = nodeOne;
            mergeNode.left = nodeTwo;
            tempQueue.add(mergeNode);
        }
        tree = tempQueue.poll();
    }
    
    public void printTreeLevelOrder() {
        Queue<Node> queue = new LinkedList<Node>(); 
        queue.add(tree); 
        while (!queue.isEmpty())  { 
            Node tempNode = queue.poll(); 
            if(tempNode.value=='\n') {
                System.out.println("\\n:"+tempNode.key);
            } else if(tempNode.value=='\t') {
                System.out.println("\\t:" + tempNode.key);
            } else {
                System.out.println(tempNode.value + ":" + tempNode.key); 
            }
            if (tempNode.left != null) { 
                queue.add(tempNode.left); 
            } 
            if (tempNode.right != null) { 
                queue.add(tempNode.right); 
            } 
        } 
    }
    
    public void computeHuffman() {
        computeHuffmanRoot(tree, "");
    }
    
    public void computeHuffmanRoot(Node tree, String s) {
        if(tree.left==null && tree.right ==null) {
            huffmanCode[tree.value-1] = s;
        } else {
            computeHuffmanRoot(tree.left, s+"0");
            computeHuffmanRoot(tree.right, s+"1");
        }
    }
    
    public void printHuffmanTable() {
        for(int i=0;i<126;i++) {
            if(huffmanCode[i]==null) {
                continue;
            } else if(i==9) {
                System.out.println ("\\n:"+huffmanCode[i]);
            } else if(i==8) {
                System.out.println("\\t:"+huffmanCode[i]);
            } else {
                char ch = (char) (i+1);
                System.out.println(ch+":"+ huffmanCode[i]);
            }
        }
    }
    
    public void printHuffmanCodedText() {
        for(int k=0;k<input.size();k++) {
            String s = input.get(k);
            char[] stringArray = s.toCharArray();
            for(char ch: stringArray) {
                System.out.print(huffmanCode[ch-1]);
            }
            if(k!=(input.size()-1)) {
                System.out.print(huffmanCode[9]);
            }
        }
    }
    
    public void readInput() {
        Scanner scr = new Scanner(System.in);
        command = scr.nextLine();
        while(scr.hasNextLine()) {
            input.add(scr.nextLine());
        }
        scr.close();
        
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Huffman h = new Huffman();
        h.readInput();
        h.frequency();
        if(command.equals("F")) {
            h.printFrequency();
        } else {
            h.buildTree();
            if(command.equals("T")) {
                h.printTreeLevelOrder();
            } else {
                h.computeHuffman();
                if(command.equals("H")) {
                    h.printHuffmanTable();
                }
                if(command.equals("M")){
                    h.printHuffmanCodedText();
                }
            }
        }
    }
    
    public static class Node implements Comparable<Node> {
        char value;
        int key;
        Node left;
        Node right;
        
        public Node(char character, int frequency) {
            value = character;
            key = frequency;
            left = null;
            right = null;
        }

        @Override
        public int compareTo(Node arg0) {
            if(this.key>arg0.key) {
                return 1;
            } else if(this.key<arg0.key) {
                return -1;
            } else {
                if(this.value>arg0.value) {
                    return 1;
                } else if(this.value<arg0.value) {
                    return -1;
                }
            }
            return 0;
        } 
        
    }

}