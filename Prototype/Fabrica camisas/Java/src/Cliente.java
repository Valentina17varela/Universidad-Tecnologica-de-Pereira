public class Cliente 
{
    public static void main(String[] args) throws CloneNotSupportedException
    {
        Camiseta c1 = new CamisetaMCorta();
        c1.setters("40", "rojo", "prototipo1");
        System.out.println(c1.impresion());

        Camiseta c2 = c1.clone();
        c2.setters("20", "azul", "Prototipo2");
        System.out.println(c2.impresion());


    }
}
