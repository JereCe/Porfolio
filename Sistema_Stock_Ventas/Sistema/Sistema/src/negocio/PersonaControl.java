/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package negocio;


import datos.RolDAO;
import datos.UsuarioDAO;
import entidades.Rol;
import entidades.Usuario;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import java.util.ArrayList;
import java.util.List;
import javax.swing.DefaultComboBoxModel;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author jerem
 */
public class PersonaControl {
    private final UsuarioDAO DATOS;
    private final RolDAO DATOSROL;
    private Usuario obj;
    private DefaultTableModel modeloTabla;
    private int registrosMostrados;
    
    
    public PersonaControl(){
        this.DATOS = new UsuarioDAO();
        this.DATOSROL = new RolDAO();
        this.obj = new Usuario();
        this.registrosMostrados = 0;
        
    }
    public DefaultTableModel listar(String Texto,int totalPorPagina,int numPagina){
        List<Usuario> lista = new ArrayList();
        lista.addAll(DATOS.listar(Texto,totalPorPagina,numPagina));
        String[] titulos={"ID","Rol ID","Rol","Usuario","Documento","N° Documento","Direccion","Telefono","Email","Clave","Estado"};
        this.modeloTabla = new DefaultTableModel(null,titulos);
        String estado;
        String[] registro = new String[11];
        this.registrosMostrados = 0;

        
        for (Usuario item:lista ) {
            if(item.isActivo()){
                estado ="Activo";
            }else{
                estado = "Inactivo";
            }
            registro[0]=Integer.toString(item.getId());
            registro[1]=Integer.toString(item.getRolId());
            registro[2]=item.getRolNombre();
            registro[3]=item.getNombre();
            registro[4]=item.getTipoDocumento();
            registro[5]=item.getNumDocumento();
            registro[6]=item.getDireccion();
            registro[7]=item.getTelefono();
            registro[8]=item.getEmail();
            registro[9]=item.getClave();
            registro[10]=estado;
            this.modeloTabla.addRow(registro);
            this.registrosMostrados = this.registrosMostrados +1;
                    
            
        }
        return modeloTabla;
        
             
    }
    
    public DefaultComboBoxModel seleccionar(){
        DefaultComboBoxModel items = new DefaultComboBoxModel();
        List<Rol> lista = new ArrayList();
        lista = DATOSROL.seleccionar();
        for (Rol item: lista ) {
            items.addElement(new Rol(item.getId(),item.getNombre()));  
        }
        return items;
        
        
        
        
    }
    
    
    private static String encriptar(String valor){
        
        MessageDigest md;
        try {
            md = MessageDigest.getInstance("SHA-256");
            
        } catch (NoSuchAlgorithmException e) {
            return null;
        }
        
        byte[] hash = md.digest(valor.getBytes());
        StringBuilder sb = new StringBuilder();
        
        for (byte b : hash) {
            sb.append(String.format("%02x", b));

            
        }
        
        return sb.toString();
        
    
    }
    public String insertar (int rolId,String nombre,String tipoDocumento, String numDocumento,String direccion,String telefono,String email,String clave){
        if(DATOS.existe(email)){
            return "El registro ya existe";
        }else{
            obj.setRolId(rolId);
            obj.setNombre(nombre);
            obj.setTipoDocumento(tipoDocumento);
            obj.setNumDocumento(numDocumento);
            obj.setDireccion(direccion);
            obj.setTelefono(telefono);
            obj.setEmail(email);
            obj.setClave(this.encriptar(clave));
            
            if(DATOS.insertar(obj)){
                return "OK";
            }else{
                return "Error en el registro";
            }
            
        }
        
        
    }
           
    
    public String actualizar (int id,int rolId,String nombre,String tipoDocumento, String numDocumento,String direccion,String telefono,String email,String emailAnt,String clave){
        if(nombre.equals(emailAnt)){
            obj.setId(id);
            obj.setRolId(rolId);
            obj.setNombre(nombre);
            obj.setTipoDocumento(tipoDocumento);
            obj.setNumDocumento(numDocumento);
            obj.setDireccion(direccion);
            obj.setTelefono(telefono);
            obj.setEmail(email);
            String encriptado;
            if (clave.length()==64) {
                encriptado = clave;
                
            } else {
                encriptado = this.encriptar(clave);
            }
            obj.setClave(encriptado);
            if(DATOS.actualizar(obj)){
                return "OK";
            }
            else{
                return "Error en la actualizacion";
            }
            
        }else{
            if(DATOS.existe(email)){
                return"El registro ya existe";
            }else{
            
                obj.setId(id);
                obj.setRolId(rolId);
                obj.setNombre(nombre);
                obj.setTipoDocumento(tipoDocumento);
                obj.setNumDocumento(numDocumento);
                obj.setDireccion(direccion);
                obj.setTelefono(telefono);
                obj.setEmail(email);
                String encriptado;
                if (clave.length() == 64) {
                    encriptado = clave;

                } else {
                    encriptado = this.encriptar(clave);
                }
                if(DATOS.actualizar(obj)){
                    return "OK";
                }else{
                    return "Error en la actualizacion";            
                }
                          
            }
           
        }                
        
    }
    
    public String desactivar (int id){
        if(DATOS.desactivar(id)){
            return"OK";
        }else{
            return "No se puede desactivar el registro";
        }
        
        
        
    }
    
    public String activar (int id){
        if(DATOS.activar(id)){
            return"OK";
        }else{
            return "No se puede activar el registro";
        }
        
    }
    
    public int total (){
        return DATOS.total();
        
    }
    
    public int totalMostrados(){
        return registrosMostrados;
    }
    
    
    
    
    
}
