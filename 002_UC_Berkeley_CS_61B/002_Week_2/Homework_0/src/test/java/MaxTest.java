import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class MaxTest {

    @Test
    public void testMaxSingleElement() {
        int[] arr = {5};
        // Expecting the only element to be the maximum
        assertEquals(5, Max.max(arr));
    }

    @Test
    public void testMaxMultipleElements() {
        int[] arr = {1, 3, 2, 5, 4};
        // Maximum value is M5
        assertEquals(5, Max.max(arr));
    }

    @Test
    public void testMaxWithAllEqualElements() {
        int[] arr = {7, 7, 7, 7};
        // All values are equal, so max should be 7
        assertEquals(7, Max.max(arr));
    }

    @Test
    public void testMaxWithZeroes() {
        int[] arr = {0, 0, 0, 0};
        // All values are zero
        assertEquals(0, Max.max(arr));
    }

    @Test
    public void testMaxLargerArray() {
        int[] arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        // Maximum value is 100
        assertEquals(100, Max.max(arr));
    }
}

