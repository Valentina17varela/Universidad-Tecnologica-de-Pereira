

public class Drizzles extends BebidaDecor{
    private Ingredientes ingredientes;

    public Drizzles(Ingredientes ingredientes) {
        super(ingredientes);
        this.ingredientes=ingredientes;
        
    }

    @Override
    public String getDescripcion() {
     return ingredientes.getDescripcion()+" + Drizzles";
    }

    @Override
    public int getprecio() {
       return ingredientes.getprecio()+1000;
    }
    
    
}




