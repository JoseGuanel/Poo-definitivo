import java.util.Scanner;

public class PrecioProducto {
    // Atributos
    private double precioOriginal;  // Precio original del producto
    private double porcentajeDescuento;  // Porcentaje de descuento

    // Constructor
    public PrecioProducto(double precioOriginal, double porcentajeDescuento) {
        this.precioOriginal = precioOriginal;
        this.porcentajeDescuento = porcentajeDescuento;
    }

    // Método para calcular el monto de descuento
    public double calcularDescuento() {
        return (precioOriginal * porcentajeDescuento) / 100;
    }

    // Método para calcular el precio final después del descuento
    public double calcularPrecioFinal() {
        double descuento = calcularDescuento();
        return precioOriginal - descuento;
    }

    // Método para mostrar información sobre el descuento
    public void mostrarInformacion() {
        double descuento = calcularDescuento();
        double precioFinal = calcularPrecioFinal();

        System.out.printf("Monto de descuento: $%.2f\n", descuento);
        System.out.printf("Precio final después del descuento: $%.2f\n", precioFinal);

        // Verificar si el descuento es mayor o menor al 20%
        if (descuento > (precioOriginal * 0.20)) {
            System.out.println("El descuento fue mayor al 20% del precio original.");
        } else {
            System.out.println("El descuento fue menor al 20% del precio original.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pedir al usuario que ingrese el precio original y el porcentaje de descuento
        System.out.print("Ingrese el precio original del producto: $");
        double precioOriginal = scanner.nextDouble();

        System.out.print("Ingrese el porcentaje de descuento: ");
        double porcentajeDescuento = scanner.nextDouble();

        // Crear un objeto PrecioProducto
        PrecioProducto producto = new PrecioProducto(precioOriginal, porcentajeDescuento);

        // Mostrar información sobre el descuento
        producto.mostrarInformacion();

        scanner.close();
    }
}
