using System;

class Program
{
    static void Main()
    {
        Console.Write("Ingrese el nombre del estudiante: ");
        string nombre = Console.ReadLine() ?? "Estudiante";

        Console.Write("Ingrese la calificación numérica (0-100): ");
        string? entrada = Console.ReadLine();

        if (int.TryParse(entrada, out int calificacion))
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
        if (calificacion is >= 90 and <= 100)
            return "A";
        if (calificacion is >= 80 and < 90)
            return "B";
        if (calificacion is >= 70 and < 80)
            return "C";
        if (calificacion is >= 60 and < 70)
            return "D";
        if (calificacion is >= 0 and < 60)
            return "F";

        return "Fuera de rango (debe ser entre 0 y 100)";
    }
}