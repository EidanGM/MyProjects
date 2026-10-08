using System;
using System.Collections.Generic;

class Program
{
    // Estructura básica para representar un libro
    class Libro
    {
        public string Titulo { get; set; }
        public bool EstaRetirado { get; set; }

        public Libro(string titulo)
        {
            Titulo = titulo;
            EstaRetirado = false;
        }
    }

    // Listas y variables para el sistema
    static List<Libro> coleccion = new List<Libro>
    {
        new Libro("Cien años de soledad"),
        new Libro("Don Quijote de la Mancha"),
        new Libro("El principito")
    };

    static int librosPrestadosUsuario = 0; // O contador de libros prestados al usuario
    static int limitePrestamo = 3;

    static void Main(string[] args)
    {
        // Ejemplo de uso de las funciones solicitadas:
        
        // 1. Probar función de búsqueda
        BuscarLibro();

        // 2. Probar función de marcar como retirado / devolver
        CambiarEstadoRetiro();

        // 3. Probar función de límite de préstamo
        TomarPrestadoLibro();
    }

    // (5pts) Función de búsqueda
    static void BuscarLibro()
    {
        Console.WriteLine("\n--- FUNCION DE BUSQUEDA ---");
        Console.Write("Ingrese el titulo del libro que desea buscar: ");
        string tituloBuscado = Console.ReadLine();

        Libro libroEncontrado = coleccion.Find(l => l.Titulo.Equals(tituloBuscado, StringComparison.OrdinalIgnoreCase));

        if (libroEncontrado != null)
        {
            if (!libroEncontrado.EstaRetirado)
            {
                Console.WriteLine($"El libro '{libroEncontrado.Titulo}' esta en la coleccion y esta disponible.");
            }
            else
            {
                Console.WriteLine($"El libro '{libroEncontrado.Titulo}' esta en la coleccion, pero actualmente se encuentra retirado.");
            }
        }
        else
        {
            Console.WriteLine("El libro no esta en la coleccion.");
        }
    }

    // (5pts) Función de límite de préstamo
    static void TomarPrestadoLibro()
    {
        Console.WriteLine("\n--- FUNCION DE LIMITE DE PRESTAMO ---");
        Console.WriteLine($"Libros actualmente prestados: {librosPrestadosUsuario} / {limitePrestamo}");

        if (librosPrestadosUsuario < limitePrestamo)
        {
            librosPrestadosUsuario++;
            Console.WriteLine("¡Libro tomado prestado con exito!");
            Console.WriteLine($"Ahora tienes {librosPrestadosUsuario} libro(s) prestado(s).");
        }
        else
        {
            Console.WriteLine("No se puede tomar prestado el libro. Has alcanzado el límite de 3 libros prestados.");
        }
    }

    // (5pts) Función que marca un libro como sacado o lo devuelve
    static void CambiarEstadoRetiro()
    {
        Console.WriteLine("\n--- FUNCION DE MARCAR/DEVOLVER LIBRO ---");
        Console.Write("Ingrese el titulo del libro para cambiar su estado (retirar/devolver): ");
        string titulo = Console.ReadLine();

        Libro libro = coleccion.Find(l => l.Titulo.Equals(titulo, StringComparison.OrdinalIgnoreCase));

        if (libro != null)
        {
            if (!libro.EstaRetirado)
            {
                libro.EstaRetirado = true;
                Console.WriteLine($"El libro '{libro.Titulo}' ha sido marcado como retirado.");
            }
            else
            {
                libro.EstaRetirado = false;
                Console.WriteLine($"Se ha eliminado la bandera de retirado. El libro '{libro.Titulo}' ha sido devuelto con exito.");
            }
        }
        else
        {
            Console.WriteLine("No se encontro un libro con ese titulo en la coleccion.");
        }
    }
}