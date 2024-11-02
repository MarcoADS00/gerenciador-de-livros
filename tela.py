from tkinter .ttk import *
from tkinter import *
from view import *
from tkinter import messagebox
from tkinter import ttk
from datetime import date 
from datetime import datetime 

hoje = datetime.today()

# cores para o app 

co0 = "#2e2d2b"   
co1 = "#feffff"  
co2 = "#4fa882" 
co3 = "#38576b" 
co4 = "#403d3d" 
co5 = "#e06636" 
co6 = "#E9A178"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"
co10 = "#6e8faf"
co11 = "#f2f4f2"

#janela do app 

window = Tk()
window.title('Biblioteca Virtual')
window.geometry('770x330')
window.configure(background=co1)
window.resizable(width= FALSE, height= FALSE)

style = Style(window)
style.theme_use("clam")


#seções 

cabecalho = Frame(window, width=770, height=50, bg=co6, relief="flat")
cabecalho.grid(row=0, column=0, columnspan=2, sticky=NSEW)

parte_esquerda = Frame(window, width=150, height=265, bg=co4, relief="solid")
parte_esquerda.grid(row=1, column=0, sticky=NSEW)

parte_direita = Frame(window, width=600, height=265, bg=co1, relief="raised")
parte_direita.grid(row=1, column=1, sticky=NSEW)

app_ = Label(cabecalho, text="Biblioteca Virtual - Gerenciamento", compound=LEFT, padx=5,anchor= NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
app_.place(x=60, y=7)


#funcoes auxiliares ao controle

def novo_usuario():

    def add(): #atribuindo os valores digitados ao BD 
        first_name = e_nome.get()
        last_name = e_last.get()
        adress = e_adress.get()
        email = e_mail.get()
        tell = e_tell.get()

        lista = [first_name, last_name, adress, email, tell]
        for i in lista: #verificando valores nulos  
            if i == '':
                messagebox.showerror('ERROR','Por favor, preencha todos os campos')
                return
        insert_user(first_name, last_name, adress, email, tell)

        messagebox.showinfo('SUCESSO','Usuário cadastrado com sucesso')
        e_nome.delete(0,END)
        e_last.delete(0,END)
        e_adress.delete(0,END)
        e_mail.delete(0,END)
        e_tell.delete(0,END)


    #TITULO
    app_ = Label(parte_direita, text="Inserir novo usuário", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co2, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    #first-name
    l_nome = Label(parte_direita, text="PRIMEIRO NOME: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_nome = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #last-name
    l_last = Label(parte_direita, text="SOBRENOME: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_last.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_last = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_last.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #adress
    l_adress = Label(parte_direita, text="ENDEREÇO:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_adress.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_adress = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_adress.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    #email
    l_mail = Label(parte_direita, text="E-MAIL:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_mail.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_mail = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_mail.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    #telefone
    l_tell = Label(parte_direita, text="TELEFONE:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_tell.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_tell = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_tell.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    #salvar 
    save = Button(parte_direita, command=add, compound=LEFT, anchor=NW, text=" SALVAR", bg=co2, fg=co4)
    save.grid(row=7, column=1, sticky=NSEW, padx=5, pady=5)
    
def ver_usuario():
    app_ = Label(parte_direita,text="Todos os usuários ", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co10, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    dados = show_users()

    list_header = ['ID','Nome','Sobrenome','Endereço','Email','Telefone']
    
    global tree

    tree = ttk.Treeview(parte_direita, selectmode="extended",
                        columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(parte_direita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(parte_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    parte_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,160,110,100,50,50,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

def novo_livro(): 

    def add():
        titulo = e_titulo.get()
        autor = e_autor.get()
        editora = e_editora.get()
        ano_publi = e_ano.get()
        isbn = e_isbn.get()

        lista = [titulo, autor, editora, ano_publi, isbn]
        for i in lista: #verificando valores nulos  
            if i == '':
                messagebox.showerror('ERROR','Por favor, preencha todos os campos')
                return
        insert_book(titulo, autor, editora, ano_publi, isbn)

        messagebox.showinfo('SUCESSO','Livro cadastrado com sucesso')
        e_titulo.delete(0,END)
        e_autor.delete(0,END)
        e_editora.delete(0,END)
        e_ano.delete(0,END)
        e_isbn.delete(0,END)


    #TITULO
    app_ = Label(parte_direita, text="Inserir novo livro", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co2, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    #titulo-livro
    l_titulo = Label(parte_direita, text="TITULO: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_titulo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_titulo = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_titulo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #autor
    l_autor = Label(parte_direita, text="AUTOR: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_autor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #editora
    l_editora = Label(parte_direita, text="EDITORA: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_editora.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    #ano-publicacao
    l_ano = Label(parte_direita, text="ANO PUBLICAÇÃO: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_ano.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    #ISBN
    l_isbn = Label(parte_direita, text="ISBN: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_isbn = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_isbn.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    #salvar 
    save = Button(parte_direita, command=add, compound=LEFT, anchor=NW, text=" SALVAR", bg=co2, fg=co4)
    save.grid(row=7, column=1, sticky=NSEW, padx=5, pady=5)
    
def ver_livros():
    app_ = Label(parte_direita,text="Todos os livros ", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co10, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    dados = ver_book()
    list_header = ['ID','Titulo','Autor','Editora','Ano','ISBN']
    
    global tree

    tree = ttk.Treeview(parte_direita, selectmode="extended",
                        columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(parte_direita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(parte_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    parte_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

def novo_emprestimo(): 

    def add():
        id_user = e_id_usuario.get()
        id_livro = e_id_livro.get()


        lista = [id_user, id_livro]
        for i in lista: #verificando valores nulos  
            if i == '':
                messagebox.showerror('ERROR','Por favor, preencha todos os campos')
                return
        insert_loan(id_user, id_livro, hoje, None)

        messagebox.showinfo('SUCESSO','Livro emprestado com sucesso')
        e_id_usuario.delete(0,END)
        e_id_livro.delete(0,END)
        


    #TITULO
    app_= Label(parte_direita, text="Inserir novo empréstimo", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co2, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    #ID usuario 
    l_id_usuario = Label(parte_direita, text="ID USUÁRIO: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_usuario.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_usuario = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_id_usuario.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #ID livro 
    l_id_livro = Label(parte_direita, text="ID LIVRO: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_id_livro = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_id_livro.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #salvar 
    save = Button(parte_direita, command=add, compound=LEFT, anchor=NW, text=" SALVAR", bg=co2, fg=co4)
    save.grid(row=7, column=1, sticky=NSEW, padx=5, pady=5) 

def ver_emprestimo():

    app_ = Label(parte_direita,text="Todos os emprestimos ", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co10, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    dados = []

    book_on_loan = get_book_on_loan()

    for book in book_on_loan:
        dado = [f"{book[0]}",f"{book[1]}", f"{book[2]}{book[3]}", f"{book[4]}", f"{book[5]}"]

        dados.append(dado)


    list_header = ['ID','Titulo','Nome','Emprestimo','Devolução']
    
    global tree

    tree = ttk.Treeview(parte_direita, selectmode="extended",
                        columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(parte_direita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(parte_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    parte_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","ne","ne","ne","ne"]
    h=[20,175,120,90,90,100,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

def devolver_emprestimo(): 
    
    def add():
        loan_id = e_id_emprestimo.get()
        return_date = e_devolucao.get()


        lista = [loan_id, return_date]
        for i in lista: #verificando valores nulos  
            if i == '':
                messagebox.showerror('ERROR','Por favor, preencha todos os campos')
                return
        update_loan_return_date(loan_id, return_date)

        messagebox.showinfo('SUCESSO',' Devolução aceita!')
        e_id_emprestimo.delete(0,END)
        e_devolucao.delete(0,END)

    #TITULO
    app_= Label(parte_direita, text=" Atualizar empréstimo", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co2, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    #ID do emprestimo  
    l_id_emprestimo = Label(parte_direita, text="ID DO EMPRESTIMO: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_emprestimo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_emprestimo = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_id_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #data retorno  
    l_devolucao = Label(parte_direita, text="DATA DE DEVOLUÇÂO: (AAAA-MM-DD) ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_devolucao.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_devolucao = Entry(parte_direita, width=25, justify='left', relief='solid')
    e_devolucao.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #salvar 
    save = Button(parte_direita, command=add, compound=LEFT, anchor=NW, text=" SALVAR", bg=co2, fg=co4)
    save.grid(row=7, column=1, sticky=NSEW, padx=5, pady=5) 

#controle do menu 
def control(i):
    if i == 'novo_usuario':
        for widget in parte_direita.winfo_children():
            widget.destroy()
        novo_usuario()

    if i == 'ver_usuario': 
        for widget in parte_direita.winfo_children():
            widget.destroy()
        ver_usuario()

    if i == 'novo_livro':
        for widget in parte_direita.winfo_children():
            widget.destroy()
        novo_livro()

    if i == 'ver_livros': 
        for widget in parte_direita.winfo_children():
            widget.destroy()
        ver_livros()

    if i == 'emprestimo':
        for widget in parte_direita.winfo_children():
            widget.destroy()
        novo_emprestimo()

    if i == 'ver_emprestimo': 
        for widget in parte_direita.winfo_children():
            widget.destroy()
        ver_emprestimo()

    if i == 'devolucao': 
        for widget in parte_direita.winfo_children():
            widget.destroy()
        devolver_emprestimo()

#menu principal - botões

#novo usuario
new_user = Button(parte_esquerda, command=lambda:control('novo_usuario'), compound=LEFT, anchor=NW, text=" NOVO USUÁRIO", bg=co4, fg=co1 ,font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
new_user.grid(row=0, column=0, sticky=NSEW, padx=5, pady=4)

#novo livro
new_book = Button(parte_esquerda, command=lambda:control('novo_livro'), compound=LEFT, anchor=NW, text=" NOVO LIVRO", bg=co4, fg=co1 ,font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
new_book.grid(row=1, column=0, sticky=NSEW, padx=5, pady=4)

#ver todos os livros 
show_book = Button(parte_esquerda, command=lambda:control('ver_livros'), compound=LEFT, anchor=NW, text=" EXIBIR LIVROS", bg=co4, fg=co1 ,font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
show_book.grid(row=2, column=0, sticky=NSEW, padx=5, pady=4)

#ver todos os usuarios 
show_user = Button(parte_esquerda, command=lambda:control('ver_usuario'), compound=LEFT, anchor=NW, text=" EXIBIR USUÁRIOS", bg=co4, fg=co1 ,font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
show_user.grid(row=3, column=0, sticky=NSEW, padx=5, pady=4)

#novo emprestimo 
new_loan = Button(parte_esquerda, command=lambda:control('emprestimo'),compound=LEFT, anchor=NW, text=" NOVO EMPRÉSTIMO", bg=co4, fg=co1 ,font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
new_loan.grid(row=4, column=0, sticky=NSEW, padx=5, pady=4)

#devolver emprestimo 
get_loan = Button(parte_esquerda, command=lambda:control('devolucao'), compound=LEFT, anchor=NW, text=" DEVOLVER EMPRÉSTIMO", bg=co4, fg=co1 ,font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
get_loan.grid(row=5, column=0, sticky=NSEW, padx=5, pady=4)

#ver emprestimos 
show_loan = Button(parte_esquerda, command=lambda:control('ver_emprestimo'), compound=LEFT, anchor=NW, text=" LIVROS EMPRESTADOS", bg=co4, fg=co1 ,font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
show_loan.grid(row=6, column=0, sticky=NSEW, padx=5, pady=4)


window.mainloop()