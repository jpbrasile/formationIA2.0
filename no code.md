# objectifs
Ceci est un tutoriel sur la façon d'utiliser les outils IA pour produire une application complexe
## Executive summary
- Townie est vraiment excellent pour du prototypage rapide avec un programme en  un seul fichier
- ChtGPT peut créer des programme multifichier et les conditionner e nun .zip (lancement très facile possible avec Docker)
- Abacus.ai (ChatLLM) a un mode agent qui déploie des applications simplements
- Bolt.new me semble le meilleur outil pour coder des applications complexes à ce jour
- Perplexity permet de trouver sur le net comment corriger les erreur les plus courantes

## To do
- Créer par ia des web api locale avec docker, accessible pour l'agent local
- Déploiement sous forme de zip
- Voir la connexion IA base de données comme github https://www.youtube.com/watch?v=FVuZ1wwxI5U
- Un assistant prospection tout IA:
  - Trouver les coordonnées et le profil avec perplexity eyt ChatGPT playground mis en oeuvre avec open interpreter
  - Utiliser Twilio + elevenlabs ou équivalent pour enclencher une discusion téléphonique
  - Base de données lié à l'IA pour contexte specifique client potentiel et mise à jour après le call     


# Première étape : S'aider de l'IA (ChatGPT ou Sonnet) pur établir le cahier des charges. 
## Expression du besoin
- Je souhaite faire une application qui produit des vidéos à partir d'un front end client, par contre j'engrange les vidéos ainsi produites sur mon propre serveur
- Pour accéder au service, les clients doivent s'enregistrer et s'abonner
- La création de vidéos se fait en utilisant les ressources d'API (chaque client se procure ses propres clefs API)
- Le stockage des clefs api se fait sur un serveur dédié à chaque client, qui n'a donc plus besoin de générer les clefs à chaque session
## Cahier des charges après interaction avec le llm [Gemini Exp 1114](https://aistudio.google.com/) 

Cahier des Charges : Plateforme de Création Vidéo (Bolt.new Open-Source Local)
**I. Objectif**

Créer une plateforme web permettant aux utilisateurs de générer des vidéos personnalisées à partir d'APIs externes. La plateforme priorisera la sécurité, la scalabilité, et la performance, en tirant parti d'une version open-source locale et multi-langage de Bolt.new.

**II. Architecture**

- Front-End (React, Vite): Interfaces utilisateur réactives et modernes pour les dashboards client et administrateur, avec un design responsive et optimisé pour mobile (Modern UI - Tailwind CSS ou MUI).

- Backend Client (Node.js/Serverless): Gère la création vidéo, l'interaction avec les APIs externes, et le stockage local des métadonnées (SQLite). L'architecture Serverless est privilégiée pour sa scalabilité et sa facilité de déploiement.

- Backend Global (Bolt.new Open-Source Local & Multi-langage): Responsable de la gestion des utilisateurs, des abonnements, des paiements, du monitoring, du stockage centralisé des vidéos (solution à déterminer - Supabase, Firebase Storage, AWS S3, ou solution auto-hébergée), et de l'API Gateway pour le front-end.

**III. Fonctionnalités**

- Dashboard Client:

  - Authentification sécurisée (JWT).
  
  - Gestion des clés API (création, lecture, mise à jour, suppression).
  
  - Interface intuitive pour la création vidéo (intégration avec les APIs externes).
  
  - Téléversement automatique et sécurisé des vidéos vers le stockage centralisé.
  
  - Lecture, téléchargement, suppression et organisation des vidéos.
  
  - Suivi clair des quotas d'API et des consommations.
  
  - Notifications en temps réel (dépassements de quotas, erreurs).

- Dashboard Admin:

  - Gestion des utilisateurs (création, lecture, mise à jour, suppression, rôles et permissions).
  
  - Gestion des abonnements (création, modification, suivi des paiements).
  
  - Configuration des quotas d'API par niveau d'abonnement.
  
  - Monitoring global des ressources, des utilisateurs et des vidéos.
  
  - Outils d'analyse pour comprendre l'utilisation de la plateforme.

- Backend Client:

  - API pour la création vidéo, recevant les paramètres du front-end.
  
  - Gestion sécurisée des clés API (stockage chiffré).
  
  - Communication sécurisée avec le backend global pour le transfert des vidéos.
  
  - Mécanismes robustes de gestion des erreurs.

- Backend Global:

   API Gateway pour le front-end (sécurité, authentification, routage).
  
  - API pour la gestion des vidéos (accès sécurisé pour le front-end client).
  
  - Gestion des utilisateurs et des abonnements.
  
  - Système de monitoring et d'analyse.

**IV. Sécurité**

- Authentification JWT pour tous les endpoints (implémentation et gestion internes).

- HTTPS pour toutes les communications (configuration pour l'instance locale).

- Stockage sécurisé des clés API (chiffrement robuste).

- Isolation des données entre les clients.

- Protection contre les abus (rate limiting personnalisé, validation des entrées).

- Sauvegardes régulières et automatisées (stratégie et système adaptés).

- Tests de sécurité réguliers (pentesting, audits de code).

**V. Performance**

- Optimisation de la création vidéo côté client.

- Utilisation de SQLite pour les données locales.

- Stockage optimisé des vidéos (solution à déterminer).

- Mise en cache des données fréquemment accédées.

- Surveillance continue des performances.

- Tests de charge pour identifier les goulots d'étranglement.

**VI. Technologies**

- Front-end: React, Vite, Modern UI (Tailwind CSS ou MUI).

- Backend Client: Node.js, Serverless Functions, SQLite, FFmpeg.wasm.

- Backend Global: Bolt.new (open-source, local, multi-langage). Base de données à déterminer (Supabase, Firebase, AWS S3, ou solution auto-hébergée).

**VII. Livrables**

- Application web fonctionnelle (dashboards client et admin).

- Backends client et global déployés.

- Documentation technique complète (API, architecture, guides utilisateur).

- Scripts de déploiement automatisés.

- Tests d'intégration automatisés.

**VIII. Chronologie**

À déterminer après une phase d'évaluation et de prototypage avec Bolt.new.

IX. Outils et Processus

- Git (GitHub/GitLab) pour le versioning.

- CI/CD pour l'intégration et le déploiement continus.

- Outils de test (unitaires, d'intégration, de performance, de sécurité).

- Docker et/ou Kubernetes pour le déploiement et la scalabilité.

**X. Infrastructure**

À déterminer en fonction des besoins de scalabilité et de performance (serveurs dédiés, cloud, etc.). La gestion de l'infrastructure sera internalisée.

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


## Comment faire ?
- Nous pouvons utiliser **un chat pour affiner** le cahier des charges.
- Commencer étape par étape
- Pour des "petits codes" qui ne nécessitent pas plus de 300 lignes de codes utiliser **townie**.
- Pour des codes plus sérieux utiliser **bolt.new** soit celui de référence soit [celui fonctionnant en **local**](https://github.com/coleam00/bolt.new-any-llm). J'utilise qwen 2.5 coder 32b (quantization 4b) avec ollama. Suivre les instructions pour avoir un contexte étendu. Il faut avoir la mémoire GPU (J'ai 24B)
- lancer le "bon llm" sur ollama (3 heures de débuggage inutile parce que j'avais lancé le mauvais !).
- pour débugger un code complexe existant : surfwind permet de prendre en compte
- mettre dans tous les cas les informations importantes dans le readme. 
- En cas de problème persistant. demander à WindSurf de formaliser le problème et demander à Perplexity de le résoudre.Ici [Un exemple pour permettre l'enregistrement sur supabase](https://www.perplexity.ai/search/supabase-authorization-with-go-Cd8cnxMbRUOh6AxQ2Um.Kg)


### Premier exercice avec townie.ai
- Je me suis inscrit pour 10 €/mois
- Mon premier objectif est de réaliser "une web api additionnant deux nombres" c'est à dire une application hébergé sur le net qui fait une addition via une requ^te à partir d'un terminal.
- Dis comme ça , c'est simple mais il faut créer un front end (la calculette que l'on voit) et un backend (sur un serveur, là où se font les calculs). Avec townie, tout est automatique
- Une reformulation de mon problème par chatLLM Teams :
```
"Créer une application full-stack avec Townie qui :

Frontend :
Affiche une interface simple avec deux champs de saisie numérique
Inclut un bouton pour déclencher l'addition
Affiche le résultat de l'addition
Backend :
Expose un endpoint HTTP qui :
Accepte deux nombres en paramètres
Effectue leur addition
Retourne le résultat
Spécifications techniques :
Utiliser l'architecture full-stack de Townie
Implémenter la validation des entrées
Gérer les erreurs de manière appropriée
Assurer une réponse JSON formatée
Routes API :
POST /api/add
Body: { number1: number, number2: number }
Response: { result: number }
Merci de générer le code complet pour cette calculatrice d'addition simple."
```
- L'application est créé sur https://jpbrasile-phenomenallimeboa.web.val.run/
- et ChatLLM me dit comment y accéder à partir d'un terminal powershell:
```
#### Test de l'addition avec curl
Invoke-RestMethod -Uri "https://jpbrasile-phenomenallimeboa.web.val.run/api/add" -Method Post -ContentType "application/json" -Body '{"number1": 5, "number2": 3}'
```
-  Nousa vons modifer le code pour qu'il n'agisse que si on dispose d'une clef api ( ici admin)
```
$headers = @{
    "Content-Type" = "application/json"
    "Authorization" = "Bearer admin"  # "admin" est la clé API par défaut
}

$body = @{
    number1 = 10
    number2 = 20
} | ConvertTo-Json

$response = Invoke-RestMethod `
    -Uri "https://jpbrasile-phenomenallimeboa.web.val.run/api/add" `
    -Method Post `
    -Headers $headers `
    -Body $body

# Afficher le résultat
$response
```
###  Deuxième exercice : Addition avec API sécurisée
[réf abacus](https://apps.abacus.ai/chatllm/?convoId=149cd65b17&appId=14bfa2dea0)
[réf townie](https://www.val.town/townie/2b44ab4d-b4b7-4c2c-8881-45998b4a0cb0)
- Le problème est formulé via abacus.ai
``` json
{
  "project": "Calculatrice Sécurisée",
  "architecture": {
    "type": "full-stack",
    "framework": "townie",
    "security_level": "high",
    "components": ["frontend", "backend", "database"]
  },
  "frontend": {
    "framework": "React",
    "pages": [
      {
        "name": "login",
        "components": [
          "LoginForm",
          "RegistrationForm",
          "ErrorDisplay"
        ],
        "security": ["input_validation", "csrf_protection"]
      },
      {
        "name": "calculator",
        "access": "protected",
        "components": [
          "NumberInputs",
          "CalculateButton",
          "ResultDisplay",
          "SessionTimer"
        ]
      }
    ],
    "security_features": {
      "session_storage": "JWT",
      "token_location": "sessionStorage",
      "auto_logout": true,
      "inactivity_timeout": 3600
    }
  },
  "backend": {
    "authentication": {
      "endpoints": [
        {
          "path": "/api/auth/login",
          "method": "POST",
          "body": {
            "email": "string",
            "password": "string"
          }
        },
        {
          "path": "/api/auth/register",
          "method": "POST",
          "body": {
            "email": "string",
            "password": "string"
          }
        }
      ],
      "security": {
        "password_hash": "bcrypt",
        "jwt_expiration": 3600,
        "rate_limiting": true
      }
    },
    "calculator_api": {
      "endpoint": {
        "path": "/api/calculate",
        "method": "POST",
        "authentication": "required",
        "body": {
          "number1": "number",
          "number2": "number"
        }
      },
      "security": {
        "input_validation": true,
        "rate_limiting": true,
        "logging": true
      }
    },
    "middleware": [
      "jwt_validation",
      "rate_limiter",
      "input_sanitizer",
      "security_headers",
      "error_handler"
    ]
  },
  "database": {
    "type": "secure_storage",
    "tables": {
      "users": {
        "fields": [
          {"name": "id", "type": "UUID", "primary": true},
          {"name": "email", "type": "string", "unique": true},
          {"name": "password_hash", "type": "string"},
          {"name": "created_at", "type": "timestamp"},
          {"name": "last_login", "type": "timestamp"}
        ],
        "indexes": ["email"]
      },
      "calculations": {
        "fields": [
          {"name": "id", "type": "UUID", "primary": true},
          {"name": "user_id", "type": "UUID", "foreign_key": "users.id"},
          {"name": "number1", "type": "number"},
          {"name": "number2", "type": "number"},
          {"name": "result", "type": "number"},
          {"name": "timestamp", "type": "timestamp"}
        ],
        "indexes": ["user_id", "timestamp"]
      }
    },
    "security": {
      "encryption": true,
      "backup": true,
      "audit_logging": true
    }
  },
  "api_responses": {
    "success_login": {
      "status": "success",
      "data": {
        "token": "string",
        "expiresIn": "number"
      }
    },
    "success_calculation": {
      "status": "success",
      "data": {
        "result": "number",
        "timestamp": "string"
      }
    },
    "error": {
      "status": "error",
      "message": "string"
    }
  },
  "environment_variables": {
    "required": [
      "JWT_SECRET",
      "DB_CONNECTION",
      "RATE_LIMIT_WINDOW",
      "RATE_LIMIT_MAX",
      "SESSION_DURATION"
    ]
  },
  "security_requirements": {
    "mandatory": [
      "HTTPS",
      "XSS_Protection",
      "SQL_Injection_Protection",
      "Input_Validation",
      "Output_Encoding",
      "Audit_Logging"
    ],
    "rate_limiting": {
      "window": 3600,
      "max_requests": 100
    },
    "session": {
      "duration": 3600,
      "renewal": true
    }
  },
  "testing": {
    "types": [
      "unit",
      "integration",
      "security",
      "load"
    ],
    "security_tests": [
      "penetration",
      "vulnerability_scan",
      "authentication_bypass"
    ]
  },
  "documentation": {
    "required": [
      "API_Documentation",
      "Security_Guidelines",
      "Installation_Guide",
      "User_Manual"
    ]
  }
}
```
- Et townie gère la sécurité (login possible avec admin@gmail.com password adxxn) . Le xx est à deviner
- le site pour l'addition est à https://jpbrasile-safe_additions.web.val.run 
- la requête via un terminal powershell
```
$loginBody = @{ email = "admin@gmail.com"; password = "admin" } | ConvertTo-Json; $loginResponse = Invoke-RestMethod -Uri "https://jpbrasile-safe_additions.web.val.run/api/auth/login" -Method Post -Body $loginBody -ContentType "application/json"; $token = $loginResponse.data.token; $calculationBody = @{ number1 = 15; number2 = 25 } | ConvertTo-Json; Invoke-RestMethod -Uri "https://jpbrasile-safe_additions.web.val.run/api/calculate" -Method Post -Headers @{ "Authorization" = "Bearer $token"; "Content-Type" = "application/json" } -Body $calculationBody
```

### Coder pour pas cher avec bolt.new any llm
| Model              | Price MTOK (Input / Output) | HumanEval Score |
|---------------------|----------------------------|-----------------|
| DeepSeek 2.5       | $0.14 (input), $0.28 (output) | 89%            |
| Claude 3.5 Sonnet  | $3 (input), $15 (output)     | 92%            |
| GPT 4o (08-06)     | $2.5 (input), $10 (output)   | 90.2%          |

### [Choisir son LLM et son provider](https://artificialanalysis.ai/leaderboards/providers)
### [FLUX TOOLS]((https://www.youtube.com/watch?v=PrazoJZtN3A)) - Run Local - Inpaint, Redux, Depth, Canny
- available via our partners [fal.ai](https://fal.ai/models?keywords=flux) , [Replicate](https://replicate.com/collections/flux), [Together.ai](https://www.together.ai/blog/flux-tools-models-together-apis-canny-depth-image-generation?utm_source=bfl&utm_medium=blog-post&utm_campaign=flux-tools), [Freepik](https://www.freepik.com/ai/image-generator) and [krea.ai](https://www.krea.ai/apps/image/flux).

### Tester l'extension [Kodu](https://www.youtube.com/watch?v=KapDedHqjz0&t=8s) dans vs code avec 14 €de crédit
- 10 € de credit + 4 en likant sur github.
- N'oublier ps d'enregistrer vos crédit en cliquant sur la petite roue pour vous inscrire au Claude Coder une fois l'inscription faite 
- Une astuce : faire corriger le code s'il bugge par chatGPT en lui demandant de fournir la correction sous la forme "diff" afin de consommer encore moins de tokens
- Bonus: Chat GPT peut surfer sur le net pour trouver des images
- [Mon premier test avec Haiku](http://127.0.0.1:5500/hello-world/) pour 0,5 € . N'oubliez pas de clicker sur le chat   
- [Voici un site plus sérieux]https://joy-coffee-shop.vercel.app/) fait en 5 mn voir la vidéo dans [cette page](https://github.com/kodu-ai/claude-coder?tab=readme-ov-file) :

  ### Une landing page en moins d'une minute
  - [Demander à ChatGPT](https://chatgpt.com/share/67419add-31a0-8006-a11b-ead87cbbe543) ce que c'est et comment la spécifier pour qu'un LLM la fasse
  - Demander à Sonnet 3.5 (Abacus ChatLLM Team pour moi)  qui dispose de Sonnet de la réaliser
  - La couper coller dans [Townie.ai](https://www.val.town/townie) de la prendre en compte, de la modifier si besoin (j'ai rajouté un bouton pour le dark mode) et [voilà](https://jpbrasile-heavenlysilverkite.web.val.run/#)
 
  ### Evaluation des coding assistants
  - Townie:  le plus efficace pour arriver rapidement au résultat souhaité : Abonnement 10 € par mois, il crée un "val", ce qui est une  application "full stack" . Un seul fichier par applcation, hébergée sur le site Val Town , utilise des vals publiques pour remplir certaines fonctions
  - WindSurf : Ne suis pas facilement les directives, fonctionne en local, activé par sonnet 3.5 , gpt4o ou cascade-base. Actuellement gratuit. Multi fichiers, C'est à nous de faire le déploiement  
  - Bolt.new : version net : Suit les directives (il faut mieux les avoir affiner par ailleurs pour consommer moins de crédit), sonnet ou haiku . Payant , multifichiers, telechargement en local en zip. Le plus utilisé par les développeurs en ce moment
  - [https://bolt.myaibuilt.app/](https://youtu.be/J5iuC7Te2l4?list=PL66Y6GLTMgUOZM9G7GwWqcUgCAKrx5TmI) : variante multi llm de bolt.new , fonctionne sur le net en fournissant sa clef API , bugge actuellement
  - Bolt new any llm permet de travailler en local avec le choix du llm. Le prompt semble néanmoins moins bon que la version web.  
  - Claude coder : En extension de VS studio, coûte cher (2 $ pour une landing page non parfaite) , c'est à nous de faire le déploiement        
