import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public boolean contains(int[] a, int n) {

      int lo=0;
		int high=a.length-1;
		
		boolean k=function(a,lo,high,n);
		return k;     
        

        
    } 
    public boolean function(int[] a,int lo,int high,int n)
    {
    	
    	if(high<=lo)
    	{
    		return n==a[high];
    	}
    	int mid=(lo+high)/2;
    	if(a[mid]>n)
    	{
    		high=mid-1;
    		return function(a,lo,high,n);
    	}
    	else if(a[mid]<n)
    	{
    		lo=mid+1;
    		
    		return function(a,lo,high,n);
    	}
    	return true;
    }

















    // tests

    // @Test
    // public void emptyArrayTest() {
    //     final boolean result = contains(new int[] {}, 1);
    //     assertFalse(result);
    // }

    @Test
    public void oneItemArrayNumberPresentTest() {
        final boolean result = contains(new int[] {1}, 1);
        assertTrue(result);
    }

    @Test
    public void oneItemArrayNumberAbsentTest() {
        final boolean result = contains(new int[] {1}, 2);
        assertFalse(result);
    }

    @Test
    public void smallArrayNumberPresentTest() {
        final boolean result = contains(new int[] {2, 4, 6}, 4);
        assertTrue(result);
    }

    @Test
    public void smallArrayNumberAbsentTest() {
        final boolean result = contains(new int[] {2, 4, 6}, 5);
        assertFalse(result);
    }

    @Test
    public void largeArrayNumberPresentTest() {
        final boolean result = contains(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 8);
        assertTrue(result);
    }

    @Test
    public void largeArrayNumberAbsentTest() {
        final boolean result = contains(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 0);
        assertFalse(result);
    }

    @Test
    public void largeArrayNumberFirstTest() {
        final boolean result = contains(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 1);
        assertTrue(result);
    }

    @Test
    public void largeArrayNumberLastTest() {
        final boolean result = contains(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 10);
        assertTrue(result);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}