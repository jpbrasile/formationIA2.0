# formationIA2.0

## Formation à l'IA en 2024: 

Dans le tableau ci-après: 3 niveaux de formation : Débutant, intermédiaire et avancé
- **Quels outils ?** : Ceux à maîtriser pour être efficace:  Halte aux problèmes ! Euh non !  "**Alt A <Problème>!**" et Harpa.ai vous répondra !
- **Le prompt** : Comment parler avec le chatbot pour que sa réponse soit pertinente ?
- **Fournir aux LLM nos propres données** : Comment le chatbot peut prendre en compte mes données ?
- **Accès à Internet**: Comment faire pour qu'il prenne les données pertinantes sur le cloud ?
- **Gérer le Contexte**: Comment composer avec sa mémoire vive qui ne peut accumuler qu'un nombre fini de données ?
- **Au delà de l'écrit** : Comment travailler avec des données non textuelles (images, son ... ) tant en entrée qu'en sortie ?
- **L'accès aux outils externes**: Comment faire que le chatbot accède à des ressources externes disponibles sur le web ?
- **Chatbots spécialisés** : Comment créer des chatbots spécialisés pour remplir certaines tâches ?
- **Travail en équipe**: Comment créer des chatbots travaillant en équipe
- **L'IA apprend toute seule** : Comment faire pour que les Chatbot apprennent de leurs erreurs ?

| Niveau        | Objectif                              | Quels outils  ?                           | [Le prompt](https://github.com/jpbrasile/formationIA2.0/wiki/4.-Le-prompting)                                           | [Fournir aux LLM nos propres données](https://github.com/jpbrasile/formationIA2.0/wiki/6.-Fournir-aux-LLM-nos-propres-donn%C3%A9es)                                               | [L'Accès à Internet](https://github.com/jpbrasile/formationIA2.0/wiki/L'acc%C3%A8s-%C3%A0-internet.md)                                            | Gérer le contexte                                             | Au delà de l'écrit                                         | L'accès aux outils externes                                               | Chatbots spécialisés                                              | Travail en équipe                                           | L'IA apprend toute seule                                               |
|---------------|---------------------------------------|-----------------------------------------|------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------|---------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| Débutant      | Utiliser l'IA         | [Nos outils:](https://github.com/jpbrasile/formationIA2.0/wiki/01:-Comment-disposer-d'outils-qui-font-tout-pour-vous-%3F)  [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/?culture=fr-fr&country=fr), [Harpa](https://harpa.ai/), [Perplexity](https://www.perplexity.ai/), [Canva](https://www.canva.com/)              | [Les bases](https://github.com/jpbrasile/formationIA2.0/blob/main/cours%20pour%20d%C3%A9butants/3-%20le%20prompting.md) |[Avec nos outils](https://github.com/jpbrasile/formationIA2.0/blob/main/cours%20pour%20d%C3%A9butants/4-%20Prise%20en%20compte%20de%20mes%20donn%C3%A9es.md)            | Avec nos outils              |  Un prompt pour demander la synthèse   | Copilot (dessin) et outils en ligne| Outils en ligne          |  |                |
| Intermédiaire | Maîtriser l'IA          | Choisir son LLM open source           | Formation au prompting   |Technique d'embedding | Formation au scraping                    | MEMGPT et LongGPT             | LLAVA1.5 et ComphyUI | Langchain, Gorilla            | emploi des GPTs openAI        |     AutoGen         |   |
| Avancé        | Créer avec l'IA       | Finetuning, Création de MOE | Prompt optimisé par programmation                   | Création de base de données locales       | AgentSearch et Wiki search | Gestion avancée du contexte (compactage)                        | Développement de solutions multimodales personnalisées | Conception d'API robustes pour des applications à grande échelle | Utilisation de GPT-4 et autres modèles avancés     | Développement d'agents autonomes capables d'apprentissage continu | Stratégies pour le développement de talents en IA et gestion des changements technologiques |

## ChatGPT C'est quoi ? : 
- [00:00](https://www.youtube.com/watch?v=PNjh4z8WF9M&t=0s) 🤖 Qu'est-ce que ChatGPT ? [Large Language Model Base: un LLM à la maternelle](https://github.com/jpbrasile/formationIA2.0/wiki/1.-LLM%E2%80%90Base) 

  - ChatGPT est une machine à approximer qui fournit des réponses basées sur ce qu'il a appris.
  - Il est efficace pour interpoler mais peut fournir de fausses réponses en l'absence de données suffisantes.
  - L'apprentissage de ChatGPT nécessite l'ajustement de ses paramètres en fonction des données d'entrée, et il a utilisé des milliards de données pour ajuster ses paramètres.

- [01:11](https://www.youtube.com/watch?v=PNjh4z8WF9M&t=71s) 📚 Comment instruire ChatGPT ? : [Le LLM à l'école](https://github.com/jpbrasile/formationIA2.0/wiki/2.-LLM%E2%80%90Instruct) 
  - Pour instruire ChatGPT, il faut lui donner des directives sur son comportement.
  - Alimenter la machine avec une nouvelle base de données de type question-réponse lui permet de mimer ce type de résultat.
  - Des gardes-fous sont nécessaires pour censurer certaines réponses et inculquer les bonnes manières.

- [02:09](https://www.youtube.com/watch?v=PNjh4z8WF9M&t=129s) 💻 Implantation de ChatGPT

  - ChatGPT est principalement disponible en ligne via le Cloud, en raison de son coût de développement.
  - Le contrôle sur l'utilisation de ChatGPT est difficile, ce qui soulève des préoccupations concernant la divulgation d'informations sensibles.
  - Un mouvement open source travaille sur des versions plus légères de ChatGPT pour des utilisations locales.

- [03:18](https://www.youtube.com/watch?v=PNjh4z8WF9M&t=198s) 🧠 La taille et le contexte des LLM : [Le LLM peut soutenir une conversation](https://github.com/jpbrasile/formationIA2.0/wiki/3.-LLM%E2%80%90Chat) 

  - Les LLM (Large Language Models) sont en constante évolution pour devenir plus légers tout en maintenant leur performance.
  - La taille des LLM est mesurée en milliards de bytes, et des versions plus compactes sont développées.
  - Le contexte, ou mémoire à court terme, est crucial pour stocker des informations pertinentes lors de l'interaction avec un LLM.
