public class B_DECORADOR {

	public static void main(String[] args) 
    {
        Ingredientes expreso= new Expreso();
        System.out.println(expreso.getDescripcion()+"\n"+expreso.getprecio());
        
        expreso=new Tall(expreso);
        System.out.println(expreso.getDescripcion()+"\n"+expreso.getprecio());
        expreso=new Drizzles(expreso);
        System.out.println(expreso.getDescripcion()+"\n"+expreso.getprecio());
        
        System.out.println("\n");
        Ingredientes chocolate= new Chocolate();
        System.out.println(chocolate.getDescripcion()+"\n"+chocolate.getprecio());
        chocolate = new Grande(chocolate);
        System.out.println(chocolate.getDescripcion()+"\n"+chocolate.getprecio());

        System.out.println("\n");
        Ingredientes te= new Te();
        System.out.println(te.getDescripcion()+"\n"+te.getprecio());

    }
    
}


