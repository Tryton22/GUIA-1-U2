from typing import TextIO
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Faltaron unas par de cosas (como agregar función al boton aceptar de la ventana de diálogo y que se viera la suma) y el texto tiene que ser sin espacios.

class Ventana_principal():

    def __init__(self):

        builder = Gtk.Builder()
        builder.add_from_file("ejemplo.ui")
        
        # Configuramos ventana principal.
        ventana = builder.get_object("principal")
        ventana.maximize()
        ventana.set_title("Ventana Guía 1 Programación")
        ventana.connect("destroy", Gtk.main_quit)

        # Agregamos nombre a los label de los cuadros de texto.
        label = builder.get_object("etiqueta")
        label.set_label("Ingrese algún texto:")
        label_1 = builder.get_object("etiqueta1")
        label_1.set_label("Ingrese algún texto:")

        # Botones de la ventana principal.
        boton = builder.get_object("boton")
        boton.connect("clicked", self.abrir_dialogo)
        boton.set_label("Aceptar")
        boton_1 = builder.get_object("boton1")
        boton_1.connect("clicked", self.limpiar_datos)
        boton_1.set_label("Reset")

        # Entradas de texto.
        self.entrada = builder.get_object("entrada")
        self.entrada.connect("activate", self.activate_entrada)
        self.entrada_1 = builder.get_object("entrada1")
        self.entrada_1.connect("activate", self.activate_entrada)

        # Label sumatoria.
        self.label_resultado = builder.get_object("resultado")

        ventana.show_all()

    # Funcíon que realiza la sumatoria.
    def activate_entrada(self, enter=None):
        # print(self.entrada.get_text())
        cadena = self.entrada.get_text()
        # print(cadena.isalpha())
        # Si es True, es cadena de netamente letras (sin espacios), si sale False, es cadena de números o mezcla.
        # No se que mas poner para que me transforme en número el texto escrito.

        if cadena.isalpha() == True:
            cadena = self.entrada.get_text_length()
            print(cadena)
        else:
            try:
                cadena = int(cadena)
                print(cadena)
            except ValueError:
                print("Ingrese algo válido.")

        # print(self.entrada_1.get_text())
        cadena_1 = self.entrada_1.get_text()

        if cadena_1.isalpha() == True:
            cadena_1 = self.entrada_1.get_text_length()
            print(cadena_1)
        else:
            try:
                cadena_1 = int(cadena_1)
                print(cadena_1)
            except ValueError:
                print("Ingrese algo válido.")

        # Realiza la suma.
        self.label_resultado.set_text(str(cadena + cadena_1))

    # Función que resetea los datos ingresados.
    def limpiar_datos(self, btn=None):
        # print("Click")
        self.entrada.set_text("")
        self.entrada_1.set_text("")
        self.label_resultado.set_text("Resultado Sumatoria")
    
    # Función que abre la ventana de diálogo.
    def abrir_dialogo(self, btn=None):
        ventana_dialogo = Ventana_dialogo()
        ventana_dialogo.dialogo.run()

class Ventana_dialogo():

    def __init__(self):

        builder = Gtk.Builder()
        builder.add_from_file("ejemplo.ui")

        self.dialogo = builder.get_object("dialog")

        # Botones de la ventana de diálogo.
        boton = builder.get_object("btn")
        boton.set_label("Aceptar")
        boton1 = builder.get_object("btn2")
        boton1.connect("clicked", self.hacer_nada)
        boton1.set_label("Cancelar") 

    # Función que cierra la ventana de dialogo y no hace nada más.
    def hacer_nada(self, btn=None):
        self.dialogo.close()

if __name__ == "__main__":
    # Llama a la función principal.
    Ventana_principal()
    Gtk.main()