public class HelloWorld {
    public static void main(String[] args) {
        divider();
        
        pl("Hello, world!");

        
        divider();

        pl("Variable Declaration");

        boolean isTrue = true;
        boolean isFalse = false;
        int doubleDigit = 11;
        double tripleDigit = 22.22;
        String string = "This is a string!";
        char character = 'x';

        divider();

        // This is a commented line.
        pl("This is not a commented line.");
        // This is another commented line.

        divider();

        pl("while loop");
        int i = 0;
        while (i < 5) {
            pl("loop " + i);
            i++;
        }

        divider();

        pl("for loop");
        for (int j = 0; j < 5; j++) {
            pl("loop" + j);
        }

        divider();
    }

    private static void p(String string) {
        System.out.print(string);
    }

    private static void pl(String string) {
        System.out.println(string);
    }

    private static void divider() {
        pl("");
        pl("-------------------------------------------"); 
        pl("");
    }
}
