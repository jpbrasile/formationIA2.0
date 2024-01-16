### Résumé Clé
L'[article](https://towardsdatascience.com/solving-reasoning-problems-with-llms-in-2023-6643bdfd606d#1acd) souligne l'évolution importante des modèles de langage à grande échelle (LLM) en 2023, notamment dans la résolution de problèmes de raisonnement et l'utilisation d'outils. Il met en évidence les progrès dans l'utilisation d'outils externes et les capacités de raisonnement interne des LLM, ainsi que l'exploration de nouvelles méthodes pour améliorer ces capacités.

### Résumé
- **Introduction et Contexte**
  - ChatGPT a fêté son premier anniversaire en 2024.
  - L'année 2023 a été marquée par de nombreux développements dans le domaine des LLM.

- **Utilisation des Outils**
  - Les LLM ont été équipés d'outils externes tels que les moteurs de recherche et les interpréteurs de code.
  - La méthode d'apprentissage en contexte permet une utilisation plus efficace des outils.
  - L'article aborde des projets spécifiques comme Toolformer, Chameleon, et ToolkenGPT.

- **Raisonnement**
  - Accent sur la résolution de problèmes complexes via les capacités de raisonnement internes des LLM.
  - Exploration des limites et des moyens d'étendre les capacités de raisonnement des LLM.

- **Création de Propres Outils par les LLM**
  - Des travaux préliminaires ont exploré la capacité des LLM à créer des outils, en particulier des fonctions Python et des règles textuelles.

- **Planification et Séries Auto**
  - Les méthodes comme le raisonnement via la planification et les séries auto démontrent des avancées dans le raisonnement plus complexe et l'auto-amélioration des LLM.

- **Observations et Évaluations**
  - Des études ont été menées sur la capacité de mémorisation des LLM et leur tendance à mémoriser des solutions plutôt qu'à raisonner de manière autonome.

- **Prévisions pour 2024**
  - Prédictions sur l'évolution future des LLM, incluant l'intégration multimodale et une meilleure compréhension du processus de raisonnement.

- **Divers**
  - L'article mentionne également des travaux connexes et des blogs sur le raisonnement des LLM.

- **Conclusion**
  - L'année 2023 a été significative pour le développement et l'utilisation des LLM dans la résolution de problèmes de raisonnement et l'utilisation d'outils, posant des bases pour de futures avancées dans ce domaine.
 

#### In-context learning :
- [Toolformer](https://arxiv.org/abs/2302.04761):
    - 🤖 Les modèles de langage (LMs) peuvent apprendre à utiliser des outils externes via des APIs simples.
    - 📚 Toolformer est un modèle formé pour décider quelles APIs appeler, quand les appeler, quels arguments passer, et comment incorporer les résultats dans les prédictions futures de tokens.
    - 💡 Cette formation est réalisée de manière auto-supervisée, nécessitant seulement quelques démonstrations pour chaque API.
    - 🧮 Toolformer intègre divers outils tels qu'une calculatrice, un système de questions-réponses, deux moteurs de recherche différents, un système de traduction et un calendrier.
    - 🚀 Toolformer améliore considérablement les performances en zéro-shot dans diverses tâches, souvent compétitives avec des modèles beaucoup plus grands, sans sacrifier ses capacités de modélisation linguistique de base.
- [Chameleon](https://arxiv.org/abs/2304.09842):
  - 🧩 Les grands modèles de langage (LLM) ont des capacités de raisonnement émergentes, mais présentent des limites telles que l'incapacité d'accéder à des informations récentes sur le Web ou des bases de connaissances spécifiques aux tâches, l'utilisation d'outils externes, et la réalisation de raisonnements mathématiques et logiques précis.
  - 🌐 Chameleon est un système d'IA qui comble ces limites en ajoutant des modules plug-and-play aux LLM pour le raisonnement compositionnel. Il synthétise des programmes en combinant divers outils tels que les LLM, les modèles de vision préfabriqués, les moteurs de recherche Web, les fonctions Python et des modules basés sur des heuristiques pour accomplir des tâches de raisonnement complexes.
  - 📊 Au cœur de Chameleon se trouve un planificateur basé sur un LLM qui assemble une séquence d'outils pour générer la réponse finale.
  - 📈 Chameleon, alimenté par GPT-4, améliore considérablement les performances sur les tâches de raisonnement intensif en connaissances multimodales, atteignant une précision globale de 86,54% sur ScienceQA et 98,78% sur TabMWP.
  - 🧠 L'analyse montre que le planificateur alimenté par GPT-4 sélectionne de manière plus cohérente et rationnelle les outils en déduisant des contraintes potentielles à partir des instructions, par rapport à un planificateur alimenté par ChatGPT.
- [Visual reasoning](https://arxiv.org/abs/2211.11559)
  - 🧠 VISPROG est une approche neuro-symbolique pour résoudre des tâches visuelles complexes et compositionnelles avec des instructions en langage naturel.
  - 📜 VISPROG génère des programmes modulaires de type Python sans nécessiter d'entraînement spécifique à la tâche.
  - 🖼️ Ces programmes peuvent utiliser différents modèles de vision par ordinateur, des routines de traitement d'image ou des fonctions Python pour produire des sorties intermédiaires.
  - 💡 Il peut être utilisé pour des tâches telles que la réponse à des questions visuelles compositionnelles, le raisonnement sur des paires d'images, l'étiquetage d'objets de connaissances factuelles et la modification d'images guidée par le langage.
  - 🌐 VISPROG étend la portée des systèmes d'IA pour résoudre des tâches complexes sans nécessiter un apprentissage spécifique à la tâche.
- [ToolkenGPT](https://arxiv.org/abs/2305.11554):
  - 💡 Les auteurs reconnaissent le soutien de la Fondation Simons et des contributeurs.
  - 💡 L'article présente ToolkenGPT, une approche pour améliorer les modèles de langage avec des outils externes.
  - 💡 Les méthodes traditionnelles de finetuning des modèles de langage avec des données de démonstration d'outils peuvent être coûteuses et limitées à un ensemble prédéfini d'outils.
  - 💡 ToolkenGPT combine les avantages des méthodes traditionnelles et de l'apprentissage en contexte pour augmenter les modèles de langage.
  - 💡 Il permet d'ajouter un nombre arbitraire d'outils en temps réel et d'améliorer leur utilisation grâce à des données de démonstration.
  - 💡 L'approche est efficace dans divers domaines, tels que la résolution de problèmes numériques, la réponse aux questions basées sur la connaissance et la génération de plans incarnés.
  - 💡 ToolkenGPT montre la capacité prometteuse d'utiliser des outils pertinents à partir d'un grand ensemble d'outils dans des scénarios complexes.
#### Most used tools: code interpreters and retrievers
- [COT](https://arxiv.org/abs/2201.11903):
  - 🧠 La génération d'une chaîne de pensée améliore les capacités de raisonnement des grands modèles de langage.
  - 📚 Cette amélioration résulte de la méthode de chaîne de pensée, qui utilise des exemples de démonstrations de chaîne de pensée.
  - 🧮 Les expériences montrent que cette méthode améliore les performances dans des tâches de raisonnement arithmétique, de bon sens et symbolique.
  - 📈 L'amélioration est particulièrement remarquable, par exemple, pour la résolution de problèmes mathématiques, surpassant même GPT-3 avec un vérificateur.
-[program aided](https://arxiv.org/abs/2211.10435):
  - 🧠 Les grands modèles de langage (LLM) ont montré une grande capacité à effectuer des tâches de raisonnement arithmétique et symbolique en utilisant des exemples limités ("few-shot prompting").
  - 🔄 Les méthodes de prompting telles que "chain-of-thought" sont efficaces pour décomposer les problèmes en étapes comprises par les LLMs, mais les LLMs commettent souvent des erreurs logiques et arithmétiques dans la solution.
  - 🤖 Le modèle PAL (Program-Aided Language) propose une approche novatrice où le LLM génère des programmes comme étapes intermédiaires de raisonnement, mais délègue la résolution à un interprète Python.
  - 📊 PAL démontre une synergie entre un LLM neuronal et un interprète symbolique, obtenant des résultats plus précis que des modèles plus grands sur 13 tâches de raisonnement mathématique, symbolique et algorithmique.
  - 📈 Par exemple, PAL avec Codex atteint une précision few-shot de pointe sur le benchmark GSM8K pour les problèmes mathématiques, surpassant PaLM-540B de 15% en top-1.
  - 🌐 Le code et les données de PAL sont disponibles publiquement.
- [program of Thougth](https://arxiv.org/abs/2211.12588):
  - 🧠 La méthode CoT est actuellement la méthode de pointe pour les tâches de raisonnement numérique complexe en utilisant des modèles de langage.
  - 💡 Le 'Program of Thoughts' (PoT) propose de séparer la computation du raisonnement en utilisant des modèles de langage pour exprimer le raisonnement sous forme de programme.
  - 📈 PoT présente une amélioration de performance moyenne d'environ 12% par rapport à CoT sur divers ensembles de données, en configuration à faible nombre d'exemples ou sans exemple.
  - 📊 En combinant PoT avec le décodage en auto-consistance, des performances de pointe sont obtenues sur tous les ensembles de données de problèmes mathématiques et des performances proches de celles de pointe sur les ensembles de données financières.
  - 💻 Les données et le code sont disponibles sur GitHub.
- [planning tasks](https://arxiv.org/abs/2305.16653): 
  - 🤖 Les grands modèles de langage (LLMs) peuvent agir comme des agents autonomes pour les tâches de prise de décision séquentielle.
  - 📈 La plupart des méthodes existantes ne planifient pas ou utilisent des plans statiques, ce qui limite la performance des agents LLM dans des environnements complexes.
  - 🔄 AdaPlanner propose une approche en boucle fermée qui permet à l'agent LLM d'affiner son plan en réponse aux retours environnementaux.
  - 📝 Il utilise des stratégies d'affinement à la fois dans le plan et en dehors du plan pour éviter les hallucinations.
  - 🧠 Il développe une structure de prompt en style de code pour faciliter la génération de plans dans diverses tâches et environnements.
  - 🎯 AdaPlanner découvre les compétences en utilisant des plans réussis comme exemples à quelques tirs, permettant à l'agent de planifier avec moins de démonstrations.
  - 🚀 Les expériences montrent qu'AdaPlanner surpasse les méthodes actuelles avec beaucoup moins d'échantillons dans différents environnements.
- [Retrieval Augmented generation](https://arxiv.org/abs/2005.11401):
  - 🧠 Les grands modèles de langage pré-entraînés stockent des connaissances factuelles dans leurs paramètres et obtiennent des résultats de pointe lorsqu'ils sont affinés pour des tâches de traitement du langage naturel (NLP) ultérieures.
  - 🌐 Cependant, leur capacité à accéder et à manipuler précisément les connaissances est limitée, ce qui les empêche de performer efficacement sur des tâches intensives en connaissances.
  - 🔍 Les modèles de récupération augmentée pour la génération (RAG) combinent une mémoire paramétrique pré-entraînée avec une mémoire non paramétrique, permettant un meilleur accès aux connaissances.
  - 📚 Ils utilisent un modèle séquentiel pré-entraîné comme mémoire paramétrique et un index de vecteurs denses de Wikipédia comme mémoire non paramétrique, accessible avec un récupérateur neuronal pré-entraîné.
  - 📊 Deux formulations de RAG sont comparées, l'une conditionnée sur les mêmes passages récupérés sur toute la séquence générée, l'autre pouvant utiliser différents passages par jeton.
  - 📈 Les modèles RAG établissent de nouvelles références sur trois tâches de questions-réponses en domaine ouvert, surpassant les modèles séquentiels paramétriques et les architectures de récupération et d'extraction spécifiques à la tâche.
  - 🗣️ Pour les tâches de génération de langage, les modèles RAG génèrent un langage plus spécifique, diversifié et factuel que les modèles séquentiels paramétriques de pointe.
- [IRCoT](https://arxiv.org/abs/2212.10509):
  - 📚 Les modèles de langage à grande échelle (LLM) basés sur des questions sont puissants pour générer des étapes de raisonnement en langage naturel ou des chaînes de pensée (CoT) pour répondre à des questions à plusieurs étapes.
  - 🧠 Cependant, ils rencontrent des difficultés lorsque les connaissances nécessaires ne sont pas disponibles pour le LLM ou ne sont pas à jour.
  - 🔄 L'approche "récupérer et lire en une étape" est insuffisante pour les questions à plusieurs étapes, car ce qu'il faut récupérer dépend de ce qui a déjà été déduit.
  - 🚀 Pour résoudre ce problème, ils proposent IRCoT, une nouvelle approche qui entrelace la récupération avec les étapes dans une CoT, guidant la récupération avec la CoT et utilisant les résultats récupérés pour améliorer la CoT.
  - 📈 En utilisant IRCoT avec GPT3, ils améliorent considérablement la récupération (jusqu'à 21 points) ainsi que les questions-réponses ultérieures (jusqu'à 15 points) sur quatre ensembles de données différents.
  - 💡 IRCoT réduit l'hallucination du modèle, ce qui entraîne un raisonnement CoT factuellement plus précis.
- [LeanDojo](https://arxiv.org/abs/2306.15626):
  - 📚 Les grands modèles de langage (LLMs) montrent une promesse dans la démonstration de théorèmes formels en utilisant des assistants de preuve tels que Lean.
  - 💡 Cependant, les méthodes existantes sont difficiles à reproduire ou à développer en raison de codes privés, de données et d'exigences de calcul élevées.
  - 🌐 LeanDojo est une aire de jeux Lean open-source qui extrait des données de Lean et permet une interaction avec l'environnement de preuve de manière programmatique.
  - 🧩 Il contient des annotations fines des prémisses dans les preuves, fournissant des données précieuses pour la sélection des prémisses, un point critique dans la démonstration de théorèmes.
  - 🤖 À partir de ces données, ReProver est développé, un prouveur basé sur LLM augmenté avec une fonction de recherche pour la sélection de prémisses à partir d'une vaste bibliothèque mathématique.
  - ⏱️ Il est peu coûteux et nécessite seulement une semaine de formation sur un GPU.
  - 🔎 Le récupérateur de ReProver utilise la capacité d'analyse de programme de LeanDojo pour identifier des prémisses accessibles et des exemples négatifs difficiles, ce qui rend la recherche beaucoup plus efficace.
  - 📊 De plus, un nouveau banc d'essai est construit, comprenant 98 734 théorèmes et preuves extraites de la bibliothèque mathématique de Lean, avec des données exigeantes nécessitant la généralisation à des théorèmes basés sur des prémisses inédites.
  - 📈 Les résultats expérimentaux montrent l'efficacité de ReProver par rapport aux méthodes non basées sur la recherche et à GPT-4.
  - 🔓 Ils fournissent ainsi le premier ensemble de prouveurs de théorèmes basés sur LLM open-source sans données propriétaires et le publient sous une licence MIT permissive pour faciliter les recherches futures.
  - 🏆 Accepté à NeurIPS 2023 en tant que présentation orale dans la catégorie "Datasets and Benchmarks Track".
- [DSPy](https://arxiv.org/abs/2310.03714):
  - 📚 La communauté de l'apprentissage automatique explore rapidement les techniques pour stimuler les modèles de langage et les empiler dans des pipelines résolvant des tâches complexes.
  - 🔄 Les pipelines de modèles de langage existants utilisent souvent des "modèles de requête" codés en dur, ce qui manque de systématicité.
  - 🧩 DSPy est un modèle de programmation qui abstrait les pipelines de modèles de langage en tant que graphes de transformation de texte.
  - 🤖 Les modules DSPy sont paramétrés et peuvent apprendre à appliquer des compositions de techniques de requêtage, d'affinage, d'augmentation et de raisonnement.
  - 🚀 Un compilateur DSPy optimise les pipelines DSPy pour maximiser une métrique donnée.
  - 📊 Deux études de cas montrent que de courts programmes DSPy permettent aux modèles GPT-3.5 et llama2-13b-chat de surpasser les méthodes traditionnelles de requêtage few-shot et les pipelines avec des démonstrations créées par des experts.
  - 💻 DSPy est disponible en ligne pour être utilisé.

## POUR ALLER PLUS LOIN

- [00:00](https://www.youtube.com/watch?v=5OneHs9GV0Y&t=0s) 🤖 Cours sur les bases de l'IA pour tous par IBM

  - Cours gratuit de Corsera pour renforcer vos connaissances fondamentales en IA.
  - Aucune expérience préalable nécessaire.
  - Vous apprendrez sur l'IA, les modèles de langage, la génération de langage naturel et plus encore.

- [02:05](https://www.youtube.com/watch?v=5OneHs9GV0Y&t=125s) 🧠 Cours sur les fondamentaux de Chat GPT

  - Comprenez la fonctionnalité et les applications de Chat GPT.
  - Découvrez le rôle d'OpenAI dans le développement de l'IA.
  - Identifiez les avantages et les limites de Chat GPT.

- [03:31](https://www.youtube.com/watch?v=5OneHs9GV0Y&t=211s) 🐍 Cours Python pour tout le monde sur Coursera

  - Apprenez la programmation en Python pour l'analyse de données et l'IA.
  - Développez des compétences en programmation et en analyse de données.
  - Obtenez un certificat de Coursera et de l'Université du Michigan.

- [05:08](https://www.youtube.com/watch?v=5OneHs9GV0Y&t=308s) 🤖 Cours sur l'Intelligence Artificielle avec Python par Harvard University

  - Explorez les bases de l'IA moderne.
  - Comprenez les concepts et les algorithmes de l'IA.
  - Utilisez des bibliothèques d'apprentissage automatique en Python.

- [06:21](https://www.youtube.com/watch?v=5OneHs9GV0Y&t=381s) 🧠 Spécialisation en Deep Learning par Deep Learning AI

  - Acquérez une compréhension approfondie du Deep Learning.
  - Appliquez la théorie et les applications pratiques en utilisant Python et TensorFlow.
  - Explorez des cas réels tels que la reconnaissance vocale et les chatbots.

- [07:30](https://www.youtube.com/watch?v=5OneHs9GV0Y&t=450s) 🕹️ Cours sur l'apprentissage par renforcement profond

  - Apprenez les méthodes basées sur la valeur et la politique en apprentissage par renforcement.
  - Comprenez les processus de décision de Markov et les équations de Bellman.
  - Formez des agents pour des tâches complexes en utilisant des techniques d'IA.

- [08:14](https://www.youtube.com/watch?v=5OneHs9GV0Y&t=494s) ✍️ Cours sur l'ingénierie de prompts pour Chat GPT

  - Maîtrisez l'ingénierie de prompts avancée pour Chat GPT.
  - Utilisez des modèles de langage pour créer des applications sophistiquées.
  - Recevez un certificat de réussite à la fin du cours.

- [08:56](https://www.youtube.com/watch?v=5OneHs9GV0Y&t=536s) 🌟 Devenir un ingénieur alimenté par l'IA

  - Apprenez à intégrer Chat GPT, GitHub Copilot et Co-pilot Labs dans votre travail.
  - Utilisez ces outils pour améliorer votre productivité en programmation.
  - Explorez les applications de l'IA dans le développement de logiciels.
 

