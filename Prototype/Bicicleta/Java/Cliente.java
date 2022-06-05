public class Cliente
{
    /**
     * @param args
     * @throws CloneNotSupportedException 
     */
    public static void main(String[] args) throws CloneNotSupportedException {
     Bicicleta bc = new BicicletaModificada();
     bc.setColor("Roja");
     bc.setRodado("22");
     System.out.println(bc.verBicicleta());
     Bicicleta bc2 = bc.clone();
     bc2.setColor("Negro");
     bc2.setRodado("30");
     
     System.out.println(bc2.verBicicleta());
    }
}
