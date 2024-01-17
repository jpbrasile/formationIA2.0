# Pour le fine tuning 
## Affiner un modèle avec ses données 
- [00:00](https://www.youtube.com/watch?v=jcABWwH1FBE&t=0s) 🤖 Vous pouvez affiner le modèle Orca 2 pour répondre aux questions de manière personnalisée en utilisant des données d'entraînement.
- [00:16](https://www.youtube.com/watch?v=jcABWwH1FBE&t=16s) 🛠️ Ce tutoriel débutant vous guide étape par étape pour affiner le modèle Orca 2.
- [00:30](https://www.youtube.com/watch?v=jcABWwH1FBE&t=30s) 📺 Abonnez-vous à la chaîne YouTube pour plus de vidéos sur l'intelligence artificielle et n'oubliez pas de liker et de partager.
- [00:44](https://www.youtube.com/watch?v=jcABWwH1FBE&t=44s) 💻 Installez les bibliothèques nécessaires via pip et créez un fichier app.py pour commencer.
- [01:10](https://www.youtube.com/watch?v=jcABWwH1FBE&t=70s) 📊 Préparez vos données d'entraînement sous forme de questions et réponses pour le modèle.
- [02:19](https://www.youtube.com/watch?v=jcABWwH1FBE&t=139s) 🧮 Déterminez la longueur de séquence maximale en analysant vos données pour économiser des ressources informatiques.
- [02:59](https://www.youtube.com/watch?v=jcABWwH1FBE&t=179s) ⚙️ Configurez le modèle Ludwig en spécifiant les caractéristiques d'entrée et de sortie, ainsi que d'autres paramètres.
- [03:28](https://www.youtube.com/watch?v=jcABWwH1FBE&t=208s) 🚀 Entraînez le modèle en utilisant les données d'entraînement et sauvegardez les résultats.
- [03:56](https://www.youtube.com/watch?v=jcABWwH1FBE&t=236s) 🧪 Testez le modèle en prédisant des réponses à partir de données de test.
- [04:40](https://www.youtube.com/watch?v=jcABWwH1FBE&t=280s) 🔄 Le processus d'entraînement du modèle est suivi avec l'affichage des scores de validation et de test.
- [05:36](https://www.youtube.com/watch?v=jcABWwH1FBE&t=336s) 🌐 Vous pouvez télécharger le modèle affiné sur Hugging Face pour une utilisation ultérieure.

## Fine-tuning d'un modèle multimodal
- [00:03](https://youtu.be/usoTCfyQxjU?t=3s) 📚 Le tutoriel se concentre sur le fine-tuning d'un modèle multimodal LLM appelé "IDFICS 9B" pour la réponse à des questions visuelles.
- [01:21](https://youtu.be/usoTCfyQxjU?t=81s) 💡 L'importance des LLM multimodaux, qui combinent le traitement du langage naturel et des données visuelles, est soulignée en raison des avancées à venir, telles que GPT-5 avec des capacités multimodales améliorées.
- [03:39](https://youtu.be/usoTCfyQxjU?t=219s) 🛠️ Le processus de fine-tuning de "IDFICS 9B" est expliqué, avec l'utilisation de bibliothèques comme Bits and Bytes pour la quantification et des configurations spécifiques. La vidéo se concentre sur le fine-tuning de "IDFICS 9B" sur un ensemble de données Pokémon Go Cards.
- [24:28](https://www.youtube.com/watch?v=usoTCfyQxjU&t=24m28s) 🚀 Le processus de prétraitement des images dans la fine-tuning d'un modèle multimodal.
- [27:28](https://www.youtube.com/watch?v=usoTCfyQxjU&t=27m28s) 📸 Comment créer des prompts pour l'inférence avec des images.
- [29:36](https://www.youtube.com/watch?v=usoTCfyQxjU&t=29m36s) 📦 Comment charger et préparer un jeu de données pour la fine-tuning d'un modèle multimodal.
- [40:17](https://www.youtube.com/watch?v=usoTCfyQxjU&t=40m17s) 💬 Comment effectuer une inférence avec un modèle fine-tuné en utilisant une URL d'image et une question.
- [44:07](https://www.youtube.com/watch?v=usoTCfyQxjU&t=44m07s) 📤 Comment pousser un modèle fine-tuné vers Hugging Face Hub pour le partager avec la communauté.

## Bibliothèque open source pour l'entraînement et la fine-tuning de modèles de vision
Le site [Deci-AI/super-gradients](https://github.com/Deci-AI/super-gradients?tab=readme-ov-file) propose une bibliothèque open source pour l'entraînement et la fine-tuning de modèles de vision par ordinateur de pointe, avec un accent sur le modèle YOLO-NAS.

- Le site Deci-AI/super-gradients offre une bibliothèque open source pour l'entraînement de modèles de vision par ordinateur de pointe.
- Le modèle YOLO-NAS est mis en avant comme une caractéristique principale de la bibliothèque.
- La bibliothèque prend en charge diverses tâches de vision par ordinateur, telles que la classification, la segmentation sémantique, la détection d'objets et l'estimation de pose.
- Il est possible de charger des modèles pré-entraînés et de les affiner pour des performances optimales.
- La bibliothèque est compatible avec des outils de déploiement tels que TensorRT et OpenVINO.
- Des tutoriels et des recettes sont disponibles pour aider les utilisateurs à démarrer rapidement.
- La bibliothèque est constamment mise à jour, avec la dernière version étant la 3.5.0.
- Le projet est sous licence Apache 2.0 et est hébergé sur GitHub.
- Une plateforme appelée Deci Platform est également mentionnée, offrant des fonctionnalités pour la compilation et la quantification automatiques de modèles.

Le site propose une bibliothèque complète pour l'entraînement et la fine-tuning de modèles de vision par ordinateur, avec un accent sur le modèle YOLO-NAS.
# Pour la "quantification
- [00:00](https://youtu.be/Kj0OIkWpfHs?t=0s) 📋 Introduction à la quantification de modèle

  - La quantification de modèle est le processus de mise en correspondance des valeurs continues avec des valeurs discrètes pour l'apprentissage automatique.
  - La quantification permet d'exécuter de grands modèles de langage sur les CPU et de décharger certaines couches vers les GPU pour accélérer les calculs.
  - Le format le plus populaire de quantification de nos jours est le TTF (Transformers Tensilica Format).

- [02:45](https://youtu.be/Kj0OIkWpfHs?t=165s) 🎯 Préparation de l'environnement et du modèle

  - Configuration d'un environnement Google Colab avec un GPU T4 gratuit et un compte Hugging Face.
  - Définition du modèle à quantifier (Neural BigLE, 147 milliards de paramètres).

- [06:47](https://youtu.be/Kj0OIkWpfHs?t=407s) 💾 Conversion en virgule flottante 16 bits

  - La conversion du modèle en virgule flottante 16 bits réduit la consommation de mémoire et améliore l'efficacité énergétique.

- [08:39](https://youtu.be/Kj0OIkWpfHs?t=519s) ⚙️ Processus de quantification

  - Exploration de la méthode de quantification Q4 KM.
  - Quantification du modèle couche par couche, réduisant les besoins en mémoire et le temps de traitement.

- [11:23](https://youtu.be/Kj0OIkWpfHs?t=683s) 📤 Téléchargement du modèle quantifié sur Hugging Face

  - Connexion à Hugging Face, initialisation de l'API et création d'un référentiel pour le modèle quantifié.
  - Téléchargement du modèle quantifié dans le référentiel Hugging Face.

- [12:52](https://youtu.be/Kj0OIkWpfHs?t=772s) 🧐 Vérification du modèle téléchargé

  - Vérification du modèle quantifié téléchargé dans le référentiel Hugging Face.
  - Confirmation du succès du processus de quantification et de téléchargement.
 
  ## RoSA : mieux que LORA
  - [00:00](https://www.youtube.com/watch?v=p1ER6aNkEMQ&t=0s) 🔍 Introduction à la méthode Rosa en PFT

  - La PFT (Parameter Efficient Tuning) est une technique de ML,
  - La méthode Rosa est une adaptation à faible rang qui prétend surpasser Laura,
  - Rosa est basée sur l'analyse robuste des composantes principales.

- [01:20](https://www.youtube.com/watch?v=p1ER6aNkEMQ&t=80s) 📊 Performance de Rosa dans des tâches génératives

  - Rosa a surpassé Laura et la fine-tuning sparse dans les tâches génératives,
  - Ils ont introduit un support système pour Rosa, notamment des GPU épars pour une efficacité mémoire et computationnelle,
  - Le code de Rosa n'est pas encore disponible, ce qui est un inconvénient.

- [03:08](https://www.youtube.com/watch?v=p1ER6aNkEMQ&t=188s) 🧐 Résumé et attente du code

  - Présentation des comparaisons de mémoire entre Lama, fft, Laura, Spa et Rosa,
  - Le code de Rosa n'est pas encore disponible, ce qui est une préoccupation,
  - L'auteur invite les commentaires et les abonnements à la chaîne.
