import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title('Cadastro de participantes')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=1)

label_nome = ttk.Label(root, text='Nome')
label_nome.grid(column=0, row=0, padx=5, pady=5)

entry_nome = ttk.Entry(root)
entry_nome.grid(column=1, row=0, padx=5, pady=5)
entry_nome.focus()

def inserir_nome():
    if len(entry_nome.get().strip()) > 0:
        lista_de_nomes.insert(tk.END, entry_nome.get())
    else:
       messagebox.showinfo('Aviso', 'Você deve digitar um nome!')
    entry_nome.delete(0, tk.END)
    entry_nome.focus()

botao_inserir = ttk.Button(root, text='Inserir', command=inserir_nome)
botao_inserir.grid(column=2, row=0)

botao_exlcuir_todos = ttk.Button(root, text='Excluit todos')
botao_exlcuir_todos.grid(column=3, row=0)

#frame_lista = ttk.Frame(root)
#frame_lista.grid(row=1)

lista_de_nomes = tk.Listbox(root)
lista_de_nomes.grid(row=1, columnspan=4, sticky=tk.EW, padx=5, pady=5)

frame_radiobutton = ttk.Frame(root)
frame_radiobutton.grid(row=2, columnspan=4)

radiobutton_sorteio_normal = ttk.Radiobutton(frame_radiobutton, text='Normal', value='Normal')
radiobutton_sorteio_normal.grid(column=0, row=0, padx=10, pady=10)

radiobutton_sorteio_ultimo = ttk.Radiobutton(frame_radiobutton, text='Último que fica', value='Invertido')
radiobutton_sorteio_ultimo.grid(column=1, row=0, padx=10, pady=10)

frame_progressbar = ttk.Frame(root)
frame_progressbar.grid(row=3, columnspan=4)

barra_de_progresso = ttk.Progressbar(frame_progressbar, orient=tk.HORIZONTAL, mode='determinate', length=350,
                                     value=0, maximum=100)
barra_de_progresso.grid(column=0, row=0, columnspan=2)

label_barradeprogresso = ttk.Label(frame_progressbar, text= 'Sorteando: 0%')
label_barradeprogresso.grid(column=0, row=1, columnspan=2)

frame_botoes = ttk.Frame(root)
frame_botoes.grid(row=4, columnspan=4)

botao_sortear = ttk.Button(frame_botoes, text='Sortear')
botao_sortear.grid(row=0, column=0, pady=10, ipady=10)

botao_cancelar = ttk.Button(frame_botoes, text='Cancelar', command=root.quit)
botao_cancelar.grid(row=0, column=1, pady=10, ipady=10)



root.mainloop()