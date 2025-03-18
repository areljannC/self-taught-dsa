import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

public class ListExercises {

	/** Returns the total sum in a list of integers */
	public static int sum(List<Integer> L) {
		int totalSum = 0;
		for (Integer i : L) totalSum += i;
		return totalSum;
	}

	/** Returns a list containing the even numbers of the given list */
	public static List<Integer> evens(List<Integer> L) {
		List<Integer> evenNums = new ArrayList<Integer>();
		for (Integer i : L) if (i % 2 == 0) evenNums.add(i);
		return evenNums;
	}

	/** Returns a list containing the common item of the two given lists */
	public static List<Integer> common(List<Integer> L1, List<Integer> L2) {
		Set<Integer> set = new HashSet<Integer>();
		List<Integer> common = new ArrayList<Integer>();
		for (Integer i : L1) set.add(i);
		for (Integer i : L2) {
			if (set.contains(i)) common.add(i);
		}
		return common;
	}


	/** Returns the number of occurrences of the given character in a list of strings. */
	public static int countOccurrencesOfC(List<String> words, char c) {
		int count = 0;
		for (String word : words) {
			for (int i = 0; i < word.length(); i++) {
				if (word.charAt(i) == c) count += 1;
			}
		}
		return count;
	}
}
