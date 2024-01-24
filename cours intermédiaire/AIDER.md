## [Aider.chat](https://aider.chat)

**Fonctionnalités:**
Aider.chat est un outil d'assistance à la programmation par intelligence artificielle qui fonctionne dans le terminal. Il offre les fonctionnalités suivantes :

- **Commandes en chat**: Permet d'exécuter des commandes directement dans le chat, qui commencent toutes par `/`. Par exemple, `/add <file>` pour ajouter des fichiers à la session de chat, ou `/undo` pour annuler le dernier commit Git effectué par aider[1].
- **Support vocal**: Vous pouvez parler à aider pour demander des modifications de code avec votre voix[1].
- **Gestion de fichiers**: Ajoutez ou supprimez des fichiers de la session de chat pour aider l'IA à déterminer quels fichiers modifier[1].
- **Exécution de commandes shell**: Exécutez des commandes shell et ajoutez éventuellement la sortie au chat[1].
- **Aide et astuces**: Utilisez `/help` pour afficher de l'aide sur toutes les commandes et recevoir des conseils pour une utilisation efficace[1].
  
**Installation**: Fait dans l'environnement conda "formation"
```Python
$env:OPENAI_API_KEY="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"
git config user.name "jpbrasile"
```

**Guide d'utilisation basique:**
1. Ouvrez votre terminal et démarrez aider.chat.
```
aider hello.js
```
voilà le résultat (ma demande en vert), le code javascript mis à jour ! 
   ![image](https://github.com/jpbrasile/formationIA2.0/assets/8331027/30ee6075-f2fc-4bca-8c2c-187eb62a048a)

3. Utilisez la commande `/add <file>` pour ajouter les fichiers sur lesquels vous souhaitez travailler.
4. Pour exécuter une commande shell, tapez `/run <command>`.
5. Si vous avez besoin d'annuler un commit, utilisez `/undo`.
6. Pour parler à aider, activez la commande `/voice` et donnez vos instructions vocalement.
7. En cas de besoin, tapez `/help` pour obtenir de l'aide sur les commandes disponibles.

## [AIDER avec un modèle local](https://aider.chat/docs/faq.html#how-can-i-run-aider-locally-from-source-code) (LM studio)

On met dans le fichier .aider.conf.yml :
```
openai-api-key:"not-needed"
openai-api-base:http://localhost:1234/v1"
```

On lance AIDER avec:
```
# Clone the repository:
git clone git@github.com:paul-gauthier/aider.git

# Navigate to the project directory:
cd aider

# Install the dependencies listed in the `requirements.txt` file:
pip install -r requirements.txt

# Run the local version of Aider:
python -m aider.main
```

