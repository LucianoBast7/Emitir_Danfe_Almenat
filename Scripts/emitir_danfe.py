import tkinter as tk
from tkinter import filedialog
import pandas as pd
import webbrowser as web
import pyautogui
import time
from tkinter import messagebox

def abrir_campos(campos):
        import webbrowser as web
        import pyautogui
        import time
        
        print(f"Abrindo {campos} campos no IOB...")
        site = "https://www.google.com"  
        x = 3082  
        y = 252  

        web.open(site)  
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')  
        time.sleep(0.5)
        pyautogui.click(x, y)  
        time.sleep(0.5)
        for _ in range(16):
            pyautogui.press('tab') 
        time.sleep(0.5)

        if campos <= 100:
            for _ in range(campos):
                pyautogui.press('enter')  
                time.sleep(0.25)
            time.sleep(5)
            print('Concluído!')
            print('\n')

        elif campos ==110: 
            campos11 = int(campos / 11) 
            for _ in range(campos11): 
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos11):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos11):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos11):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos11):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos11):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos11):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos11):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos11):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos11):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130) 
            for _ in range(campos11):
                pyautogui.press('enter') 
                time.sleep(0.50)
            time.sleep(50)
            print('Concluído!')

        elif campos ==120:
            campos12 = int(campos / 12)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos12):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            print('Concluído!')

        elif campos ==130:
            campos13 = int(campos / 13)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos13):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            print('Concluído!')

        elif campos ==140:
            campos14 = int(campos / 14)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos14):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            print('Concluído!')

        elif campos == 150:  # Tempo médio de execução entre 7 e 9 minutos
            campos15 = int(campos / 15)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos15):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            print('Concluído!')

        elif campos == 160:
            campos16 = int(campos / 16)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos16):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            print('Concluído!')

        elif campos == 170:
            campos17 = int(campos / 17)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(1)
            time.sleep(120)
            for _ in range(campos17):
                pyautogui.press('enter')
                time.sleep(1)
            time.sleep(120)
            print('Concluído!')

        elif campos == 180:
            campos18 = int(campos / 18)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos18):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            print('Concluído!')

        elif campos == 190:
            campos19 = int(campos / 19)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos19):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            print('Concluído!')

        elif campos == 200:  # Tempo médio para a execução entre 18 e 20 minutos
            campos20 = int(campos / 20)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.25)
            time.sleep(130)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(50)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            for _ in range(campos20):
                pyautogui.press('enter')
                time.sleep(0.50)
            time.sleep(120)
            print('Concluído!')


def principal():
    def selecionar_arquivo_excel():
        raiz = tk.Tk()
        raiz.withdraw()
        caminho_arquivo = filedialog.askopenfilename(
            filetypes=[("Arquivos Excel", "*.xlsx *.xls *.xlsm")],
            title="Selecione a planilha"
        )
        if caminho_arquivo:
            try:
                dados = pd.read_excel(caminho_arquivo)
                print('\n')
                print("Arquivo carregado com sucesso!")
                print('\n')
                return dados, caminho_arquivo
            except Exception as e:
                print(f"Erro ao carregar o arquivo: {e}")
                return None, None
        else:
            print("Nenhum arquivo selecionado.")
            return None, None

    def contar_coluna_a_a_partir_de_a10(dados):
        dados_coluna_a = dados.iloc[8:, 0]
        contagem = dados_coluna_a.dropna().shape[0]
        return contagem

    def colar_chaves(chaves):
        site = "https://www.google.com"
        x = 3082
        y = 252

        web.open(site)
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(0.5)
        pyautogui.click(x, y)
        time.sleep(0.5)
        for _ in range(18):
            pyautogui.press('tab')
        for i, chave in enumerate(chaves):
            pyautogui.typewrite(str(chave))
            time.sleep(0.25)
            if i < len(chaves) - 1:
                for _ in range(4):
                    pyautogui.press('tab')
                    time.sleep(0.25)
    
    mensagem = "Concluído"
    dados, caminho_arquivo = selecionar_arquivo_excel()
    for _ in range(1):
        if dados is not None and caminho_arquivo is not None:
            contagem = contar_coluna_a_a_partir_de_a10(dados)
            print(f"Total de Chaves: {contagem}")
            print('\n')
            chaves = dados.iloc[8:, 0].dropna().tolist()
            colar_chaves(chaves)
            messagebox.showinfo("", mensagem)

def orientacoes_de_uso():
    def exibir_mensagem():
        mensagem = "1. Deixar o navegador aberto no monitor da direita\n\n2. Deixar a tela do IOB aberta na aba: Documentos Referenciados\n\n3. Deixar o site IOB na guia mais a direita do browser\n\n4. Se o Total de chaves for maior do que 100, o numero de campos abertos precisa terminar com 0, ou seja, para uma nota de 122 chaves, devem ser abertor 130 campos, para uma de 187, devem ser abertos 190, e assim por diante"
        messagebox.showinfo("Orientações de Uso", mensagem)


    def botao():
        root = tk.Tk()
        root.title("Orientações - Uso do Progrma")
        root.geometry("400x200")

        label_orientacoes = tk.Label(root, text="Clique aqui para ver as orientações:")
        label_orientacoes.pack(pady=20)

        botao_orientacoes = tk.Button(root, text="Exibir Orientações", command=exibir_mensagem)
        botao_orientacoes.pack()

        sair_button = tk.Button(root, text="Voltar a Tela Principal", command=root.destroy)
        sair_button.pack(pady=10)
        root.mainloop()

    botao()

def verificar_quantidades_campos():
    
    def selecionar_arquivo_excel():
        raiz = tk.Tk()
        raiz.withdraw()
        caminho_arquivo = filedialog.askopenfilename(
            filetypes=[("Arquivos Excel", "*.xlsx *.xls *.xlsm")],
            title="Selecione a planilha"
        )
        if caminho_arquivo:
            try:
                dados = pd.read_excel(caminho_arquivo)
                print("\nArquivo carregado com sucesso!\n")
                return dados, caminho_arquivo
            except Exception as e:
                print(f"Erro ao carregar o arquivo: {e}")
                return None, None
        else:
            print("Nenhum arquivo selecionado.")
            return None, None
    
    def contar_coluna_a_a_partir_de_a10(dados):
        dados_coluna_a = dados.iloc[8:, 0]  
        contagem = dados_coluna_a.dropna().shape[0]  
        return contagem
    
    def obter_valor_danfe(dados):
        valor_danfe = dados.iloc[6, 4]
        if pd.isna(valor_danfe):
            return "Valor não disponível"
        else:
            return valor_danfe
    dados, caminho_arquivo = selecionar_arquivo_excel()

    if dados is not None and caminho_arquivo is not None:
        contagem = contar_coluna_a_a_partir_de_a10(dados)
        valor_danfe = obter_valor_danfe(dados)
        
        messagebox.showinfo("Total", f"Campos: {contagem}\nValor DANFE: {str(valor_danfe)}")


def interface_abrir_campos():
    root = tk.Tk()
    root.title("Abrir Campos - IOB Emissor")
    root.geometry("400x250")
    mensagem = "Concluído"

    def abrir_campos_callback():
        try:
            for _ in range(1):    
                campos = int(entry.get())
                abrir_campos(campos)
                messagebox.showinfo("", mensagem)
        except ValueError:
            print("Por favor, digite um número válido.")

    def verificar_campos_excel():
        verificar_quantidades_campos()
        
    frame = tk.Frame(root)
    frame.pack(pady=20)
    label = tk.Label(frame, text="Quantos campos serão abertos?")
    label.pack()
    entry = tk.Entry(frame)
    entry.pack()

    abrir_button = tk.Button(frame, text="Abrir Campos", command=abrir_campos_callback)
    abrir_button.pack(pady=10)

    verificar_campos = tk.Button(frame,text="Verificar Quantidade", command=verificar_campos_excel)
    verificar_campos.pack(pady=10)

    sair_button = tk.Button(frame, text="Voltar a Tela Principal", command=root.destroy)
    sair_button.pack(pady=10)
    root.mainloop()

        
def interface():
    root = tk.Tk()
    root.title("Emitir DANFE")
    root.geometry("400x250")

    def colar_chaves():
        principal()

    def orientacoes1():
        orientacoes_de_uso()

    frame = tk.Frame(root)
    frame.pack(pady=20)
    label = tk.Label(frame, text="Selecione uma opção")
    label.pack()

    abrir_campos_button = tk.Button(frame, text ="1. Abrir Campos", command=interface_abrir_campos)
    abrir_campos_button.pack(pady=10)

    colar_chaves_button = tk.Button(frame, text="2. Colar Chaves", command=colar_chaves)
    colar_chaves_button.pack(pady=10)

    orientacoes_button = tk.Button(frame, text="3. Orientações", command=orientacoes1)
    orientacoes_button.pack(pady=10)

    sair_button = tk.Button(frame, text="0. Sair do Sistema", command=root.quit)
    sair_button.pack(pady=10)
    root.mainloop()
            
if __name__ == "__main__":
    interface()