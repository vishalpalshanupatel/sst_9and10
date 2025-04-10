using System;

class CalculatorWithExceptions
{
    static void Main()
    {
        try
        {
            Console.Write("Enter the first number: ");
            int num1 = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter the second number: ");
            int num2 = Convert.ToInt32(Console.ReadLine());

            int sum = num1 + num2;
            int difference = num1 - num2;
            int product = num1 * num2;
            double quotient = num2 != 0 ? (double)num1 / num2 : 0;

            string sumType = (sum % 2 == 0) ? "even" : "odd";

            Console.WriteLine($"Sum: {sum} ({sumType})");
            Console.WriteLine($"Difference: {difference}");
            Console.WriteLine($"Product: {product}");
            if (num2 != 0)
                Console.WriteLine($"Quotient: {quotient}");
            else
                Console.WriteLine("Cannot divide by zero.");
        }
        catch (FormatException)
        {
            Console.WriteLine("Invalid input. Please enter valid numbers.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
