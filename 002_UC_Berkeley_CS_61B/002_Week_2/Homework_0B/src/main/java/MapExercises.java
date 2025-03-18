import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class MapExercises {
	/** Returns a map from every lower case letter to the number corresponding to that letter, where 'a' is
	 * 1, 'b' is 2, 'c' is 3, ..., 'z' is 26.
	 */
	public static Map<Character, Integer> letterToNum() {
		Map<Character, Integer> letterNumMap = new TreeMap<Character, Integer>();
		for (int i = 0; i < 26; i++) {
			letterNumMap.put((char)('a' + i), i + 1);
		}
		return letterNumMap;
	}

	/** Returns a map from the integers in the list to their squares. For example, if the input list
	 *  is [1, 3, 6, 7], the returned map goes from 1 to 1, 3 to 9, 6 to 36, and 7 to 49.
	 */
	public static Map<Integer, Integer> squares(List<Integer> nums) {
		Map<Integer, Integer> squaredMap = new TreeMap<Integer, Integer>();
		for (Integer i : nums) squaredMap.put(i, i * i);
		return squaredMap;
	}

	/** Returns a map of the counts of all words that appear in a list of words. */
	public static Map<String, Integer> countWords(List<String> words) {
		Map<String, Integer> wordCount = new TreeMap<String, Integer>();
		for (String word : words) {
			if (wordCount.containsKey(word)) {
				wordCount.put(word, wordCount.get(word) + 1);
			} else {
				wordCount.put(word, 1);
			}
		}
		return wordCount;
	}
}
