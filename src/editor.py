import os
import tkinter as tk
import tkinter.font as font
from tkinter import scrolledtext
from tkinter import filedialog as tkFileDialog



class editor(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title(os.name=='posix' and 'untitled' or u'無題')
        self.file_name=None
        
        # self.root = tk.Tk()
        self.my_font = font.Font(self.master, family="MS Gothic")
    
    def custom_menu(self):
        #メニューバー
        menubar = tk.Menu(self.master, font=self.my_font)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="新規(N)", command=self.new_memo)
        filemenu.add_command(label="開く(O)...", command=self.open_memo)
        filemenu.add_command(label="上書き保存(S)", command=self.save_memo)
        filemenu.add_command(label="名前を付けて保存(A)...", command=self.saveas_memo)
        filemenu.add_separator()
        filemenu.add_command(label="メモ帳の終了(X)", command=self.master.quit)
        menubar.add_cascade(label="ファイル(F)", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="About...")
        menubar.add_cascade(label="編集(E)", menu=editmenu)


        self.master.config(menu=menubar)
    
    def create_mainwindow(self):
        # エディター
        self.text_widget = scrolledtext.ScrolledText(self.master, wrap=tk.NONE, font=self.my_font)
        self.text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.text_widget.pack(fill=tk.BOTH, expand=1)
        self.text_widget.focus_set()
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        
        self.master.title("無題 - メモ帳")
        self.master.iconbitmap(default="../image/icon.ico")
        self.master.geometry("500x250")
        
        self.custom_menu()
        
        
        
        self.master.mainloop()
    
    def new_memo(self):
        self.file_name=None
        self.master.title(os.name=='posix' and 'untitled' or u'無題')
        self.text_widget.delete('1.0', tk.END)
        
    def open_memo(self, event=None):
        fname = tkFileDialog.askopenfilename(filetypes =[('text files', '*.txt'), ('all files', '*.*')])
        if fname:
            self.text_widget.delete('1.0', tk.END)
            f=open(fname, encoding="utf-8")
            import pdb;pdb.set_trace()
            self.text_widget.insert(tk.END, f.read())
            f.close()
            self.file_name = fname
            self.master.title(fname)

    def save(self, f):
        f.write(self.text_widget.get('1.0', tk.END))
        f.close()
        
    def save_memo(self, event=None):
        if self.file_name:
            self.save(open(self.file_name, 'w'))
        else:
            self.saveas_memo()

    def saveas_memo(self):
        fname = tkFileDialog.asksaveasfilename(filetypes =[('text files', '*.txt')])
        if fname:
            self.save(open(fname, 'w'))
            self.file_name=fname
            self.master.title(fname)
            


def main():
    # main_window()
    root = tk.Tk()
    main_window = editor(root)
    main_window.create_mainwindow()


if __name__ == '__main__':

    main()