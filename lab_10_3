using System;

class LoopsAndFunctions
{
    static void Main()
    {
        // For loop to print numbers from 1 to 10
        Console.WriteLine("Printing numbers from 1 to 10:");
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine(i);
        }

        // While loop to ask user input until "exit"
        string input = "";
        while (input.ToLower() != "exit")
        {
            Console.Write("Enter a number or type 'exit' to quit: ");
            input = Console.ReadLine();
            if (input.ToLower() != "exit")
            {
                Console.WriteLine($"You entered: {input}");
            }
        }

        // Function to calculate factorial
        Console.Write("Enter a number to calculate factorial: ");
        int num = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine($"Factorial of {num} is {Factorial(num)}");
    }

    static int Factorial(int n)
    {
        if (n == 0 || n == 1)
            return 1;
        else
            return n * Factorial(n - 1);
    }
}
