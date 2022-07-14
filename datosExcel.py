from asyncore import write
from tkinter import messagebox
import sqlite3
import csv


def exportar():
    miConexion = sqlite3.connect("zodiacales")
    miCursor= miConexion.cursor()
    
    try:
        miCursor.execute("SELECT * FROM respuestas")
        archivos= miCursor.fetchall()
        for i in archivos:
            print(i)
            
            with open("Datos.csv", "w", newline="") as file:
                writer= csv.writer(file)
                writer.writerow(['id_respuesta','optimistaR', 'pesimistaR', 'confianzaR', 'atencionR', 'afectoR', 'extrovertidaR','introvertida','inteligenteR','deprimeR','fiestaR','fisicoR','ejercicioR','solitariaR','viajarR','estacionR','emprendedorR','elementoR'])
                writer.writerows(archivos)
                
        messagebox.showinfo("EXPORTACION", "Exportación exitosa")
    except:
        messagebox.showwarning("NO EJECUTADO", "No se pudo exportar la información")