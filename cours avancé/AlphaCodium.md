## [AlphaCodium](https://github.com/Codium-ai/AlphaCodium)

- [00:00](https://www.youtube.com/watch?v=0-ptMUUSZ7w&t=0s) 🤖 Présentation d'AlphaCodium, une nouvelle approche pour la génération de code avec les modèles de langage.
  - Introduction du concept AlphaCodium, un outil basé sur les modèles de langage pour améliorer la génération de code.
  - AlphaCodium résout des problèmes spécifiques aux modèles de langage lors de la génération de code, notamment la syntaxe et les cas d'utilisation.

- [01:08](https://www.youtube.com/watch?v=0-ptMUUSZ7w&t=68s) 🚀 Améliorations apportées par AlphaCodium et disponibilité du code sur GitHub.
  - AlphaCodium a augmenté l'efficacité de GP4 de 19% à 44% sur un ensemble de données de codage complexe.
  - Le code AlphaCodium est accessible sur GitHub pour une installation et un test locaux.

- [02:06](https://www.youtube.com/watch?v=0-ptMUUSZ7w&t=126s) 💻 Processus d'installation d'AlphaCodium sur un système local.
  - Démonstration de l'installation d'AlphaCodium sur un système Linux.
  - Instructions détaillées pour cloner le repo, installer les exigences et configurer l'API OpenAI.

- [04:24](https://www.youtube.com/watch?v=0-ptMUUSZ7w&t=264s) 📊 Téléchargement et utilisation du jeu de données pour AlphaCodium.
  - Téléchargement et décompression d'un jeu de données pour tester AlphaCodium.
  - Explication de la procédure de téléchargement et de préparation des données.

- [05:48](https://www.youtube.com/watch?v=0-ptMUUSZ7w&t=348s) 🧪 Exécution d'AlphaCodium pour résoudre un problème spécifique.
  - Utilisation d'AlphaCodium pour résoudre un problème de codage à partir d'un jeu de données.
  - Explication du processus de sélection et de résolution d'un problème de codage.

- [07:57](https://www.youtube.com/watch?v=0-ptMUUSZ7w&t=477s) 📝 Conclusion et implications d'AlphaCodium.
  - Résumé des capacités d'AlphaCodium et de son impact potentiel.
  - Invitation à explorer davantage le papier et le code pour ceux qui sont intéressés.
 
### Installation dans un environement conda
```
conda create --name alphacodium
conda activate alphacodium
git clone https://github.com/Codium-ai/AlphaCodium.git
cd  .\AlphaCodium\
pip install -r requirements.txt
$env:ENV_FOR_DYNACONF = "development"
python -m alpha_codium.solve_problem --dataset_name "C:\Users\test\Documents\Formation IA\AlphaCodium\AlphaCodium\codecontests_valid_and_test_processed_alpha_codium\valid_and_test_processed" --split_name test --problem_number 0

```
-  Il faut télécharger la base de données https://huggingface.co/datasets/talrid/CodeContests_valid_and_test_AlphaCodium/resolve/main/codecontests_valid_and_test_processed_alpha_codium.zip
-  Nous avons modifié le code de "C:\Users\test\Documents\Formation IA\AlphaCodium\AlphaCodium\alpha_codium\llm\ai_handler.py" pour le faire fonctionner avec lm studio (mixtral-8x7b-instruct-v0.1.Q5_0.gguf)
  ```   try:
        try:
            if "gpt" in get_settings().get("config.model").lower():

                # Accessing the LOCAL variable from environment
                LOCAL = os.getenv('LOCAL', '0') # Default to '0' if not set

                if "gpt" in get_settings().get("config.model").lower():
                    if LOCAL == '1':
                        # Configuration for local server
                        openai.api_key = "not needed"
                        openai.api_base = "http://localhost:1234/v1"
                        litellm.api_base = "http://localhost:1234/v1"
                        litellm.openai_key = "not needed"
                    else:
                        # Configuration for OpenAI's API
                        openai.api_key = get_settings().openai.key
                        #openai.api_base = "https://api.openai.com/v1"
                        #litellm.api_base = "https://api.openai.com/v1"
                        litellm.openai_key = get_settings().openai.key

   ```
-AlphaCodium est lancé sur le premier problème avec :
 ```
$env:LOCAL = "1" # Sets LOCAL to 1 for local server
# or
$env:LOCAL = "0" # Sets LOCAL to 0 for using OpenAI's API
```
- Il faut créer un fichier "C:\Users\test\Documents\Formation IA\AlphaCodium\AlphaCodium\alpha_codium\settings\.secrets.toml" contenant:
```
[openai]
key="sk-wsZQ.....vPyiuaDA"
```
- Nous avons modifié le GPT par défaut d'OpenAI dans C:\Users\test\Documents\Formation IA\AlphaCodium\AlphaCodium\alpha_codium\settings\configuration.toml
- En effet GPT-4-1106-preview est 3 fois [moins cher](https://openai.com/pricing) pour les mêmes performances
```
[config]
model="gpt-4-1106-preview"
#model="gpt-4-0613"
```
- Puis on lance la résolution d'un problème avec :
``` 
 python -m alpha_codium.solve_problem --dataset_name "C:\Users\test\Documents\Formation IA\AlphaCodium\AlphaCodium\codecontests_valid_and_test_processed_alpha_codium\valid_and_test_processed" --split_name test --problem_number 0
 ```

- Les problèmes traités se retrouvent [ici](https://huggingface.co/datasets/deepmind/code_contests)
- Actuelleemnt (26/01/2024) alphacodium ne résoud aucun problème, même en configuration GPT4. LE problème 1 est résolu en 2 itérations sur ChatGPT avec le prompt:
```
problem description:
Mr. Chanek lives in a city represented as a plane. He wants to build an amusement park in the shape of a circle of radius r. 
The circle must touch the origin (point (0, 0)).
There are n bird habitats that can be a photo spot for the tourists in the park. The i-th bird habitat is at point p_i = (x_i, y_i). 

Find the minimum radius r of a park with at least k bird habitats inside. 

A point is considered to be inside the park if and only if the distance between p_i and the center of the park is less than or equal 
to the radius of the park.
Note that the center and the radius of the park do not need to be integers.

In this problem, it is guaranteed that the given input always has a solution with r ≤ 2 ⋅ 10^5.

Input

The first line contains two integers n and k (1 ≤ n ≤ 10^5, 1 ≤ k ≤ n) — the number of bird habitats in the city and the number of bird 
habitats required to be inside the park.
The i-th of the next n lines contains two integers x_i and y_i (0 ≤ |x_i|, |y_i| ≤ 10^5) — the position of the i-th bird habitat.

Output

Output a single real number r denoting the minimum radius of a park with at least k bird habitats inside. It is guaranteed that the given 
input always has a solution with r ≤ 2 ⋅ 10^5.
Your answer is considered correct if its absolute or relative error does not exceed 10^{-4}.
Formally, let your answer be a, and the jury's answer be b. Your answer is accepted if and only if \frac{|a - b|}{max{(1, |b|)}} ≤ 10^{-4}.

Examples

Input

8 4
-3 1
-4 4
1 5
2 2
2 -2
-2 -4
-1 -1
-6 0

Output

3.1622776589


Input

1 1
0 0


Output

0.0000000000

Note

In the first example, Mr. Chanek can put the center of the park at (-3, -1) with radius √{10} ≈ 3.162. It can be proven this is the minimum r.
```

  

