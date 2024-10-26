
import tkinter as tk
from tkinter import messagebox
import os

# Vérifier si le fichier "mots.txt" existe
if os.path.isfile("mots.txt"):
    # Lire les mots à partir du fichier "mots.txt"
    with open("mots.txt", "r") as f:
        mots = [ligne.strip() for ligne in f if ligne.strip()]  # Supprime les lignes vides
else:
    # Utiliser la liste de mots par défaut si le fichier n'est pas trouvé
    mots = ["chat", "chien", "maison", "école", "voiture"]

class JeuDeFrappe:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Frappe")
        self.master.configure(bg="#add8e6")
        self.index = 0
        self.mots_corrects = 0  # Compteur des mots réussis du premier coup
        self.attempted_words = 0  # Compteur des tentatives de mots

        # Initialisation de l'interface
        self.label_mot = tk.Label(master, text=mots[self.index], font=("Helvetica", 24), bg="#add8e6")
        self.label_mot.pack(pady=20)

        self.entry = tk.Entry(master, font=("Helvetica", 24))
        self.entry.pack(pady=20)
        self.entry.bind('<Return>', self.verifier_mot)

        self.bouton_verifier = tk.Button(master, text="Vérifier", command=self.verifier_mot)
        self.bouton_verifier.pack(pady=20)

        self.label_resultat = tk.Label(master, text="", font=("Helvetica", 18), bg="#add8e6")
        self.label_resultat.pack(pady=20)

    def verifier_mot(self, event=None):
        mot_saisi = self.entry.get().strip()
        mot_attendu = mots[self.index]
        mot_saisi_normalized = " ".join(mot_saisi.split())

        if mot_saisi_normalized == mot_attendu:
            # Si la tentative est correcte dès le premier coup
            if self.attempted_words == self.index:
                self.mots_corrects += 1
            self.label_resultat.config(text="Correct !", fg="green")
            self.index += 1
            self.attempted_words += 1
            if self.index < len(mots):
                self.label_mot.config(text=mots[self.index])
                self.entry.delete(0, tk.END)
            else:
                self.afficher_resultat()
        else:
            self.label_resultat.config(text="Essaye encore.", fg="red")
            self.entry.delete(0, tk.END)

    def afficher_resultat(self):
        # Calculer et afficher le taux de réussite dès le premier coup
        # taux_reussite = (self.mots_corrects / len(mots)) * 100
        #message = f"Vous avez terminé la dictée !\nTaux de réussite (sans erreurs dès le premier coup) : {taux_reussite:.2f}%"
        message = f"Vous avez terminé la dictée !\n"
        
        # Demander si l'utilisateur veut recommencer
        if messagebox.askyesno("Félicitations", f"{message}\nVoulez-vous recommencer ?"):
            self.recommencer()
        else:
            self.master.quit()

    def recommencer(self):
        # Réinitialiser les compteurs et l'interface pour une nouvelle dictée
        self.index = 0
        self.mots_corrects = 0
        self.attempted_words = 0
        self.label_mot.config(text=mots[self.index])
        self.label_resultat.config(text="")
        self.entry.delete(0, tk.END)

root = tk.Tk()
jeu = JeuDeFrappe(root)
root.mainloop()
