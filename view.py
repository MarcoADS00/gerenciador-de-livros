import sqlite3 

# conectar banco de dados
def connect(): 
	con = sqlite3.connect('dados.db')
	return con; 

# inserir livros 
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
	conn = connect()
	conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) \
		VALUES (?,?,?,?,?)", (titulo, autor, editora, ano_publicacao, isbn))
	conn.commit()
	conn.close()

#exibir livros 

def ver_book():
	conn = connect()
	livros = conn.execute("SELECT * FROM livros").fetchall()
	conn.close()

	return livros

# teste livro
#ver_book()


#inserir usuário
def insert_user(nome, sobrenome, endereco, email, telefone): 
	conn = connect()
	conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) \
					VALUES (?,?,?,?,?)",(nome, sobrenome, endereco, email, telefone))
	conn.commit()
	conn.close()

#exibir usuários
def show_users():
	conn = connect()
	c = conn.cursor()
	c.execute("SELECT * FROM usuarios")
	users = c.fetchall()
	conn.close()
	return users  

# inserir emprestimos 
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao): 
	conn = connect()
	conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) \
					VALUES (?, ?, ?, ?)",(id_livro, id_usuario, data_emprestimo, data_devolucao))
	conn.commit()
	conn.close()

# exibir emprestimos
def get_book_on_loan():
	conn = connect()
	result = conn.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo,\
							emprestimos.data_devolucao FROM livros \
							INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
							INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
							WHERE emprestimos.data_devolucao IS NULL").fetchall()
	conn.close()
	return result

# exibir devoluções/ inserir
def update_loan_return_date(id_emprestimo, data_devolucao):
	conn = connect()
	conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?",(data_devolucao, id_emprestimo))
	conn.commit()
	conn.close()
 
livros_emprestados = get_book_on_loan()


#insert_user("Marcos", "Dias", "Rua Sentinela,13", "Marcos@gmail.com", "55 999 99")
#insert_book("Dom Quixote","Viva", 2015, 0000 )
#update_loan_return_date(2,"2024-10-14")
#print(livros_emprestados)

#insert_loan(1,1,"2024-10-13", None)
#print(get_book_on_loan())

# teste book 
#insert_book("Dom Quixote", "Monel", "EDIT001", 1056, "123456") 

# teste user 
 #insert_user("Marcos", "Dias", "Rua da Sentinela, 13","marcos@gmail.com", "123355445")





