from tkinter import *
from turtle import left, right
from matplotlib.pyplot import pause
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
import numpy as np
import sympy as sym
from sympy import *
import matplotlib.pyplot as plt
from tkinter import messagebox

win =Tk()
win.geometry("1000x550")
win["bg"] = "#FF5C01"
win.title("Software para Cálculo Numérico")
style = {"fund":"#FF5C01"}
#Imagem
def pagina_integracao():
    integracao = Frame(win)
    integracao["bg"] = style["fund"]
    integracao.pack()

    #Frame titulo
    in_titulo = Frame(integracao)
    in_titulo["bg"] = style["fund"]
    in_titulo.pack()

    titulo = Label(in_titulo, text="Integração Numérica",font="Calibri 45 bold",fg="white")
    titulo["bg"] = style["fund"]
    titulo.pack()

    #Frame função
    in_func = Frame(integracao)
    in_func["bg"] = style["fund"]
    in_func.pack()

    #texto função
    text_funcao = Label(in_func, text="Função: ",font="Arial 17 bold",fg="white")
    text_funcao["bg"] = style["fund"]
    text_funcao.pack(side="left")

    #entrada de função
    funcao = Text(in_func,width="40",height="1",font="Arial 25")
    funcao.pack()

    #Valores de a,b,precisao
    in_valores = Frame(integracao)
    in_valores["bg"] = style["fund"]
    in_valores.pack(pady=15)

    #Valores de A
    text_a = Label(in_valores,text="Valor de A:",font="arial 15 bold",fg="white")
    text_a["bg"] = style["fund"]
    text_a.pack(side="left")

    valor_a = Text(in_valores,width="16",height="1")
    valor_a.pack(side="left")
    #Valores de B
    text_b = Label(in_valores, text="Valor de B:",font="arial 15 bold",fg="white")
    text_b["bg"] = style["fund"]
    text_b.pack(side="left")

    valor_b = Text(in_valores,width="16", height="1")
    valor_b.pack(side="left")

    # Valores de precisao
    text_prec = Label(in_valores, text="Interações:",font="arial 15 bold",fg="white")
    text_prec["bg"] = style["fund"]
    text_prec.pack(side="left")

    valor_prec = Text(in_valores, width="16", height="1")
    valor_prec.pack(side="left")

    #Botão
    in_botao = Frame(integracao)
    in_botao["bg"] = style["fund"]
    in_botao.pack()
    
    #FRAME de Baixo
    in_baixo = Frame(integracao)
    in_baixo["bg"] = style["fund"]
    in_baixo["width"] = 900
    in_baixo.pack(pady=50,)

    #Frame de resutado
    in_resultado = Frame(in_baixo)
    in_resultado["bg"] = style["fund"]
    in_resultado.pack(side="left",padx=60)

    #texto resultado de cima
    text_resultado = Label(in_resultado, text="Resultado", fg="white")
    text_resultado["font"] = "arial 15 bold"
    text_resultado["bg"] = style["fund"]
    text_resultado.pack()

    #texto resultado
    resultado = Label(in_resultado, text="0.0000004",font="arial 30 bold",fg="white")
    resultado["bg"] = "#B1510F"
    resultado.pack()


    #Explicação do metodo
    in_explic = Frame(in_baixo)
    in_explic["bg"] = "#B1510F"
    in_explic.pack()

    #Nome do titulo
    titulo_metodo = Label(in_explic,text="Método de trapezio",font="arial 15 bold",fg="white")
    titulo_metodo["bg"] = "#B1510F"
    titulo_metodo.pack()

    #explicação do metodo
    explic = Label(in_explic,text="""A ideia principal da Regra do Trapézio
    é aproximar a função por um
    polinômio de primeiro grau,
    ou seja uma reta.""",font="arial 20 bold",fg="white")
    explic["bg"] = "#B1510F"
    explic.pack()
    def trapezio():
        funcao_simp = funcao.get("1.0","end")
        v_a = int(valor_a.get("1.0","end"))
        v_b = int(valor_b.get("1.0","end"))
        v_prec = int(valor_prec.get("1.0","end"))
        xf = Symbol('x')
        fx = expand(funcao_simp)
        px = lambdify(xf,fx)
        a=v_a
        b=v_b
        n=v_prec

        x = np.linspace(a, b, n+1, dtype=float)
        y = px(x)
        h = (b - a) / n
        s = y[0] + 2.0 * np.sum(y[1:-1]) + y[-1]

        #Saida
        result = 0.5 * h * s
        resultado['text'] = result
        titulo_metodo['text'] = "Método do Trapézio"
        explic["text"] = """A ideia principal da Regra do Trapézio
    é aproximar a função por um
    polinômio de primeiro grau,
    ou seja uma reta."""
    def simpson():
        funcao_simp = funcao.get("1.0","end")
        v_a = int(valor_a.get("1.0","end"))
        v_b = int(valor_b.get("1.0","end"))
        v_prec = int(valor_prec.get("1.0","end"))
        xf = Symbol('x')
        fx = expand(funcao_simp)
        px = lambdify(xf,fx) 

        a=v_a
        b=v_b
        n=v_prec

        #Calculo
        if int(n) % 2: # para garantir numero par de intervalos
            n += 1

        x = np.linspace(a, b, n+1, dtype=float)
        y = px(x)
        h = (b - a) / n
        Si = np.sum(y[1:-1:2]) # posicoes impares
        Sp = np.sum(y[2:-1:2]) # posicoes pares

        S = y[0] + 4 * Si + 2 * Sp + y[-1]

        #Saida

        result = h * S / 3
        resultado['text'] = result
        titulo_metodo['text'] = "Método de Simpson"
        explic["text"] = """A Regra 1/3 de Simpson resulta
        da integração da função f(x)
        no intervalo [a, b] a partir
        da aproximação polinomial de
        segundo grau de Lagrange, com
        pontos igualmente espaçados
        x0 = a, x2 = b e x1 = a + h,
        onde h = (b - a)/2."""

    def calcular():
        if(int(valor_prec.get("1.0","end"))>1000):
            simpson()
        else:
            trapezio()

    inte_iniciar = Button(in_botao,text="Iniciar", font="arial 15 bold", width="16", height="1",command=calcular)
    inte_iniciar["bg"] = "blue"
    inte_iniciar["fg"] = "white"
    inte_iniciar["border"] = 0
    inte_iniciar.pack()

def Interpolacao():
    interpolacao = Frame(win)
    interpolacao["bg"] = style["fund"]
    interpolacao.pack()

    #Frame titulo
    inter_titulo = Frame(interpolacao)
    inter_titulo["bg"] = style["fund"]
    inter_titulo.pack()

    #titulo
    int_titulo = Label(inter_titulo,text="INTERPOLAÇÃO",font="Calibri 45 bold",fg="white")
    int_titulo.pack()
    int_titulo["bg"] = style["fund"]

    #FRAME DA ENTRADA
    inter_entrada = Frame(interpolacao)
    inter_entrada["bg"] = style["fund"]
    inter_entrada.pack()

    #Frame de pontos
    inter_pontos = Frame(inter_entrada)
    inter_pontos["bg"] = style["fund"]
    inter_pontos.pack()

    #Frame  pontos de cima
    frame_x = Frame(inter_pontos)
    frame_x["bg"] = style["fund"]
    frame_x.pack()

    #texto
    text_x = Label(frame_x,text="X: ",font="arial 16 bold",fg="white")
    text_x["bg"] = style["fund"]
    text_x.pack(side="left")

    #input
    val_x = Text(frame_x,height=1,font="arial 15",width=50)
    val_x.pack(side='left',padx=10)
    #botao

    #frame pontos de baixo
    frame_fx = Frame(inter_pontos)
    frame_fx["bg"] = style["fund"]
    frame_fx.pack()

    text_fx = Label(frame_fx,text="F(x): ",font="arial 16 bold",fg="white")
    text_fx["bg"] = style["fund"]
    text_fx.pack(side="left")

    #input
    val_fx = Text(frame_fx,height=1,font="arial 15",width=60)
    val_fx.pack(side='left')

    #PARTE DE BAIXO
    frame_baixo = Frame(interpolacao)
    frame_baixo["bg"] = style["fund"]
    frame_baixo.pack(pady=20)

    #BAIXO_DIREITO
    baixo_direito = Frame(frame_baixo)
    baixo_direito["bg"] = style["fund"]
    baixo_direito.pack(side="left",padx=20)

    #Gráfico de Exemplo
    fig = Figure(figsize = (3, 3), dpi = 100)     
    y = [i**3 for i in range(101)] 
    plot1 = fig.add_subplot(111) 
    plot1.plot(y) 
    canvas = FigureCanvasTkAgg(fig, master = baixo_direito)   
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    #BAIXO_ ESQUERDO
    baixo_esquerdo = Frame(frame_baixo)
    baixo_esquerdo["bg"] = "#B1510F"
    baixo_esquerdo.pack()

    #Explicação da Escolha
    metodo = Label(baixo_esquerdo,text="Método de Lagrange",font="arial 20 bold",fg="white")
    metodo["bg"] = "#B1510F"
    metodo.pack()
    
    expli_met = Label(baixo_esquerdo, text="""Em análise numérica, polinômio de Lagrange 
    é o polinômio de interpolação de um
    conjunto de pontos na forma de Lagrange.""",font="arial 15 bold",fg="white")
    expli_met["bg"] = "#B1510F"
    expli_met.pack(pady=10)
    #Esquação
    
    baixo = Frame(interpolacao)
    baixo["bg"] = style["fund"]
    baixo.pack()
    print(Tk.winfo_screenwidth)
    ti_equacao = Label(baixo,text="Resultado",font="arial 20 bold",fg="white")
    ti_equacao["bg"] = style["fund"]
    ti_equacao.pack()

    equacao = Label(baixo,text="x**2+4**x",font="arial 15 bold",fg="white")
    equacao["bg"] = "#B1510F"
    equacao.pack()
    def newton(xf,fx):
        metodo['text'] = "Método de Newton"
        expli_met["text"] = """Em análise numérica, o método de Newton  
        tem o objetivo de estimar as raízes 
        de uma função. Para isso, escolhe-se 
        uma aproximação inicial para esta. 
        Após isso, calcula-se a equação 
        da reta tangente (por meio da derivada) 
        ao gráfico da função nesse ponto e 
        a interseção dela com o eixo das
        abcissas, a fim de encontrar uma
        melhor aproximação para a raiz."""
        def interpNewton(x,y,xi):
            n = len(x)
            fdd = [[None for x in range(n)] for x in range(n)]

            for i in range(n):
                fdd[i][0] = y[i] 

            for j in range(1,n):
                for i in range(n-j):
                    fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])

            #fdd_table = pd.DataFrame(fdd)
            #print(fdd_table)
            xterm = 1
            yint  = fdd[0][0]
            for order in range(1,n):
                xterm = xterm*(xi - x[order-1])
                yint  = yint + fdd[0][order]*xterm
            
            return yint

        x  = xf
        y  = fx
        xp = 0.5
        yp = interpNewton(x,y,2) 
        t  = np.arange(-10,10.0,0.5)
        yt = []

        plot1.clear()
        for i in t:
            yt.append(interpNewton(x,y,i))
        
        equacao["text"] = f"f(2): {yp}"

        plot1.plot(t,yt,'b-')
        plot1.plot(x,y,'ro')
        plot1.plot(xp,yp,'g*')
        plot1.grid()
        canvas.draw()

    def lagrange(x,fx):
        metodo["text"] = "Método de Lagrange"
        expli_met["text"] = "A quantidade de pontos é maior,\nentão o método de lagrange é mais eficiente!"
        xi = np.array(x)
        fi = np.array(fx)

        # PROCEDIMIENTO
        # Polinomio de Lagrange
        n = len(xi)
        x = sym.Symbol('x')
        polinomio = 0
        divisorL = np.zeros(n, dtype = float) #Cria uma lista de zeros (dtype = Float significa que eles tem ponto: 0.000)
        for i in range(0,n,1):
            # Termino de Lagrange
            numerador = 1
            denominador = 1
            for j  in range(0,n,1):
                if (j!=i):
                    numerador = numerador*(x-xi[j])
                    denominador = denominador*(xi[i]-xi[j])
            terminoLi = numerador/denominador

            polinomio = polinomio + terminoLi*fi[i]
            divisorL[i] = denominador


        # Simplificar o Polinomio
        poli_simples = polinomio.expand() 
        equacao["text"] = poli_simples
        equacao['font'] = f"arial {int(win.winfo_screenmmwidth()*0.04)} bold"
        expli_met["text"] = """Em análise numérica, polinômio de Lagrange
        é o polinômio de interpolação de
        um conjunto de pontos na forma de Lagrange."""
        #Faz com que esse polinomio se torne uma função dentro do python (Chamada: px(3))
        px = sym.lambdify(x,poli_simples) 

        # Pontos para o Gráfico
        tamanho = 100 #Serve para identificar a quantidade de elementos da linha 41
        a = np.min(xi) #Retorna o valor minimo de xi
        b = np.max(xi) #Retorna o valor maximo de xi
        pxi = np.linspace(a,b,tamanho) #Cria uma lista com "Tamanho" elementos q vão de a até b no mesmo intervalo

        #Coloca os valores de pxi na função para saber seus resultados e encontrar os resultados (Formato de lista)
        pfi = px(pxi)
        plot1.clear()
        for y in range(0,len(xi)):
            plot1.plot(xi[y],fi[y], 'o')
        plot1.plot(pxi,pfi) 
        canvas.draw()
    #Mudar o Gráfico
    def grafico(): 
        pontos_x = val_x.get("1.0","end")
        pontos_fx = val_fx.get("1.0","end")

        try:
            pontos_x = list(map(float,pontos_x.split(" ")))
            pontos_fx = list(map(float,pontos_fx.split(" ")))
        except ValueError:
            messagebox.showerror("Dados de Entrada incorretos","Valores de Entrada com espaços ou caracteres invalidos")
        if(len(pontos_x)>=5):
            lagrange(pontos_x,pontos_fx)
        else:
            newton(pontos_x,pontos_fx)

    inciar_inter = Button(frame_x,text="Iniciar",command=grafico, border=0,bg="blue",fg="white",width=10)
    inciar_inter["font"] = "Arial 10"
    inciar_inter.pack()


#IR PARA A OUTRA PAGINA

def inicial_interpola():
    ini.destroy()
    Interpolacao()

def inicial_integracao():
    ini.destroy()
    pagina_integracao()
#PAGINA PRINCIPAL

ini = Frame(win)
ini["bg"] = style["fund"]
ini.pack()

    #Imagem
bg = PhotoImage(file=r"C:\Users\Gustavo Tocantins\Desktop\Projetos\Professor\Teste\a.png")
image = bg.subsample(5,5) 
label1 = Label(ini, image = image) 
label1["bg"] = style["fund"]
label1.pack()

    #Frame titulo
ini_titulo = Frame(ini)
ini_titulo["bg"] = style["fund"]
ini_titulo.pack(pady=10)

titulo = Label(ini_titulo, text="CÁLCULO NUMÉRICO", font="Calibri 45 bold",fg="white")
titulo["bg"] = style["fund"]
titulo.pack()

    #Frame dos Botões
ini_button = Frame(ini)
ini_button["bg"] = style["fund"]
ini_button.pack()
     
interpo = Button(ini_button, text="Interpolação Polinomial",bg="black",fg="white",width=40)
interpo["height"] = 2
interpo["border"] = 0
interpo["font"] = "arial 15"
interpo["command"] = inicial_interpola
interpo.pack(pady=10)

integra = Button(ini_button, text="Integração Numérica",bg="black",fg="white",width=40)
integra["height"] = 2
integra["border"] = 0
integra["font"] = "arial 15"
integra["command"] = inicial_integracao
integra.pack()

    #Frame alunos
ini_alunos = Frame(ini)
ini_alunos["bg"] = style["fund"]
ini_alunos.pack(pady=20)

alun = Label(ini_alunos, text="Alunos: Gustavo, Naoki, Eduarda e Adriano")
alun["bg"] = style["fund"]
alun["fg"] = "white"
alun.pack()



win.mainloop()
