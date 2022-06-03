import java.util.StringTokenizer;

public class EjerciciosJr {
    public static void main(String[] args) throws Exception {

        //1.- invertir una cadena de texto
        System.out.println("invertir una cadena de texto\n");
        System.out.println("FORMA 1");
        String texto = "Hola mundo";
        String texto2 = "";
        for (int i = texto.length() - 1; i >= 0; i--) {
            texto2 += texto.charAt(i);
        }
        System.out.println(texto2+"\n");
        //forma 2
        System.out.println("FORMA 2");
        StringBuilder sb = new StringBuilder(texto);
        texto = sb.reverse().toString();
        System.out.println(texto+"\n");


        //2.- Calcular cuantas veces se repite un caracter
        //forma 1
        System.out.println("Calcular cuantas veces se repite un caracter\n");
        System.out.println("FORMA 1");
        String texto3 = "Hola mundo";
        int contador = 0;
        char caracter = 'o';
        for (int i = 0; i < texto3.length(); i++) {
            if (texto3.charAt(i) == caracter) {
                contador++;
            }
        }
        System.out.println("El caracter " +"'"+caracter+"'"+ " se repite "+contador+" veces\n");
        //forma 2
        System.out.println("FORMA 2");
        contador = texto3.length() - texto3.replace("o", "").length();
        System.out.println("El caracter " +"'"+caracter+"'"+ " se repite "+contador+" veces\n");

        //3.- Distancia de Hamming
        System.out.println("Calcular la distancia de Hamming\n");
        String texto4 = "patitosw";    
        String texto5 = "paratosa";   
        int distancia = 0;
        if (texto4.length() != texto5.length()) {
            System.out.println("No se puede calcular la distancia de Hamming");
        } else {
            for (int i = 0; i < texto4.length(); i++) {
                if (texto4.charAt(i) != texto5.charAt(i)) {
                    distancia++;
                }
            }
            System.out.println("La distancia de Hamming es: "+distancia+"\n");
        }

        //4.- Contador de palabras
        System.out.println("Contador de palabras\n");
        String texto6 = "    Un     texto   que     tiene  palabras     ";
        StringTokenizer st = new StringTokenizer(texto6);
        System.out.println("El texto tiene "+st.countTokens()+" palabras\n");

        //5.- Contador de números
        System.out.println("Contador de números\n");
        var texto7 = "an1298jq???da!22121230001masA";
        String [] words = texto7.split("[0-9]");
        int words3 = words.length-1;
        System.out.println("Cantidad numeros: "+words3+"\n");
    }
}
