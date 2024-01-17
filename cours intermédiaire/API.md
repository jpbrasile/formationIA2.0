## LangChain
- [00:00](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 🤖 LangChain est un framework permettant de créer des applications alimentées par l'IA en JavaScript et en Python.
- [00:13](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 🛡️ LangChain peut se connecter à des sources de données externes telles que des bases de données, des points d'API, des fichiers texte, etc.
- [00:27](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 📚 Cette série est axée sur les débutants, et vous apprendrez à créer un chatbot IA en quelques minutes.
- [01:10](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 📦 Vous aurez besoin de Node.js, d'un éditeur de code comme VS Code, et vous initierez un projet Node.js avec `npm init`.
- [02:05](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 📦 Vous installerez les dépendances LangChain et LangChain OpenAI avec `npm install`.
- [02:42](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 🔑 Vous créerez un modèle LangChain OpenAI en utilisant votre clé API OpenAI.
- [04:03](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 💬 Vous utiliserez le modèle pour générer des réponses en utilisant la méthode `invoke`.
- [05:13](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 💬 Vous explorerez d'autres méthodes telles que `batch` et `stream` pour obtenir plusieurs réponses ou un flux continu.
- [06:34](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 🔑 Vous stockerez votre clé API OpenAI dans une variable d'environnement pour plus de sécurité.
- [08:00](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 🔧 Vous explorerez les paramètres du modèle, tels que le nom du modèle, la température, le nombre maximum de tokens et la verbosité.
- [09:20](https://www.youtube.com/watch?v=MaSynwSIty4&list=PL4HikwTaYE0EG379sViZZ6QsFMjJ5Lfwj) 🤖 Vous avez créé votre première application LangChain et chatbot, et vous explorerez les modèles de prompt pour contrôler la conversation.
- [00:00](https://www.youtube.com/watch?v=VeqhLz3E_To&t=0s) 🤖 Dans cette vidéo, nous abordons l'utilisation des modèles de prompts pour contrôler le comportement de l'IA de LangChain.
- [01:09](https://www.youtube.com/watch?v=VeqhLz3E_To&t=69s) 🃏 Les modèles de prompts permettent de créer des applications AI qui génèrent des réponses spécifiques en fonction des mots saisis par l'utilisateur, comme des blagues basées sur un mot donné.
- [02:05](https://www.youtube.com/watch?v=VeqhLz3E_To&t=125s) 💬 Il existe deux méthodes pour créer des modèles de prompts : `doFromTemplate` pour une configuration simple et `fromMessages` pour plus de flexibilité.
- [03:38](https://www.youtube.com/watch?v=VeqhLz3E_To&t=218s) 🔗 La création d'une chaîne (chain) permet de combiner un modèle de prompt avec le modèle d'IA pour obtenir des réponses personnalisées.
- [05:16](https://www.youtube.com/watch?v=VeqhLz3E_To&t=316s) 📜 La méthode `fromMessages` permet de créer des modèles de prompts en utilisant des paires clé-valeur pour les messages système et humains, offrant une approche plus dynamique et propre.
- [06:47](https://www.youtube.com/watch?v=VeqhLz3E_To&t=407s) 🔄 LangChain propose des outils pour formater les réponses de manière précise en utilisant des analyseurs de sortie (output parsers).
-  [00:00](https://www.youtube.com/watch?v=vvZ4cyxl99Q&t=0s) 🤖 Les output parsers de LangChain permettent de contrôler la structure et le format des réponses renvoyées par l'IA.
- [02:03](https://www.youtube.com/watch?v=vvZ4cyxl99Q&t=123s) 🧰 Le parser "string output parser" permet de convertir une réponse en chaîne de caractères.
- [05:03](https://www.youtube.com/watch?v=vvZ4cyxl99Q&t=303s) 📋 Le parser "comma separated list output parser" transforme une chaîne en un tableau JavaScript.
- [10:18](https://www.youtube.com/watch?v=vvZ4cyxl99Q&t=618s) 🏷️ Le parser "structured output parser" permet de convertir une réponse en un objet JavaScript structuré.
- [11:54](https://www.youtube.com/watch?v=vvZ4cyxl99Q&t=714s) 🌟 Le parser "from Zod schema" permet de créer des structures complexes et d'extraire des informations de manière avancée.


| Explications | Code Python |
|---------------|-------------|
| **Importation de Modules** : `import { ChatOpenAI } from "@langchain/openai";` importe une fonctionnalité de `ChatOpenAI` depuis le module `langchain/openai`. `import readline from "readline";` et `import * as dotenv from "dotenv";` importent les modules `readline` et `dotenv`. | `import { ChatOpenAI } from "@langchain/openai";`<br>`import readline from "readline";`<br>`// Import environment variables`<br>`import * as dotenv from "dotenv";`<br>`dotenv.config();` |
| **Configuration des Variables d'Environnement** : `dotenv.config();` charge les variables d'environnement. | `dotenv.config();` |
| **Création d'une Interface de Lecture** : `const rl = readline.createInterface({...});` crée une interface de lecture pour lire les entrées de l'utilisateur. | `// Create a readline interface to read user input`<br>`const rl = readline.createInterface({ input: process.stdin, output: process.stdout, });` |
| **Fonction de Communication avec l'IA** : `async function chatCompletion(text){...}` est une fonction asynchrone qui utilise le modèle `gpt-3.5-turbo` d'OpenAI pour obtenir une réponse. | `// Create a function to call the Langchain API`<br>`async function chatCompletion(text) {`<br>`const model = new ChatOpenAI({ modelName: "gpt-3.5-turbo", temperature: 0.9, });`<br>`const response = await model.invoke(text);`<br>`console.log("AI:", response.content); }` |
| **Affichage de la Réponse de l'IA** : `console.log("AI:", response.content);` affiche la réponse de l'IA. | `console.log("AI:", response.content);` |
| **Fonction pour Demander l'Entrée de l'Utilisateur** : `function getPrompt() {...}` pose une question et appelle `chatCompletion` ou ferme l'interface. | `// Create a function to ask for user input`<br>`function getPrompt() { rl.question("Enter your prompt: ", (input) => { if (input.toUpperCase() === "EXIT") { rl.close(); } else { chatCompletion(input).then(() => getPrompt()); } }); }`<br>`getPrompt(); // Start the prompt` |
