import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juntador de PDF")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Colors
        self.primary_color = "#4361ee"
        self.secondary_color = "#3f37c9"
        self.accent_color = "#4cc9f0"
        self.bg_color = "#f0f0f0"
        self.text_color = "#333333"
        
        # Store selected PDF file paths
        self.pdf_files = []
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Title label with decorative underline
        title_frame = tk.Frame(main_frame, bg=self.bg_color)
        title_frame.pack(fill="x", pady=10)
        
        title_label = tk.Label(
            title_frame, 
            text="Juntador de PDF",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        title_label.pack()
        
        separator = tk.Frame(title_frame, height=2, width=200, bg=self.primary_color)
        separator.pack(pady=8)
        
        # Files selection section
        files_frame = tk.LabelFrame(
            main_frame, 
            text="Selecione os arquivos", 
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            padx=15, 
            pady=15
        )
        files_frame.pack(fill="both", expand=True, pady=10)
        
        # PDF list and controls
        list_controls_frame = tk.Frame(files_frame, bg=self.bg_color)
        list_controls_frame.pack(side="left", fill="both", expand=True)
        
        # Files listbox with scrollbar
        list_frame = tk.Frame(list_controls_frame, bg=self.bg_color)
        list_frame.pack(fill="both", expand=True, pady=5)
        
        self.files_listbox = tk.Listbox(
            list_frame,
            selectmode=tk.SINGLE,
            height=10,
            bd=2,
            relief=tk.GROOVE,
            font=("Helvetica", 9),
            bg="white",
            selectbackground=self.accent_color
        )
        self.files_listbox.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.files_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.files_listbox.config(yscrollcommand=scrollbar.set)
        
        # Buttons for file operations
        buttons_frame = tk.Frame(files_frame, bg=self.bg_color, padx=10)
        buttons_frame.pack(side="right", fill="y")
        
        add_button = tk.Button(
            buttons_frame,
            text="Adicionar PDF",
            command=self.add_pdf,
            bg=self.accent_color,
            fg="white",
            activebackground=self.primary_color,
            activeforeground="white",
            width=15,
            bd=1,
            pady=5
        )
        add_button.pack(pady=5)
        
        remove_button = tk.Button(
            buttons_frame,
            text="Remover PDF",
            command=self.remove_pdf,
            bg=self.accent_color,
            fg="white",
            activebackground=self.primary_color,
            activeforeground="white",
            width=15,
            bd=1,
            pady=5
        )
        remove_button.pack(pady=5)
        
        move_up_button = tk.Button(
            buttons_frame,
            text="↑ Mover para Cima",
            command=self.move_pdf_up,
            bg=self.accent_color,
            fg="white",
            activebackground=self.primary_color,
            activeforeground="white",
            width=15,
            bd=1,
            pady=5
        )
        move_up_button.pack(pady=5)
        
        move_down_button = tk.Button(
            buttons_frame,
            text="↓ Mover para Baixo",
            command=self.move_pdf_down,
            bg=self.accent_color,
            fg="white",
            activebackground=self.primary_color,
            activeforeground="white",
            width=15,
            bd=1,
            pady=5
        )
        move_down_button.pack(pady=5)
        
        # Action section
        action_frame = tk.Frame(main_frame, bg=self.bg_color)
        action_frame.pack(fill="x", pady=15)
        
        # Merge button
        merge_button = tk.Button(
            action_frame, 
            text="Juntar PDFs", 
            command=self.merge_pdfs,
            bg=self.primary_color, 
            fg="white", 
            font=("Helvetica", 12, "bold"),
            activebackground=self.secondary_color,
            activeforeground="white",
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        merge_button.pack(pady=5)
        
        # Status bar
        status_frame = tk.Frame(main_frame, bg=self.bg_color)
        status_frame.pack(fill="x", side="bottom")
        
        self.status_label = tk.Label(
            status_frame, 
            text="Pronto para juntar arquivos PDF",
            bg=self.bg_color,
            fg="#666666",
            font=("Helvetica", 8)
        )
        self.status_label.pack(side="left")
        
        # Counter for files
        self.counter_label = tk.Label(
            status_frame,
            text="0 arquivos selecionados",
            bg=self.bg_color,
            fg="#666666",
            font=("Helvetica", 8)
        )
        self.counter_label.pack(side="right")
        
    def add_pdf(self):
        file_paths = filedialog.askopenfilenames(
            title="Selecionar arquivos PDF",
            filetypes=[("PDF Files", "*.pdf")]
        )
        
        if file_paths:
            for file_path in file_paths:
                self.pdf_files.append(file_path)
                self.files_listbox.insert(tk.END, os.path.basename(file_path))
            
            self.update_counter()
            self.status_label.config(text=f"{len(file_paths)} arquivo(s) adicionado(s)")
    
    def remove_pdf(self):
        selected_index = self.files_listbox.curselection()
        
        if not selected_index:
            messagebox.showinfo("Aviso", "Nenhum arquivo selecionado para remover.")
            return
        
        index = selected_index[0]
        filename = self.files_listbox.get(index)
        self.files_listbox.delete(index)
        self.pdf_files.pop(index)
        self.update_counter()
        self.status_label.config(text=f"Arquivo removido: {filename}")
    
    def move_pdf_up(self):
        selected_index = self.files_listbox.curselection()
        
        if not selected_index:
            messagebox.showinfo("Aviso", "Nenhum arquivo selecionado para mover.")
            return
            
        index = selected_index[0]
        if index == 0:
            return  # Already at the top
            
        # Swap in the list
        self.pdf_files[index], self.pdf_files[index-1] = self.pdf_files[index-1], self.pdf_files[index]
        
        # Update listbox
        filename = self.files_listbox.get(index)
        self.files_listbox.delete(index)
        self.files_listbox.insert(index-1, filename)
        self.files_listbox.selection_set(index-1)
        self.status_label.config(text=f"Arquivo movido para cima: {filename}")
    
    def move_pdf_down(self):
        selected_index = self.files_listbox.curselection()
        
        if not selected_index:
            messagebox.showinfo("Aviso", "Nenhum arquivo selecionado para mover.")
            return
            
        index = selected_index[0]
        if index == len(self.pdf_files) - 1:
            return  # Already at the bottom
            
        # Swap in the list
        self.pdf_files[index], self.pdf_files[index+1] = self.pdf_files[index+1], self.pdf_files[index]
        
        # Update listbox
        filename = self.files_listbox.get(index)
        self.files_listbox.delete(index)
        self.files_listbox.insert(index+1, filename)
        self.files_listbox.selection_set(index+1)
        self.status_label.config(text=f"Arquivo movido para baixo: {filename}")
    
    def update_counter(self):
        count = len(self.pdf_files)
        text = f"{count} arquivo{'s' if count != 1 else ''} selecionado{'s' if count != 1 else ''}"
        self.counter_label.config(text=text)
    
    def merge_pdfs(self):
        if len(self.pdf_files) < 2:
            messagebox.showerror("Erro", "Por favor selecione pelo menos 2 PDFs para juntar.")
            return
            
        try:
            self.status_label.config(text="Processando...")
            self.root.update()
            
            # Create a PdfMerger object
            merger = PdfMerger()
            
            # Append all the PDFs to the merger
            for pdf_file in self.pdf_files:
                merger.append(pdf_file)
            
            # Ask user where to save the merged PDF
            output_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
                title="Salvar PDF Unido Como"
            )
            
            if output_path:
                # Write the merged PDF to the output file
                with open(output_path, "wb") as output_file:
                    merger.write(output_file)
                
                self.status_label.config(text=f"PDFs unidos com sucesso! Salvo em: {os.path.basename(output_path)}")
                messagebox.showinfo("Sucesso", f"{len(self.pdf_files)} PDFs unidos com sucesso!\nSalvo em: {output_path}")
            else:
                self.status_label.config(text="Operação cancelada pelo usuário.")
            
            # Close the merger
            merger.close()
            
        except Exception as e:
            self.status_label.config(text=f"Erro: {str(e)}")
            messagebox.showerror("Erro", f"Um erro ocorreu: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
