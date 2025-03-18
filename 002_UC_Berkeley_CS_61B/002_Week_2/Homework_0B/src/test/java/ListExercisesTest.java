import static org.junit.Assert.*;
import org.junit.Test;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ListExercisesTest {

	@Test
	public void testSum() {
		// Test with a non-empty list
		List<Integer> lst1 = Arrays.asList(1, 2, 3, 4);
		assertEquals("The sum of [1, 2, 3, 4] should be 10", 10, ListExercises.sum(lst1));

		// Test with an empty list
		List<Integer> lst2 = new ArrayList<>();
		assertEquals("The sum of an empty list should be 0", 0, ListExercises.sum(lst2));
	}

	@Test
	public void testEvens() {
		// Test with a list containing both odd and even numbers
		List<Integer> lst = Arrays.asList(1, 2, 3, 4, 5, 6);
		List<Integer> expected = Arrays.asList(2, 4, 6);
		List<Integer> result = ListExercises.evens(lst);
		assertEquals("The even numbers should be [2, 4, 6]", expected, result);
	}

	@Test
	public void testCommon() {
		// Test with two lists that have common elements
		List<Integer> lst1 = Arrays.asList(1, 2, 3, 4, 5, 6);
		List<Integer> lst2 = Arrays.asList(4, 5, 6, 7, 8, 9);
		List<Integer> expected = Arrays.asList(4, 5, 6);
		List<Integer> common1 = ListExercises.common(lst1, lst2);
		assertEquals("The common elements should be [4, 5, 6]", expected, common1);

		// Test with one list empty
		List<Integer> lst3 = new ArrayList<>();
		List<Integer> common2 = ListExercises.common(lst2, lst3);
		assertTrue("The common elements with an empty list should be empty", common2.isEmpty());
	}

	@Test
	public void testCountOccurrencesOfC() {
		// Test with a list of strings
		List<String> lst = Arrays.asList("hello", "world", "welcome");

		// 'o' occurs 3 times across the list: "hell**o**", "w**o**rld", "welc**o**me"
		assertEquals("The character 'o' should occur 3 times", 3, ListExercises.countOccurrencesOfC(lst, 'o'));

		// 'a' does not occur in any string
		assertEquals("The character 'a' should occur 0 times", 0, ListExercises.countOccurrencesOfC(lst, 'a'));

		// 'l' occurs 4 times: "he**ll**o", "worl**d** (only one l here)", "we**l**come"
		assertEquals("The character 'l' should occur 4 times", 4, ListExercises.countOccurrencesOfC(lst, 'l'));
	}
}

