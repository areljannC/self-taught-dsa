import static org.junit.Assert.*;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class DessertTest {

	@Test
	public void testDessertMethods() {
		// Capture standard output
		ByteArrayOutputStream outContent = new ByteArrayOutputStream();
		PrintStream originalOut = System.out;
		System.setOut(new PrintStream(outContent));

		// Create first dessert and test printDessert()
		Dessert brownie = new Dessert(1, 2);
		brownie.printDessert();
		assertEquals("Expected output for brownie", "1 2 1", outContent.toString().trim());

		// Reset output capture
		outContent.reset();

		// Create second dessert and test printDessert()
		Dessert iceCream = new Dessert(3, 4);
		iceCream.printDessert();
		assertEquals("Expected output for iceCream", "3 4 2", outContent.toString().trim());

		// Reset output capture
		outContent.reset();

		// Call printDessert() on first dessert again
		brownie.printDessert();
		assertEquals("Expected output for brownie printed second time", "1 2 2", outContent.toString().trim());

		// Reset output capture
		outContent.reset();

		// Test main method
		Dessert.main(new String[]{});
		assertEquals("Expected output from main method", "I love dessert!", outContent.toString().trim());

		// Restore original System.out
		System.setOut(originalOut);
	}
}

