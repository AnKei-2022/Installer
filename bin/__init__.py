import os
from .bin import png, zip_f



def load():
    with open(f"{os.path.expanduser('~')}\\i.png", "bw") as f:
        f.write(png)
    with open(f"{os.path.expanduser('~')}\\p.zip", "bw") as f:
        f.write(zip_f)
    


def files_check() -> bool:
    n_1 = os.path.exists(f"{os.path.expanduser('~')}\\i.png")
    n_2 = os.path.exists(f"{os.path.expanduser('~')}\\p.zip")
    return n_1 and n_2
