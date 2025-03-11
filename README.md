# PDF Merger - Juntador de PDF

Um aplicativo simples para juntar múltiplos arquivos PDF em um único documento.

Criado devido a uma demanda interna do escritório de juntar de maneira simples e ilimitada diversos arquivos PDFs

## Recursos

- Interface gráfica amigável criada com Tkinter
- Suporte para selecionar múltiplos arquivos PDF
- Possibilidade de reorganizar a ordem dos PDFs antes de juntá-los
- Visualização da lista de arquivos selecionados
- Feedback visual do status das operações

## Como usar

1. **Iniciar o aplicativo**: Execute o arquivo `main.py` para abrir a interface gráfica.

2. **Adicionar arquivos**:
   - Clique no botão "Adicionar PDF" para selecionar um ou mais arquivos PDF
   - Os nomes dos arquivos selecionados aparecerão na lista

3. **Organizar arquivos**:
   - Selecione um arquivo na lista
   - Use os botões "↑ Mover para Cima" e "↓ Mover para Baixo" para reorganizar a ordem
   - A ordem na lista determina a ordem final no PDF combinado (de cima para baixo)

4. **Remover arquivos**:
   - Selecione um arquivo na lista
   - Clique no botão "Remover PDF" para removê-lo da seleção

5. **Juntar PDFs**:
   - Clique no botão "Juntar PDFs" quando estiver satisfeito com a seleção
   - Escolha um local e nome para salvar o arquivo PDF combinado
   - Aguarde a mensagem de sucesso

## Requisitos

- Python 3.6 ou superior
- PyPDF2
- Tkinter (geralmente vem pré-instalado com Python)

## Instalação

1. Clone ou baixe este repositório
2. Instale as dependências:
```
pip install PyPDF2
```
3. Execute o aplicativo:
```
python main.py
```

## Criando executável
Através da biblioteca PyInstaller,
Utilize o comando:
```
python -m PyInstaller --onefile --windowed main.py
```
Isso ira gerar as pastas build e dist se não estiverem feitas, na pasta dist terá o executável que pode ser compartilhado a outros usuários que não possuem Python instalado

## Solução de problemas

- **Erro ao juntar PDFs**: Verifique se todos os arquivos selecionados são PDFs válidos
- **Arquivos não aparecem**: Certifique-se de selecionar arquivos com extensão `.pdf`
- **Mensagem de erro**: Se ocorrer algum erro durante o processo, uma mensagem será exibida com detalhes

## Licença

Este projeto é de uso livre.
