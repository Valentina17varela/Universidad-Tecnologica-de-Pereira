public abstract class Bicicleta implements Cloneable
{
    private String color;
    private String rodado;
   
    /**
     * Metodo clonador
     */
    public Bicicleta clone() throws CloneNotSupportedException
    {return (Bicicleta) super.clone();}
    
    public abstract String verBicicleta();
   
       //Getters and Setters
    public String getColor(){return color;}
   
    public void setColor(String color) 
    {this.color = color;}
   
    public String getRodado() {return rodado;}
   
    public void setRodado(String rodado) 
    {this.rodado = rodado;}
}

