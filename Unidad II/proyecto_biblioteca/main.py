from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.gestorPrestamos import GestorPrestamos
from modelos.biblioteca import Biblioteca
from modelos.bibliotecario import Bibliotecario
from modelos.alumno import Alumno

#Crear biblioteca
biblioteca = Biblioteca("Biblioteca Central")

#Crear biblotecario
bibliotecario1 = Bibliotecario("Carlos", "B001", "IA")

#Crear libros
libro1 = Libro("Pepa Pig", "Bucanero", "12345")
libro2 = Libro("Teoría de Evolución del Ser Humano", "Jorge el curioso", "12345")

#Bibliotecario registra libros
bibliotecario1.registrar_libro(biblioteca, libro1)
bibliotecario1.registrar_libro(biblioteca, libro2)

#Libros disponibles
biblioteca.listar_libros()

#Crear usuario
alumno =Alumno("Ana", "A001", "Alumno")

#Crear gestor de prestamos
gestor = GestorPrestamos()

#Realizar prestamo
gestor.realizar_prestamo(libro1, alumno, "18-04-2026")

#Imprimir prestamos
gestor.listar_prestamos()

print(bibliotecario1.descripcion())
print(alumno.descripcion())


#usuario1 = Usuario("Valeria", "2521578", "Estudiante")

