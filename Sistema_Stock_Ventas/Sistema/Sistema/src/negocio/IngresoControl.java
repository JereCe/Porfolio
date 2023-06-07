/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package negocio;



import datos.IngresoDAO;


import entidades.DetalleIngreso;
import entidades.Ingreso;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author jerem
 */
public class IngresoControl {
    private final IngresoDAO DATOS;
    private Ingreso obj;
    private DefaultTableModel modeloTabla;
    private int registrosMostrados;
    
    
    public IngresoControl(){
        this.DATOS = new IngresoDAO();
        
        this.obj = new Ingreso();
        this.registrosMostrados = 0;
        
    }
    public DefaultTableModel listar(String Texto,int totalPorPagina,int numPagina){
        List<Ingreso> lista = new ArrayList();
        lista.addAll(DATOS.listar(Texto,totalPorPagina,numPagina));
        String[] titulos={"ID","Usuario ID","Usuario","Proveedor ID","Proveedor","Tipo Comprobante","Serie","Numero","Fecha","Impuesto","Total","Estado"};
        this.modeloTabla = new DefaultTableModel(null,titulos);
        
        String[] registro = new String[12];
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        
        this.registrosMostrados = 0;

        
        for (Ingreso item:lista ) {
            registro[0]=Integer.toString(item.getId());
            registro[1]=Integer.toString(item.getUsuarioId());
            registro[2]=item.getUsuarioNombre();
            registro[3]=Integer.toString(item.getPersonaId());
            registro[4]=item.getPersonaNombre();
            registro[5]=item.getTipoComprobante();
            registro[6]=item.getSerieComprobante();
            registro[7]=item.getNumeroComprobante();
            registro[8]=sdf.format(item.getFecha());
            registro[9]=Double.toString(item.getImpuesto());
            registro[10]=Double.toString(item.getTotal());
            registro[11]=item.getEstado();
            
            this.modeloTabla.addRow(registro);
            this.registrosMostrados = this.registrosMostrados +1;
                    
            
        }
        return modeloTabla;
        
             
    }
    

    
    public String insertar (int personaId,String tipoComprobamte,String serieComprobante,String numComprobante,double impuesto,double total,DefaultTableModel modeloDetalles){
        if(DATOS.existe(serieComprobante,numComprobante)){
            return "El registro ya existe";
        }else{
            obj.setUsuarioId(Variables.usuarioId);
            obj.setPersonaId(personaId);
            obj.setTipoComprobante(tipoComprobamte);
            obj.setSerieComprobante(serieComprobante);
            obj.setNumeroComprobante(numComprobante);
            obj.setImpuesto(impuesto);
            obj.setTotal(total);
            
            List <DetalleIngreso> detalles = new ArrayList();
            int articuloId;
            int cantidad;
            double precio;
            
            for(int i = 0;i<modeloDetalles.getRowCount();i++){
                articuloId=Integer.parseInt(String.valueOf(modeloDetalles.getValueAt(i, 0)));
                cantidad=Integer.parseInt(String.valueOf(modeloDetalles.getValueAt(i, 3)));
                precio=Double.parseDouble(String.valueOf(modeloDetalles.getValueAt(i, 4)));
               detalles.add(new DetalleIngreso(articuloId,cantidad,precio));
            }
            obj.setDetalles(detalles);

            if(DATOS.insertar(obj)){
                return "OK";
            }else{
                return "Error en el registro";
            }
            
        }
        
        
    }
           

    public String anular (int id){
        if(DATOS.anular(id)){
            return"OK";
        }else{
            return "No se puede anular el registro";
        }
        
        
        
    }
    
    
    
    public int total (){
        return DATOS.total();
        
    }
    
    public int totalMostrados(){
        return registrosMostrados;
    }
    
    
    
    
    
}
