# Emissor de DANFE

Este projeto utiliza o script `emitir_danfe.py` e/ou o arquivo executável `emitir_danfe.exe` para automatizar o processo de emissão de DANFEs (Documento Auxiliar da Nota Fiscal Eletrônica), integrando a inserção de chaves diretamente em um sistema via interface gráfica e automação de navegador.

## Funcionalidades

- **Abrir Campos**: Abre automaticamente campos necessários para a inserção das chaves no sistema.
- **Colar Chaves**: Extrai chaves de um arquivo Excel e as cola no sistema.
- **Verificar Quantidade de Campos**: Conta quantos campos estão disponíveis na planilha a partir da célula A10.
- **Exibir Orientações**: Mostra orientações sobre como utilizar o sistema e configurar o ambiente.

## Pré-requisitos

- **Python 3.x**
- Bibliotecas Python:
  - `tkinter`
  - `pandas`
  - `pyautogui`
  - `webbrowser`
  - `time`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/LucianoBast7/Emitir_Danfe_Almenat.git
   ```
# Interface Principal

Selecione uma das opções na interface gráfica:

- **Abrir Campos**: Digite o número de campos e clique para abrir automaticamente os campos no sistema.
- **Colar Chaves**: Seleciona um arquivo Excel contendo as chaves para colar no sistema.
- **Orientações**: Exibe orientações sobre como usar o sistema corretamente.

## Estrutura do Código

- **Função `abrir_campos`**: Automatiza o processo de abertura de campos no navegador utilizando a biblioteca `pyautogui`.
- **Função `principal`**: Gerencia a seleção do arquivo Excel, conta as chaves e realiza o processo de colagem automática.
- **Função `interface_abrir_campos`**: Interface gráfica para inserir o número de campos a serem abertos.
- **Função `interface`**: Interface principal que oferece várias opções para o usuário.

# Notas Importantes

## Orientações:
- Mantenha o navegador aberto no monitor da direita.
- Certifique-se de que o sistema IOB esteja aberto na aba "Documentos Referenciados".
- Para notas com mais de 100 chaves, o número de campos abertos precisa ser múltiplo de 10.
