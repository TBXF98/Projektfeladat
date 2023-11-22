#Kő-Papír-Olló-Gyík-Spock játék
import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import datetime


def main():
    nev = simpledialog.askstring("Név megadása", "Mi a neved?")
    ablak = tk.Tk()
    KPOGS(ablak, nev)
    ablak.mainloop()


class KPOGS:
    def __init__(self, root, nev):
        self.root = root
        self.root.title("Kő-Papír-Olló-Gyík-Spock")
        self.nev = nev
        self.gombfelulet()


    def gombfelulet(self):
        for valasztas in ["Kő", "Papír", "Olló", "Gyík", "Spock"]:
            tk.Button(
                text=valasztas, padx=20, pady=20, font=(20),
                command=lambda v=valasztas: self.jatek(v)
            ).pack(side=tk.LEFT, padx=20)
        magyarazo_gomb = tk.Button(self.root, text="Szabályok",padx=10, pady=10, font=(10), command=self.szabalymenu)
        magyarazo_gomb.pack(padx=10)


    def szabalymenu(self):
        szabalyokablak = tk.Toplevel(self.root)
        szabalyokablak.title("Játékszabályok")
        szabalyok = tk.Label(szabalyokablak, text=(
            "A játék szabályai:\n"
            "- Kő legyőzi az Ollót és a Gyíkot.\n"
            "- Papír legyőzi a Követ és Spock-ot.\n"
            "- Olló legyőzi a Gyíkot és a Papírt.\n"
            "- Gyík legyőzi Spock-ot és a Papírt.\n"
            "- Spock legyőzi az Ollót és a Követ."
        ))
        szabalyok.pack(pady=20)


    def jatek(self, jatekosv):
        gepv = random.choice(['Kő', 'Papír', 'Olló', 'Gyík', 'Spock'])

        eredmeny = self.eredmeny_meghatarozasa(jatekosv, gepv)

        uzenet =( self.nev + " választott: " + jatekosv + "\n" "Számítógép választott: " + gepv + "\n""Eredmény: " + eredmeny )
        messagebox.showinfo("Eredmény", uzenet)

        self.eredmeny_mentese(self.nev, jatekosv, gepv, eredmeny)

        self.root.destroy()

    def eredmeny_meghatarozasa(self, jatekosv, gepv):
        if jatekosv == gepv:
            return "Döntetlen"
        elif (
            (jatekosv == 'Kő' and gepv in ['Olló', 'Gyík']) or
            (jatekosv == 'Papír' and gepv in ['Kő', 'Spock']) or
            (jatekosv == 'Olló' and gepv in ['Gyík', 'Papír']) or
            (jatekosv == 'Gyík' and gepv in ['Spock', 'Papír']) or
            (jatekosv == 'Spock' and gepv in ['Olló', 'Kő'])
        ):
            return "Győztél!"
        else:
            return "A számítógép győzött."

    def eredmeny_mentese(self, nev, jatekosv, gepv, eredmeny):
        idopont = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("kpogs.txt", 'a', encoding='utf-8') as fajl:
            fajl.write(idopont + " - " + nev + " választása: " + jatekosv + ", Számítógép választása: " + gepv + ", Eredmény: " + eredmeny + "\n")



if __name__ == "__main__":
    main()

