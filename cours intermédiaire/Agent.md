## Autogen studio
- Initialisation des codes API:
  ```
  $env:OAI_CONFIG_LIST = Get-Content .\OAI_CONFIG_LIST
  ``` 

- [00:00](https://www.youtube.com/watch?v=4ZqJSfV4818&t=0s) 🚀 Introduction à Autogen Studio 2.0

  - Nouvelles fonctionnalités et expansion de la fonctionnalité.
  - Objectif de création d'une équipe d'agents.
  - Création d'un agent pour extraire le transcript d'une vidéo YouTube.

- [02:20](https://www.youtube.com/watch?v=4ZqJSfV4818&t=140s) 🤖 Nouveautés dans Autogen Studio 2.0

  - Présentation des nouvelles fonctionnalités de l'interface.
  - Introduction à la création de modèles personnalisés.
  - Possibilité d'avoir des équipes d'agents plus grandes.

- [03:29](https://www.youtube.com/watch?v=4ZqJSfV4818&t=209s) 🗝️ Configuration de l'API OpenAI

  - Création d'une clé API pour Autogen Studio.
  - Ajout de l'API Key à Autogen Studio.
  - Préparation de l'utilisation de l'API OpenAI dans le projet.

- [08:11](https://www.youtube.com/watch?v=4ZqJSfV4818&t=491s) 🔄 Création d'un Flux de Travail (Workflow)

  - Création d'un workflow pour coordonner les actions des agents.
  - Attribution des rôles aux agents dans le workflow.
  - Configuration du flux de travail pour réaliser une tâche spécifique.

- [10:48](https://www.youtube.com/watch?v=4ZqJSfV4818&t=648s) 🛠️ Débogage et Test du Workflow

  - Résolution d'un problème lié à l'API Key.
  - Exécution du workflow dans l'environnement Autogen Studio.
  - Observation des interactions entre les agents et les résultats du workflow.

- [14:22](https://www.youtube.com/watch?v=4ZqJSfV4818&t=862s) 📄 Résultats du Workflow

  - Analyse des résultats du workflow, y compris le transcript et la structure suggérée pour un blog post et un tweet thread.
  - Remarque sur l'absence d'affichage des résultats dans l'interface utilisateur d'Autogen Studio.

- [15:04](https://www.youtube.com/watch?v=4ZqJSfV4818&t=904s) ✅ Conclusion et Perspectives

  - Récapitulation des étapes du tutoriel.
  - Appel à l'intérêt pour des tutoriels supplémentaires avec des cas d'utilisation réels.
  - Invitation à aimer, s'abonner et commenter.
 
## ChatGpt pour avoir les "skills" de nos agents  (les outils)
```
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def fetch_youtube_transcript(video_url: str) -> Optional[str]:
    """
    Fetches the transcript of a YouTube video without using the YouTube Data API.

    Args:
        video_url (str): The URL of the YouTube video.

    Returns:
        Optional[str]: The transcript of the video as a string if available, otherwise None.
    """

    # Extract video ID from URL
    video_id = video_url.split('v=')[1]

    try:
        # Retrieve the available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Fetch the transcript in the desired language, let's assume English
        transcript = transcript_list.find_transcript(['en'])

        # Fetch the actual transcript data
        transcript_data = transcript.fetch()

        # Convert the transcript into a single string
        transcript_text = "\n".join([entry['text'] for entry in transcript_data])

        return transcript_text
    except (TranscriptsDisabled, NoTranscriptFound):
        # If transcripts are disabled or not found return None
        return None

# Example usage:
video_url = 'https://www.youtube.com/watch?v=your_video_id'
print(fetch_youtube_transcript(video_url))

```
## Création d'un agent pour récupérer les transcripts Youtube (transcript_getter)
- Lancement de autogen studio:
```
 autogenstudio ui --port 8081
```
- On doit initialiser
- System prompt: "You are AI agent that uses the "fetch_youtube_transcript" skill to get a YouTube transcript for subsequent processing
- Outils: "fetch_youtube_transcript"
## Agent content_writer
- Description : "Takes raw YouTube video transcripts and converts it into blog posts and tweet threads."
- System prompt:"You are an insightful, intelligent, and witty content writer who is able to take raw YouTube video transcripts and turn them into blog posts and tweet threads."
## Workflow (User et les deuxagents précédents)
- The workflow is described as taking a YouTube URL, getting the transcript of the video, and then creating a blog post and tweet thread from that transcript
- **System prompt**:You are a helpful assistant skilled at coordinating a group of other assistants to solve a task. The task you will solve is taking a YouTube URL, having an agent use the fetch_youtube_transcript skill to get the transcript from the YouTube video, pass that transcript to a content writer, and then having the content writer create a blog post and tweet thread based on that transcript

## Installation pour que Autogen V2 fonctionne en local 
- Nous avons créé le fichier "C:\Users\test\Documents\Formation IA\Autogen2\autogen\OAI_CONFIG_LIST"
```
[   
    {
        "model": "lm studio api",
        "api_key": "not needed",
        "base_url": "http://localhost:1234/v1"
        
    },
    {
        "model": "gpt-4-turbo-preview",
        "api_key": "sk-YqwdMu.... yJ3eJgKDJ"
    },
    {
        "model": "<your Azure OpenAI deployment name>",
        "api_key": "<your Azure OpenAI API key here>",
        "base_url": "<your Azure OpenAI API base here>",
        "api_type": "azure",
        "api_version": "2023-07-01-preview"
    },
    {
        "model": "<your Azure OpenAI deployment name>",
        "api_key": "<your Azure OpenAI API key here>",
        "base_url": "<your Azure OpenAI API base here>",
        "api_type": "azure",
        "api_version": "2023-07-01-preview"
    }
]

```

## Autogen:
- [00:00](https://youtu.be/Cl19yWHhc2g?t=0s) 🤖 AutoGen Studio vous permet de construire des agents IA capables d'accomplir des tâches de manière efficace.
- [00:55](https://youtu.be/Cl19yWHhc2g?t=55s) 🛡️ AutoGen a accompli une tâche en 45 secondes, ce qui prendrait de 30 à 60 minutes à un assistant humain.
- [02:16](https://youtu.be/Cl19yWHhc2g?t=136s) 💼 AutoGen Studio simplifie le processus de création et d'utilisation d'agents IA, le rendant plus accessible même aux non-programmeurs.
- [04:46](https://youtu.be/Cl19yWHhc2g?t=286s) 🚀 La configuration d'AutoGen Studio implique la création d'un environnement Anaconda, l'installation des packages requis et la configuration d'une clé API OpenAI.
- [15:58](https://youtu.be/Cl19yWHhc2g?t=958s) 🎨 AutoGen Studio peut être utilisé pour donner des instructions à des agents IA afin d'accomplir diverses tâches, telles que la génération d'images basée sur des descriptions.
- [19:24](https://youtu.be/Cl19yWHhc2g?t=1164s) 📊 AutoGen Studio permet la création de plusieurs agents IA dans différents services, tels que la conception, la programmation, les tests et la documentation.
- [20:35](https://youtu.be/Cl19yWHhc2g?t=1235s) 💪 Les efforts de collaboration de plusieurs agents travaillant ensemble ont tendance à produire de meilleurs résultats qu'un seul agent travaillant en isolation.
- [21:30](https://youtu.be/Cl19yWHhc2g?t=1290s) 🚀 La nouvelle interface utilisateur d'AutoGen Studio simplifie le processus de création d'agents, facilitant la définition des rôles et des messages système.
- [21:43](https://youtu.be/Cl19yWHhc2g?t=1303s) 🛠️ AutoGen Studio peut générer du code de base pour la création de compétences, mais les utilisateurs doivent spécifier l'API et les services à utiliser.
- [22:12](https://youtu.be/Cl19yWHhc2g?t=1332s) 🌟 AutoGen Studio s'améliore continuellement, offrant des compétences réutilisables et rendant le développement IA plus accessible, même pour les non-développeurs.
### Tutorial:

## AutoGen, MemGPT avec des LLM locaux

- [00:00](https://www.youtube.com/watch?v=8RtxvXIx61Y&t=0s) 🤖 Pour utiliser LM Studio avec un LLM open source et MGPT, commencez par télécharger et installer LM Studio sur votre système.
- [01:09](https://www.youtube.com/watch?v=8RtxvXIx61Y&t=69s) 🧩 Vous pouvez rechercher et télécharger des modèles open source LLM depuis LM Studio en utilisant des critères tels que la popularité ou la récence.
- [02:04](https://www.youtube.com/watch?v=8RtxvXIx61Y&t=124s) ⚙️ Après le téléchargement, chargez le modèle dans LM Studio et démarrez le serveur local pour interagir avec le LLM sans nécessiter une clé API.
- [03:28](https://www.youtube.com/watch?v=8RtxvXIx61Y&t=208s) 🧰 Préparez Autogen et MGPT en créant un nouveau projet, en définissant des variables d'environnement et en configurant les agents.
- [06:00](https://www.youtube.com/watch?v=8RtxvXIx61Y&t=360s) 🧪 Configurez le LLM en spécifiant des paramètres tels que le numéro de graine et le délai de réponse pour obtenir des réponses cohérentes.
- [07:11](https://www.youtube.com/watch?v=8RtxvXIx61Y&t=431s) 🤖 Créez des agents, tels que l'agent utilisateur et l'agent assistant, pour interagir avec le LLM en définissant leurs rôles et configurations.
- [08:32](https://www.youtube.com/watch?v=8RtxvXIx61Y&t=512s) 💡 Si vous le souhaitez, utilisez MGPT comme agent de codage pour obtenir des réponses de codage spécifiques.
- [10:36](https://www.youtube.com/watch?v=8RtxvXIx61Y&t=636s) 📝 Exécutez le code, interagissez avec le modèle LLM en utilisant les agents et examinez les résultats dans LM Studio ou votre environnement de développement.
- [12:13](https://www.youtube.com/watch?v=8RtxvXIx61Y&t=733s) 🌐 En utilisant un LLM open source avec Autogen, vous n'avez pas besoin de clé API, ce qui peut être économique lors des tests. Prochainement, une vidéo détaillée sur Autogen et ses agents.


[Lmstudio](https://lmstudio.ai/)

[memgpt](https://github.com/cpacker/MemGPT)

## AutoGen studio : Tutorial
- [00:00](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=0s) 🚀 Présentation d'AutoGen Studio par l'équipe de recherche Microsoft : un projet d'agent IA révolutionnaire, entièrement open source et exécutable localement.

  - Introduction d'AutoGen Studio pour créer des équipes d'agents IA.
  - Utilisation possible avec ChatGPT et modèles locaux.
  - Applications variées : analyse de données boursières, planification de voyages, programmation.

- [01:23](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=83s) 📦 Installation d'AutoGen Studio et configuration de l'environnement Python.

  - Processus d'installation d'AutoGen Studio et création d'un environnement Conda.
  - Installation de Python 3.11 et activation de l'environnement.

- [02:04](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=124s) 🔑 Configuration de la clé API OpenAI et démarrage d'AutoGen Studio.

  - Création et configuration de la clé API OpenAI pour AutoGen Studio.
  - Démarrage d'AutoGen Studio avec un port spécifique et accès via un navigateur.

- [02:59](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=179s) 🧠 Explication des compétences et des agents dans AutoGen Studio.

  - Description des compétences et leur utilisation pour les agents IA.
  - Exemples de compétences : génération d'images, recherche de documents sur arXiv.

- [04:23](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=263s) 🤖 Création et gestion des agents IA dans AutoGen Studio.

  - Processus de création d'agents IA avec des rôles et des outils spécifiques.
  - Exemples d'agents : Assistant Principal et Proxy Utilisateur.

- [05:19](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=319s) 🌐 Configuration de flux de travail et gestion des groupes de discussion dans AutoGen Studio.

  - Création de flux de travail intégrant des équipes et des tâches spécifiques.
  - Configuration de la gestion de groupes de discussion pour une collaboration efficace.

- [06:32](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=392s) 💻 Démonstration de l'utilisation de modèles locaux avec AutoGen Studio.

  - Utilisation de modèles locaux pour alimenter AutoGen Studio.
  - Exemples d'intégration de modèles locaux dans des flux de travail.

- [09:46](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=586s) 📝 Création de compétences et de sessions de test dans AutoGen Studio.

  - Processus de création de nouvelles compétences et de sessions de test.
  - Exemples pratiques de création et de test de compétences dans AutoGen Studio.

- [11:08](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=668s) 🎨 Utilisation de compétences spécifiques pour générer des images et effectuer des tâches spécifiques.

  - Démonstration de la génération d'images en utilisant des compétences spécifiques.
  - Importance de l'assignation des compétences adéquates aux agents pour des tâches spécifiques.

- [12:02](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=722s) 🌍 Configuration d'AutoGen Studio pour une utilisation complètement locale avec des modèles locaux.

  - Installation des outils nécessaires pour l'utilisation locale d'AutoGen Studio.
  - Explication du processus de configuration pour une utilisation locale.

- [14:22](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=862s) ⚙️ Création et configuration d'agents IA locaux dans AutoGen Studio.

  - Création d'agents IA alimentés par des modèles locaux.
  - Configuration détaillée des agents pour une intégration réussie dans AutoGen Studio.

- [15:21](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=921s) 🔄 Mise en place de flux de travail avec des agents IA locaux dans AutoGen Studio.

  - Configuration de flux de travail spécifiques utilisant des agents IA locaux.
  - Exemple de configuration de flux de travail pour l'agent IA "Mistal".

- [16:44](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=1004s) 🖥️ Tests de performance et validation des configurations d'agents locaux dans AutoGen Studio.

  - Tests pratiques pour valider la configuration des agents locaux.
  - Exemples de tâches exécutées par les agents locaux pour démontrer leur fonctionnement.

- [18:08](https://www.youtube.com/watch?v=mUEFwUU0IfE&t=1088s) 🛠️ Personnalisation avancée et possibilités d'extension d'AutoGen Studio.

  - Discussion sur la personnalisation et l'extension d'AutoGen Studio.
  - Suggestions pour implémenter une logique de déconnexion personnalisée et partage entre équipes.

[GitHub de AutoGen Studio](https://github.com/microsoft/autogen/tree/main/samples/apps/autogen-studio)

## Autogen UI
Résumé détaillé de la vidéo ["AutoGen 2.0 UI: AI-Powered Travel Agents transforming travel Industry"](https://www.youtube.com/watch?v=azT2QTSdvyA)

### Introduction :

#### Présentation de l'interface utilisateur AutoGen, permettant la création de chats de groupe et l'ajout de compétences à des agents virtuels pour collaborer ensemble.
- Objectif : Créer des agents de voyage IA pour organiser des voyages de 7 jours.
#### Configuration de l'AutoGen Studio UI :

- Installation et activation d'AutoGen Studio sur Python 3.11.
- Installation de la compétence de recherche "DougDoug Go" pour permettre aux agents de chercher des informations en ligne.
- Lancement de l'interface utilisateur AutoGen Studio sur le port 8081.
#### Création et configuration des agents :

- Trois agents sont créés : le gestionnaire d'agents de voyage, l'expert en sélection de ville et l'agent local.
- Chaque agent reçoit une compétence de recherche sur Internet et un message système spécifique.
- Le gestionnaire d'agents de voyage organise l'itinéraire, la météo, les suggestions d'emballage et le budget.
- L'expert en sélection de ville se concentre sur la météo, les événements saisonniers et autres informations locales.
 - L'agent local fournit des informations détaillées sur les attractions, coutumes locales, événements spéciaux et recommandations d'activités quotidiennes.
#### Création de workflows pour collaboration entre agents :

- Un workflow de groupe de discussion est créé, intégrant les trois agents pour travailler ensemble.
- Le gestionnaire de groupe de discussion coordonne l'interaction entre les agents.
#### Démo de l'AutoGen Studio en action :

- L'utilisateur demande aux agents de planifier un voyage à Londres en février 2024.
- Les agents utilisent la compétence de recherche pour trouver des informations pertinentes sur Londres, y compris la météo, les événements et les coûts de voyage.
- Résultat : Un itinéraire de 7 jours est généré, avec des détails sur les activités quotidiennes, le budget et les considérations météorologiques.
#### Limitations et bugs observés :

- Limitation à un maximum de neuf interactions dans l'interface utilisateur.
- Quelques problèmes techniques avec la compétence de recherche, qui devraient être résolus dans les versions futures.
#### Conclusion :

- AutoGen 2.0 UI démontre l'efficacité des agents IA dans la planification de voyages, offrant des résultats rapides et détaillés.
- Incitation à suivre la chaîne pour plus de vidéos similaires.
- La vidéo montre comment AutoGen 2.0 UI utilise l'intelligence artificielle pour transformer l'industrie du voyage, en permettant une planification de voyage rapide et efficace grâce à la collaboration de plusieurs agents IA spécialisés

## CrewAI : l'alternative à AutoGen
- [00:00](https://www.youtube.com/watch?v=qFNge4IrERk&t=0s) 🤖 [Crew AI](https://github.com/joaomdmoura/crewAI) est un nouveau framework qui permet de créer des agents et de leur assigner des tâches.
- [00:27](https://www.youtube.com/watch?v=qFNge4IrERk&t=27s) 🚀 Vous pouvez créer un agent de recherche et un agent de rédaction avec Crew AI pour rechercher des tendances en intelligence artificielle et écrire un article.
- [01:08](https://www.youtube.com/watch?v=qFNge4IrERk&t=68s) 💼 Pour commencer, vous devez installer Crew AI, activer l'environnement, et configurer votre clé API OpenAI.
- [02:16](https://www.youtube.com/watch?v=qFNge4IrERk&t=136s) 🎯 Vous pouvez définir des agents avec des rôles et des objectifs spécifiques, comme un agent de recherche et un agent de rédaction.
- [03:35](https://www.youtube.com/watch?v=qFNge4IrERk&t=215s) 🔄 Vous initialisez le processus de Crew AI en créant une liste d'agents et de tâches, puis en lançant le processus.
- [04:30](https://www.youtube.com/watch?v=qFNge4IrERk&t=270s) 🧩 Les agents travaillent ensemble, le chercheur recherchant des informations et le rédacteur créant un article en fonction des résultats.
- [05:37](https://www.youtube.com/watch?v=qFNge4IrERk&t=337s) 💡 Vous pouvez intégrer des modèles de langage tels qu'OlaMa pour améliorer la qualité des tâches de recherche et de rédaction.
- [06:59](https://www.youtube.com/watch?v=qFNge4IrERk&t=419s) 📚 La qualité des résultats peut dépendre de la puissance du modèle de langage que vous utilisez avec Crew AI.
- [07:28](https://www.youtube.com/watch?v=qFNge4IrERk&t=448s) ✅ En suivant ces étapes, vous pouvez créer et utiliser vos propres agents Crew AI pour effectuer des tâches spécifiques en intelligence artificielle.

- [**Exemples d'emploi**](https://mer.vin/2024/01/crewai-example-code/)
  - Pour travailler avec un LLM de LM studio:
```Python
import os
os.environ[OPENAI_API_KEY]="not used"
os.environ[OPENAI_API-BASE]="http://localhost:1234.v1"
```   
- **Autre exemple:**
  - Je vais extraire les points clés du prochain extrait de la transcription vidéo :
  
  - [00:00](https://www.youtube.com/watch?v=U5TAI_SGllA&t=0s) 🤖 Présentation des agents de création de publications LinkedIn avec Crew AI, y compris le coach, l'influenceur et le critique, chacun utilisant un modèle de langage différent.
  - [00:26](https://www.youtube.com/watch?v=U5TAI_SGllA&t=26s) 🧰 Étape initiale : Installation des modules de langage, création d'un fichier app.py et importation des bibliothèques nécessaires.
  - [01:09](https://www.youtube.com/watch?v=U5TAI_SGllA&t=69s) 🛠️ Initialisation des modèles de langage, y compris Mistral AI, Gemini Pro et Azure Chat GPT, avec les clés API appropriées.
  - [03:00](https://www.youtube.com/watch?v=U5TAI_SGllA&t=180s) 👩‍💼👨‍💼 Création d'agents, dont le coach, l'influenceur et le critique, avec des tâches spécifiques, comme la recherche de tendances en IA et la création de publications LinkedIn.
  - [04:25](https://www.youtube.com/watch?v=U5TAI_SGllA&t=265s) 🚀 Création de l'équipage avec la liste des agents et des tâches, puis déclenchement de l'équipage pour commencer le processus.
  - [05:06](https://www.youtube.com/watch?v=U5TAI_SGllA&t=306s) 📝 Exécution du code et suivi du flux de travail, du coach à l'influenceur et enfin au critique, créant une publication LinkedIn sur les nouvelles compétences en IA pour 2024.
  
  Ces points clés résument les étapes du processus de création de publications LinkedIn à l'aide de Crew AI avec différents modèles de langage.

- [**Encore d'autres**:](https://github.com/joaomdmoura/crewAI-examples/)
