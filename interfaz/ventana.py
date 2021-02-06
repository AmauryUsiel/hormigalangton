import tkinter as tk
from tkinter import ttk


class Ventana:
    def __init__(self, titulo, tam):
        self.root = tk.Tk()
        self.root.title(titulo)
        self.root.geometry(tam)

        # crear el layout
        visor = tk.Frame(master=self.root, width=400, height=1000, bg="gray")
        visor.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        controles = tk.Frame(master=self.root, width=300, height=1000, bg="gray")
        controles.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        self.hacer_controles(controles)

    def hacer_controles(self, controles):

        contenedor = tk.Frame(master=controles, width=300, height=800, bg="blue")
        contenedor.pack(fill=tk.BOTH, side=tk.LEFT, expand=False, padx=20, pady=20)
        contenedor.pack_propagate(0)

        label = tk.Label(master=contenedor, text="Elegir variante")
        label.pack(side=tk.TOP, anchor=tk.NW)

        self.cmb_variante = ttk.Combobox(master=contenedor)
        self.cmb_variante.pack(side=tk.TOP, ancho=tk.NW)
        self.cmb_variante["values"] = ["Clasica", "4 hormigas"]

        botones = tk.Frame(master=contenedor, width=300, height=800, bg="green")
        botones.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        botones.pack_propagate(0)

        tk.Button(master=botones, text="Cargar hormigas").grid(
            row=0, column=0, padx=20, pady=20
        )
        tk.Button(master=botones, text="Cargar Matriz").grid(
            row=1, column=0, padx=20, pady=20
        )
        tk.Button(master=botones, text="Guardar configuracion").grid(
            row=0, column=1, padx=20, pady=20
        )
        tk.Button(master=botones, text="Guardar matriz").grid(
            row=1, column=1, padx=20, pady=20
        )
        tk.Button(master=botones, text="Estadisticas").grid(
            row=2, column=0, padx=20, pady=20
        )
        tk.Button(master=botones, text="Media y Varianza").grid(
            row=2, column=1, padx=20, pady=20
        )

        seccionhormigas = tk.Frame(
            master=contenedor, width=300, height=300, bg="violet"
        )
        seccionhormigas.pack(fill=tk.BOTH, expand=False, side=tk.TOP)

    def ejecutar(self):
        self.root.mainloop()