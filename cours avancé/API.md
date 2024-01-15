## Avec un langage open source mieux que GPT4: 
- 💡 NexusRaven-V2, un modèle d'IA générative open source de 13 milliards de paramètres, surpasse GPT-4 dans les appels de fonction en langage naturel, permettant d'exécuter des instructions en code.
- 📈 NexusRaven-V2 présente une amélioration allant jusqu'à 7 % dans le taux de réussite des appels de fonction par rapport à GPT-4, sans être formé sur les fonctions utilisées dans l'évaluation.
- 🌐 NexusRaven-V2 est open source et commercial, utilisant des données générées par Nexusflow sans recourir à des modèles propriétaires, ce qui le rend accessible aux développeurs communautaires et aux entreprises.
- 🤝 L'intégration de NexusRaven-V2 est facilitée par des artefacts open source, permettant de remplacer facilement les API de fonction propriétaires par NexusRaven-V2 dans les flux de travail logiciels.
- 📊 Nexus-Function-Calling est un benchmark open source pour évaluer les appels de fonction, avec un leaderboard Huggingface contenant des exemples humains variés pour diverses utilisations et difficultés.
- 🔍 NexusRaven-V2 surpasse GPT-4 de 4 % en moyenne dans les appels de fonction sur un benchmark humain, avec une meilleure gestion des variations dans les descriptions des fonctions par les développeurs.
- 📦 Un package Python "nexusraven" est publié pour faciliter l'intégration de NexusRaven-V2, permettant de convertir le code d'appel de fonction en format JSON.
- 📆 Le modèle a été publié en décembre 2023, et Nexusflow encourage la collaboration avec la communauté pour développer davantage l'écosystème de modèles ouverts.

### Essais sur [colab](https://t.ly/Ge1Pj)
- Utiliser un GPU T4 dans le notebook
- Synthèse:
    - 🌟 RavenV2.ipynb est un document qui introduit l'appel de fonctions et Raven, un modèle de traitement du langage naturel open source.
    - 🤖 L'appel de fonctions, dans le contexte des modèles de langage, consiste à identifier et exécuter des fonctions prédéfinies avec des arguments pertinents.
    - 👍 L'appel de fonctions est important car il permet aux modèles de langage d'interagir avec divers outils fournis par les utilisateurs, ce qui élargit leur utilité et leur capacité à répondre de manière précise aux requêtes.
    - 🦅 Raven est non seulement compétent en appel de fonctions, mais il fournit également des explications sur les appels qu'il a émis, ce qui rend la génération plus interprétable.
    - 🌡️ L'exemple de l'API météo montre comment Raven utilise des fonctions pour répondre à une question sur la météo à Seattle en obtenant d'abord les coordonnées de la ville, puis en récupérant les données météo actuelles.
    - 🚀 Vous pouvez personnaliser les fonctions fournies dans le prompt et expérimenter avec Raven pour répondre à vos propres questions.
    - 📡 L'URL de l'API pour interagir avec Raven est fournie, ainsi que des fonctions pour envoyer des requêtes et obtenir des réponses.
