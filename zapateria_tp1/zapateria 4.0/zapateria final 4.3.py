import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
from tkinter.font import Font

MAX=20

NroFac = 1
fecha = time.strftime("%d/%m/%y")


class DatosFacturas:
    def __init__(self,NroFactura,Fecha,IdVendedor,IdLocal,IdCliente,DescCliente,ImporteTotal):
        self.NroFactura = NroFactura
        self.Fecha = Fecha
        self.IdVendedor = IdVendedor
        self.IdLocal = IdLocal
        self.IdCliente = IdCliente
        self.DescCliente = DescCliente
        self.ImporteTotal = ImporteTotal
    
    def __repr__(self):
        return " Nº:{0} - Fecha:{1} - IDVendedor:{2} - IDLocal:{3} - IDCliente:{4} - NombreCliente:{5} - Total:{6}".format(self.NroFactura,self.Fecha,self.IdVendedor,self.IdLocal,self.IdCliente,self.DescCliente,self.ImporteTotal)


lstFacturas = [] 

class DetalleFacturas:
    def __init__(self,NroFactura,IdProducto,Cantidad,PrecioUnitario):
        self.NroFactura = NroFactura
        self.IdProducto = IdProducto
        self.Cantidad = Cantidad
        self.PrecioUnitario = PrecioUnitario
        
    def __repr__(self):
        return "Nº:{0} - Producto:{1} - Cantidad:{2} - Precio:{3}".format(self.NroFactura,self.IdProducto,self.Cantidad,self.PrecioUnitario)


lstDetalleFacturas = []



class Categoria:
    def __init__(self,IDcategoria,NombreCategoria):
        self.IDcategoria=  IDcategoria
        self.NombreCategoria= NombreCategoria
    def __repr__(self):
        return " ID: %i,Nombre: %s" % (self.IDcategoria, self.NombreCategoria)
    
lstCategorias= [] 



class Producto:
    def __init__(self,IDproducto, DescProducto,IDcat,Precio, StockActual):
        self.IDproducto = IDproducto
        self.DescProducto = DescProducto
        self.IDcat = IDcat
        self.Precio = Precio
        self.StockActual = StockActual
        
        
    def __repr__(self):
        return "ID: %i, Producto: %s,Categoria %i, $: %i, Stock: %i" % (self.IDproducto,self.DescProducto,self.IDcat,self.Precio,self.StockActual)





lstProductos=[]



class Locales:
    def __init__(self, IDlocal, NombreLocal ):
        self.IDlocal=  IDlocal
        self.NombreLocal= NombreLocal
    def __repr__(self):
        return " ID: %i,Nombre: %s" % (self.IDlocal, self.NombreLocal)
    
lstLocales= []


class Vendedores:
    def __init__(self, IDVendedor, NombreVendedor ):
        self.IDVendedor=  IDVendedor
        self.NombreVendedor= NombreVendedor
    def __repr__(self):
        return " ID: %i,Vendedor: %s" % (self.IDVendedor, self.NombreVendedor)
    
lstVendedor= []

class Clientes:
    def __init__(self,IDCliente,NombreCliente,EmailCliente):
        self.IDCliente=  IDCliente
        self.NombreCliente= NombreCliente
        self.EmailCliente = EmailCliente
    def __repr__(self):
        return " ID: %i,Cliente: %s,Email: %s" % (self.IDCliente, self.NombreCliente,self.EmailCliente)
    
lstClientes= []


def VentanaABMCategorias():
    LstCategorias = Toplevel()
    frame = Frame(LstCategorias)
    LstCategorias.title("Lista de categorias")
    LstCategorias.grab_set()
    LstCategorias.geometry("380x300")
    LstCategorias.configure(background="white")
    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT,fill=Y)
    listbox = Listbox(frame,yscrollcommand=scroll.set, width= 20)
    scroll.config(command=listbox.yview)
    for i in range (0,len(lstCategorias)):
        if lstCategorias[i].IDcategoria != 0:
            listbox.insert(i,lstCategorias[i])
    listbox.pack()
    frame.pack()
    LblID = Label(LstCategorias,text="Ingresar ID De la categoria: ")
    LblID.pack(fill=X)
    ID= 0
    EntryID= Entry(LstCategorias,textvariable = ID)
    EntryID.pack(fill=X) 
    BotonModificar = Button(LstCategorias, text="Modificar",command=lambda: ModificarCategoria(EntryID,listbox))
    BotonModificar.pack(fill=X)
    BotonAgregar = Button(LstCategorias, text="Agregar", command=lambda: CategoriaCarga(listbox))
    BotonAgregar.pack(fill=X)
    BotonBorrar = Button(LstCategorias, text = "Borrar", command=lambda: BorrarCategoria(EntryID,listbox))
    BotonBorrar.pack(fill=X)
    root.wait_window(LstCategorias)

def ModificarCategoria(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstCategorias)):
          if lstCategorias[j].IDcategoria == ID and lstCategorias[j].IDcategoria != 0:
            VentanaModificarCategoria(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,20):
        if lstCategorias[i].IDcategoria != 0:
            listbox.insert(i,lstCategorias[i])
    EntryID.delete(0, 'end')
    
    
def VentanaModificarCategoria(ID):
    modificarCategoria = Toplevel()
    modificarCategoria.title("Modificar Categoria")
    modificarCategoria.grab_set()
    modificarCategoria.geometry("380x300")
    modificarCategoria.configure(background="white")
    etiqueta_text= Label(modificarCategoria,text="Modificar Categoria")
    etiqueta_text.pack(side=TOP)
    IDMod= ID
    NombreMod= lstCategorias[IDMod-1].NombreCategoria
    IDmodificar=Entry(modificarCategoria)
    IDmodificar.insert(0,ID)
    IDmodificar.config(state=DISABLED)
    IDmodificar.pack()
    Nombremodificar=Entry(modificarCategoria)
    Nombremodificar.insert(0,NombreMod)
    Nombremodificar.pack()
    boton=Button(modificarCategoria,text="Modificar Categoria",command=lambda: ModCategoria(Nombremodificar,IDmodificar))
    boton.pack(side=TOP)
    root.wait_window(modificarCategoria)
    
def ModCategoria(Nombremodificar,IDmodificar):
    ID=int(IDmodificar.get())
    nombre=Nombremodificar.get()
    for h in range(0,len(lstCategorias)):
        if lstCategorias[h].IDcategoria== ID:
            lstCategorias[h].NombreCategoria = nombre
            messagebox.showinfo(message="Categoria modificada", title="Titulo")

def CategoriaCarga(listbox):
    VentanaCargaCategoria()
    listbox.delete(0,'end')
    for i in range (0,len(lstCategorias)):
        if lstCategorias[i].IDcategoria != 0:
            listbox.insert(i,lstCategorias[i])

def VentanaCargaCategoria():
    Vcargacategoria = Toplevel()
    Vcargacategoria.title("Cargar Categoria")
    Vcargacategoria.grab_set()
    Vcargacategoria.geometry("380x300")
    Vcargacategoria.configure(background="white")
    etiqueta_text= Label(Vcargacategoria,text="valor")
    etiqueta_text.pack(side=TOP)
    valor= " "
    nombrecategoria=Entry(Vcargacategoria,textvariable = valor)
    nombrecategoria.pack(side=TOP)
    boton=Button(Vcargacategoria,text="Cargar Nueva categoria",command=lambda:CargarCategoria(nombrecategoria,valor))
    boton.pack(side=TOP)
    root.wait_window(Vcargacategoria)
        
def CargarCategoria(nombrecategoria,valor):
    nombrecat=nombrecategoria.get()
    lstCategorias.append(Categoria(len(lstCategorias)+1,nombrecat))           
    nombrecategoria.delete(0, 'end')
    messagebox.showinfo(message="Categoria Cargada", title="Titulo")
    return
        
def BorrarCategoria(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstCategorias)):
          if lstCategorias[j].IDcategoria == ID and lstCategorias[j].IDcategoria != 0:
            BajaCategoria(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,len(lstCategorias)):
        if lstCategorias[i].IDcategoria != 0:
            listbox.insert(i,lstCategorias[i])
    EntryID.delete(0, 'end')
    
def BajaCategoria(ID):    
    for j in range(0,len(lstCategorias)):
        if lstCategorias[j].IDcategoria== ID:
            lstCategorias[j]=Categoria(0,"")
            messagebox.showinfo(message="Categoria Borrada", title="Titulo")
            return


    
def VentanaABMVendedor(): 
    LstVendedor = Toplevel()
    frame = Frame(LstVendedor)
    LstVendedor.title("Lista de Vendedores")
    LstVendedor.grab_set()
    LstVendedor.geometry("380x300")
    LstVendedor.configure(background="white")
    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT,fill=Y)
    listbox = Listbox(frame,yscrollcommand=scroll.set, width= 50)
    scroll.config(command=listbox.yview)
    for i in range (0,len(lstVendedor)):
        if lstVendedor[i].IDVendedor != 0:
            listbox.insert(i,lstVendedor[i])
    listbox.pack()
    frame.pack()
    LblID = Label(LstVendedor,text="Ingresar ID Del Vendedor: ")
    LblID.pack(fill=X)
    ID= 0
    EntryID= Entry(LstVendedor,textvariable = ID)
    EntryID.pack(fill=X) 
    BotonModificar = Button(LstVendedor, text="Modificar",command=lambda:ModificarVendedor(EntryID,listbox))
    BotonModificar.pack(fill=X)
    BotonAgregar = Button(LstVendedor, text="Agregar", command=lambda:VendedorCarga(listbox))
    BotonAgregar.pack(fill=X)
    BotonBorrar = Button(LstVendedor, text = "Borrar", command=lambda:BorrarVendedor(EntryID,listbox))
    BotonBorrar.pack(fill=X)
    root.wait_window(LstVendedor)    


        
def ModificarVendedor(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstVendedor)):
          if lstVendedor[j].IDVendedor == ID and lstVendedor[j].IDVendedor != 0:
            VentanaModificarVendedor(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,len(lstVendedor)):
        if lstVendedor[i].IDVendedor != 0:
            listbox.insert(i,lstVendedor[i])
    EntryID.delete(0, 'end')
    
def VentanaModificarVendedor(ID):
    ModificarVendedor = Toplevel()
    ModificarVendedor.title("Modificar Vendedor")
    ModificarVendedor.grab_set()
    ModificarVendedor.geometry("380x300")
    ModificarVendedor.configure(background="white")
    Etiqueta_text= Label(ModificarVendedor,text="Modificar Vendedor")
    Etiqueta_text.pack(side=TOP)
    IDMod= ID
    NombreMod= lstVendedor[IDMod-1].NombreVendedor 
    IDModificar=Entry(ModificarVendedor)
    IDModificar.insert(0,ID)
    IDModificar.config(state=DISABLED)
    IDModificar.pack()
    NombreModificar=Entry(ModificarVendedor)
    NombreModificar.insert(0,NombreMod)
    NombreModificar.pack()
    boton=Button(ModificarVendedor,text="Modificar Vendedor",command=lambda: ModVendedor(NombreModificar,IDModificar))
    boton.pack(side=TOP)
    root.wait_window(ModificarVendedor)
    
def ModVendedor(NombreModificar,IDModificar):
    ID=int(IDModificar.get())
    nombre=NombreModificar.get()
    for h in range(0,len(lstVendedor)):
        if lstVendedor[h].IDVendedor== ID:
            lstVendedor[h].NombreVendedor = nombre
            messagebox.showinfo(message="Vendedor Modificado", title="Titulo")

def VendedorCarga(listbox):
    VentanaCargaVendedor()
    listbox.delete(0,'end')
    for i in range (0,len(lstVendedor)):
        if lstVendedor[i].IDVendedor != 0:
            listbox.insert(i,lstVendedor[i])


    
def VentanaCargaVendedor():
    VcargaVendedor = Toplevel()
    VcargaVendedor.title("Cargar Vendedor")
    VcargaVendedor.grab_set()
    VcargaVendedor.geometry("380x300")
    VcargaVendedor.configure(background="white")
    Etiqueta_text= Label(VcargaVendedor,text="valor")
    Etiqueta_text.pack(side=TOP)
    valor= " "
    nombreVendedor=Entry(VcargaVendedor,textvariable = valor)
    nombreVendedor.pack(side=TOP)
    boton=Button(VcargaVendedor,text="Cargar Nuevo Vendedor",command=lambda:CargarVendedor(nombreVendedor,valor))
    boton.pack(side=TOP)
    root.wait_window(VcargaVendedor)



        
def CargarVendedor(NombreVendedor,valor):
    nombreven=NombreVendedor.get()
    lstVendedor.append(Vendedores(len(lstVendedor)+1,nombreven))
    valor= " "
    NombreVendedor.delete(0, 'end')
    messagebox.showinfo(message="Vendedor Cargado", title="Titulo")
    return
        
def BorrarVendedor(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstVendedor)):
          if lstVendedor[j].IDVendedor == ID and lstVendedor[j].IDVendedor != 0:
            BajaVendedor(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,len(lstVendedor)):
        if lstVendedor[i].IDVendedor != 0:
            listbox.insert(i,lstVendedor[i])
    EntryID.delete(0, 'end')
    
def BajaVendedor(ID):    
    for j in range(0,len(lstVendedor)):
        if lstVendedor[j].IDVendedor== ID:
            lstVendedor[j]=Vendedores(0,"")
            messagebox.showinfo(message="Vendedor Eliminado", title="Titulo")
            return

    
def VentanaABMlocales(): 
    LstLocales = Toplevel()
    frame = Frame(LstLocales)
    LstLocales.title("lista de locales")
    LstLocales.grab_set()
    LstLocales.geometry("380x300")
    LstLocales.configure(background="white")
    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT,fill=Y)
    listbox = Listbox(frame,yscrollcommand=scroll.set, width= 50)
    scroll.config(command=listbox.yview)
    for i in range (0,len(lstLocales)):
        if lstLocales[i].IDlocal != 0:
            listbox.insert(i,lstLocales[i])
    listbox.pack()
    frame.pack()
    LblID = Label(LstLocales,text="Ingresar ID Del Local: ")
    LblID.pack(fill=X)
    ID= 0
    EntryID= Entry(LstLocales,textvariable = ID)
    EntryID.pack(fill=X) 
    BotonModificar = Button(LstLocales, text="Modificar",command=lambda:ModificarLocal(EntryID,listbox))
    BotonModificar.pack(fill=X)
    BotonAgregar = Button(LstLocales, text="agregar", command=lambda:LocalesCarga(listbox))
    BotonAgregar.pack(fill=X)
    BotonBorrar = Button(LstLocales, text = "Borrar", command=lambda:BorrarLocal(EntryID,listbox))
    BotonBorrar.pack(fill=X)
    root.wait_window(LstLocales)

def ModificarLocal(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstLocales)):
          if lstLocales[j].IDlocal == ID and lstLocales[j].IDlocal != 0:
            VentanaModificarLocal(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,len(lstLocales)):
        if lstLocales[i].IDlocal != 0:
            listbox.insert(i,lstLocales[i])
    EntryID.delete(0, 'end')
    
    
    

def VentanaModificarLocal(ID):
    ModificarLocal = Toplevel()
    ModificarLocal.title("Modificar Locales")
    ModificarLocal.grab_set()
    ModificarLocal.geometry("380x300")
    ModificarLocal.configure(background="white")
    etiqueta_text= Label(ModificarLocal,text="Modificar Local")
    etiqueta_text.pack(side=TOP)
    IDMod= ID
    NombreMod= lstLocales[IDMod-1].NombreLocal 
    IDmodificar=Entry(ModificarLocal)
    IDmodificar.insert(0,ID)
    IDmodificar.config(state=DISABLED)
    IDmodificar.pack()
    Nombremodificar=Entry(ModificarLocal)
    Nombremodificar.insert(0,NombreMod)
    Nombremodificar.pack()
    boton=Button(ModificarLocal,text="Modificar Local",command=lambda: ModLocal(Nombremodificar,IDmodificar))
    boton.pack(side=TOP)
    root.wait_window(ModificarLocal)
    
def ModLocal(Nombremodificar,IDmodificar):
    ID=int(IDmodificar.get())
    nombre=Nombremodificar.get()
    for h in range(0,len(lstLocales)):
        if lstLocales[h].IDlocal== ID:
            lstLocales[h].NombreLocal = nombre
            messagebox.showinfo(message="Local modificado", title="Titulo")

def LocalesCarga(listbox):
    VentanaCargaLocal()
    listbox.delete(0,'end')
    for i in range (0,len(lstLocales)):
        if lstLocales[i].IDlocal != 0:
            listbox.insert(i,lstLocales[i])
        
def VentanaCargaLocal():
    Vcargalocal = Toplevel()
    Vcargalocal.title("Cargar Locales")
    Vcargalocal.grab_set()
    Vcargalocal.geometry("380x300")
    Vcargalocal.configure(background="white")
    etiqueta_text= Label(Vcargalocal,text="valor")
    etiqueta_text.pack(side=TOP)
    valor= " "
    nombrelocal=Entry(Vcargalocal,textvariable = valor)
    nombrelocal.pack(side=TOP)
    boton=Button(Vcargalocal,text="Cargar Nuevo Local",command=lambda:Cargarlocal(nombrelocal,valor))
    boton.pack(side=TOP)
    root.wait_window(Vcargalocal)
    
    
def Cargarlocal(nombrelocal,valor):
    nombreloc=nombrelocal.get()
    lstLocales.append(Locales(len(lstLocales)+1,nombreloc))
    nombrelocal.delete(0, 'end')
    messagebox.showinfo(message="Local Cargado", title="Titulo")
    return
    
    
def BorrarLocal(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstLocales)):
          if lstLocales[j].IDlocal == ID and lstLocales[j].IDlocal != 0:
            BajaLocal(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,len(lstLocales)):
        if lstLocales[i].IDlocal != 0:
            listbox.insert(i,lstLocales[i])
    EntryID.delete(0, 'end')
    
def BajaLocal(ID):    
    for j in range(0,len(lstLocales)):
        if lstLocales[j].IDlocal== ID:
            lstLocales[j]=Locales(0,"")
            messagebox.showinfo(message="Local Borrado", title="Titulo")
            return


    
def VentanaABMProducto():
    LstProductos = Toplevel()
    frame = Frame(LstProductos)
    LstProductos.title("Lista De Productos")
    LstProductos.grab_set()
    LstProductos.geometry("380x300")
    LstProductos.configure(background="White")
    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT,fill=Y)
    listbox = Listbox(frame,yscrollcommand=scroll.set, width= 50)
    scroll.config(command=listbox.yview)
    for i in range (0,len(lstProductos)):
        if lstProductos[i].IDproducto != 0:
            listbox.insert(i,lstProductos[i])
    listbox.pack()
    frame.pack()
    LblID = Label(LstProductos,text="Ingresar ID De la Producto: ")
    LblID.pack(fill=X)
    ID= 0
    EntryID= Entry(LstProductos,textvariable = ID)
    EntryID.pack(fill=X) 
    BotonModificar = Button(LstProductos, text="Modificar",command=lambda: ModificarProducto(EntryID,listbox))
    BotonModificar.pack(fill=X)
    BotonAgregar = Button(LstProductos, text="Agregar", command=lambda: ProductoCarga(listbox))
    BotonAgregar.pack(fill=X)
    BotonBorrar = Button(LstProductos, text = "Borrar", command=lambda: BorrarProducto(EntryID,listbox))
    BotonBorrar.pack(fill=X)
    root.wait_window(LstProductos)
    
    
def ModificarProducto(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstProductos)):
          if lstProductos[j].IDproducto == ID and lstProductos[j].IDproducto != 0:
            VentanaModificarProducto(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,len(lstProductos)):
        if lstProductos[i].IDproducto != 0:
            listbox.insert(i,lstProductos[i])
    EntryID.delete(0, 'end')
    
    
def VentanaModificarProducto(ID):
    ModificarProducto = Toplevel()
    ModificarProducto.title("Modificar Producto")
    ModificarProducto.grab_set()
    ModificarProducto.geometry("500x500")
    ModificarProducto.configure(background="white")
    etiqueta_id= Label(ModificarProducto,text="ID")
    etiqueta_id.pack()
    IDMod= ID
    NombreMod= lstProductos[IDMod-1].DescProducto
    IDmodificar=Entry(ModificarProducto)
    IDmodificar.insert(0,ID)
    IDmodificar.config(state=DISABLED)
    IDmodificar.pack()
    etiqueta_nombre= Label(ModificarProducto,text="Descripcion Producto")
    etiqueta_nombre.pack()
    Nombremodificar=Entry(ModificarProducto)
    Nombremodificar.insert(0,NombreMod)
    Nombremodificar.pack()
    etiqueta_categoria= Label(ModificarProducto,text="categoria")
    etiqueta_categoria.pack()
    catMod= lstProductos[IDMod-1].IDcat
    catmodificar=Entry(ModificarProducto)
    catmodificar.insert(0,catMod)
    catmodificar.pack()

    etiqueta_precio= Label(ModificarProducto,text="Precio")
    etiqueta_precio.pack()
    PrecioMod= lstProductos[IDMod-1].Precio
    Preciomodificar=Entry(ModificarProducto)
    Preciomodificar.insert(0,PrecioMod)
    Preciomodificar.pack()
    etiqueta_stock= Label(ModificarProducto,text="Stock")
    etiqueta_stock.pack()
    StockMod= lstProductos[IDMod-1].StockActual
    Stockmodificar=Entry(ModificarProducto)
    Stockmodificar.insert(0,StockMod)
    Stockmodificar.pack()




    
    boton=Button(ModificarProducto,text="Modificar Local",command=lambda: ModProducto(Nombremodificar,IDmodificar,Preciomodificar,Stockmodificar,catmodificar))
    boton.pack(side=TOP)
    root.wait_window(ModificarProducto)
    
def ModProducto(Nombremodificar,IDmodificar,Preciomodificar,Stockmodificar,catmodificar):
    ID=int(IDmodificar.get())
    nombre = Nombremodificar.get()
    Precio = int(Preciomodificar.get())
    Stock = int(Stockmodificar.get())
    categoria= int(catmodificar.get())
    for h in range(0,len(lstProductos)):
        if lstProductos[h].IDproducto== ID:
            lstProductos[h].DescProducto = nombre
            lstProductos[h].Precio = Precio
            lstProductos[h].StockActual = Stock
            lstProductos[h].IDcat = categoria
            
            
            messagebox.showinfo(message="Producto modificado", title="Titulo")
            
def ProductoCarga(listbox):
    VentanaCargaProducto()
    listbox.delete(0,'end')
    for i in range (0,len(lstProductos)):
        if lstProductos[i].IDproducto != 0:
            listbox.insert(i,lstProductos[i])

def VentanaCargaProducto():
    VcargaProducto = Toplevel()
    VcargaProducto.title("Alta Producto")
    VcargaProducto.grab_set()
    VcargaProducto.geometry("380x300")
    VcargaProducto.configure(background="white")
    etiqueta_nombre= Label(VcargaProducto,text="Descripcion Producto")
    etiqueta_nombre.pack()
    valornombre= " "
    nombreproducto=Entry(VcargaProducto)
    nombreproducto.pack()
    etiqueta_categoria= Label(VcargaProducto,text="Categoria")
    etiqueta_categoria.pack()
    valorcategoria= 0
    categoriaproducto=Entry(VcargaProducto)
    categoriaproducto.pack()
    etiqueta_precio= Label(VcargaProducto,text="Precio")
    etiqueta_precio.pack()
    valorprecio= 0
    precioproducto=Entry(VcargaProducto)
    precioproducto.pack()
    etiqueta_stock= Label(VcargaProducto,text="Stock")
    etiqueta_stock.pack()
    valorstock= 0
    stockproducto=Entry(VcargaProducto)
    stockproducto.pack()
    boton=Button(VcargaProducto,text="Cargar Nuevo Producto",command=lambda:CargarProducto(nombreproducto,precioproducto,stockproducto,categoriaproducto))
    boton.pack()
    root.wait_window(VcargaProducto)

def CargarProducto(nombreproducto,precioproducto,stockproducto,categoriaproducto):
    nombre=nombreproducto.get()
    precio=int(precioproducto.get())
    stock=int(stockproducto.get())
    categoria=int(categoriaproducto.get())

    lstProductos.append(Producto(len(lstProductos)+1,nombre,categoria,precio,stock))           
    nombreproducto.delete(0, 'end')
    precioproducto.delete(0, 'end')
    stockproducto.delete(0, 'end')
    categoriaproducto.delete(0, 'end') 
    messagebox.showinfo(message="producto cargado Cargado", title="Titulo")
    return
    
   

        
def BorrarProducto(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstProductos)):
          if lstProductos[j].IDproducto == ID and lstProductos[j].IDproducto != 0:
            BajaProducto(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,len(lstProductos)):
        if lstProductos[i].IDproducto != 0:
            listbox.insert(i,lstProductos[i])
    EntryID.delete(0, 'end')        

def BajaProducto(ID):    
    for j in range(0,len(lstProductos)):
        if lstProductos[j].IDproducto== ID:
            lstProductos[j]=Producto(0,"",0,0,0)
            messagebox.showinfo(message="Producto  Borrado", title="Titulo")
            return
        
        
        
        
        
def VentanaABMCliente():
    LstClientes = Toplevel()
    frame = Frame(LstClientes)
    LstClientes.title("Lista de Clientes")
    LstClientes.grab_set()
    LstClientes.geometry("380x300")
    LstClientes.configure(background="white")
    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT,fill=Y)
    listbox = Listbox(frame,yscrollcommand=scroll.set, width= 50)
    scroll.config(command=listbox.yview)
    for i in range (0,len(lstClientes)):
        if lstClientes[i].IDCliente != 0:
            listbox.insert(i,lstClientes[i])
    listbox.pack()
    frame.pack()
    LblID = Label(LstClientes,text="Ingresar ID Del Cliente: ")
    LblID.pack(fill=X)
    ID= 0
    EntryID= Entry(LstClientes,textvariable = ID)
    EntryID.pack(fill=X) 
    BotonModificar = Button(LstClientes, text="Modificar",command=lambda: ModificarCliente(EntryID,listbox))
    BotonModificar.pack(fill=X)
    BotonAgregar = Button(LstClientes, text="Agregar", command=lambda: ClienteCarga(listbox))
    BotonAgregar.pack(fill=X)
    BotonBorrar = Button(LstClientes, text = "Borrar", command=lambda: BorrarCliente(EntryID,listbox))
    BotonBorrar.pack(fill=X)
    root.wait_window(LstClientes)       


def ModificarCliente(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstClientes)):
          if lstClientes[j].IDCliente == ID and lstClientes[j].IDCliente != 0:
            VentanaModificarCliente(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,len(lstClientes)):
        if lstClientes[i].IDCliente != 0:
            listbox.insert(i,lstClientes[i])
    EntryID.delete(0, 'end')
    

def VentanaModificarCliente(ID):
    modificarCliente = Toplevel()
    modificarCliente.title("Lista de Clientes")
    modificarCliente.grab_set()
    modificarCliente.geometry("380x300")
    modificarCliente.configure(background="white")
    etiqueta_text= Label(modificarCliente,text="Modificar Cliente")
    etiqueta_text.pack(side=TOP)
    IDMod= ID
    NombreMod= lstClientes[IDMod-1].NombreCliente
    EmailMod = lstClientes[IDMod-1].EmailCliente
    IDmodificar=Entry(modificarCliente)
    IDmodificar.insert(0,ID)
    IDmodificar.config(state=DISABLED)
    IDmodificar.pack()
    Nombremodificar=Entry(modificarCliente)
    Nombremodificar.insert(0,NombreMod)
    Nombremodificar.pack()
    etiqueta = Label(modificarCliente,text="Ingrese Email actualizado")
    etiqueta.pack()
    Emailmodificar=Entry(modificarCliente)
    Emailmodificar.insert(0,EmailMod)
    Emailmodificar.pack()
    
    boton=Button(modificarCliente,text="Modificar Cliente",command=lambda: ModCliente(Nombremodificar,IDmodificar,Emailmodificar))
    boton.pack(side=TOP)
    root.wait_window(modificarCliente)
    
def ModCliente(Nombremodificar,IDmodificar,EmailCliente):
    ID=int(IDmodificar.get())
    nombre=Nombremodificar.get()
    email = EmailCliente.get()
    for h in range(0,len(lstClientes)):
        if lstClientes[h].IDCliente== ID:
            lstClientes[h].NombreCliente = nombre
            lstClientes[h].EmailCliente = email
            
            
            messagebox.showinfo(message="Cliente modificado", title="Modificado")


def ClienteCarga(listbox):
    VentanaCargaCliente()
    listbox.delete(0,'end')
    for i in range (0,len(lstClientes)):
        if lstClientes[i].IDCliente != 0:
            listbox.insert(i,lstClientes[i])
        
def VentanaCargaCliente():
    Vcargacliente = Toplevel()
    Vcargacliente.title("Lista de Clientes")
    Vcargacliente.grab_set()
    Vcargacliente.geometry("380x300")
    Vcargacliente.configure(background="white")
    etiqueta_text= Label(Vcargacliente,text="Agregar nombre del Cliente",bg="white")
    etiqueta_text.pack(side=TOP)
    valor= " "
    nombrecliente=Entry(Vcargacliente,textvariable = valor)
    nombrecliente.pack(side=TOP)
    Etiqueta= Label(Vcargacliente,text="Agregar Email del cliente",bg="white")
    Etiqueta.pack(side=TOP)
    emailcliente=Entry(Vcargacliente)
    emailcliente.pack(side=TOP)
    boton=Button(Vcargacliente,text="Cargar Nuevo Cliente",command=lambda:CargarCliente(nombrecliente,valor,emailcliente))
    boton.pack(side=TOP)
    root.wait_window(Vcargacliente)
    
def CargarCliente(nombrecliente,valor,emailcliente):
    _nombre=nombrecliente.get()
    _email = emailcliente.get()
    lstClientes.append(Clientes(len(lstClientes)+1,_nombre,_email))    
    valor= " "
    nombrecliente.delete(0, 'end')
    emailcliente.delete(0,'end')
    messagebox.showinfo(message="Cliente Cargado", title="Cargado")
    return
        
    
def BorrarCliente(EntryID,listbox):
    try:
       ID=int(EntryID.get())
       for j in range(0,len(lstClientes)):
          if lstClientes[j].IDCliente == ID and lstClientes[j].IDCliente != 0:
            BajaCliente(ID)
            break
       else:
         messagebox.showwarning("Atención","ID No existente")
    except:
        messagebox.showerror("Atención","ID Invalida")
    listbox.delete(0,'end')
    for i in range (0,len(lstClientes)):
        if lstClientes[i].IDCliente != 0:
            listbox.insert(i,lstClientes[i])
    EntryID.delete(0, 'end')
    
def BajaCliente(ID):    
    for j in range(0,len(lstClientes)):
        if lstClientes[j].IDCliente== ID:
            lstClientes[j]=Clientes(0,"","")
            messagebox.showinfo(message="Cliente eliminado", title="Eliminado")
            return

def ValidacionVendedor(IDVendedorEntry):
       try:
            IDv = int(IDVendedorEntry.get())
            for i in range(0,len(lstVendedor)):
                    if lstVendedor[i].IDVendedor == IDv:
                        messagebox.showinfo("Validacion","El ID es Valido")
                        IDVendedorEntry.config(state=DISABLED)
                        
                        
                        return
            else:
                messagebox.showwarning("Validacion","El ID no invalido")
                V1 = False
                return
       except:
          messagebox.showerror("Validacion","El ID debe ser numerico")
          V1 = False
          
    
    

def ValidacionLocal(IDLocalEntry):
    try:
        IDl = int(IDLocalEntry.get())
        for j in range(0,len(lstLocales)):
            if IDl == lstLocales[j].IDlocal:
                messagebox.showinfo("Validacion","El ID es Valido")
                IDLocalEntry.config(state=DISABLED)
                return
        else:
             messagebox.showwarning("Validacion","El ID no Existe")
             return 
    except:
        messagebox.showerror("Validacion","El ID debe ser numerico")
        return
    
def ValidarCliente(IDClienteEntry,NombreClienteEntry):
    try:
       IDc = int(IDClienteEntry.get())
       for i in range(0,len(lstClientes)):
           if IDc == lstClientes[i].IDCliente:
               nombre = lstClientes[i].NombreCliente
               NombreClienteEntry.delete(0,'end')
               NombreClienteEntry.insert(0,nombre)
               IDClienteEntry.config(state=DISABLED)
               NombreClienteEntry.config(state=DISABLED)
               messagebox.showinfo("Validacion","El ID es Valido")
               return
       else:
            messagebox.showwarning("Validacion","El ID no Existe")
            NombreClienteEntry.delete(0,'end')
            return
    except:
        messagebox.showwarning("Validacion","El ID debe ser numerico")
        NombreClienteEntry.delete(0,'end')
        return
    
def VerificacionProducto(IDProductoEntry,CantidadEntry,PrecioEntry):
    try:
        IDp = int(IDProductoEntry.get())
        C = int(CantidadEntry.get())
        for j in range(0,len(lstProductos)):
            if IDp == lstProductos[j].IDproducto:
                Precio = lstProductos[j].Precio
                PrecioEntry.delete(0,'end')
                if C <= lstProductos[j].StockActual and C >= 0 and C != 0:
                 messagebox.showinfo("Validacion","ID: Valido \nCantidad: Valida ")
                 PrecioEntry.insert(0,Precio)
              
                 
                 return
        else:
            messagebox.showwarning("Validacion","El ID o la cantidad son incorrectos")
            PrecioEntry.delete(0,'end')
    except:
        messagebox.showerror("Validacion","El ID y la cantidad deben ser numericos")
        PrecioEntry.delete(0,'end')
               
def Facturar(IDFacEntry,FechaEntry,IDVendedorEntry,IDLocalEntry,IDClienteEntry,IDProductoEntry,CantidadEntry,NombreClienteEntry,listbox,PrecioEntry):
    total=0
    global NroFac
    
    
    facid=int(IDFacEntry.get())
    fecha=FechaEntry.get()
    venid=int(IDVendedorEntry.get())
    locid=int(IDLocalEntry.get())
    cliid=int(IDClienteEntry.get())
    nombrecli=NombreClienteEntry.get()
    
    for i in range (0,len(lstDetalleFacturas)):
        if lstDetalleFacturas[i].NroFactura == facid:
            precio = lstDetalleFacturas[i].PrecioUnitario
            cantidad = lstDetalleFacturas[i].Cantidad
            suma= precio * cantidad
            total = total + suma
        for j in range (0,len(lstProductos)):
            if lstProductos[j].IDproducto == lstDetalleFacturas[i].IdProducto:
            
                lstProductos[j].StockActual = lstProductos[j].StockActual - lstDetalleFacturas[i].Cantidad
               
    lstFacturas.append(DatosFacturas(facid,fecha,venid,locid,cliid,nombrecli,total))
    
 
    
    NroFac += 1
    IDFacEntry.config(state=NORMAL)
    IDFacEntry.delete(0,'end')                   
    IDFacEntry.insert(0,NroFac)
    IDFacEntry.config(state=DISABLED)
    IDVendedorEntry.config(state=NORMAL)
    IDLocalEntry.config(state=NORMAL)
    IDClienteEntry.config(state=NORMAL)
    NombreClienteEntry.config(state=NORMAL)
    IDVendedorEntry.delete(0, 'end')
    IDLocalEntry.delete(0, 'end')
    IDClienteEntry.delete(0, 'end')
    NombreClienteEntry.delete(0, 'end')
    IDProductoEntry.delete(0, 'end')
    CantidadEntry.delete(0, 'end')
    IDFacEntry.delete(0,'end')
    PrecioEntry.delete(0,'end')
    listbox.delete(0,'end')
    messagebox.showinfo("Información","Subida Correcta")
    
    
    return 
    
    
            
            
    









def Factura():
    
    global NroFac
    global fecha
    global NroLocal
    
    #Busca ID del local
    for j in range(0,len(lstFacturas)):
     if lstFacturas[j].NroFactura == NroFac - 1:
       NroLocal = lstFacturas[j].IdLocal
       break
    
    
    V = Toplevel()
    V.geometry("500x650")
    V.config(bg="white")
    titulo = Font(family="Times New Roman",size=35)
    sub = Font(family="Times New Roman",size=20)
    Cuerpo = Font(family="cursive",size=15)
    
    LNombre = Label(V,text="Zapateria",bg="white")
    LNombre.config(font=titulo)
    LNombre.place(x=10,y=0)
    LNombre.pack(fill=X)
    
    Direccion = Label(V,text="Calle Falsa 123",bg="white")
    Direccion.config(font=Cuerpo)
    Direccion.place(x=10,y=60)
    
    #Busca Nombre Local
    
    for i in range(0,len(lstLocales)):
        if lstLocales[i].IDlocal == NroLocal:
            L = lstLocales[i].NombreLocal
            break
        
    NombreCiudad = L
    NomCiu = StringVar()
    NomCiu.set(NombreCiudad)
    

    ImprimirCiudad = Label(V,textvariable=NomCiu,bg="white")
    ImprimirCiudad.config(font=Cuerpo)
    ImprimirCiudad.place(x=10,y=90)
    
    
    Zip = Label(V,text="7167",bg="white")
    Zip.config(font=Cuerpo)
    Zip.place(x=10,y=120)
    
    Tel = Label(V,text="12345667",bg="white")
    Tel.config(font=Cuerpo)
    Tel.place(x=180,y=60)
    
    Email = Label(V,text="Zapateria@outlook.com",bg="white")
    Email.config(font=Cuerpo)
    Email.place(x=180,y=90)
    
    Web = Label(V,text="Zapateria.com",bg="white")
    Web.config(font=Cuerpo)
    Web.place(x=180,y=120)
    
    DatosCliente = Label(V,text="Datos del Cliente",bg="white")
    DatosCliente.config(font=Cuerpo)
    DatosCliente.place(x=10,y=170)
    
    
    #Datos del Cliente
    for j in range(0,len(lstFacturas)):
      if lstFacturas[j].NroFactura == NroFac - 1: 
        ClienteID = lstFacturas[j].IdCliente
        break
    
    #Busca Datos Cliente
    for i in range(0,len(lstClientes)):
        if lstClientes[i].IDCliente == ClienteID:
            NombreCli = lstClientes[i].NombreCliente
            EmailCli = lstClientes[i].EmailCliente
            break
        
    N = NombreCli
    N_ = StringVar()
    N_.set(N)
    
    E = EmailCli
    E_ = StringVar()
    E_.set(E)
    
    ImprimirCliente = Label(V,textvariable=N_,bg="white")
    ImprimirCliente.config(font=Cuerpo)
    ImprimirCliente.place(x=10,y=200)
    
    ImprimirEmail = Label(V,textvariable=E_,bg="white")
    ImprimirEmail.config(font=Cuerpo)
    ImprimirEmail.place(x=10,y=230)
    
    
    Fac = Label(V,text="Factura Nº",bg="white")
    Fac.config(font=Cuerpo)
    Fac.place(x=10,y=380)
    
    N = NroFac - 1 
    N_ = IntVar()
    N_.set(N)
    
    Nro = Label(V,textvariable=N_,bg="white")
    Nro.config(font=Cuerpo)
    Nro.place(x=45,y=410)
    
    FacFecha = Label(V,text="Fecha",bg="white")
    FacFecha.config(font=Cuerpo)
    FacFecha.place(x= 10,y=470)
    
    F = fecha
    F_ = IntVar()
    F_.set(F)
    
    ImprimirFecha = Label(V,textvariable=F_,bg="white")
    ImprimirFecha.config(font=Cuerpo)
    ImprimirFecha.place(x=10,y=500)
    
    MontoTotal = Label(V,text="Total $:",bg="white")
    MontoTotal.config(font=Cuerpo)
    MontoTotal.place(x=300,y=470)
    
    for i in range(0,len(lstFacturas)):
        Monto = lstFacturas[i].ImporteTotal
        
    T = Monto
    T_ = IntVar()
    T_.set(T)
    
    ImprimirTotal = Label(V,textvariable=T_,bg="white")
    ImprimirTotal.config(font=Cuerpo)
    ImprimirTotal.place(x=300,y=500)
    
    listbox = Listbox(V,width=50,height=15)
    
    listbox.place(x=180,y=180)
    
    for j in range(0,len(lstDetalleFacturas)):
        if lstDetalleFacturas[j].NroFactura == NroFac -1 :
            listbox.insert(j,lstDetalleFacturas[j])
                    
    
    
    
            
            
    
    
    
    
    
def AgregaraLista(IDProductoEntry,CantidadEntry,IDFacEntry,PrecioEntry,listbox):
    CantiProd = int(CantidadEntry.get())
    Pr = int(PrecioEntry.get())
        
    IDProd = int(IDProductoEntry.get())
    ID = int(IDFacEntry.get())
    Pr = int(PrecioEntry.get())
    ImporTot = Pr * CantiProd
    
    lstDetalleFacturas.append(DetalleFacturas(ID,IDProd,CantiProd,Pr)) 
                    

                
    listbox.delete(0,'end')
    for i in range (0,len(lstDetalleFacturas)):
        if lstDetalleFacturas[i].NroFactura == ID:
            listbox.insert(i,lstDetalleFacturas[i])
    
    CantidadEntry.delete(0,'end')
    IDProductoEntry.delete(0,'end')
    PrecioEntry.delete(0,'end')
    
    CantidadEntry.config(state=NORMAL)
    IDProductoEntry.config(state=NORMAL)
    PrecioEntry.config(state=NORMAL)
                


def PantallaFacturacion():
    Facturacion =Toplevel()
    Facturacion.title("Facturacion")
    Facturacion.geometry("500x500")
    Facturacion.configure(background="white")
    IDFacLabel= Label(Facturacion,text="Nº Factura",bg="white")
    IDFacEntry=Entry(Facturacion,justify="center",bg="light green")
    IDFacEntry.insert(0,len(lstFacturas)+1)
    
    IDFacEntry.config(state=DISABLED)
    
    IDFacLabel.place(x=15, y=20, width=90, height=30)
    IDFacEntry.place(x=20, y=50, width=100, height=30)
    fecha = time.strftime("%d/%m/%y")
    FechaLabel= Label(Facturacion,text="Fecha",bg="white")
    FechaEntry=Entry(Facturacion,justify="center",bg="light green")
    FechaEntry.insert(0,fecha)
    FechaEntry.config(state=DISABLED)
    FechaLabel.place(x=340, y=20, width=80, height=30)
    FechaEntry.place(x=360, y=50, width=100, height=30)
    
    IDVendedorLabel= Label(Facturacion,text="ID Vendedor",bg="white")
    IDVendedorEntry=Entry(Facturacion,justify="center",bg="light green")
    IDVendedorLabel.place(x=20, y=85, width=85, height=30)
    IDVendedorEntry.place(x=20, y=115, width=100, height=30)
    VendedorCompBtn=Button(Facturacion,text="Comprobar",command=lambda:ValidacionVendedor(IDVendedorEntry))
    VendedorCompBtn.place(x=130, y=115, width=100, height=30)
    IDLocalLabel= Label(Facturacion,text="ID De Local",bg="white")
    IDLocalEntry=Entry(Facturacion,justify="center",bg="light green")
    IDLocalLabel.place(x=250, y=85, width=80, height=30)
    IDLocalEntry.place(x=250, y=115, width=100, height=30)
    LocalCompBtn=Button(Facturacion,text="Comprobar",command=lambda:ValidacionLocal(IDLocalEntry))
    LocalCompBtn.place(x=360, y=115, width=100, height=30)
    
    IDClienteLabel= Label(Facturacion,text="ID De Cliente",bg="white")
    IDClienteEntry=Entry(Facturacion,justify="center",bg="light green")
    IDClienteLabel.place(x=15, y=150, width=100, height=30)
    IDClienteEntry.place(x=20, y=180, width=100, height=30)
    ClienteCompBtn=Button(Facturacion,text="Comprobar",command=lambda:ValidarCliente(IDClienteEntry,NombreClienteEntry))
    ClienteCompBtn.place(x=130, y=180, width=100, height=30)
    NombreClienteLabel= Label(Facturacion,text="Nombre Cliente",bg="white")
    NombreClienteEntry=Entry(Facturacion,justify="center",bg="light green")
    NombreClienteLabel.place(x=250, y=150, width=100, height=30)
    NombreClienteEntry.place(x=250, y=180, width=120, height=30)
    
    IDProductoLabel= Label(Facturacion,text="ID Producto",bg="white")
    IDProductoEntry=Entry(Facturacion,justify="center",bg="light green")
    IDProductoLabel.place(x=15, y=250, width=95, height=30)
    IDProductoEntry.place(x=20, y=280, width=100, height=30)
    CantidadLabel= Label(Facturacion,text="Cantidad",bg="white")
    CantidadEntry=Entry(Facturacion,justify="center",bg="light green")
    CantidadLabel.place(x=140, y=250, width=85, height=30)
    CantidadEntry.place(x=150, y=280, width=100, height=30)
    PrecioLabel = Label(Facturacion,text="Precio",bg="white")
    PrecioLabel.place(x=240, y=250, width=95, height=30)
    PrecioEntry = Entry(Facturacion,justify="center",bg="light green")
    PrecioEntry.place(x=260, y=280, width=100, height=30)
    CargaCompBtn=Button(Facturacion,text="Comprobar",command=lambda:VerificacionProducto(IDProductoEntry,CantidadEntry,PrecioEntry))
    CargaCompBtn.place(x=380, y=280, width=100, height=30)
    DetalleLabel= Label(Facturacion,text="Lista Productos: ")
    DetalleLabel.place(x=50, y=320, width=100, height=30)
    listbox = Listbox(Facturacion)
    listbox.place(x=20, y=345 ,width=250, height=150)
    listbox.delete(0,'end')
    for i in range (0,len(lstDetalleFacturas)):
        listbox.insert(i,lstDetalleFacturas[i])
    listbox.delete(0,'end')
    
    AgregarALista=Button(Facturacion,text="Agregar a la lista",command=lambda:AgregaraLista(IDProductoEntry,CantidadEntry,IDFacEntry,PrecioEntry,listbox))
    AgregarALista.place(x=350,y=340,width=100, height=30)
    
    ListoCompBtn=Button(Facturacion,text="Facturar",command=lambda:Facturar(IDFacEntry,FechaEntry,IDVendedorEntry,IDLocalEntry,IDClienteEntry,IDProductoEntry,CantidadEntry,NombreClienteEntry,listbox,PrecioEntry))
    ListoCompBtn.place(x=350, y=400, width=100, height=30)


    MostrarFacBtn=Button(Facturacion,text="Mostrar Factura",command=lambda:Factura())
    MostrarFacBtn.place(x=350, y=460, width=100, height=30)
    #MostrarFacBtn.config(state=DISABLED)

def CargarDatos():
    
    with open('Productos.csv', 'r') as productos:        
        for linea in productos:
            a= linea.split(';')
            lstProductos.append(Producto(int(a[0]), a[1], int(a[2]), int(a[3]), int(a[4])))
    with open('categorias.csv', 'r') as categorias:        
        for linea in categorias:
            a= linea.split(';')
            lstCategorias.append(Categoria(int(a[0]),a[1]))
            
    with open('locales.csv', 'r') as locales:        
        for linea in locales:
            a= linea.split(';')
            lstLocales.append(Locales(int(a[0]), a[1]))
            
    with open('vendedores.csv', 'r') as vendedores:        
        for linea in vendedores:
            a= linea.split(';')
            lstVendedor.append(Vendedores(int(a[0]), a[1] ))

    with open('clientes.csv', 'r') as clientes:        
        for linea in clientes:
            a= linea.split(';')
            lstClientes.append(Clientes(int(a[0]), a[1], a[2]))
    
    with open('facturas.csv', 'r') as facturas:        
        for linea in facturas:
            a= linea.split(';')
            lstFacturas.append(DatosFacturas(int(a[0]), a[1], int(a[2]),int(a[3]),int(a[4]),a[5],int(a[6])))
    
    with open('detalleFacturas.csv', 'r') as detalleFacturas:        
        for linea in detalleFacturas:
            a= linea.split(';')
            lstDetalleFacturas.append(DetalleFacturas(int(a[0]), int(a[1]),int(a[2]),int(a[3])))
    
    
def PantallaPrincipal():
    root.title("Zapateria")
    root.geometry("400x300")
    root.configure(background="white")


    menubar = Menu(root)
    root.config(menu=menubar)
    
    MenuVendedor = Menu(menubar, tearoff=0)
    MenuVendedor.add_command(label="ABM Vendedores",command=VentanaABMVendedor)
    MenuVendedor.add_separator()
    MenuVendedor.add_command(label="Salir", command=root.quit)

    MenuLocal = Menu(menubar, tearoff=0)
    MenuLocal.add_command(label="ABM Locales",command=VentanaABMlocales)
    MenuLocal.add_separator()
    MenuLocal.add_command(label="Salir", command=root.quit)

    MenuCategoria = Menu(menubar, tearoff=0)
    MenuCategoria.add_command(label="ABM Categorias", command=VentanaABMCategorias)
    MenuCategoria.add_separator()
    MenuCategoria.add_command(label="Salir", command=root.quit)
    
    MenuProducto = Menu(menubar, tearoff=0)
    MenuProducto.add_command(label="ABM Producto", command=VentanaABMProducto)
    MenuProducto.add_separator()
    MenuProducto.add_command(label="Salir", command=root.quit)
    
    MenuCliente = Menu(menubar, tearoff=0)
    MenuCliente.add_command(label="ABM Clientes",command=VentanaABMCliente)
    MenuCliente.add_separator()
    MenuCliente.add_command(label="Salir", command=root.quit)
    
    MenuFacturacion = Menu(menubar, tearoff=0)
    MenuFacturacion.add_command(label="Facturacion",command=PantallaFacturacion)
    MenuFacturacion.add_separator()
    MenuFacturacion.add_command(label="Salir", command=root.quit)
    
    
    CargarDatos()
    


    menubar.add_cascade(label="Vendedores", menu=MenuVendedor )
    menubar.add_cascade(label="Locales", menu=MenuLocal)
    menubar.add_cascade(label="Categoria", menu=MenuCategoria )
    menubar.add_cascade(label="Producto", menu=MenuProducto )
    menubar.add_cascade(label="Clientes", menu=MenuCliente )
    menubar.add_cascade(label="Facturacion", menu=MenuFacturacion )



    root.mainloop()   
    
root = Tk()
PantallaPrincipal()
