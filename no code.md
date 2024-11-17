# objectifs
Ceci est un tutoriel sur la façon d'utiliser les outils IA pour produire une application complexe
# Première étape : S'aider de l'IA (ChatGPT ou Sonnet) pur établir le cahier des charges. 
## Expression du besoin
- Je souhaite faire une application qui produit des vidéos à partir d'un front end client, par contre j'engrange les vidéos ainsi produites sur mon propre serveur
- Pour accéder au service, les clients doivent s'enregistrer et s'abonner
- La création de vidéos se fait en utilisant les ressources d'API (chaque client se procure ses propres clefs API)
- Le stockage des clefs api se fait sur un serveur dédié à chaque client, qui n'a donc plus besoin de générer les clefs à chaque session
## Cahier des charges après interaction avec le llm [Gemini Exp 1114](https://aistudio.google.com/) 

## 1. Objectif
- Plateforme web de gestion d'APIs personnalisées.
- Création de vidéos côté client à l'aide de ressources via API.
- Stockage des vidéos sur le serveur global.
- Multi-clients avec isolation complète.
- Interfaces séparées : Dashboard client et Dashboard admin global.

## 2. Architecture
### Front-End
- **Framework : Vite (avec React)**.
- Interfaces utilisateur réactives et modulaires.
- Développement rapide et validation indépendante des modules.
- Composants principaux :
  - **Dashboard Client** :
    - Gestion des vidéos (création, téléversement, lecture).
    - Suivi des consommations API et des quotas d'abonnement.
    - Historique et état des vidéos créées.
  - **Dashboard Admin Global** :
    - Supervision des clients.
    - Gestion des abonnements et des paiements.
    - Monitoring des ressources globales et des vidéos.
    - Gestion des permissions et des accès.

### Back-End Client
- **Framework : Townie (Val Town)**.
- Base de données : **SQLite** pour stocker les métadonnées des vidéos et les clés API.
- Gestion de la logique métier client pour :
  - Récupérer les ressources nécessaires via API (images, textes, musiques, etc.).
  - Orchestrer le processus de création vidéo côté client.
  - Transférer les vidéos finalisées vers le serveur global pour stockage.
- Exécution sécurisée et sandboxée.

### Back-End Global
- **Framework : NestJS**.
- Centralisation des services critiques :
  - Gestion des abonnements et paiements.
  - Supervision des back-ends clients via le Dashboard Admin.
  - Monitoring global et analytics.
  - Stockage centralisé des vidéos créées côté client (Firebase Storage ou autre solution).
  - API pour permettre l'accès sécurisé aux vidéos depuis le front-end.

## 3. Features
### Front-End
#### Dashboard Client
- Login sécurisé.
- Gestion des vidéos :
  - Création à partir des ressources API.
  - Téléversement automatique vers le serveur global.
  - Visionnage et téléchargement des vidéos stockées.
- Suivi des consommations API :
  - Nombre d'appels API utilisés.
  - Suivi des quotas selon le niveau d'abonnement.
- Historique des vidéos :
  - Liste des vidéos créées avec leur statut (en attente, validée, etc.).
  - Actions disponibles : supprimer, éditer, télécharger.
- Notifications :
  - Alertes pour dépassement de quotas ou erreurs de création vidéo.

#### Dashboard Admin Global
- Gestion des utilisateurs :
  - Ajout, modification, et suppression de comptes clients.
  - Gestion des permissions et niveaux d'accès.
- Gestion des abonnements :
  - Suivi des paiements et des niveaux d'abonnement.
  - Paramétrage des quotas par abonnement.
- Monitoring global :
  - Statistiques sur les vidéos créées (nombre, volume total, performances).
  - Suivi des ressources consommées par client.
- Analytics :
  - Rapports sur l'utilisation des APIs, des vidéos, et des performances système.
  - Graphiques interactifs pour visualiser les données clés.

### Back-End Client
- Gestion des clés API.
- Accès et orchestration des ressources via API pour la création vidéo.
- Stockage SQLite pour :
  - Métadonnées des vidéos (statut, ID, etc.).
  - Données API et configurations spécifiques au client.
- Transfert sécurisé des vidéos créées vers le serveur global.

### Back-End Global
- Supervision des clients et contrôle des permissions.
- Gestion centralisée des abonnements.
- Monitoring global des usages (vidéos générées, ressources consommées).
- Stockage centralisé des vidéos avec accès sécurisé.
- API pour le front-end pour récupérer ou diffuser les vidéos.

## 4. Sécurité
- Chiffrement des données sensibles (AES-256 pour SQLite).
- Authentification JWT pour les utilisateurs.
- Isolation stricte entre les back-ends clients.
- Protection des APIs avec des mécanismes anti-abus (rate limiting, IP whitelisting).
- Transferts sécurisés des vidéos vers le serveur global (HTTPS ou protocole équivalent).
- Sauvegardes automatiques régulières.

## 5. Performance
- Création vidéo optimisée côté client pour réduire la charge serveur.
- SQLite comme base légère et rapide pour les données locales.
- Firebase pour le stockage global des vidéos.
- Système de cache pour accélérer les réponses API.
- Monitoring des ressources globales et par client.

## 6. Tech Stack
### Front-End
- **Framework** : Vite (React).
- **UI Framework** : Modern UI (TailwindCSS ou MUI).
- **Design** : Responsive et mobile-friendly.

### Back-End Client
- **Framework** : Townie (Val Town).
- **Database** : SQLite (par client).
- **Logiciel vidéo** : Utilisation de librairies JS comme `FFmpeg.wasm` pour générer les vidéos localement.

### Back-End Global
- **Framework** : NestJS.
- **Database** : Firebase pour les données globales.
- **Stockage** : Firebase Storage ou AWS S3 pour les vidéos.
- **API Gateway** : Gestion centralisée des flux.

## 7. Avantages
- **Création vidéo déportée** : Charge serveur réduite en déléguant la génération vidéo au client.
- **Stockage centralisé** : Toutes les vidéos sont accessibles de manière centralisée, simplifiant l'administration et l'accès.
- **Modularité** : Développement et validation indépendants des modules.
- **Isolation client** : Données et traitements isolés pour chaque client.
- **Scalabilité** : Ajout facile de nouveaux clients ou services.
- **Sécurité renforcée** : Gestion stricte des accès et sauvegardes régulières.

## 8. Deliverables
- Application web complète.
- **Dashboard Client** : Interface dédiée aux utilisateurs finaux.
- **Dashboard Admin** : Interface dédiée à l'administration globale.
- Back-ends client et global.
- Documentation technique (API, architecture, guides utilisateurs).
- Interfaces front-end modulaires.
- Système de déploiement automatisé.

## 9. Timeline
- **MVP : 6 mois**.
  - **Phase 1** : Conception de l'architecture.
  - **Phase 2** : Développement du back-end global.
  - **Phase 3** : Développement du Dashboard Client.
  - **Phase 4** : Développement du back-end client (SQLite + APIs vidéo).
  - **Phase 5** : Développement du Dashboard Admin.
  - **Phase 6** : Tests unitaires et d’intégration.
  - **Phase 7** : Déploiement.

## 10. Outils et Processus
- **Gestion de projet** : Agile (sprints de 2 semaines).
- **Versioning** : Git (GitHub/GitLab).
- **CI/CD** : GitHub Actions ou GitLab CI.
- **Tests** : Vitest (front-end), Jest (back-end global), Val Town sandbox (clients).
- **Déploiement** : Docker et Kubernetes pour un déploiement modulable.

## Nos outils de création (et ce qu'en pense Perplexity)
### [Bolt.new](bolt.new)
### **Avantages de Bolt.new**

- **Génération de code par IA** : Permet de créer des applications complètes à partir de simples prompts textuels, sans besoin de coder.
- **Capacités full-stack** : Gère à la fois le frontend et le backend dans un environnement unique, avec intégration de bases de données (ex. Supabase) et déploiement (ex. Netlify).
- **Personnalisation** : Possibilité d'éditer manuellement le code généré, d'ajouter des packages NPM et de configurer des backends.
- **Scalabilité** : Fonctionnalités d'auto-scaling, équilibrage de charge et gestion du cache pour assurer la performance.
- **Détection d'erreurs en temps réel** : Aide à minimiser les bugs pendant le développement.

### **Limites pour les applications complexes**

- **Personnalisation UI limitée** : L'IA peut avoir du mal avec des interfaces utilisateur très complexes ou spécifiques.
- **Problèmes de performance** : Des ralentissements peuvent survenir avec des projets plus volumineux ou complexes.
- **Inexactitudes de l'IA** : L'IA peut parfois générer du code incorrect ou incomplet, nécessitant des corrections manuelles.

### **Conclusion**

Bolt.new est idéal pour créer rapidement des prototypes ou des applications de complexité moyenne sans coder. Cependant, pour des projets très complexes ou nécessitant une personnalisation poussée, il peut être nécessaire d'utiliser des outils complémentaires ou d'impliquer des développeurs.
### [Windsurf](https://codeium.com/windsurf)
Windsurf est un éditeur de code assisté par IA qui se distingue par sa rapidité et ses suggestions d'autocomplétion précises, ce qui peut être un atout pour créer une application complexe sans code. Grâce à son système **Cascade Flow**, il offre un flux de travail fluide et une intégration avec les plugins VS Code, permettant une grande extensibilité. Cependant, Windsurf reste principalement orienté vers l'édition de code avec assistance IA, ce qui pourrait ne pas correspondre parfaitement à une approche purement no-code, où des interfaces visuelles sont généralement privilégiées pour la création d'applications.

Si ton objectif est de construire une application complexe sans écrire de code, Windsurf pourrait ne pas être le meilleur choix, car il est davantage conçu pour accélérer le développement de code existant plutôt que pour offrir une véritable expérience no-code avec des outils visuels. Pour des projets totalement no-code, il serait plus judicieux d'explorer des plateformes spécialisées comme Webflow ou Adalo, qui permettent de créer des applications complexes via des interfaces drag-and-drop sans avoir à toucher au code[1][2][3].

Citations:

[1] https://dev.to/dev_michael/why-windsurf-is-the-best-free-ai-code-editor-youve-never-heard-of-3ofj

[2] https://3veta.com/blog/business-advice/advantages-and-disadvantages-of-no-code-apps-and-platforms/

[3] https://www.sfappworks.com/blogs/no-code-development-platforms

[4] https://www.lowcode.agency/blog/capabilities-and-limitations-of-no-code-low-code-development-platforms
### [Townie](https://www.val.town/townie/signup?next=%2Ftownie) 
**Townie** est une plateforme no-code prometteuse pour créer des applications full-stack complexes, entièrement gratuitement. Elle se distingue par sa capacité à générer des applications complètes, incluant des bases de données SQL automatiques et des API puissantes, tout en offrant une interface simple pour les utilisateurs non techniques. Townie permet également de partager facilement des applications via des URL en direct, ce qui est idéal pour la collaboration. Cependant, il semble que Townie soit limité à la création d'applications monopage, ce qui peut poser problème pour des projets nécessitant des interfaces plus complexes ou multi-pages[1][3].

Cela dit, Townie reste une option intéressante pour développer rapidement des MVPs ou des applications simples à modérées sans avoir à coder. La plateforme offre une bonne flexibilité grâce à l'intégration de bases de données et d'API, mais sa limitation aux applications monopage pourrait restreindre son usage pour des projets plus ambitieux. Si ton projet nécessite une application complexe avec plusieurs pages ou fonctionnalités avancées, Townie pourrait ne pas être suffisant, et tu devrais envisager d'autres outils no-code plus robustes[1][3].

Citations:

[1] https://www.youtube.com/watch?v=l9NyuajxjrI

[2] https://www.belighted.com/blog/top-4-pros-and-cons-no-code

[3] https://blog.val.town/blog/codegen/

[4] https://3veta.com/blog/business-advice/advantages-and-disadvantages-of-no-code-apps-and-platforms/
