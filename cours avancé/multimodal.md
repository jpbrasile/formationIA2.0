## Animer des objets 3D
- [00:00](https://www.youtube.com/watch?v=M5CexnLe4dg&t=0s) 🎶 Introduction et prérequis

  - Pour animer des objets en 3D, vous aurez besoin de Blender et de Mixamo.
  - Assurez-vous d'avoir un compte Adobe, c'est gratuit.
  - Présentation des exemples et des étapes à suivre.


- [01:05](https://www.youtube.com/watch?v=M5CexnLe4dg&t=65s) 🖥️ Importation de l'objet 3D dans Blender

  - Ouvrez Blender, importez l'objet au format OBJ.
  - Effectuez des ajustements, comme la rotation et le lissage des matériaux.
  - Préparation de l'objet pour l'animation.


- [05:34](https://www.youtube.com/watch?v=M5CexnLe4dg&t=334s) 🎨 Nettoyage de la texture UV

  - Importez une image de fond pour projeter sur le modèle 3D.
  - Utilisation de l'éditeur UV pour optimiser la texture.
  - Répartition de la texture sur l'objet en deux parties.


- [06:40](https://www.youtube.com/watch?v=M5CexnLe4dg&t=400s) 📦 Exportation vers Mixamo

  - Exportez le modèle en format FBX depuis Blender.
  - Utilisez Mixamo pour appliquer des animations au personnage.
  - Réglages pour l'exportation, y compris l'incorporation des textures.


- [08:47](https://www.youtube.com/watch?v=M5CexnLe4dg&t=527s) 🎬 Partage de l'animation

  - Deux méthodes de partage : capture d'écran avec Snipping Tool ou téléchargement du fichier FBX.
  - Démonstration rapide de l'utilisation de Snipping Tool.
  - Importation du fichier FBX dans Blender pour la visualisation et l'exportation finale.


- [12:23](https://www.youtube.com/watch?v=M5CexnLe4dg&t=743s) 🎥 Assemblage dans Adobe Premiere

  - Importation de la séquence d'images dans Adobe Premiere.
  - Création d'une vidéo à partir des images.
  - Aperçu rapide du processus d'assemblage dans Premiere.
 
## Créer un [audiobook](https://blog.finxter.com/how-i-created-an-audiobook-app-with-streamlit/) avec streamlit
- L'auteur a créé un didacticiel sur la création d'une application d'audiobook avec Streamlit.
- L'application permet aux utilisateurs de télécharger des livres au format PDF, TXT, DOCX ou EPUB.
- Le texte est extrait des fichiers en fonction de leur format.
- Le texte extrait est converti en audio à l'aide de la bibliothèque gTTS (Google Text-to-Speech).
- Un lecteur audio est intégré à l'application pour permettre aux utilisateurs d'écouter l'audiobook.
- L'application est conçue pour les développeurs Python qui souhaitent ajouter un projet à leur portfolio.
-L'auteur encourage les lecteurs à déployer l'application sur [Streamlit Cloud](https://sree369nidhi-audiobook-pdf-to-audiobook-42v3t3.streamlit.app/) pour une utilisation pratique.
### Faire en sorte qu'il s'active dès l'ouverture de la page
- Pour lire automatiquement un fichier audio dans une application Streamlit après l'avoir généré avec la bibliothèque de synthèse vocale Google Text-to-Speech, vous pouvez utiliser le code suivant comme exemple. Ce code repose sur l'utilisation d'une fonction personnalisée pour encoder le fichier audio en base64 et l'insérer dans un élément HTML `<audio>` avec l'attribut `autoplay` activé.

- La [référence](https://discuss.streamlit.io/t/how-to-play-an-audio-file-automatically-generated-using-text-to-speech-in-streamlit/33201) qui a permis à Harpa.ai de générer le code 

- Voici un exemple complet d'application Streamlit pour jouer automatiquement un fichier audio :

```python
import streamlit as st
import base64

# Fonction pour lire automatiquement un fichier audio
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as audio_file:
        audio_data = audio_file.read()
    audio_base64 = base64.b64encode(audio_data).decode()
    audio_html = f"""
    <audio controls autoplay="true">
    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# Exemple d'utilisation de la fonction
st.write("# Application de lecture automatique d'audio")
st.write("Cet audio se jouera automatiquement à l'ouverture de la page.")

# Indiquez ici le chemin vers votre fichier audio
file_path = "votre_fichier_audio.mp3"
autoplay_audio(file_path)
```

Ce code fonctionne de la manière suivante :
- La fonction `autoplay_audio` prend le chemin d'un fichier audio et le lit.
- Elle encode ensuite le contenu du fichier en base64, nécessaire pour l'incorporer dans un élément HTML.
- Un élément HTML `<audio>` est créé avec l'attribut `autoplay` pour lancer la lecture dès que la page est chargée.
- L'élément HTML est inséré dans la page Streamlit avec `st.markdown` et `unsafe_allow_html=True`.

Assurez-vous que le fichier audio que vous voulez jouer (`votre_fichier_audio.mp3`) est accessible par le script.

## Animer une image à partir d'une vidéo:

https://www.youtube.com/watch?v=vPziSNI35Io&t=12s 
