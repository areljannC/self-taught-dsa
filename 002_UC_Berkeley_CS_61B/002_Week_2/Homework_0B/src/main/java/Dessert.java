public class Dessert {
	private int flavor;
	private int price;
	public static int numDesserts = 0;

	public Dessert(int flavor, int price) {
		this.flavor = flavor;
		this.price = price;
		this.numDesserts += 1;
	}

	public void printDessert() {
		System.out.printf("%d %d %d", this.flavor, this.price, this.numDesserts);
	}

	public static void main(String[] args) {
		System.out.print("I love dessert!");
	}
}
