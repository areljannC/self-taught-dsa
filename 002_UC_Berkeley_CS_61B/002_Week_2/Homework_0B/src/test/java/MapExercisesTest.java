import static org.junit.Assert.*;
import org.junit.Test;
import java.util.*;

public class MapExercisesTest {

	@Test
	public void testLetterToNum() {
		Map<Character, Integer> map = MapExercises.letterToNum();
		assertNotNull("Map should not be null", map);
		assertEquals("Map should contain 26 entries", 26, map.size());
		for (int i = 0; i < 26; i++) {
			char letter = (char) ('a' + i);
			assertTrue("Map should contain key: " + letter, map.containsKey(letter));
			assertEquals("Value for '" + letter + "' should be " + (i + 1), 
					Integer.valueOf(i + 1), map.get(letter));
		}
	}

	@Test
	public void testSquares() {
		List<Integer> lst = Arrays.asList(1, 3, 6, 7);
		Map<Integer, Integer> map = MapExercises.squares(lst);
		assertNotNull("Returned map should not be null", map);
		assertEquals("Map should have 4 entries", 4, map.size());
		assertEquals("Square of 1 should be 1", Integer.valueOf(1), map.get(1));
		assertEquals("Square of 3 should be 9", Integer.valueOf(9), map.get(3));
		assertEquals("Square of 6 should be 36", Integer.valueOf(36), map.get(6));
		assertEquals("Square of 7 should be 49", Integer.valueOf(49), map.get(7));
	}

	@Test
	public void testCountWords() {
		List<String> lst = Arrays.asList(
				"hug", "hug", "hug", "hug",
				"shreyas", "shreyas", "shreyas",
				"ergun", "ergun",
				"cs61b"
				);
		Map<String, Integer> map = MapExercises.countWords(lst);
		assertNotNull("Returned map should not be null", map);
		// Verify counts for each expected word.
		assertEquals("Count for 'hug' should be 4", Integer.valueOf(4), map.get("hug"));
		assertEquals("Count for 'shreyas' should be 3", Integer.valueOf(3), map.get("shreyas"));
		assertEquals("Count for 'ergun' should be 2", Integer.valueOf(2), map.get("ergun"));
		assertEquals("Count for 'cs61b' should be 1", Integer.valueOf(1), map.get("cs61b"));
		// Also, the map should contain exactly 4 keys.
		assertEquals("Map should have 4 keys", 4, map.size());
	}
}

