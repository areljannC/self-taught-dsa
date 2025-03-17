import org.junit.Test;
import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class DrawTriangleTest {
	@Test
    public void testDrawTriangleWith5Rows() {
        // Capture the standard output
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));

        // Run the method under test
        DrawTriangle.drawTriangle(5);

        // Restore original System.out
        System.setOut(originalOut);

        // Construct the expected output (each line printed with a newline at the end)
        String expectedOutput = 
                  "    *    \n"   // 4 spaces, *, 4 spaces
                + "   ***   \n"   // 3 spaces, ***, 3 spaces
                + "  *****  \n"   // 2 spaces, *****, 2 spaces
                + " ******* \n"    // 1 space, 7 stars, 1 space
                + "*********\n";   // 9 stars

        assertEquals(expectedOutput, outContent.toString());
    }
}
