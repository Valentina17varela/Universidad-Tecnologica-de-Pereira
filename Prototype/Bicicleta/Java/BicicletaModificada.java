public class BicicletaModificada extends Bicicleta 
{
    @Override
    public String verBicicleta() 
    {
    
     return "Este es el color: " + this.getColor() + " El rodado es: " + this.getRodado();
    }
}

