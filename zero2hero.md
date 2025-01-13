### RoadMap
- Programmer avec l'IA
  - **VS code**, **Docker** , **Github** en préalable 
  - **Bolt.diy** avec **deepseekV3** est le meilleur framework pour créer une application.Pendre **gemini** s'y besoin multimodal
  - **Townie** (Val Town) crée et dépoie très facilement des site web 
  - **Roo Cline** est une extension pour **VS code**    
  - Se former aux frameworks: Le code à été créer sur chatllm d'abacus et repris pour un déploiement rapide sur townie ( de val Town)
    - [_tailwind_](https://jpbrasile-tailwindcsscheatsheetquiz.web.val.run/)
    - [_html_](https://jpbrasile-wholesomeindigotortoise.web.val.run/) 
    - [_REACT_](https://jpbrasile-illustriousbeigechimpanzee.web.val.run) (Ici j'ai demandé que les styles soient réalisés avec Tailwind, j'ai utilisé le large contexte de Gemini pour écrire le code complet, à partir d'une base qui provenait d'Abacus. En cas de bugs, comme le code est grand (1000 lignes de code), je demandais les corrections en mode diff. Ensuite j'ai fait le portage sur Townie pour un déploiement en un clic.   

### Création d'un teaser, déployée sur le web à partir des données mise au format markdown, en suivant un style que l'on maîtrise avec Townie 
<details>
  <summary>[En entrée]</summary>
  
## 💡 Le Thésard 2.0 : Architecte d'un Futur Décarboné

### 🚀 Thésard 2.0 : L'avenir se réinvente.
Le Thésard 2.0 : une nouvelle approche de la recherche doctorale, une ambition : **transformer le monde**! Pendant ses trois années de thèse, il ne se contente pas d'explorer, il **façonne**. Son objectif : **décarboner** notre société grâce à des **technologies innovantes** et **rentables**.

### 🤔 D’abord comprendre l’enjeu et les besoins
Le Thésard 2.0 est l'architecte de sa recherche. Il choisit sa cible dans le vaste champ de la **décarbonation**, il se rapproche activement des futurs utilisateurs son procédé, ses clients potentiels. Leurs retours précisent son objectif pour que sa thèse réponde à un besoin **réel** et **tangible**.

### 🎯 Une thèse avec un TRL 7 en objectif
La thèse dépasse le cadre académique : Elle permet l’**innovation** avec un socle initial en TR4, propulsé vers de nouveaux sommets avec une **solution concrète pour la décarbonation**, prête à être implémentée dans le **monde réel**.

### ⚡ Faire plus et mieux en 3 ans !
Le Thésard 2.0 est un **pilote** de la technologie, non son passager. ‘’Il s’assoie sur les épaules de l’IA’’ :
  *  🔎 Pour faire l'état de l'art plus facilement avec le **Web Scrapper 2.0**
  *  🧠 Pour en assimiler le contenu avec le **professeur 2.0**
  *  ✍️ Pour l'aider dans la rédaction et la mise en forme de sa thèse


### ⚙️ Il façonne le clone de son procédé au fil des expérimentations
  * 🧪 Il s’appuie sur les dernières avancées dans le **calcul scientifique**
  * 👯 Il crée le **procédé 2.0**, le **jumeau numérique** de son procédé
  * 🚀 Il va plus facilement vers le processus optimal grâce à un **optimiseur 2.0**


### 🤝 L'intelligence collective et l'innovation partagée :
Pour le Thésard 2.0, l'innovation est **collective**. Il exploite un **générateur pulsé 2.0**, développe un réacteur pensé pour l'industrie, et partage son expérience en **IA** et **jumeaux numériques** via le **Fablab 2.0** qui réunit tous les thésard 2.0 et où l’**impression 3D de céramique des réacteurs** est permise.

### 📈 Le passage à l'échelle, fruit d'un effort concerté :
C’est **travailler en équipe** pour un but commun : ensemble, thésards 2.0, centres de recherche et industriels en support, donneront vie au **pilote 2.0** qui **validera votre procédé** jusqu’à 200 kW moyen et 1 MW crête. Vous transformez nos travaux préliminaires visant à constituer la dream team et le tour de table financier en réalité.

### 💼 Du thésard 2.0 au professionnel 2.0
Au-delà de la thèse vous partez sur le chemin professionnel avec un **réseau professionnel** solide car bâti sur un travail commun, un **jumeau numérique** et d’un autre outil multi-usage : celui d’avoir appris à **apprendre à apprendre** !
</details>

[et en sortie](https://jpbrasile-teasertemplate.web.val.run/)

- Le code est réutilisable pour l'adapter à tout contenu en markdown. On y arrive avec ce prompt dans townie:

`
Je veux que la partie code soit indépendante du contenu fourni en mode markdown.  ce n'est pas le cas actuellement Il faut passer par une étape préalable qui transforme la syntaxe markdown en syntaxe Tailwind via l'appel à une fonction   
`
