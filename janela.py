import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Projeto Tkinter')
root.resizable(False, False)
#root.attributes('-alpha', 0.8)

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

tk.Label(root, text='Primeiro label', bg='#FF0083', fg='white').pack()
#ttk.Label(root, text= 'Label temático').pack()

outro_label = tk.Label(root)

outro_label['text'] = 'Outro label'
outro_label['bg'] = '#3F9FFF'
outro_label['fg'] = '#FFFFFF'
outro_label.pack()

mais_um_label = ttk.Label(root)
mais_um_label.config(text='Terceiro label', foreground='blue')
mais_um_label.pack()

password = tk.StringVar()

campo_de_texto = ttk.Entry(root, textvariable=password, show='#')
campo_de_texto.pack()

botao = ttk.Button(root, text='Clique aqui!')
botao.config(state='disabled')
botao.pack()


root.mainloop()