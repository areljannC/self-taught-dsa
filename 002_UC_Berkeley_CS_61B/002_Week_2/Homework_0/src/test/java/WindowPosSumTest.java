import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

public class WindowPosSumTest {

    @Test
    public void testWindowPosSumExample1() {
        // Example from the problem statement:
        // Input: a = {1, 2, -3, 4, 5, 4}, n = 3
        // Expected output: {4, 8, -3, 13, 9, 4}
        int[] a = {1, 2, -3, 4, 5, 4};
        int n = 3;
        WindowPosSum.windowPosSum(a, n);
        int[] expected = {4, 8, -3, 13, 9, 4};
        assertArrayEquals("Test Example 1", expected, a);
    }

    @Test
    public void testWindowPosSumExample2() {
        // Second example from the problem statement:
        // Input: a = {1, -1, -1, 10, 5, -1}, n = 2
        // Expected output: {-1, -1, -1, 14, 4, -1}
        int[] a = {1, -1, -1, 10, 5, -1};
        int n = 2;
        WindowPosSum.windowPosSum(a, n);
        int[] expected = {-1, -1, -1, 14, 4, -1};
        assertArrayEquals("Test Example 2", expected, a);
    }

    @Test
    public void testWindowPosSumWithAllNegative() {
        // If all elements are negative, nothing should change.
        int[] a = {-5, -3, -10};
        int n = 2;
        WindowPosSum.windowPosSum(a, n);
        int[] expected = {-5, -3, -10};
        assertArrayEquals("All negatives remain unchanged", expected, a);
    }

    @Test
    public void testWindowPosSumWhenWindowExceedsArray() {
        // Testing when n is larger than the number of remaining elements.
        // For example, with a single positive element.
        int[] a = {7};
        int n = 5;
        WindowPosSum.windowPosSum(a, n);
        int[] expected = {7};
        assertArrayEquals("Single element array", expected, a);
    }
    
    @Test
    public void testWindowPosSumWhenNIsZero() {
        // When n is 0, we sum from a[i] to a[i + 0] (i.e. just a[i]), so the array remains unchanged.
        int[] a = {3, 4, 5};
        int n = 0;
        WindowPosSum.windowPosSum(a, n);
        int[] expected = {3, 4, 5};
        assertArrayEquals("n=0 should leave array unchanged", expected, a);
    }
}

