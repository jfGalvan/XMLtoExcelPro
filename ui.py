import os
import sys
import shutil
import base64
import tempfile
from datetime import datetime
from io import BytesIO
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from embedded_images import LOGO_BASE64, ICONO_BASE64
from xml_processor import process_directory

class XML2ExcelApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Convertidor de Facturas XML a Excel")
        self.geometry("900x600")
        self.minsize(900, 600)
        # Establecer icono de la ventana desde base64
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.ico') as tmp_icon:
                tmp_icon.write(base64.b64decode(ICONO_BASE64))
                icon_path = tmp_icon.name
            self.iconbitmap(icon_path)
        except Exception:
            pass
        self.colors = {
            'primary': '#1976d2',
            'secondary': ('#ff9800', '#ffa726'),
            'tertiary': ('#43a047', '#66bb6a'),
            'text_primary': '#222831'
        }
        self.selected_path = tk.StringVar()
        self.files_found = tk.IntVar(value=0)
        self.files_processed = tk.IntVar(value=0)
        self.processing = False
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # Panel principal (izquierdo)
        left_panel = ctk.CTkFrame(self, fg_color="#f5f5f5", corner_radius=20, width=340)
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(20,10), pady=20)
        left_panel.grid_rowconfigure(0, weight=1)
        left_panel.grid_columnconfigure(0, weight=1)

        # Centrado vertical de logo y título
        left_content = ctk.CTkFrame(left_panel, fg_color="transparent")
        left_content.grid(row=0, column=0, sticky="n")
        left_content.grid_rowconfigure(0, weight=1)
        left_content.grid_columnconfigure(0, weight=1)

        # Logo embebido desde base64
        try:
            from PIL import Image
            from customtkinter import CTkImage
            logo_img = Image.open(BytesIO(base64.b64decode(LOGO_BASE64)))
            logo_img = logo_img.resize((140, 140), Image.LANCZOS)
            logo_ctkimage = CTkImage(light_image=logo_img, size=(140, 140))
            logo_label = ctk.CTkLabel(left_content, image=logo_ctkimage, text="", fg_color="#f5f5f5")
            logo_label.grid(row=0, column=0, pady=(0,10))
        except Exception as e:
            logo_label = ctk.CTkLabel(left_content, text="XML2Excel", font=ctk.CTkFont(size=24, weight="bold"))
            logo_label.grid(row=0, column=0, pady=(0,10))

        # Título y subtítulo centrados
        title_label = ctk.CTkLabel(left_content, text="XML2Excel Pro", font=ctk.CTkFont(size=28, weight="bold"), text_color="#222831")
        title_label.grid(row=1, column=0, pady=(0,2))
        subtitle_label = ctk.CTkLabel(left_content, text="Convierte tus facturas XML a Excel\nde forma rápida y sencilla", font=ctk.CTkFont(size=16), text_color="#666")
        subtitle_label.grid(row=2, column=0, pady=(0,20))

        # Sección de selección de archivos
        archivos_label = ctk.CTkLabel(left_content, text="\uD83D\uDCC1 Selección de Archivos", font=ctk.CTkFont(size=18, weight="bold"), text_color="#222831")
        archivos_label.grid(row=3, column=0, pady=(0,10), sticky="w")

        # Botones con mismo ancho y separación
        button_width = 240
        seleccionar_btn = ctk.CTkButton(left_content, text="Seleccionar Directorio", width=button_width, height=40, fg_color="#1976d2", hover_color="#1565c0", text_color="#fff", font=ctk.CTkFont(size=16, weight="bold"), corner_radius=10, command=self.select_directory)
        seleccionar_btn.grid(row=4, column=0, pady=(0,10), sticky="ew")
        # Cuadro sombreado para mostrar la ruta seleccionada justo debajo del botón
        self.path_frame = ctk.CTkFrame(left_content, fg_color="#ededed", corner_radius=8)
        self.path_frame.grid(row=5, column=0, sticky="ew", padx=0, pady=(0,10))
        self.path_label = ctk.CTkLabel(self.path_frame, text="", font=ctk.CTkFont(size=14), text_color="#444444", anchor="w")
        self.path_label.pack(fill="x", padx=12, pady=6)
        # Reubicar los demás botones y secciones
        self.process_btn = ctk.CTkButton(left_content, text="⚡ Procesar facturas", width=button_width, height=40, command=self.process_files, fg_color=self.colors['secondary'][0], text_color="#fff", font=ctk.CTkFont(weight="bold"), state="disabled")
        self.process_btn.grid(row=6, column=0, pady=(0,10), sticky="ew")
        open_btn = ctk.CTkButton(left_content, text="Abrir carpeta de resultados", width=button_width, height=40, command=self.open_dest_folder, fg_color=self.colors['tertiary'][0], text_color="#fff", font=ctk.CTkFont(weight="bold"))
        open_btn.grid(row=7, column=0, pady=(0,10), sticky="ew")

    # Panel derecho con ancho fijo
        self.right_panel = ctk.CTkFrame(self, fg_color="#fff", corner_radius=20, width=340)
        self.right_panel.grid(row=0, column=1, sticky="nsew", padx=(10,20), pady=20)
        self.right_panel.grid_rowconfigure(0, weight=1)
        self.right_panel.grid_columnconfigure(0, weight=1)
        # Configurar proporción igual entre paneles
        self.grid_columnconfigure(0, weight=1, uniform="panel")
        self.grid_columnconfigure(1, weight=1, uniform="panel")
    # Crear todos los widgets del panel derecho
        self.create_right_panel(self.right_panel)

    def resource_path(self, relative_path):
        # Obtiene la ruta absoluta del recurso, compatible con PyInstaller.
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)



    def create_right_panel(self, parent):
        # Usar self.right_panel en lugar de parent directamente
        # Estado del sistema
        status_card = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        status_card.pack(fill="x", pady=(0, 15))
        status_title = ctk.CTkLabel(status_card, text="ℹ️ Estado del Sistema", font=ctk.CTkFont(size=15, weight="bold"), text_color="#000000", anchor="w")
        status_title.pack(anchor="w", padx=20, pady=(20, 10))
        status_frame = ctk.CTkFrame(status_card, fg_color="transparent")
        status_frame.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(status_frame, text="Estado:", anchor="w", text_color="#000000").pack(side="left")
        self.status_indicator = ctk.CTkLabel(status_frame, text="🟢 Listo", anchor="e", font=ctk.CTkFont(weight="bold"), text_color="#000000")
        self.status_indicator.pack(side="right")
        files_frame = ctk.CTkFrame(status_card, fg_color="transparent")
        files_frame.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(files_frame, text="Archivos encontrados:", anchor="w", text_color="#000000").pack(side="left")
        self.files_found_label = ctk.CTkLabel(files_frame, text="0", anchor="e", font=ctk.CTkFont(weight="bold"), text_color="#000000")
        self.files_found_label.pack(side="right")
        processed_frame = ctk.CTkFrame(status_card, fg_color="transparent")
        processed_frame.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(processed_frame, text="Procesados:", anchor="w", text_color="#000000").pack(side="left")
        self.files_processed_label = ctk.CTkLabel(processed_frame, text="0", anchor="e", font=ctk.CTkFont(weight="bold"), text_color="#000000")
        self.files_processed_label.pack(side="right")
        self.progress_bar = ctk.CTkProgressBar(status_card, height=12, corner_radius=6, progress_color=self.colors['secondary'])
        self.progress_bar.pack(fill="x", padx=20, pady=(10, 20))
        self.progress_bar.set(0)

        # Configuración
        config_card = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        config_card.pack(fill="x", pady=(0, 15))
        config_title = ctk.CTkLabel(config_card, text="⚙️ Configuración", font=ctk.CTkFont(size=15, weight="bold"), text_color="#000000", anchor="w")
        config_title.pack(anchor="w", padx=20, pady=(20, 10))
        format_frame = ctk.CTkFrame(config_card, fg_color="transparent")
        format_frame.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(format_frame, text="Formato salida:", anchor="w", text_color="#000000").pack(side="left")
        ctk.CTkLabel(format_frame, text="Excel (.xlsx)", anchor="e", font=ctk.CTkFont(weight="bold"), text_color="#000000").pack(side="right")
        dest_frame = ctk.CTkFrame(config_card, fg_color="transparent")
        dest_frame.pack(fill="x", padx=20, pady=(5, 20))
        ctk.CTkLabel(dest_frame, text="Carpeta destino:", anchor="w", text_color="#000000").pack(side="left")
        self.dest_folder_label = ctk.CTkLabel(dest_frame, text="Resultados/", anchor="e", font=ctk.CTkFont(weight="bold"), text_color="#000000")
        self.dest_folder_label.pack(side="right")

        # Log de actividad
        log_card = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        log_card.pack(fill="both", expand=True)
        log_title = ctk.CTkLabel(log_card, text="📋 Log de Actividad", font=ctk.CTkFont(size=15, weight="bold"), text_color="#000000", anchor="w")
        log_title.pack(anchor="w", padx=20, pady=(20, 10))
        self.log_text = ctk.CTkTextbox(log_card, height=150, font=ctk.CTkFont(family="Consolas", size=11), fg_color=("gray90", "gray10"))
        self.log_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        self.add_log_entry("Sistema iniciado correctamente")
        self.add_log_entry("Esperando selección de directorio...")

    def select_directory(self):
        directory = filedialog.askdirectory(title="Seleccionar directorio con archivos XML")
        if directory:
            self.selected_path.set(directory)
            self.path_label.configure(text=f"📁 {directory}")
            self.path_label.grid(row=2, column=0, sticky="ew", padx=25, pady=10)
            xml_files = self.count_xml_files(directory)
            self.files_found.set(xml_files)
            self.files_found_label.configure(text=str(xml_files))
            self.files_processed.set(0)
            self.files_processed_label.configure(text="0")
            self.progress_bar.set(0)
            if xml_files > 0:
                self.process_btn.configure(state="normal")
                self.update_status("🟢 Directorio seleccionado", f"Se encontraron {xml_files} archivos XML")
            else:
                self.process_btn.configure(state="disabled")
                self.update_status("🟡 Sin archivos XML", "No se encontraron archivos XML en el directorio")
            self.add_log_entry(f"Directorio seleccionado: {directory}")
            self.add_log_entry(f"Archivos XML encontrados: {xml_files}")

    def count_xml_files(self, directory):
        try:
            xml_count = len([f for f in os.listdir(directory) if f.lower().endswith('.xml')])
            return xml_count
        except:
            return 0

    def process_files(self):
        if self.processing:
            return
        self.processing = True
        self.process_btn.configure(state="disabled", text="⏳ Procesando...")
        self.files_processed.set(0)
        self.files_processed_label.configure(text="0")
        self.progress_bar.set(0)
        self.update_status("🟡 Procesando", "Convirtiendo archivos XML a Excel...")
        xml_dir = self.selected_path.get()
        try:
            import xml_processor
            import pandas as pd
            xml_files = [f for f in os.listdir(xml_dir) if f.lower().endswith('.xml')]
            total_files = len(xml_files)
            processed = 0
            datos = []
            processed_dir = os.path.join(xml_dir, 'procesados_xml')
            os.makedirs(processed_dir, exist_ok=True)
            for idx, file in enumerate(xml_files):
                path = os.path.join(xml_dir, file)
                try:
                    data = xml_processor.extract_data_from_xml(path)
                    datos.append(data)
                    processed += 1
                    self.files_processed.set(processed)
                    self.files_processed_label.configure(text=str(processed))
                    self.progress_bar.set(processed/total_files if total_files else 0)
                    self.update_status("🟡 Procesando", f"Procesando archivo {file} ({processed}/{total_files})")
                    self.add_log_entry(f"Procesado: {file}")
                    self.update()
                except Exception as e:
                    self.add_log_entry(f"Error procesando {file}: {str(e)}")
            # Generar el reporte Excel
            resumen = ""
            if datos:
                df = pd.DataFrame(datos)
                if not df.empty:
                    df['Fecha'] = pd.to_datetime(df['Fecha'])
                    df = df[df['Total'] > 1].sort_values('Fecha')
                    excel_path = os.path.join(xml_dir, f"reporte_facturas_{datetime.now():%Y%m%d_%H%M%S}.xlsx")
                    df.to_excel(excel_path, index=False)
                    resumen = f"✅ Procesadas {len(df)} facturas. Exportado a {excel_path}"
                    self.add_log_entry(f"Archivo Excel generado: {excel_path}")
                else:
                    resumen = "⚠️ No se encontraron facturas válidas."
            else:
                resumen = "⚠️ No se encontraron archivos XML válidos."
            # Mover los archivos procesados
            for file in xml_files:
                try:
                    shutil.move(os.path.join(xml_dir, file), os.path.join(processed_dir, file))
                except Exception as e:
                    self.add_log_entry(f"Error al mover {file}: {str(e)}")
            dest_path = processed_dir
            self.dest_folder_label.configure(text=dest_path)
            self.processing = False
            self.process_btn.configure(state="normal", text="⚡ Procesar Facturas")
            self.update_status("🟢 Completado", resumen)
        except Exception as e:
            self.processing = False
            self.process_btn.configure(state="normal", text="⚡ Procesar Facturas")
            self.update_status("🔴 Error", str(e))
            self.add_log_entry(f"Error al procesar archivos: {str(e)}")

    def open_dest_folder(self):
        xml_dir = self.selected_path.get()
        try:
            if not os.path.isdir(xml_dir):
                raise Exception("No se ha seleccionado un directorio válido.")
            import platform
            system = platform.system()
            if system == "Windows":
                os.startfile(xml_dir)
            elif system == "Darwin":
                os.system(f"open '{xml_dir}'")
            else:
                os.system(f"xdg-open '{xml_dir}'")
            self.add_log_entry(f"Abriendo carpeta seleccionada: {xml_dir}")
        except Exception as e:
            self.add_log_entry(f"Error al abrir carpeta seleccionada: {str(e)}")
            messagebox.showerror("Error", f"No se pudo abrir la carpeta seleccionada: {str(e)}")

    def update_status(self, status, message=None):
        color = None
        if "Procesando" in status:
            color = self.colors['secondary'][0]
        elif "Completado" in status or "Listo" in status:
            color = self.colors['tertiary'][0]
        elif "Error" in status:
            color = "#d32f2f"
        else:
            color = self.colors['text_primary']
        self.status_indicator.configure(text=status, text_color=color)
        if message:
            self.add_log_entry(message)

    def add_log_entry(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        self.log_text.insert("end", log_message)
        self.log_text.see("end")
