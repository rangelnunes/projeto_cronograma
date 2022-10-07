import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title('Tela de sorteio com PACK')
root.resizable(False, False)

# frame 1
frame1 = ttk.Frame(root)
frame1.pack(padx=10, pady=10)

label_nome = ttk.Label(frame1, text='Nome')
label_nome.pack(side=tk.LEFT)

entry_nome = ttk.Entry(frame1)
entry_nome.pack(side=tk.LEFT)

botao_inserir = ttk.Button(frame1, text='Inserir')
botao_inserir.pack()
# frame 2
frame2 = ttk.Frame(root)
frame2.pack(padx=10, pady=1, expand=True, fill=tk.X)

lista_de_nomes = tk.Listbox(frame2)
lista_de_nomes.pack(fill=tk.X)

# frame3
frame3 = ttk.Frame(root)
frame3.pack(padx=10, pady=10)

def pega_nome():
    nome = entry_nome.get()
    messagebox.showinfo('messagem qualquer', f'Seja bem vindo {nome}')

botao_sortear = ttk.Button(frame3, text='Sortear', command=pega_nome)
botao_sortear.pack(side=tk.LEFT, ipadx=10, ipady=5)

botao_cancelar = ttk.Button(frame3, text='Cancelar', command=root.quit)
botao_cancelar.pack(ipadx=10, ipady=5)


root.mainloop()