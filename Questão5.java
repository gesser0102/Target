/*
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

 */

import java.util.Scanner;

public class Questão5{
        
        public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite uma string: ");
        String original = scanner.nextLine();
        scanner.close();
        
        char[] chars = original.toCharArray();
        
        for (int i = 0, j = chars.length - 1; i < j; i++, j--) {
            char temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
        }
        
        String invertida = new String(chars);
        
        System.out.println("String invertida: " + invertida);
    }
}