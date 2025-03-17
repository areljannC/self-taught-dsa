public class Max {
	public static int max(int[] m) {
		int maxInt = -1;

		for (int i = 0; i < m.length; i++) {
			if (m[i] > maxInt) {
				maxInt = m[i];
			}
		}

		return maxInt;
	}
}
