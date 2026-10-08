using System;

namespace ConsoleApp
{
    class Calculator
    {
        public int number1;
        public int number2;

        public int Add()
        {
            return number1 + number2;
        }

        public static void Main(string[] args)
        {
            Calculator calc = new Calculator();
            calc.number1 = 5;
            calc.number2 = 10;
            int sumResult = calc.Add();
            Console.WriteLine("El resultado de la suma es: " + sumResult);

            NumberDisplay display = new NumberDisplay();
            display.DisplayNumbers();

            UserInput userInput = new UserInput();
            userInput.GreetUser();
        }
    }

    class NumberDisplay
    {
        public void DisplayNumbers()
        {
            Console.WriteLine("Números del 1 al 10:");
            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine(i);
            }
        }
    }

    class UserInput
    {
        public void GreetUser()
        {
            Console.WriteLine("Por favor, introduce tu nombre:");
            string name = Console.ReadLine();
            Console.WriteLine("¡Bienvenido, " + name + "! Qué gusto tenerte por aquí.");
        }
    }
}