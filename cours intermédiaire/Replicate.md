

# Guide d'Installation et d'Utilisation de Replicate

## Introduction

Ce guide vous montrera comment installer et utiliser Replicate avec des exemples de code Python pour accéder au modèle de langage Llama 2 70B. Suivez les étapes ci-dessous pour commencer.

## Étape 1 : Créez un Compte Replicate

1. Rendez-vous sur le site web de Replicate : [Replicate](https://lifeboat.replicate.dev/).

2. Inscrivez-vous et créez un compte Replicate.

## Étape 2 : Copiez Votre Clé API Replicate

3. Après avoir créé votre compte, copiez votre clé API Replicate dans un endroit sûr

## Étape 3 : Variable d'environnement:
Dans un terminal powerShell  renseignez la variable avec votre clef
```
$env:REPLICATE_API_TOKEN = "r8....me" 
```
## Étape 4 : Exemple de code python: app.py :
   ```python
# Utilise l'environnement conda "replicate":

#conda create --name replicate python=3.9
#conda activate replicate
#pip install replicate
# dans un terminal powershell : 
#$env:REPLICATE_API_TOKEN = "r8_A7on1VwSgmGOPEjhdhRMUFS7TQUGWQy1QG9me"

import replicate
output = replicate.run(
    "mistralai/mixtral-8x7b-instruct-v0.1:cf18decbf51c27fed6bbdc3492312c1c903222a56e3fe9ca02d6cbe5198afc10",
    input={
        "top_k": 50,
        "top_p": 0.9,
        "prompt": "équation de la magnétostatique reliant le potentiel vecteur magnétique à la densité de courant. Raisonne pas à pas mais soit très concis: les formules sans commentaire",
        "temperature": 0.6,
        "max_new_tokens": 512,
        "prompt_template": "<s>[INST] {prompt} [/INST]"
    }
)
output_string = ''.join(output)
print(output_string)
```

## On lance le code dans un terminal avec
```Python
python run app.py
```
et on obtient en sortie:
```
La magnétostatique est décrite par l'équation de Maxwell-Ampère, qui relie le champ magnétique à la densité de courant :

∇ x B = μ₀J

où B est le champ magnétique, J est la densité de courant, et μ₀ est la perméabilité du vide.

En utilisant le potentiel vecteur magnétique A, défini par B = ∇ x A, on peut réécrire l'équation de Maxwell-Ampère sous la forme :   

∇ x (∇ x A) = μ₀J

En utilisant une identité vectorielle, on obtient l'équation de la magnétostatique en termes de A :

∇ (∇ . A) - ∇²A = μ₀J

Comme il n'y a pas de charge monopolaire magnétique, on a ∇ . B = ∇ . (∇ x A) = 0, ce qui implique que ∇ . A est une constante. On peut donc choisir la jauge de Coulomb, où cette constante est nulle, ce qui simplifie l'équation en :

- ∇²A = μ₀J

Cette équation montre que le potentiel vecteur magnétique A est directement proportionnel à la densité de courant J
```
