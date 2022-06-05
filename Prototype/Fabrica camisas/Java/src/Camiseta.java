public abstract class Camiseta implements Cloneable
{

    public String talla;
    public String color; 
    public String estampado;

    public Camiseta clone() throws CloneNotSupportedException
    {
        return (Camiseta) super.clone();
    }

    public void setters (String talla, String color, String estampado)
    {
            this.talla = talla;
            this.color = color;
            this.estampado = estampado;
    }

    public String getters()
    {
        return "Talla: "+talla+" Color: "+color+" Estampado: "+estampado;
    }

    public abstract String impresion();

}
