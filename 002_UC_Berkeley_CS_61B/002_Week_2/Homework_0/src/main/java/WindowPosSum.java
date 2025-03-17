public class WindowPosSum {
	public static void windowPosSum(int[] a, int n) {
		for (int i = 0; i < a.length; i++) {
			if (a[i] < 0) continue;
			int sum = 0;
			for (int j = i; j <= i + n && j < a.length; j++) {
				sum += a[j];
			}
			a[i] = sum;
		}
	}
}
