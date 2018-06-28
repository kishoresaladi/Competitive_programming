import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Trie {
    static int i;
    // implement a trie and use it to efficiently store string
    private int n;              
    private Node root;   

    private static class Node
    {
        private char c;                        
        private Node left, mid, right;  
        private Integer val;                    
    }
	public boolean contains(String key) 
	{
	   if(key=="")
	    {
	        key="\0";
	    }
        if (key == null) 
        {
            
            throw new IllegalArgumentException("empty");
        }
        return get(key) != null;
    }

	public Integer get(String key) 
	{
	    if(key=="")
	    {
	        key="\0";
	    }
        if (key == null) 
        {
            throw new IllegalArgumentException("calls get() with null argument");
        }
        if (key.length() == 0) throw new IllegalArgumentException("key must have length >= 1");
        Node x = get(root, key, 0);
        if (x == null) return null;
        return x.val;
    }

    private Node get(Node x, String key, int d) {
        if (x == null) return null;
        if (key.length() == 0) throw new IllegalArgumentException("key must have length >= 1");
        char c = key.charAt(d);
        if      (c < x.c)              return get(x.left,  key, d);
        else if (c > x.c)              return get(x.right, key, d);
        else if (d < key.length() - 1) return get(x.mid,   key, d+1);
        else                           return x;
    }
	public void put(String key, Integer val) 
	{
	    if(key=="")
	    {
	        key="\0";
	    }
        if (key == null) {
            throw new IllegalArgumentException("calls put() with null key");
        }
        if (!contains(key)) n++;
        root = put(root, key, val, 0);
    }

    private Node put(Node x, String key, Integer val, int d) {
        char c = key.charAt(d);
        if (x == null) {
            x = new Node();
            x.c = c;
        }
        if      (c < x.c)               x.left  = put(x.left,  key, val, d);
        else if (c > x.c)               x.right = put(x.right, key, val, d);
        else if (d < key.length() - 1)  x.mid   = put(x.mid,   key, val, d+1);
        else                            x.val   = val;
        return x;
    }

   

        public boolean addWord(String word) 
        {
            
         
            
            if(!contains(word))
            {
                System.out.println(word);
                System.out.println(i);
            System.out.println(true);
            put(word,i++);
                return true;
            }
            else
            {
                System.out.println(false);
                return false;
            }
        }
    

   

    @Test
    public void trieTest() {
        final Trie trie = new Trie();

        boolean result = trie.addWord("catch");
        assertTrue(result);

        result = trie.addWord("cakes");
        assertTrue(result);

        result = trie.addWord("cake");
        assertTrue(result);

        result = trie.addWord("cake");
        assertFalse(result);

        result = trie.addWord("caked");
        assertTrue(result);

        result = trie.addWord("catch");
        assertFalse(result);

        result = trie.addWord("");
        assertTrue(result);

        result = trie.addWord("");
        assertFalse(result);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Trie.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}