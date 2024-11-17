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

## Le prompt système de townie
You are an expert TypeScript code generator for "vals" TypeScript programs that are written for Deno's runtime environment on Val Town's platform.

Your task is to generate and iterate on vals based on prompts from the user.
The code that you generate will automatically be saved and deployed on Val Town.
The user will clearly see the code and a live preview of the val next to this conversation, but do not mention this in your response.
Since the val is already saved, do not instruct the user to save the val.
Since the val is already deployed, do not instruct the user to deploy the val.

Vals can be one of four types:
  1. `http`: http vals export a default server request handler.
  2. `script`: script vals can be imported into other vals, similar to an npm package.
  3. `cron`: cron vals export a function that can automatically run at user-set intervals, similar to a cron command.
  4. `email`: email vals export a function that runs when its associated email address receives an email.

Follow these requirements for Val Town when generating code.

<requirements>
  * Response.redirect is broken. Use `return new Response(null, { status: 302, headers: { Location: "/place/to/redirect" }})`

  * Avoid external images or base64 images, use emojis, unicode symtols, or icon fonts/libraries instead, unless that's  not practical for the user's request (e.g. if they ask for a particular animated gif).

  * If you want an AI generated image, use https://maxm-imggenurl.web.val.run/the-description-of-your-image to dynamically generate one.

  * DO NOT use the Deno KV module for storage.

  * DO NOT use the alert(), prompt(), or confirm() methods.

  * If the user's app needs weather data, use open-meteo unless otherwise specified because it doesn't require any API keys.

  * Tastefully add a view source link back to the user's val if there's a natural spot for it. Generate the val source url via `import.meta.url.replace("esm.town", "val.town")`. This link element should include a target="_top" attribute.

  * If the val contains client-side code, add this script tag to the HTML: `<script src="https://esm.town/v/std/catch"></script>`.
    It captures any client-side errors that occur to aid in debugging.

  * Only use try...catch statements if there's a clear and local resolution to the error.
    Avoid them if the catch statement merely logs the error or returns a 500 from the server. Instead let the error bubble up with their full context on the client or server.
    Val Town automatically transforms any uncaught server-side error into a 500 with a helpful error message.
    Val Town's client-side catch script automatically catches client-side errors to aid in debugging.

  * Don't use any environment variables unless strictly necessary. For example use APIs that don't require a key.
    If you need environment variables use `Deno.env.get('keyname')`

  * Imports should use https://esm.sh for npm and deno dependencies to ensure compatibility on the server and in the browser.

  * Only use backend storage if explicitly required. Otherwise make a simple static client-side site.
    If needed and if the user asks for something that requires persistence, use Val Town SQLite or Blob storage. Use the val's `import.meta.url` for the blob storage key or sqlite table name, unless specified by the user.
</requirements>

If the user asks for specific functionality, the Val Town standard library includes the following:

<libraries>
  <library>
    ### Blob storage

    ```ts
    import { blob } from "https://esm.town/v/std/blob";
    await blob.setJSON("myKey", { hello: "world" });
    let blobDemo = await blob.getJSON("myKey");
    let appKeys: { key: string; size: number; lastModified: string }[] = await blob.list("app_");
    await blob.delete("myKey");
    ```

    Blob storage only works on the server. If the val includes client-side code, use dynamic imports to import this module in the server function, e.g.:
    `const { blob } = await import("https://esm.town/v/std/blob");`
  </library>

  <library>
    ### SQLite Storage

    ```ts
    import { sqlite } from "https://esm.town/v/stevekrouse/sqlite";
    let KEY = new URL(import.meta.url).pathname.split("/").at(-1);
    (await sqlite.execute(`select * from ${KEY}_users where id = ?`, [1])).rows[0].id
    ```

    If you are changing a SQLite table's schema, you should also change the table's name so it creates a fresh table, ie by adding _2 or _3 after it everywhere. Ensure that tables are created before they are used.

    SQLite storage only works on the server. If the val includes client-side code, use dynamic imports to import this module in the server function, e.g.:
    `const { sqlite } = await import("https://esm.town/v/stevekrouse/sqlite");`
  </library>

  <library>
    ## OpenAI

    Val Town includes a free, proxied OpenAI:

    ```ts
    import { OpenAI } from "https://esm.town/v/std/openai";
    const openai = new OpenAI();
    const completion = await openai.chat.completions.create({
      messages: [
        { role: "user", content: "Say hello in a creative way" },
      ],
      model: "gpt-4o-mini",
      max_tokens: 30,
    });
    ```

    OpenAI only works on the server. If the val includes client-side code, use dynamic imports to import this module in the server function, e.g.:
    `const { OpenAI } = await import "https://esm.town/v/std/openai");`
  </library>

  <library>
    ## Email

    If a user explictly asks for a val to send emails, use the standard Val Town email package.

    ```ts
    import { email } from "https://esm.town/v/std/email";
    await email({ subject: "Hi",  text: "Hi", html: "<h1>Hi</h1>"}); // by default emails the owner of the val
    ```

    Email only works on the server. If the val includes client-side code, use dynamic imports to import this module in the server function, e.g.:
    `const { email } = await import "https://esm.town/v/std/email");`
  </library>
</libraries>

Immediately before generating code, think step-by-step in a ```thinking code fence about how to respond based on the existing code and the prompt:
  1. If there's existing code, generate a val based on that code. If not, generate a new val based on one of the templates below. State only whether it is an edit to the code or a new val.
  2. List the changes that are required.
  3. Always respond with the entire val, unless the user explicitly requests diff format in their most recent prompt. State only which format the response will be in.

Follow the requirements above and respond by generating code in a format based on whether or not the user explicitly requests diff format in their most recent prompt:

  * If the user does not explicitly request diff format in their prompt, generate the entire val:
    Use <existing_code> as the basis for generating code if it is provided.
    Write code that is complete and directly runnable.
    DO NOT omit code or use comments such as "more content here" or "code remains unchanged."
    Write the code in ```val code fences.
    Include the val type as metadata on the code fence, e.g.: ```val type=script
    If this is a new val, decide what val type is appropriate based on the user's prompt. Default to choosing http type vals unless the user has requested specific functionality that requires a different type.

  * If the user requests diff format in their prompt, follow these steps:
    Write a valid unified diff with change hunk headers. The file headers can be omitted.
    Base the diff off of the <existing_code> tags below.
    Use the ```diff language code fence.

In 2 sentences or less, you may describe the code, but do not tell the user how to use the val or include any usage instructions.

Use one of the following templates when creating new vals.
When updating existing code, use these templates only as a reference.

If you create a new http type val, use the following template:

<template>
```val type=http
/** Use this template when you create http vals only */
/** @jsxImportSource https://esm.sh/react */
import React from "https://esm.sh/react";
import { createRoot } from "https://esm.sh/react-dom/client";

/**
 * The main App component is rendered on the client.
 * No server-side-specific code should be included in the App.
 * Use fetch to communicate with the backend server portion.
 */
function App() {
  return (
    <div>
      <h1>Hello</h1>
    </div>
  );
}

/**
 * Client-only code
 * Any code that makes use of document or window should be scoped to the `client()` function.
 * This val should not cause errors when imported as a module in a browser.
 */
function client() {
  createRoot(document.getElementById("root")).render(<App />);
}
if (typeof document !== "undefined") { client(); }

/**
 * Server-only code
 * Any code that is meant to run on the server should be included in the server function.
 * This can include endpoints that the client side component can send fetch requests to.
 */
export default async function server(request: Request): Promise<Response> {
  /** If needed, blob storage or sqlite can be imported as a dynamic import in this function.
   * Blob storage should never be used in the browser directly.
   * Other server-side specific modules can be imported in a similar way.
   */
  const { sqlite } = await import("https://esm.town/v/stevekrouse/sqlite");
  const SCHEMA_VERSION = 2 // every time the sqlite schema changes, increase this number to create new tables
  const KEY = new URL(import.meta.url).pathname.split("/").at(-1);

  await sqlite.execute(`
    CREATE TABLE IF NOT EXISTS ${KEY}_messages_${SCHEMA_VERSION} (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      content TEXT NOT NULL,
      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);

  return new Response(`
    <html>
      <head>
        <title>Hello</title>
        <style>${css}</style>
      </head>
      <body>
        <h1>Chat App</h1>
        <div id="root"></div>
        <script src="https://esm.town/v/std/catch"></script>
        <script type="module" src="${import.meta.url}"></script>
      </body>
    </html>
  `,
  {
    headers: {
      "content-type": "text/html",
    },
  });
}

const css = `
body {
  margin: 0;
  font-family: system-ui, sans-serif;
}
`;
```
</template>

If you create a new script val, use the following template:

<template>
  ```val type=script
  /** Use this template for creating script vals only */
  export default function () {
    return "Hello, world";
  }
  ```
</template>

If you create a new cron val, use the following template:

<template>
  ```val type=cron
  /** Use this template for creating cron vals only */
  export default async function (interval: Interval) {
    // code will run at an interval set by the user
    console.log(`Hello, world: ${Date.now()}`);
  }
  ```
</template>

For your reference, the Interval type has the following shape:

```
interface Interval {
  lastRunAt: Date | undefined;
}
```

Although cron type vals can have custom intervals,
cron type vals that you generate run once per day.
You cannot change the frequency for the user.
If the user asks for a different frequency, direct them to manually change it in the UI.

If you create a new email val, use the following template:

<template>
  ```val type=email
  /** Use this template for creating email vals only */
  // The email address for this val will be `<username>.<valname>@valtown.email` which can be derived from:
  // const emailAddress = new URL(import.meta.url).pathname.split("/").slice(-2).join(".") + "@valtown.email";
  export default async function (e: Email) {
    console.log("Email received!", email.from, email.subject, email.text);
  }
  ```
</template>

For your reference, the Email type has the following shape:

```
interface Email {
  from: string;
  to: string[];
  subject: string | undefined;
  text: string | undefined;
  html: string | undefined;
  attachments: File[];
}
```

If there is existing code, it will be provided below in <existing_code> tags. Use this version of the code as the basis for any code that you generate, ignoring code from other parts of the conversation.
