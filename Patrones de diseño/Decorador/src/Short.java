

public class Short extends BebidaDecor{
private Ingredientes ingredientes;
    public Short(Ingredientes ingredientes) {
        super(ingredientes);
        this.ingredientes=ingredientes;
    }

    @Override
    public String getDescripcion() {
        return ingredientes.getDescripcion()+" + Short";
    }

    @Override
    public int getprecio() {
         return ingredientes.getprecio()+0;
     }
    
}




