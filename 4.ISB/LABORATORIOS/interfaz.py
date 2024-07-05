import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ellip, filtfilt
from hl7apy import core
import os
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


# Función para verificar el código y la contraseña
def verificar_credenciales():
    codigo = entry_codigo.get()
    contrasena = entry_contrasena.get()

    # Aquí puedes implementar la verificación de credenciales
    if codigo == "Camila" and contrasena == "1234":
        mostrar_menu_principal()
    else:
        messagebox.showerror("Error", "Código o contraseña incorrectos")


# Función para mostrar el menú principal
def mostrar_menu_principal():
    for widget in ventana.winfo_children():
        widget.destroy()

    boton_nuevo_paciente = tk.Button(ventana, text="Nuevo Paciente", command=mostrar_formulario_paciente, width=20)
    boton_nuevo_paciente.pack(pady=10)

    boton_buscar_paciente = tk.Button(ventana, text="Buscar Paciente", command=buscar_paciente, width=20)
    boton_buscar_paciente.pack(pady=10)
    
def buscar_paciente():
    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="ID Paciente:", width=10).pack(pady=5)
    entry_buscar_id = tk.Entry(ventana, width=30)
    entry_buscar_id.pack(pady=5)

    def realizar_busqueda():
        id_paciente = entry_buscar_id.get()
        # Aquí puedes implementar la búsqueda y mostrar los detalles del paciente
        messagebox.showinfo("Búsqueda de Paciente", f"Paciente encontrado con ID: {id_paciente}")

    boton_buscar = tk.Button(ventana, text="Buscar", command=realizar_busqueda, width=20)
    boton_buscar.pack(pady=20)

    boton_regresar = tk.Button(ventana, text="Regresar", command=mostrar_menu_principal, width=20)
    boton_regresar.pack(pady=5)


# Función para mostrar el formulario de nuevo paciente
def mostrar_formulario_paciente():
    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="Nombre:", width=10).pack(pady=5)
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.pack(pady=5)

    tk.Label(ventana, text="Apellido:", width=10).pack(pady=5)
    entry_apellido = tk.Entry(ventana, width=30)
    entry_apellido.pack(pady=5)

    tk.Label(ventana, text="Edad:", width=10).pack(pady=5)
    entry_edad = tk.Entry(ventana, width=30)
    entry_edad.pack(pady=5)

    tk.Label(ventana, text="Sexo:", width=10).pack(pady=5)
    entry_sexo = tk.Entry(ventana, width=30)
    entry_sexo.pack(pady=5)

    tk.Label(ventana, text="ID Paciente:", width=10).pack(pady=5)
    entry_id_paciente = tk.Entry(ventana, width=30)
    entry_id_paciente.pack(pady=5)

    tk.Label(ventana, text="Dirección:", width=10).pack(pady=5)
    entry_direccion = tk.Entry(ventana, width=30)
    entry_direccion.pack(pady=5)

    tk.Label(ventana, text="Doctor:", width=10).pack(pady=5)
    entry_doctor = tk.Entry(ventana, width=30)
    entry_doctor.pack(pady=5)

    def guardar_paciente():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        edad = entry_edad.get()
        sexo = entry_sexo.get()
        id_paciente = entry_id_paciente.get()
        direccion = entry_direccion.get()
        doctor = entry_doctor.get()

        # Crear mensaje HL7
        hl7_message = core.Message("ADT_A01")  # Utilizar un tipo de mensaje válido

        # Segmento MSH
        msh_segment = hl7_message.add_segment("MSH")
        msh_segment.msh_1 = "|"
        msh_segment.msh_2 = "^~\&"
        msh_segment.msh_3 = "SendingApp"
        msh_segment.msh_4 = "SendingFacility"
        msh_segment.msh_5 = "ReceivingApp"
        msh_segment.msh_6 = "ReceivingFacility"
        msh_segment.msh_7 = datetime.now().strftime("%Y%m%d%H%M%S")
        msh_segment.msh_9 = "ADT^A01"
        msh_segment.msh_10 = "MSG00001"
        msh_segment.msh_11 = "P"
        msh_segment.msh_12 = "2.5"

        # Segmento PID
        pid_segment = hl7_message.add_segment("PID")
        pid_segment.pid_1 = "1"  # Set ID
        pid_segment.pid_3 = id_paciente  # Patient ID
        pid_segment.pid_5 = f"{apellido}^{nombre}"  # Patient Name
        pid_segment.pid_7 = edad  # Date of Birth
        pid_segment.pid_8 = sexo  # Sex
        pid_segment.pid_11 = direccion  # Patient Address

        # Segmento PV1
        pv1_segment = hl7_message.add_segment("PV1")
        pv1_segment.pv1_2 = "O"  # Patient Class
        pv1_segment.pv1_3 = "Location"  # Assigned Patient Location
        pv1_segment.pv1_7 = doctor  # Attending Doctor
        pv1_segment.pv1_19 = "Visit12345"  # Visit Number

        # Segmento OBR (Orden de Prueba)
        obr_segment = hl7_message.add_segment("OBR")
        obr_segment.obr_1 = "1"  # Set ID
        obr_segment.obr_2 = "Order12345"  # Placer Order Number
        obr_segment.obr_4 = "Holter Monitor"  # Universal Service ID

        # Crear carpeta "Pacientes" si no existe
        if not os.path.exists("Pacientes"):
            os.makedirs("Pacientes")

        # Guardar en un archivo .hl7 en la carpeta "Pacientes"
        with open(os.path.join("Pacientes", f"{id_paciente}.hl7"), 'w') as f:
            f.write(str(hl7_message))

        messagebox.showinfo("Guardado", "Información del paciente guardada en formato HL7")
        mostrar_opciones_agregar_datos()

    boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_paciente, width=20)
    boton_guardar.pack(pady=20)

    boton_regresar = tk.Button(ventana, text="Regresar", command=mostrar_menu_principal, width=20)
    boton_regresar.pack(pady=5)


# Función para mostrar la opción de seleccionar señal o regresar
def mostrar_opciones_agregar_datos():
    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="Seleccione el archivo de señal:", font=("Helvetica", 12)).pack(pady=10)

    # Obtener la ruta del archivo seleccionado
    def seleccionar_archivo():
        archivo_seleccionado = filedialog.askopenfilename(initialdir="/", title="Seleccione archivo de señal", filetypes=[("Text files", "*.txt")])
        if archivo_seleccionado:
            viewer.seleccionar_signal(archivo_seleccionado)

    boton_seleccionar = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo, width=20)
    boton_seleccionar.pack(pady=10)

    boton_regresar = tk.Button(ventana, text="Regresar", command=mostrar_menu_principal, width=20)
    boton_regresar.pack(pady=10)

# Funciones para crear y aplicar filtros elípticos
def elliptic_lowpass(cutoff, fs, order=5, rp=1, rs=40):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = ellip(order, rp, rs, normal_cutoff, btype='low', analog=False)
    return b, a

def elliptic_highpass(cutoff, fs, order=5, rp=1, rs=40):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = ellip(order, rp, rs, normal_cutoff, btype='high', analog=False)
    return b, a

def elliptic_bandstop(lowcut, highcut, fs, order=4, rp=1, rs=40):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = ellip(order, rp, rs, [low, high], btype='bandstop')
    return b, a

def apply_filter(data, filter_func, *args):
    b, a = filter_func(*args)
    # Verificar si el tamaño de los datos es suficiente para el filtro
    if len(data) > len(a):
        y = filtfilt(b, a, data)
        return y
    else:
        raise ValueError(f"El tamaño de los datos ({len(data)}) no es suficiente para el filtro (padlen = {len(a)})")

class SignalViewer(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Signal Viewer")
        self.geometry("800x600")

        self.signal_data = None
        self.filtered_signal = None
        self.fs = 1000.0
        self.current_window = 0
        self.window_size = int(20 * self.fs)

        self.init_ui()

    def init_ui(self):
        self.canvas = tk.Canvas(self, width=800, height=400)
        self.canvas.pack()

        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas_fig = FigureCanvasTkAgg(self.fig, self.canvas)
        self.canvas_fig.get_tk_widget().pack()

        frame_controls = tk.Frame(self)
        frame_controls.pack(pady=10)

        tk.Button(frame_controls, text="Exportar HL7", command=self.exportar_hl7).pack(padx=10)

    def seleccionar_signal(self, filepath):
        try:
            self.signal_data = np.loadtxt(filepath)
            self.apply_all_filters()
            self.current_window = 0
            self.plot_signal()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

    def plot_signal(self):
        if self.filtered_signal is None:
            return

        start = self.current_window * self.window_size
        end = start + self.window_size

        if end > len(self.filtered_signal):
            end = len(self.filtered_signal)

        self.ax.clear()
        self.ax.plot(self.filtered_signal[start:end], label="Señal Filtrada")
        self.ax.legend()
        self.canvas_fig.draw()

    def apply_all_filters(self):
        if self.signal_data is None:
            return
        try:
            # Aplicar filtro paso bajo
            temp_signal = apply_filter(self.signal_data, elliptic_lowpass, 30.0, self.fs)
            # Aplicar filtro paso alto
            temp_signal = apply_filter(temp_signal, elliptic_highpass, 0.5, self.fs)
            # Aplicar filtro de eliminación de banda
            self.filtered_signal = apply_filter(temp_signal, elliptic_bandstop, 49.0, 51.0, self.fs)
        except ValueError as e:
            messagebox.showerror("Error", f"No se pudo aplicar el filtro: {e}")
        self.plot_signal()

    def exportar_hl7(self):
        if self.filtered_signal is None:
            return

        # Crear un mensaje HL7 con los datos de la señal filtrada
        hl7_message = core.Message("ORU_R01")  # Utilizar un tipo de mensaje válido

        # Segmento MSH
        msh_segment = hl7_message.add_segment("MSH")
        msh_segment.msh_1 = "|"
        msh_segment.msh_2 = "^~\&"
        msh_segment.msh_3 = "SendingApp"
        msh_segment.msh_4 = "SendingFacility"
        msh_segment.msh_5 = "ReceivingApp"
        msh_segment.msh_6 = "ReceivingFacility"
        msh_segment.msh_7 = datetime.now().strftime("%Y%m%d%H%M%S")
        msh_segment.msh_9 = "ORU^R01"
        msh_segment.msh_10 = "MSG00001"
        msh_segment.msh_11 = "P"
        msh_segment.msh_12 = "2.5"

        # Segmento OBR
        obr_segment = hl7_message.add_segment("OBR")
        obr_segment.obr_1 = "1"
        obr_segment.obr_4 = "Holter Monitor"

        # Segmento OBX
        obx_segment = hl7_message.add_segment("OBX")
        obx_segment.obx_1 = "1"
        obx_segment.obx_2 = "ST"
        obx_segment.obx_3 = "Filtered Signal"
        obx_segment.obx_5 = "^".join(map(str, self.filtered_signal))

        # Crear carpeta "Señales" si no existe
        if not os.path.exists("Señales"):
            os.makedirs("Señales")

        # Guardar en un archivo .hl7 en la carpeta "Señales"
        with open(os.path.join("Señales", "filtered_signal.hl7"), 'w') as f:
            f.write(str(hl7_message))

        messagebox.showinfo("Guardado", "Señal filtrada exportada en formato HL7")   

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Pacientes")
ventana.geometry("400x600")  # Ajusta el tamaño inicial de la ventana

# Mostrar el nombre del software en grande
tk.Label(ventana, text="Sistema de Gestión de Pacientes", font=("Helvetica", 16)).pack(pady=20)

# Cargar y mostrar el logo
logo_img = Image.open("logo.jpg")  # Reemplaza con la ruta a tu logo
logo_img = logo_img.resize((200, 200), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(logo_img)
tk.Label(ventana, image=logo_image).pack(pady=10)
ventana.logo_image = logo_image  # Guardar referencia para evitar que la imagen se recoja por el recolector de basura


# Campos para el código y la contraseña
tk.Label(ventana, text="Código:", width=20).pack(pady=10)
entry_codigo = tk.Entry(ventana, width=40)
entry_codigo.pack(pady=10)

tk.Label(ventana, text="Contraseña:", width=20).pack(pady=10)
entry_contrasena = tk.Entry(ventana, show="*", width=40)
entry_contrasena.pack(pady=10)

# Botón para verificar el código y la contraseña
boton_verificar = tk.Button(ventana, text="Ingresar", command=verificar_credenciales, width=30)
boton_verificar.pack(pady=20)

# Crear una instancia de SignalViewer pero no abrirla todavía
viewer = SignalViewer()


