public class PrecioEntradaParque {
    public static void main(String[] args) {
        // Definir la edad directamente
        int edad = 15; // Cambia este valor para probar con diferentes edades

        // Determinar el precio de la entrada según la edad
        int precioEntrada;

        if (edad < 12) {
            precioEntrada = 2000;  // Niños
            System.out.println("Categoría: Niños");
        } else if (edad >= 12 && edad <= 17) {
            precioEntrada = 3500;  // Adolescentes
            System.out.println("Categoría: Adolescentes");
        } else {
            precioEntrada = 5000;  // Adultos
            System.out.println("Categoría: Adultos");
        }

        // Mostrar el precio de la entrada
        System.out.printf("El precio de la entrada es: $%d\n", precioEntrada);
    }
}
