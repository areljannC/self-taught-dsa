public class DrawTriangle {
	public static void drawTriangle(int n) {
		int maxChar = n + (n - 1);
		char[] line = new char[maxChar];
		for (int i = 0; i < maxChar; i++) {
			line[i] = ' ';
		}

		int lp, rp;
		lp = rp = maxChar / 2;
		for (int i = 0; i < n; i++) {
			line[lp - i] = '*';
			line[rp + i] = '*';
			System.out.println(new String(line));
		}
	}
}
