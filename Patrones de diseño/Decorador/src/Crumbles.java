

public class Crumbles extends BebidaDecor{
    private Ingredientes ingredientes;

    public Crumbles(Ingredientes ingredientes) {
        super(ingredientes);
        this.ingredientes=ingredientes;
        
    }

    @Override
    public String getDescripcion() {
     return ingredientes.getDescripcion()+" + Crumbles";
    }

    @Override
    public int getprecio() {
       return ingredientes.getprecio()+1500;
    }
    
    
}
