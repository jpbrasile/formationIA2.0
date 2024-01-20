## [Pour commencer](https://colab.research.google.com/?hl=fr) : Mixtral (sur HuggingFace) et Haystack
- Le notebook Colab : https://colab.research.google.com/drive/15AQHnr0yshjc4Qvr4Vx3lyPHc-bCLXqj?hl=fr#scrollTo=N3K6-AzFJ2OR
- [00:00](https://www.youtube.com/watch?v=_CBBz2lCR5U&t=0s) 📋 Présentation générale du sujet

  - Introduction à Mixtral 8x7B, modèle de langue,

  - Mixtral 8x7B est un modèle de langue haute qualité avec une licence Apache 2,

  - Il est performant sur de nombreux benchmarks, notamment en génération de code.

- [02:01](https://www.youtube.com/watch?v=_CBBz2lCR5U&t=121s) 🛠️ Configuration de l'environnement

  - Installation des prérequis, comme Haystack,

  - Obtention et configuration d'un jeton d'accès Hugging Face,

  - Importation de bibliothèques et outils nécessaires.

- [05:04](https://www.youtube.com/watch?v=_CBBz2lCR5U&t=304s) 📄 Traitement de document PDF

  - Téléchargement et traitement d'un document PDF,

  - Utilisation de la bibliothèque PDF2 pour extraire le texte,

  - Nettoyage et préparation du texte pour l'analyse.

- [08:01](https://www.youtube.com/watch?v=_CBBz2lCR5U&t=481s) ⚙️ Création du pipeline RAG

  - Configuration de la base de données en mémoire avec le modèle BM25,

  - Définition du pipeline RAG avec Mixtral 8x7B,

  - Spécification du modèle de question-réponse.

- [09:54](https://www.youtube.com/watch?v=_CBBz2lCR5U&t=594s) 🧐 Test de l'inférence

  - Exemples d'interrogation du modèle RAG,

  - Réponses du modèle en fonction du contexte du document,

  - Démonstration de l'utilisation du modèle pour répondre à des questions.

## Avec HuggingFace
- Le site [Hugging Face](https://huggingface.co/models) permet aux utilisateurs de tester des modèles d'intelligence artificielle sans avoir besoin de compétences techniques avancées.
- Les modèles d'IA disponibles sur Hugging Face sont divers, provenant de grandes entreprises telles que Microsoft, OpenAI, Mistral AI, Meta (la maison mère de Facebook) et Google, ainsi que de projets plus confidentiels.
- Les utilisateurs peuvent explorer les modèles en fonction de différentes catégories telles que la vision par ordinateur, le traitement automatique du langage naturel, l'audio, l'apprentissage par renforcement et le multimodal.
- Il est possible de tester ces modèles en utilisant des démonstrations en ligne directement sur le site, sans nécessiter de compétences techniques avancées.
- Les résultats des démonstrations en ligne peuvent être limités par rapport aux performances des modèles locaux, mais ils offrent une idée générale des capacités de l'IA.
- Hugging Face propose également des applications d'apprentissage automatique créées par la communauté, offrant des exemples plus concrets d'utilisation de l'IA.
- Certaines capacités sur Hugging Face sont gratuites, tandis que d'autres peuvent être payantes en fonction des ressources techniques nécessaires.
- En fin de compte, Hugging Face rend l'IA plus accessible au grand public, même s'il est possible d'aller plus loin en téléchargeant et en configurant les modèles localement.


## Ressources GitHub pour l'exploration de modèles par catégorie

Les utilisateurs peuvent explorer les modèles en fonction de différentes catégories telles que la vision par ordinateur, le traitement automatique du langage naturel, l'audio, l'apprentissage par renforcement et le multimodal.

### Vision par ordinateur
- [computer-vision](https://github.com/topics/computer-vision)

### Traitement automatique du langage naturel (TALN)
- [ESI_TALN](https://github.com/projeduc/ESI_TALN)
- [french-nlp](https://github.com/topics/french-nlp?l=python&o=asc&s=updated)

### Audio
- [Large-Audio-Models](https://github.com/liusongxiang/Large-Audio-Models)
- [audio-pretrained-model](https://github.com/balavenkatesh3322/audio-pretrained-model)

### Apprentissage par renforcement
- [DeepRL](https://github.com/vintel38/DeepRL)
- [RLADL](https://github.com/ATidiane/RLADL)

### Multimodal
- [Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models)

## Avec Colab:


### Synthèse du [Notebook](https://colab.research.google.com/drive/1tbNU3sT375kwDPm6jEpwp9KiORmsGcrU#scrollTo=Byov1aYybtaS)

Ce notebook présente différentes étapes pour générer des images à l'aide d'un modèle de génération de texte vers image appelé "Stable Diffusion". Voici un résumé des étapes principales :

1. **Installation des dépendances** :
   - Les packages `diffusers` et `transformers` sont installés à l'aide de la commande `!pip install`.

2. **Chargement du modèle Stable Diffusion** :
   - Un modèle de génération d'image Stable Diffusion est chargé à partir de Hugging Face Model Hub.

3. **Définition de la fonction de génération d'image** :
   - Une fonction `get_completion_sd(prompt)` est définie pour générer une image à partir d'une requête textuelle.

4. **Exécution de la génération d'image** :
   - Une requête textuelle (prompt) est fournie pour générer une image. Par exemple, le prompt peut être "baby llama, wearing red muffler, grazing, open field, sunset".

5. **Enregistrement de l'image générée** :
   - L'image générée est enregistrée sous le nom "llama.jpg".

6. **Installation de Gradio** :
   - Le package Gradio est installé pour créer une interface utilisateur permettant d'interagir avec le modèle de génération.

7. **Définition de la fonction Gradio** :
   - Une fonction `get_completion(prompt)` est définie pour intégrer le modèle Stable Diffusion avec Gradio.

8. **Création de l'interface utilisateur Gradio** :
   - Une interface utilisateur Gradio est créée pour permettre aux utilisateurs de saisir un prompt et de générer une image.

9. **Lancement de l'application** :
   - L'application Gradio est lancée, ce qui permet aux utilisateurs d'interagir avec le modèle de génération d'image en fournissant des prompts.

En résumé, ce notebook présente un flux de travail pour utiliser un modèle de génération Stable Diffusion pour créer des images à partir de prompts textuels, et il offre une interface utilisateur conviviale pour cette tâche.

