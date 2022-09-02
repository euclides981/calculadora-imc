from tkinter import *
import webbrowser

window = Tk()
window.title('Calculadora - IMC')
window.geometry('310x270')
window.configure(bg='white')
window.resizable(False, False)
window.iconbitmap('imc.ico')


def sobreimc():
    label_resultado_texto['text'] = 'IMC: Indice de Massa Corporal\nMedida internacional' \
                                    ' usada para calcular\nse uma pessoa está no peso ideal.'


def limpar():
    label_resultado_texto['text'] = ''
    label_resultado['text'] = ''
    input_peso.delete(0, END)
    input_altura.delete(0, END)
    input_peso.focus()


def link():
    webbrowser.open('https://euclides981.github.io/')


barraDeMenus = Menu(window)
menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label='O que é IMC', command=sobreimc)
menuSobre.add_command(label='Limpar Formulario', command=limpar)
menuSobre.add_command(label='Autor', command=link)
menuSobre.add_separator()
menuSobre.add_command(label='fechar', command=window.quit)
barraDeMenus.add_cascade(label='Sobre', menu=menuSobre)
window.config(menu=barraDeMenus)


cor1 = '#F4F4F4'
cor2 = '#58A5D1'
botao = '#0099CC'

frame_up = Frame(window, width=310, height=50, bg=cor1, pady=2, padx=0, relief='flat')
frame_up.grid(row=0, column=0, stick=NSEW)

frame_down = Frame(window, width=310, height=180, bg=cor1, pady=0, padx=0, relief='flat')
frame_down.grid(row=1, column=0, stick=NSEW)

app_title = Label(frame_up, text='Calculadora de IMC', width=21, height=1, padx=0, relief='flat', anchor='center',
                  font='Verdana 16 bold', bg=cor2, fg=cor1)
app_title.place(x=0, y=8)


def calcular():

    peso_usuario = input_peso.get()
    peso = float(peso_usuario.replace(',', '.'))

    altura_usuario = input_altura.get()
    altura = float(altura_usuario.replace(',', '.'))

    imc = peso / altura ** 2

    if imc < 18.5:
        label_resultado_texto['text'] = 'Você está Abaixo do peso'

    elif 18.5 <= imc < 25:
        label_resultado_texto['text'] = 'Você está Dentro do peso'

    elif 25 <= imc < 30:
        label_resultado_texto['text'] = 'Você está com Sobrepeso'

    else:
        label_resultado_texto['text'] = 'Você está com Obesidade'

    label_resultado['text'] = '{:.{}f}'.format(imc, 1)


label_peso = Label(frame_down, text='Insira seu Peso', height=1, padx=0, relief='flat', anchor='center',
                   font='Verdana 10 bold', bg=cor2, fg=cor1)
label_peso.grid(row=0, column=0, stick=NSEW, pady=10, padx=3)
input_peso = Entry(frame_down, width=5, relief='solid', font='Verdana 10 bold', justify='center')
input_peso.grid(row=0, column=1, stick=NSEW, pady=10, padx=3)

label_altura = Label(frame_down, text='Insira sua Altura', height=1, padx=0, relief='flat', anchor='center',
                     font='Verdana 10 bold', bg=cor2, fg=cor1)
label_altura.grid(row=1, column=0, stick=NSEW, pady=10, padx=3)
input_altura = Entry(frame_down, width=5, relief='solid', font='Verdana 10 bold', justify='center')
input_altura.grid(row=1, column=1, stick=NSEW, pady=10, padx=3)

label_resultado = Label(frame_down, text='???', width=4, height=1, padx=8, pady=12, relief='flat', anchor='center',
                        font='Verdana 24 bold', bg=cor2, fg=cor1)
label_resultado.place(x=198, y=10)

label_resultado_texto = Label(frame_down, text='Seu resultado aparecerá aqui', width=34, height=2, padx=0, pady=15,
                              relief='flat', anchor='center', font='Verdana 10 bold', bg=cor2, fg=cor1)
label_resultado_texto.place(x=0, y=85)

botao_calcular = Button(frame_down, command=calcular, text='CALCULAR', width=34, height=1, overrelief=SOLID,
                        relief='raised', font='Verdana 10 bold', bg=botao, fg=cor1, cursor="target", border=0)
botao_calcular.grid(row=4, column=0, stick=NSEW, pady=80, padx=0, columnspan=35)

window.mainloop()
