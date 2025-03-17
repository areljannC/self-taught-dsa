import static org.junit.Assert.*;
import org.junit.Test;
import java.util.Arrays;
import java.util.List;

public class JavaExercisesTest {

	@Test
	public void testMakeDice() {
		int[] dice = JavaExercises.makeDice();
		assertNotNull("Dice array should not be null", dice);
		assertEquals("Dice array should have length 6", 6, dice.length);
		for (int i = 0; i < 6; i++) {
			assertEquals("Element " + i + " should be " + (i + 1), i + 1, dice[i]);
		}
	}

	@Test
	public void testTakeOrder() {
		// Test for customer "Ergun"
		String[] orderErgun = JavaExercises.takeOrder("Ergun");
		assertNotNull("Order for Ergun should not be null", orderErgun);
		assertEquals("Ergun's order should have 4 items", 4, orderErgun.length);
		String[] expectedErgun = {"beyti", "pizza", "hamburger", "tea"};
		assertArrayEquals("Ergun's order is incorrect", expectedErgun, orderErgun);

		// Test for customer "Erik"
		String[] orderErik = JavaExercises.takeOrder("Erik");
		assertNotNull("Order for Erik should not be null", orderErik);
		assertEquals("Erik's order should have 4 items", 4, orderErik.length);
		String[] expectedErik = {"sushi", "pasta", "avocado", "coffee"};
		assertArrayEquals("Erik's order is incorrect", expectedErik, orderErik);

		// Test for any other customer (e.g., "Noah")
		String[] orderOther = JavaExercises.takeOrder("Noah");
		assertNotNull("Order for other customers should not be null", orderOther);
		assertEquals("Order for other customers should have 3 items", 3, orderOther.length);
		// All elements should be null (default value in a new String[3])
		for (String item : orderOther) {
			assertNull("Each item should be null", item);
		}
	}

	@Test
	public void testFindMinMax() {
		int[] testArray1 = {1, 2, 3, 4, 5, 6};
		// Difference should be 6 - 1 = 5
		assertEquals("findMinMax should return 5", 5, JavaExercises.findMinMax(testArray1));

		int[] testArray2 = {2, 4, 6, 8};
		// Difference should be 8 - 2 = 6
		assertEquals("findMinMax should return 6", 6, JavaExercises.findMinMax(testArray2));
	}

	@Test
	public void testHailstone() {
		// For input 20, the expected hailstone sequence is:
		// 20, 10, 5, 16, 8, 4, 2, 1
		List<Integer> result = JavaExercises.hailstone(20);
		assertNotNull("Hailstone sequence should not be null", result);
		List<Integer> expected = Arrays.asList(20, 10, 5, 16, 8, 4, 2, 1);
		assertEquals("Hailstone sequence does not match expected sequence", expected, result);
	}
}

