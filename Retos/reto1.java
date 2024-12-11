
package javaapplication2;

import java.util.Scanner;


public class JavaApplication2 {


    public static void main(String[] args) {
        Scanner keyword= new Scanner(System.in);
        System.out.println("1.Suma 2.Resta 3.Multiplicación 4.División.");
        int decision= keyword.nextInt();
        System.out.println("Ingresa x: ");
        
        int x= keyword.nextInt();
        System.out.println("Ingresa y: ");
        int y= keyword.nextInt();
        double resultado = 0;
        switch(decision) {
            case 1 ->  {
                resultado = x + y;
                break;
                }
            case 2 ->  {
                resultado = x - y;
                break;
            }
            case 3 ->  {
                resultado = x*y;
                break;
            }
            case 4 ->  {
                resultado = x/y;
                break;
            }
            default -> {
                System.out.println("ERES TONTO TIO");
            }
        }
        
        System.out.println(resultado);
    }
    
}

