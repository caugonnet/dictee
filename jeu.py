
import tkinter as tk
from tkinter import messagebox

# Liste des mots de la dictée
mots = ["chat", "chien", "maison", "école", "voiture"]

class JeuDeFrappe:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Frappe")
        self.index = 0

        self.label_mot = tk.Label(master, text=mots[self.index], font=("Helvetica", 24))
        self.label_mot.pack(pady=20)

        self.entry = tk.Entry(master, font=("Helvetica", 24))
        self.entry.pack(pady=20)
        self.entry.bind('<Return>', self.verifier_mot)

        self.bouton_verifier = tk.Button(master, text="Vérifier", command=self.verifier_mot)
        self.bouton_verifier.pack(pady=20)

        self.label_resultat = tk.Label(master, text="", font=("Helvetica", 18))
        self.label_resultat.pack(pady=20)

    def verifier_mot(self, event=None):
        # Récupérer le mot saisi et le mot attendu
        mot_saisi = self.entry.get().strip()
        mot_attendu = mots[self.index]

        # Nettoyer les espaces en excès du mot saisi
        mot_saisi_normalized = " ".join(mot_saisi.split())

        # Vérification du mot normalisé contre le mot attendu
        if mot_saisi_normalized == mot_attendu:
            self.label_resultat.config(text="Correct !", fg="green")
            self.index += 1
            if self.index < len(mots):
                self.label_mot.config(text=mots[self.index])
                self.entry.delete(0, tk.END)
            else:
                messagebox.showinfo("Félicitations", "Vous avez terminé la dictée !")
                self.master.quit()
        else:
            self.label_resultat.config(text="Essaye encore.", fg="red")
            self.entry.delete(0, tk.END)

root = tk.Tk()
jeu = JeuDeFrappe(root)
root.mainloop()
