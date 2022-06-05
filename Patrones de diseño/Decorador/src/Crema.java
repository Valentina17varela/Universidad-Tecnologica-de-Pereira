
public class Crema extends BebidaDecor{
private Ingredientes ingredientes;
    public Crema(Ingredientes ingredientes) {
        super(ingredientes);
        this.ingredientes=ingredientes;
    }

    @Override
    public String getDescripcion() {
    return ingredientes.getDescripcion()+" + Crema";   
    }

    @Override
    public int getprecio() {
     return ingredientes.getprecio()+500;  
    }
    
}





