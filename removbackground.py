from rembg import remove
from PIL import Image, ImageTk
from tkinter import filedialog, Tk

def remover_fundo(input_path, output_path):
    try:
        # Abrir a imagem de entrada
        input_imagem = Image.open(input_path)

        # Remover o fundo usando a biblioteca rembg
        output_imagem = remove(input_imagem)

        # Salvar a imagem de saída
        output_imagem.save(output_path)
        print("Fundo removido com sucesso e imagem salva em", output_path)

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

def selecionar_arquivo():
    # Abrir uma janela de seleção de arquivo
    filepath = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif")])
    return filepath

if __name__ == "__main__":
    # Usar Tkinter para selecionar o arquivo de entrada
    root = Tk()
    root.withdraw()  # Ocultar a janela principal do Tkinter
    input_path = selecionar_arquivo()

    # Verificar se o caminho do arquivo é válido antes de continuar
    if not input_path:
        print("Nenhum arquivo selecionado. Encerrando.")
    else:
        # Permitir que o usuário escolha o local e o formato ao salvar a imagem
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Imagens PNG", "*.png")])

        # Verificar se o caminho de saída é válido antes de continuar
        if output_path:
            remover_fundo(input_path, output_path)
        else:
            print("Nenhum local de salvamento selecionado. Encerrando.")
