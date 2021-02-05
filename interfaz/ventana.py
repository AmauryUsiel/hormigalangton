import tkinter as tk


class Ventana:
    def __init__(self, titulo, tam):
        self.root = tk.Tk()
        self.root.title(titulo)
        self.root.geometry(tam)

        # crear el layout
        visor = tk.Frame(master=self.root, width=400, height=1000, bg="red")
        visor.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        controles = tk.Frame(master=self.root, width=300, height=1000, bg="blue")
        controles.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
        controles.pack_propagate(0)

        self.hacer_controles(controles)

    def hacer_controles(self, contenedor):
        label = tk.Label(master=contenedor, text="Panel de control")
        label.pack()

    def ejecutar(self):
        self.root.mainloop()