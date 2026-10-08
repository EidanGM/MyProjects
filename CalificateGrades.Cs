using System;

class Program
{
    static void Main()
    {
        Console.Write("Ingrese el nombre del estudiante: ");
        string nombre = Console.ReadLine();

        Console.Write("Ingrese la calificación numérica (0-100): ");
        if (int.TryParse(Console.ReadLine(), out int calificacion))
        {
            string letra = ClasificarCalificacion(calificacion);
            Console.WriteLine($"\nResultado: El/La estudiante {nombre} obtuvo una calificación de {letra}.");
        }
        else
        {
            Console.WriteLine("Entrada no válida. Por favor, ingrese un número entero.");
        }
    }
    
    static string ClasificarCalificacion(int calificacion)
    {
        switch (calificacion)
        {
            case >= 90 and <= 100:
                return "A";
            case >= 80 and < 90:
                return "B";
            case >= 70 and < 80:
                return "C";
            case >= 60 and < 70:
                return "D";
            case < 60 and >= 0:
                return "F";
            default:
                return "Fuera de rango (debe ser entre 0 y 100)";
        }
    }
}