import os
import shutil
from gui import *
from tkinter import ttk
from zipfile import ZipFile
from win32com.client import Dispatch



def install(master: CTk, canvas: CTkCanvas):
    def size_processing(n: int) -> str:
        sizes = {
            1024: "КБ",
            1048576: "МБ",
            1073741824: "ГБ",
            1099511627776: "ТБ"
        }
        s = []
        name = []
        for i in sizes:
            n_2 = n // i
            if n_2 != 0:
                s.append(n_2)
                name.append(sizes[i])
        if s != []:
            for sn in sizes:
                n_2 = n // sn
                if n_2 == min(s):
                    return f"{min(s)} {sizes[sn]}"
        else:
            return f"{n} байт"
    
    def create_lnk(path: str, target: str, wDir: str):
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        #shortcut.IconLocation = icon
        shortcut.save()
    
    def reinstall():
        if os.path.exists("C:\\Program Files\\MyProgram"):
            uninstall()
            install_p()
        else:
            install_p()

    def uninstall():
        shutil.rmtree("C:\\Program Files\\MyProgram")
        os.remove(f"{os.path.expanduser('~')}\\Desktop\\MyProgram.lnk")
        os.remove("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\MyProgram.lnk")
    
    def install_p():
        if os.path.exists("C:\\Program Files\\MyProgram"):
            os.remove(f"{os.path.expanduser('~')}\\i.png")
            os.remove(f"{os.path.expanduser('~')}\\p.zip")
        else:
            print("Install 1 begin.")
            os.mkdir(f"C:\\Program Files\\MyProgram")
            path = f"C:\\Program Files\\MyProgram"
            z.extractall(path)
            print("Install 1 end.")
            print("Install 2 begin.")
            path = f"{os.path.expanduser('~')}\\Desktop\\MyProgram.lnk"
            target = r"C:\\Program Files\\MyProgram\\PyProgram.exe"
            wDir = r"C:\\Program Files\\MyProgram"
            create_lnk(path, target, wDir)
            create_lnk(
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\MyProgram.lnk",
                target,
                wDir
            )
            print("Install END.")
        
            state.configure(text="Установлено", text_color="green")

    canvas.destroy()
    z = ZipFile(f"{os.path.expanduser('~')}\\p.zip")
    info = z.infolist()

    files = [text_file.filename for text_file in info]
    size = [text_file.file_size for text_file in info]
    data = []
    for i in range(0, len(files)):
        data.append([files[i], size_processing(size[i])])

    ttk.Style().configure("BW.TLabel", foreground="white", background="gray14")
    table = ttk.Treeview(
        master,
        columns=("Файл", "Размер"),
        show="headings",
        style="BW.TLabel"
    )
    table.heading("Файл", text="Файл")
    table.heading("Размер", text="Размер")

    for file in data:
        table.insert("", END, values=file)

    state = CTkLabel(
        master,
        text="Не установлено",
        text_color="red"
    )

    frame = CTkFrame(
        master,
        fg_color="gray14"
    )

    install_b = CTkButton(
        frame,
        text="Установить",
        corner_radius=0,
        command=install_p
    )

    uninstall_b = CTkButton(
        frame,
        text="Удалить",
        corner_radius=0,
        command=uninstall
    )


    state.pack(side="bottom", anchor="nw")
    frame.place(relx=0.5, rely=0.5, anchor="center")
    install_b.pack(fill="x")

    if os.path.exists("C:\\Program Files\\MyProgram"):
        state.configure(text="У вас уже установлено", text_color="green")
        install_b.configure(text="Переустановить", command=reinstall)
        uninstall_b.pack(fill="x")

    #if os.path.exists(f"C:\Program Files\\MyProgram"):
    #    state.configure(text="У вас уже установлено", text_color="green")
    #    os.remove(f"{os.path.expanduser('~')}\\i.png")
    #    os.remove(f"{os.path.expanduser('~')}\\p.zip")
    #else:
    #    print("Install 1 begin.")
    #    os.mkdir(f"C:\\Program Files\\MyProgram")
    #    path = f"C:\\Program Files\\MyProgram"
    #    z.extractall(path)
    #    print("Install 1 end.")
    #    print("Install 2 begin.")
    #    os.symlink(
    #        dst="C:\\Program Files\\MyProgram\\PyProgram.exe",
    #        src="C:\\Users\\Lenovo\\Desktop\\MyProgram.lnk",
    #        target_is_directory=True
    #    )
    #    print("Install END.")
    #    os.remove(f"{os.path.expanduser('~')}\\i.png")
    #    os.remove(f"{os.path.expanduser('~')}\\p.zip")
    #
    #    state.configure(text="Установлено", text_color="green")
