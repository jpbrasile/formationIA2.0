## Equivalent de ChatGPT (multimodal et avec mémoire RAG) en local
### Tuto en Video
- [00:00](https://youtu.be/CUjO8b6_ZuM?t=0s) 🎬 Introduction au projet
  - Création d'une application de chat multimodale locale avec des modèles locaux.
  - Fonctionnalités telles que la gestion vocale, la description d'images et la conversation avec des fichiers PDF.

- [02:01](https://youtu.be/CUjO8b6_ZuM?t=121s) 🛠️ Configuration de l'environnement de développement
  - Mise en place de l'environnement Python avec les dépendances requises.
  - Utilisation de Streamlit comme interface frontend pour l'application.

- [06:10](https://youtu.be/CUjO8b6_ZuM?t=370s) 🤖 Intégration de GPT-3 pour les réponses
  - Création de la logique pour envoyer les questions de l'utilisateur au modèle GPT-3 et afficher les réponses.
  - Gestion de la mémoire de la conversation pour suivre les échanges.

- [15:19](https://youtu.be/CUjO8b6_ZuM?t=919s) 📜 Gestion de l'historique du chat
  - Affichage de l'historique des conversations dans l'interface utilisateur.
  - Mise en place d'une barre latérale pour basculer entre les sessions de chat précédentes.

- [20:30](https://youtu.be/CUjO8b6_ZuM?t=1230s) 💾 Sauvegarde et chargement de l'historique du chat
  - Création de fonctions pour sauvegarder et charger l'historique du chat au format JSON.
  - Gestion de la persistance des conversations pour les sessions futures.
- [22:31](https://youtu.be/CUjO8b6_ZuM?t=1351s) 🤖 Fonction de sauvegarde de l'historique du chat

  - La fonction de sauvegarde de l'historique du chat est définie pour gérer la sauvegarde de l'historique des messages du chat dans l'application.

- [24:20](https://youtu.be/CUjO8b6_ZuM?t=1460s) 🗝️ Gestion de la clé de session

  - La gestion de la clé de session permet de gérer les sessions de chat et de créer de nouvelles clés de session si nécessaire.

- [31:12](https://youtu.be/CUjO8b6_ZuM?t=1872s) 🎤 Traitement audio

  - L'intégration du traitement audio permet d'enregistrer et de transcrire des messages vocaux dans l'application.

- [39:31](https://youtu.be/CUjO8b6_ZuM?t=2371s) 📷 Traitement des images

  - L'intégration du traitement des images permet de télécharger des images et de générer des descriptions en texte basées sur les images téléchargées.
- [45:02](https://www.youtube.com/watch?v=CUjO8b6_ZuM&t=2702s) 🛠️ Configuration du traitement des images

  - Configuration du traitement des images,
  
  - Explication du traitement des images dans l'application de chat.

- [46:12](https://www.youtube.com/watch?v=CUjO8b6_ZuM&t=2772s) 📄 Traitement des fichiers PDF

  - Chargement de la base de données vectorielle pour les fichiers PDF,
  
  - Extraction du texte à partir des fichiers PDF,
  
  - Ajout des documents PDF à la base de données vectorielle.

- [54:47](https://www.youtube.com/watch?v=CUjO8b6_ZuM&t=3287s) 🧩 Fonctionnement du chat avec les fichiers PDF

  - Activation du chat avec les fichiers PDF,
  
  - Utilisation de la chaîne de traitement pour les questions et réponses avec les fichiers PDF,
  
  - Discussion sur les possibilités d'optimisation de la chaîne.

- [01:02:06](https://www.youtube.com/watch?v=CUjO8b6_ZuM&t=3726s) 🎨 Amélioration de l'interface utilisateur

  - Intégration de modèles HTML et CSS pour améliorer l'apparence de l'interface utilisateur,
  
  - Personnalisation des modèles pour les messages utilisateur et bot,
  
  - Conseils pour optimiser l'affichage des messages dans la fenêtre de chat.
### [Répertoire GitHub pour l'installation](https://github.com/Leon-Sander/local_multimodal_ai_chat)
