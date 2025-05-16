import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

## Creamos la clase animal usando el constructor __init__ y sus atributos dentro del self
class Animal:
    def __init__(self, nombre, tipo_alimentacion):
        self.nombre = nombre
        self.tipo_alimentacion = tipo_alimentacion

    def __str__(self):
        return f"Nombre: {self.nombre}, Alimentación: {self.tipo_alimentacion}"

## Se crea el organizador del animal
class OrganizadorAnimalesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Organizador de Animales") ## Titulo del programa

        self.lista_animales = [] ## Inicializa la lista vacía llamada "lista_animales" para almacenar los objetos Animal

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")

        self.frame_agregar = ttk.Frame(self.notebook)
        self.frame_mostrar = ttk.Frame(self.notebook)

        self.notebook.add(self.frame_agregar, text='Agregar Animal') ## Boton de agregar
        self.notebook.add(self.frame_mostrar, text='Mostrar Animales') ## Boton de mostrar

        ## Llama a los métodos para crear la interfaz de cada pestaña
        self._crear_interfaz_agregar()
        self._crear_interfaz_mostrar()

## Interfaz del programa para agregar animales
    def _crear_interfaz_agregar(self):
        ttk.Label(self.frame_agregar, text="Nombre del animal:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre = ttk.Entry(self.frame_agregar)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.frame_agregar, text="Tipo de alimentación:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.combo_alimentacion = ttk.Combobox(self.frame_agregar, values=["Herbívoro", "Carnívoro", "Omnívoro"])  ## Creamos el menu desplegable
        self.combo_alimentacion.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.combo_alimentacion.set("Herbívoro") # Valor por defecto, aparece como primera opcion

        btn_agregar = ttk.Button(self.frame_agregar, text="Agregar", command=self._agregar_animal) ## Botones
        btn_agregar.grid(row=2, column=0, columnspan=2, pady=10)

        self.frame_agregar.columnconfigure(1, weight=1)

## Interfaz del programa para mostrar animales
    def _crear_interfaz_mostrar(self):
        ## Etiqueta para indicar la selección del tipo de animales a mostrar
        self.label_mostrar = ttk.Label(self.frame_mostrar, text="Seleccione el tipo de animales a mostrar:")
        ## Organiza la etiqueta
        self.label_mostrar.pack(pady=5)

        ## Menú desplegable para seleccionar el tipo de animales a mostrar
        self.combo_mostrar = ttk.Combobox(self.frame_mostrar, values=["todos", "herbívoro", "carnívoro", "omnívoro"])
        self.combo_mostrar.pack(pady=5)
        self.combo_mostrar.set("todos")

        btn_mostrar = ttk.Button(self.frame_mostrar, text="Mostrar", command=self._mostrar_animales)
        btn_mostrar.pack(pady=10)

        ## Creación del widget Treeview (tabla) para mostrar los animales
        self.tree = ttk.Treeview(self.frame_mostrar, columns=("Nombre", "Alimentación"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Alimentación", text="Alimentación")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

## Método para agregar un nuevo animal a la lista
    def _agregar_animal(self):
        nombre = self.entry_nombre.get()
        tipo_alimentacion = self.combo_alimentacion.get().lower() ## Convertimos a minúsculas para consistencia

        if nombre and tipo_alimentacion in ["herbívoro", "carnívoro", "omnívoro"]: ## Comparamos en minúsculas
            animal = Animal(nombre, tipo_alimentacion)
            self.lista_animales.append(animal) ## Aquí se añade el animal a la lista
            messagebox.showinfo("Éxito", f"{nombre} ha sido agregado.")
            self.entry_nombre.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese un nombre y un tipo de alimentación válido.")

## Método para mostrar los animales según el tipo seleccionado
    def _mostrar_animales(self):
        tipo_seleccionado = self.combo_mostrar.get()
        self._actualizar_lista_mostrada(tipo_seleccionado)

## Método para actualizar la tabla de animales mostrada
    def _actualizar_lista_mostrada(self, tipo="todos"):
        # Limpiar la tabla actual
        for item in self.tree.get_children():
            self.tree.delete(item)

        animales_a_mostrar = self.lista_animales
        if tipo != "todos":
            ## Filtramos la lista de animales según el tipo seleccionado (en minúsculas)
            animales_a_mostrar = [animal for animal in self.lista_animales if animal.tipo_alimentacion == tipo]

        for animal in animales_a_mostrar:
            self.tree.insert("", tk.END, values=(animal.nombre, animal.tipo_alimentacion))

def main():
    root = tk.Tk()
    app = OrganizadorAnimalesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()