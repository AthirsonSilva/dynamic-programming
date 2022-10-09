import java.util.Stack;

public class Logic {
    public static void main(String[] args) {
        stackQuestion();
    }

    public static void stackQuestion() {
        Stack<Integer> stack = new Stack<Integer>();

        stack.push(78);

        stack.pop();

        stack.push(44);
        stack.push(12);
        stack.push(18);

        stack.pop();

        stack.push(19);

        stack.pop();
        stack.pop();

        stack.push(12);
        stack.push(28);

        System.out.println(stack);
    }

    public static void loopQuestion() {
        int x = 1;

        for (int i = 1; i <= 128; i += i) {
            x += x;
        }

        System.out.print(x + " ");
    }
}

