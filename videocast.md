Ceci est la road map pour créer une vidéocast haut de gamme
## Création du podcast
### Scénario:
Crée le scénario en interagissant avec un llm avec le prompt :
"Fournis-moi le texte d'un podcast en **100** mots environ entre deux personnages concertant le [sujet]
sous la forme [voix 1] texte [voix 2] texte [voix 1] ....
[sujet] **L'IA dans 50 ans** [/sujet]" 

Le résultat avec ChatGPT": [Podcast]

[Voix 1] : Bonjour et bienvenue à tous ! Aujourd’hui, on se pose une grande question : à quoi ressemblera l’intelligence artificielle dans 50 ans ?

[Voix 2] : Salut ! Une question fascinante. Personnellement, je pense que l’IA sera omniprésente, intégrée dans nos vies au point qu’on ne la remarquera plus, comme l’électricité aujourd’hui.

[Voix 1] : C’est probable ! Mais est-ce qu’elle sera plus autonome ? Certains disent qu’elle pourrait dépasser l’intelligence humaine.

[Voix 2] : Oui, mais cela soulève aussi des enjeux éthiques. Il faudra veiller à ce que l’IA reste un outil au service de l’humanité.

[Voix 1] : Absolument. Merci pour ces réflexions ! À bientôt.

### Voice over 
- Nous allons utiliser le [plugin de ChatGPT pour windows ou mac](https://openai.com/chatgpt/desktop/) qui offre des qualités de voix exceptionnelles, huit voix sont disponibles qui parlent avec les intonnations requises par le texte lu et le prompt que l'on peut lui donner en supplément.
- Le problème est que si on active le mode voix, on part sur un nouveau chat et on n'a plus la main pour injecter le texte à lire.
- La solution est de personaliser notre ChatGPT pour qu'il le connaisse grâce à la [customisation](https://raw.githubusercontent.com/jpbrasile/images/refs/heads/main/Capture%20d'%C3%A9cran%202024-11-20%20084559.png), en cliquant sur "personnaliser ChatGPT". 
- voilà le type de script à insérer:
Tu es un acteur qui joue la voix 1 pendant qu'on enregistre:
"Répète mot à mot seulement la [voix 1] du [podcast] suivant en laissant une période de silence pour la voix 2 **puis tu continues ton script jusqu'au bout .  Lis en étant expressif car tu joues le personnage. Démarre sans attendre mes directives car le micro est inhibé pendant l'enregistrement. 

[podcast]

[Voix 1] : Bonjour à toutes et à tous, bienvenue dans notre podcast ! Aujourd'hui, nous allons parler des bienfaits de la méditation. Pour commencer, qu'est-ce que ça signifie pour toi, la méditation ?

[Voix 2] : Salut ! Merci de m'avoir invité. Pour moi, la méditation, c'est un moment de pause dans le tumulte de la journée. Mais je sais qu'il y a beaucoup d'approches différentes. Et toi, comment tu pratiques ?

[Voix 1] : Oui, tu as raison. Pour ma part, je me concentre beaucoup sur la respiration. Par exemple, chaque matin, je fais une séance de 10 minutes. Ça m'aide à démarrer la journée avec clarté.

[Voix 2] : Intéressant ! Moi, je préfère méditer en soirée. Ça me permet de décompresser après une journée bien remplie. Je trouve que ça aide vraiment à mieux dormir.

[Voix 1] : Ah, c'est une bonne idée. En parlant de ça, il y a une question que beaucoup de gens posent : faut-il forcément être assis en tailleur pour méditer ?

[Voix 2] : Pas du tout ! En fait, on peut méditer partout : assis sur une chaise, allongé, ou même en marchant. L'important, c'est d'être à l'aise.[/podcast]


- La voix 1 doit maintenant être enregistrée sous la forme d'un mp3. Il faut pour ça rediriger le flux sonore sur VLC media player 
- Ensuite changer de voix dans le prompt système et enregistrer la voix 2
### Création des deux avatars parlant à partir d'une vidéo
- pouvant provenir d'un text --> image --> video)
- [référence open source](https://github.com/TMElyralab/MuseTalk?tab=readme-ov-file)

### Montage final de la video sur Capcut ou Canva:
- coupure des blancs dans la bande son pour que le podcast se fasse sans latence
