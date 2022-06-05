

public class Tall extends BebidaDecor{
    private Ingredientes ingredientes;
        public Tall(Ingredientes ingredientes) {
            super(ingredientes);
            this.ingredientes=ingredientes;
        }
    
        @Override
        public String getDescripcion() {
            return ingredientes.getDescripcion()+" + Tall";
        }
    
        @Override
        public int getprecio() {
             return ingredientes.getprecio()+1000;
         }
        
    }
    
