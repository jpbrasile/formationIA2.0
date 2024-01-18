<details>
<summary>Tutoriel sur la Synchronisation entre GitHub et Local</summary>

## Concepts de Base
1. **Git et GitHub**
   Git est un système de contrôle de version distribué qui permet de suivre les modifications apportées aux fichiers. GitHub est un service en ligne qui héberge des dépôts Git, facilitant la collaboration et la gestion de projets.

2. **Clone**
   Cloner un dépôt signifie créer une copie locale du dépôt qui se trouve sur GitHub.

3. **Commit**
   Un commit est une capture de l'état de vos fichiers à un moment donné. C'est comme une photographie de votre projet.

4. **Push**
   Push envoie vos commits locaux sur le serveur GitHub. Cela met à jour le dépôt en ligne avec vos modifications locales.

5. **Pull**
   Pull récupère les modifications depuis le dépôt GitHub et les fusionne dans votre répertoire local.

6. **Branch**
   Une branche est une version parallèle de votre dépôt. Elle est utile pour développer des fonctionnalités, corriger des bugs, ou tester des idées en isolation.

## Exemple Pratique

### Configuration Initiale
Assurez-vous que Git est installé sur votre machine. Configurez votre identité Git :
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
Cloner un Répertoire
Trouvez le dépôt sur GitHub que vous voulez cloner. Copiez son URL.
Clonez le dépôt :

git clone https://github.com/user/repo.git
Faire des Changements et Commits
Faites des modifications dans les fichiers de votre dépôt local. Ajoutez les fichiers modifiés à la zone de staging :

git add .
Créez un commit avec vos modifications :

git commit -m "Description des changements"
Envoyer les Modifications sur GitHub
Envoyez vos commits locaux vers GitHub :

git push
Récupérer les Modifications de GitHub
Pour récupérer les derniers changements du dépôt GitHub :

git pull
Travailler avec les Branches
Créer une nouvelle branche :

git branch nom_de_la_branche
Basculer vers cette branche :

git checkout nom_de_la_branche
Fusionner les changements d'une branche dans la branche principale (main) :

git checkout main
git merge nom_de_la_branche
Pousser une Branche sur GitHub
Pour envoyer une nouvelle branche sur GitHub :

git push -u origin nom_de_la_branche
```
