

public abstract class BebidaDecor implements Ingredientes {
   private Ingredientes ingredientes;

    public BebidaDecor(Ingredientes ingredientes) {
        this.ingredientes = ingredientes;
    }
    public Ingredientes getIngredientes(){
        return this.ingredientes;
    }
   
}




