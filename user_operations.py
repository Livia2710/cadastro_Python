from tkinter import messagebox

# Inicialliza a classe com referencia ao banco de dados e a interface do usuário
class UserOperations:
    def __init__(self, db, ui):
        self.db = db
        self.ui = ui

    # Cadatrar um novo usuário no banco de dados
    def cadastrar(self):
        nome = self.ui.nome_entry.get()
        if nome:
            self.db.insert_user(nome)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.ui.nome_entry.delete(0, 'end')
            self.ui.carregar_dados()
        else:
            messagebox.showerror("Erro", "Por favor, preencha o campo Nome.")

    # Atualiza as informações de um usuario existente
    def atualizar_usuario(self):
        if self.ui.selected_user:
            novo_nome = self.ui.nome_entry.get()
            if novo_nome:
                self.db.update_user(self.ui.selected_user[0], novo_nome)
                messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
                self.ui.carregar_dados()
                self.ui.nome_entry.delete(0, 'end')
                self.ui.selected_user = None
            else:
                messagebox.showerror ("Erro", "Por favor, preencha o campo Nome.")
        else:
            messagebox.showerror("Erro", "Por favor, selecione um usuário para atualizar.")
    
    # Excklui um usuário do banco de dados
    def excluir_usuario(self):
        if self.ui.selected_user:
            if messagebox.askyesno("Confirmar", "Tem certeza que deeja excluir este usuário?"):
                self.db.delete_user(self.ui.selected_user[0])
                messagebox.showinfo("Sucesso", "Usuário ecluido com sucesso!")
                self.ui.carregar_dados()
                self.ui.nome_entry.delete(0, 'end')
                self.ui.selected_user = None
        else:
            messagebox.showerror("Erro", "Por favor, selecione um usuário para excluir.")
