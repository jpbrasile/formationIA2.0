<strong>Différence entre GitHub Codespaces et GitHub Actions</strong><br>
GitHub Codespaces est pour le développement en ligne, GitHub Actions pour l'automatisation des workflows.

<details>
<summary><strong>Tutoriel sur la Synchronisation entre GitHub et Local</strong></summary>
<p>

<strong>Concepts de Base</strong><br>
1. <strong>Git et GitHub</strong>: Git est un système de contrôle de version distribué qui permet de suivre les modifications apportées aux fichiers. GitHub est un service en ligne qui héberge des dépôts Git, facilitant la collaboration et la gestion de projets.<br>
2. <strong>Clone</strong>: Cloner un dépôt signifie créer une copie locale du dépôt qui se trouve sur GitHub.<br>
3. <strong>Commit</strong>: Un commit est une capture de l'état de vos fichiers à un moment donné. C'est comme une photographie de votre projet.<br>
4. <strong>Push</strong>: Push envoie vos commits locaux sur le serveur GitHub. Cela met à jour le dépôt en ligne avec vos modifications locales.<br>
5. <strong>Pull</strong>: Pull récupère les modifications depuis le dépôt GitHub et les fusionne dans votre répertoire local.<br>
6. <strong>Branch</strong>: Une branche est une version parallèle de votre dépôt. Elle est utile pour développer des fonctionnalités, corriger des bugs, ou tester des idées en isolation.<br>

<strong>Exemple Pratique</strong><br>
<strong>Configuration Initiale</strong><br>
Assurez-vous que Git est installé sur votre machine. Configurez votre identité Git :<br>
<code>git config --global user.name "Votre Nom"</code><br>
<code>git config --global user.email "votre.email@example.com"</code><br>

<strong>Cloner un Répertoire</strong><br>
Trouvez le dépôt sur GitHub que vous voulez cloner. Copiez son URL.<br>
<code>git clone https://github.com/user/repo.git</code><br>

<strong>Faire des Changements et Commits</strong><br>
Faites des modifications dans les fichiers de votre dépôt local. Ajoutez les fichiers modifiés à la zone de staging :<br>
<code>git add .</code><br>
Créez un commit avec vos modifications :<br>
<code>git commit -m "Description des changements"</code><br>

<strong>Envoyer les Modifications sur GitHub</strong><br>
Envoyez vos commits locaux vers GitHub :<br>
<code>git push</code><br>

<strong>Récupérer les Modifications de GitHub</strong><br>
Pour récupérer les derniers changements du dépôt GitHub :<br>
<code>git pull</code><br>

<strong>Travailler avec les Branches</strong><br>
Créer une nouvelle branche :<br>
<code>git branch nom_de_la_branche</code><br>
Basculer vers cette branche :<br>
<code>git checkout nom_de_la_branche</code><br>
Fusionner les changements d'une branche dans la branche principale (main) :<br>
<code>git checkout main</code><br>
<code>git merge nom_de_la_branche</code><br>

<strong>Pousser une Branche sur GitHub</strong><br>
Pour envoyer une nouvelle branche sur GitHub :<br>
<code>git push -u origin nom_de_la_branche</code><br>

</p>
</details>

<details>
<summary><strong>Tutoriel sur GitHub Codespaces</strong></summary>
<p>
<strong>Qu'est-ce que GitHub Codespaces ?</strong><br>
Un environnement de développement intégré (IDE) basé sur le cloud.<br>

<strong>Comment utiliser GitHub Codespaces ?</strong><br>
a. <strong>Démarrage d'un Codespace</strong>: Ouvrez le référentiel sur GitHub, cliquez sur Code, puis sur Open with Codespaces et New codespace.<br>
b. <strong>Développement dans Codespaces</strong>: Codez, exécutez et déboguez dans votre navigateur.<br>
c. <strong>Exemple d'utilisation</strong>:<br>
<pre><code>
Clonage et modification d'un projet
1. Ouvrez le Codespace pour le référentiel.
2. Clonez avec 'git clone [URL_DU_REPO]'.
3. Modifiez les fichiers et utilisez git.
</code></pre>
</p>
</details>

<details>
<summary><strong>Tutoriel sur GitHub Actions</strong></summary>
<p>
<strong>Qu'est-ce que GitHub Actions ?</strong><br>
Un outil d'automatisation pour créer des workflows personnalisés.<br>

<strong>Comment utiliser GitHub Actions ?</strong><br>
a. <strong>Création d'un Workflow</strong>: Créez un dossier .github/workflows et un fichier YAML.<br>
b. <strong>Configuration du Workflow</strong>: Définissez les étapes et événements déclencheurs en YAML.<br>
c. <strong>Exemple de Workflow</strong>:<br>
<pre><code>
Workflow pour l'intégration continue
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run a script
        run: echo "Workflow déclenché"
</code></pre>
</p>
</details>



<details>
<summary><strong>Utilisation de helloWorld.py avec GitHub Codespaces</strong></summary>
<p>
<strong>Ouvrez un Codespace pour votre référentiel :</strong><br>
- Sur la page de votre référentiel sur GitHub, cliquez sur le bouton Code puis choisissez Open with Codespaces.<br>
- Cliquez sur New codespace pour démarrer un environnement de développement.<br>
<strong>Travaillez avec helloWorld.py dans Codespaces :</strong><br>
- Une fois dans Codespaces, votre référentiel sera déjà cloné.<br>
- Naviguez jusqu'à votre fichier helloWorld.py et modifiez-le dans l'éditeur en ligne.<br>
- Pour exécuter le script, ouvrez un terminal dans Codespaces et tapez <code>python helloWorld.py</code>.<br>
<strong>Sauvegardez vos changements :</strong><br>
- Utilisez <code>git add</code>, <code>git commit</code>, et <code>git push</code> pour sauvegarder les modifications dans votre référentiel.<br>
</p>
</details>

<details>
<summary><strong>Utilisation de helloWorld.py avec GitHub Actions</strong></summary>
<p>
<strong>Créez un Workflow GitHub Actions :</strong><br>
- Dans votre référentiel GitHub, créez un dossier .github/workflows si nécessaire.<br>
- Créez un fichier YAML dans ce dossier, par exemple <code>python-app.yml</code>.<br>
<strong>Configurez le Workflow pour exécuter helloWorld.py :</strong><br>
- Exemple de fichier YAML pour exécuter votre script Python lors d'un push sur la branche principale:<br>
<pre><code>
name: Run Python Script
on: push
  branches: [ main ]
jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          # Installez vos dépendances ici
      - name: Run script
        run: python helloWorld.py
</code></pre>
<strong>Activez le Workflow :</strong><br>
- Une fois le fichier YAML poussé dans votre référentiel, GitHub Actions sera configuré pour exécuter votre script à chaque push sur la branche spécifiée.<br>
</p>
</details>
