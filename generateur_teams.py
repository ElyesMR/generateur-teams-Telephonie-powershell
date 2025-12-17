import tkinter as tk
from tkinter import messagebox
import os # Indispensable pour trouver le chemin du fichier

def generer_liste():
    contenu_upn = text_area_upn.get("1.0", tk.END)
    contenu_tel = text_area_tel.get("1.0", tk.END)
    
    lignes_upn = contenu_upn.splitlines()
    lignes_tel = contenu_tel.splitlines()
    
    liste_upn_propre = [x for x in lignes_upn if x.strip()]
    liste_tel_propre = [x for x in lignes_tel if x.strip()]
    
    if len(liste_upn_propre) != len(liste_tel_propre):
        messagebox.showwarning("Attention", f"Quantités différentes !\nEmails : {len(liste_upn_propre)}\nNuméros : {len(liste_tel_propre)}")
        return

    resultat_final = ""
    
    for upn, tel in zip(liste_upn_propre, liste_tel_propre):
        clean_upn = upn.replace("mailto:", "").strip()
        clean_tel = tel.strip()
        
        # Commande 1 : Assignation
        cmd_assign = f"Set-CsPhoneNumberAssignment -Identity {clean_upn} -PhoneNumber {clean_tel} -PhoneNumberType DirectRouting"
        resultat_final += cmd_assign + "\n"
        
        # Commande 2 : Activation Voix (si coché)
        if var_voice.get():
            cmd_voice = f"Set-CsPhoneNumberAssignment -Identity {clean_upn} -EnterpriseVoiceEnabled $TRUE"
            resultat_final += cmd_voice + "\n"
        
    text_area_resultat.delete("1.0", tk.END)
    text_area_resultat.insert("1.0", resultat_final)

def copier_tout():
    fenetre.clipboard_clear()
    fenetre.clipboard_append(text_area_resultat.get("1.0", tk.END))
    label_info.config(text="Tout copié !", fg="green")

# --- Interface Graphique ---
fenetre = tk.Tk()
fenetre.title("Générateur Teams Pro")
fenetre.geometry("900x800")

# --- HEADER (LOGO + TITRE) ---
frame_header = tk.Frame(fenetre)
frame_header.pack(fill="x", pady=10, padx=10)

# --- CORRECTION DU LOGO ---
try:
    # 1. On trouve le dossier où se trouve CE fichier python
    dossier_script = os.path.dirname(os.path.abspath(__file__))
    
    # 2. On crée le chemin complet vers l'image (dossier + nom du fichier)
    chemin_image = os.path.join(dossier_script, "logo.png")
    
    # 3. On charge l'image avec ce chemin précis
    img_logo = tk.PhotoImage(file=chemin_image)
    
    # Optionnel : réduire l'image si elle est trop grosse (ici divisé par 2)
    # img_logo = img_logo.subsample(2, 2) 

    label_logo = tk.Label(frame_header, image=img_logo)
    label_logo.pack(side=tk.LEFT, padx=10)
    
    # Astuce pour éviter un bug d'affichage courant
    label_logo.image = img_logo 

except Exception as e:
    print(f"Erreur logo : {e}")
    # Si ça ne marche pas, on affiche un texte à la place
    tk.Label(frame_header, text="[Logo]", fg="red").pack(side=tk.LEFT)

# Le Titre
label_titre = tk.Label(frame_header, text="Générateur PowerShell Teams", font=("Arial", 16, "bold"))
label_titre.pack(side=tk.LEFT)

# --- Zone Supérieure ---
frame_top = tk.Frame(fenetre)
frame_top.pack(pady=5, padx=10, fill="both", expand=True)

# Colonne Gauche
frame_left = tk.Frame(frame_top)
frame_left.pack(side=tk.LEFT, fill="both", expand=True)
tk.Label(frame_left, text="1. Coller les UPN (Emails) ici :", font=("Arial", 10, "bold")).pack()
text_area_upn = tk.Text(frame_left, height=12, width=35)
text_area_upn.pack(fill="both", expand=True)

# Colonne Droite
frame_right = tk.Frame(frame_top)
frame_right.pack(side=tk.RIGHT, fill="both", expand=True)
tk.Label(frame_right, text="2. Coller les TÉLÉPHONES ici :", font=("Arial", 10, "bold")).pack()
text_area_tel = tk.Text(frame_right, height=12, width=35)
text_area_tel.pack(fill="both", expand=True)

# --- Options ---
frame_options = tk.Frame(fenetre)
frame_options.pack(pady=5)

var_voice = tk.BooleanVar()
var_voice.set(True)

case_voice = tk.Checkbutton(frame_options, text="Ajouter la commande 'EnterpriseVoiceEnabled $TRUE'", variable=var_voice, font=("Arial", 11))
case_voice.pack()

# --- Bouton ---
bouton_generer = tk.Button(fenetre, text="Générer les scripts", command=generer_liste, bg="#0078d7", fg="white", height=2, font=("Arial", 11, "bold"))
bouton_generer.pack(pady=10, ipadx=20)

# --- Résultat ---
tk.Label(fenetre, text="3. Résultat (Copier-coller dans PowerShell) :", font=("Arial", 10, "bold")).pack()
text_area_resultat = tk.Text(fenetre, height=15, fg="blue", bg="#f8f9fa")
text_area_resultat.pack(padx=10, pady=5, fill="both", expand=True)

bouton_copier = tk.Button(fenetre, text="Copier tout le résultat", command=copier_tout, bg="#dddddd")
bouton_copier.pack(pady=5)

label_info = tk.Label(fenetre, text="")
label_info.pack()

fenetre.mainloop()