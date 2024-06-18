
from customtkinter import *
import os
from tkinter import messagebox

# usando o from biblioteca e importando toda ela com o * e mais facil escrever os codigos
# fica mais simples e rapido

# cor da janela
set_appearance_mode("mode")
#set_default_color_theme("dark-blue")

# criando janela
janela = CTk()
janela.title("sistema de login")
janela.geometry("300x300")
janela.resizable(False, False)
#janela.iconbitmap("imagem/icons8-afundanço-50.ico")
# imagem de fundo
# imagem_te_amo =  PhotoImage(file=' C:\Users\iuryd\Desktop\teste program\pagina loguim\imagem\imagem.png')
# imagem_te_amo= logo.subsample(3,3)
# figura1=Label(image=imagem_te_amo)
# figura1.grid(row=0, column=0, pady=5 , padx=5)


# criando texto da janela
texto = CTkLabel(janela, text="Fazer login", text_color="blue")
texto.pack(padx=10, pady=10)

# espaco de entrada
email = CTkEntry(janela, placeholder_text="insira seu e-mail", border_color="blue")
email.pack(padx=10, pady=10)

# espaco da senha
senha = CTkEntry(janela, placeholder_text="insira sua senha", show="*", border_color="blue")
senha.pack(padx=10, pady=10)


# definir funcao do checkbox
def ver_senha():
    if senha.cget('show') == '*':
        senha.configure(show='')

    else:
        senha.configure(show='*')


# ver a senha
ver_senha = CTkCheckBox(janela, text="ver sua senha", command=ver_senha)
ver_senha.pack(padx=10, pady=10)


#  funçao do clique

def clique_login():

    #banco de dados
    email_final = email.get()
    senha_final = senha.get()

    email1 = '123'
    senha1 = '123'

#logica do login
    if email1=='' or senha_final=='':
        messagebox.showinfo(title="dados",message="insira seus dados")




    else:
        if email_final != email1:
            messagebox.showerror(title="erro",message="logim incorreto")

        elif senha_final != senha1:
            messagebox.showerror(title="erro",message="senha incorreto")

        else :
            print("login concluido")
            # fazendo abir outro programa
            os.startfile("html/aula 02.html")

# botao de login
botao = CTkButton(janela, text="login", command=clique_login)
botao.pack(padx=10, pady=10)


# funçao do cadastro
def clique_cadastro():
    print("fazer fazer cadastro")



# botao cadastro
cadastrar = CTkButton(janela, text="Cadastrar", command=clique_cadastro, fg_color="green", hover_color="green")
cadastrar.pack(padx=10, pady=10)

texto_mensagem = CTkLabel(janela, text="")
texto_mensagem.pack(padx=10, pady=10)

janela.mainloop()
