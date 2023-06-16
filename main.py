import bin
import install as i
from gui import *
from PIL import Image
from elevate import elevate

elevate(False)
root = CTk()
root.title("Installer")
root.geometry("700x500")
root.resizable(False, False)
set_appearance_mode("dark")

def install():
    button_install.configure(state="disabled")
    i.install(root, canvas)

def close():
    root.quit()

if not bin.files_check():
    bin.load()

canvas = CTkCanvas(
    root,
    width=700,
    height=500,
    bg="gray14",
    highlightcolor="gray14"
)
canvas.create_line(0, 64, 700, 64, fill="white")
canvas.create_text(50, 32, text="Windows New", justify="center", fill="white")

png = CTkLabel(
    canvas,
    text="",
    height=0,
    image=CTkImage(
        Image.open(f"{os.path.expanduser('~')}\\i.png"),
        size=(64, 64)
    )
)

description = CTkTextbox(
    canvas,
    width=690,
    height=400
)

button_install = CTkButton(
    canvas,
    text="Далее",
    width=0,
    height=0,
    text_color="white",
    command=install
)

png.place(x=634, y=0)
description.place(x=5, y=66)
button_install.place(x=650, y=475)
canvas.pack()

description.insert(END, "PyProgram v 1.0.3.4567\nКакое-то описание и сарказм))")
description.configure(state="disabled")
description.tag_add("program", "1.0", "1.9")
description.tag_config("program", foreground="springgreen")

root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()