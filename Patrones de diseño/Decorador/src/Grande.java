

public class Grande extends BebidaDecor{
    private Ingredientes ingredientes;
        public Grande(Ingredientes ingredientes) {
            super(ingredientes);
            this.ingredientes=ingredientes;
        }
    
        @Override
        public String getDescripcion() {
            return ingredientes.getDescripcion()+" + Grande";
        }
    
        @Override
        public int getprecio() {
             return ingredientes.getprecio()+2000;
         }
        
    }
    
