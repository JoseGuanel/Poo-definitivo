import java.util.Scanner;

public class ConversorMoneda {
    public static void main(String[] args) {
        // Crear un objeto Scanner para la entrada de datos
        Scanner scanner = new Scanner(System.in);
        
        // Solicitar al usuario ingresar la cantidad en pesos chilenos
        System.out.print("Ingrese la cantidad en pesos chilenos: ");
        double pesosChilenos = scanner.nextDouble();

        // Mostrar opciones de moneda
        System.out.println("Seleccione la moneda de destino:");
        System.out.println("1: Dólares (tipo de cambio = 0.0011)");
        System.out.println("2: Euros (tipo de cambio = 0.00095)");
        System.out.println("3: Yenes (tipo de cambio = 0.15)");
        System.out.println("4: Libras Esterlinas (tipo de cambio = 0.00084)");
        System.out.println("5: Yuanes (tipo de cambio = 0.0073)");
        
        // Leer la opción del usuario
        System.out.print("Ingrese la opción (1-5): ");
        int opcion = scanner.nextInt();

        double montoConvertido = 0;

        // Estructura de control para convertir la cantidad a la moneda seleccionada
        switch (opcion) {
            case 1: // Dólares
                montoConvertido = pesosChilenos * 0.0011;
                System.out.printf("El monto convertido a dólares es: $%.2f\n", montoConvertido);
                break;
            case 2: // Euros
                montoConvertido = pesosChilenos * 0.00095;
                System.out.printf("El monto convertido a euros es: €%.2f\n", montoConvertido);
                break;
            case 3: // Yenes
                montoConvertido = pesosChilenos * 0.15;
                System.out.printf("El monto convertido a yenes es: ¥%.2f\n", montoConvertido);
                break;
            case 4: // Libras Esterlinas
                montoConvertido = pesosChilenos * 0.00084;
                System.out.printf("El monto convertido a libras esterlinas es: £%.2f\n", montoConvertido);
                break;
            case 5: // Yuanes
                montoConvertido = pesosChilenos * 0.0073;
                System.out.printf("El monto convertido a yuanes es: ¥%.2f\n", montoConvertido);
                break;
            default: // Opción no válida
                System.out.println("Error: opción no válida.");
                break;
        }
        
        // Cerrar el escáner
        scanner.close();
    }
}
