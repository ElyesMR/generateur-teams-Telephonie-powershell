# 📞 Générateur de Commandes Teams PowerShell

Ce projet est une application de bureau (GUI) développée en Python qui permet d'automatiser la génération de scripts PowerShell pour la téléphonie Microsoft Teams (Direct Routing).

Il est conçu pour faciliter le travail des administrateurs systèmes en traitant des listes d'utilisateurs en masse depuis Excel.

## 🚀 Fonctionnalités

* **Interface Graphique (GUI) :** Utilisation simple sans ligne de commande grâce à Tkinter.
* **Traitement en masse (Bulk) :** Copiez-collez des colonnes entières depuis Excel (UPN et Numéros).
* **Nettoyage intelligent :**
    * Supprime automatiquement les préfixes `mailto:` collés par erreur.
    * Supprime les espaces inutiles.
* **Mode "Entreprise Voice" :** Case à cocher pour ajouter automatiquement le pavé numerique (`EnterpriseVoiceEnabled $TRUE`).
* **Génération instantanée :** Crée une liste de commandes PowerShell prête à l'emploi.

## 🛠️ Prérequis

* Python 3.x
* Module Tkinter (inclus par défaut avec Python)

## 💻 Installation et Utilisation

1.  **Cloner le projet**
    ```bash
    git clone  https://github.com/ElyesMR/generateur-teams-Telephonie-powershell.git
    ```

2.  **Lancer l'application**
    Ouvrez un terminal dans le dossier du projet et lancez :
    ```bash
    python generateur_teams.py
    ```
    *(Assurez-vous d'utiliser le bon nom de fichier si vous l'avez renommé)*

3.  **Générer les scripts**
    * Collez vos adresses emails (UPN) dans la colonne de gauche.
    * Collez vos numéros de téléphone dans la colonne de droite.
    * Cochez l'option "Enterprise Voice" si nécessaire.
    * Cliquez sur **Générer**.
    * Copiez le résultat et collez-le dans votre fenêtre PowerShell administrateur.

## 👤 Auteur

**Elyes**

---
*Projet réalisé pour automatiser l'assignation des numéros SDA (Direct Routing).*