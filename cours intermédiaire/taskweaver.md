## Installation
- Faite dans l'environneemnt conda (taskweaver env)
- Suivre les instructions
- Attention : le fichier "taskweaver_config.json" doit être mis dans C:\Users\test\Documents\Formation IA\taskweaver\TaskWeaver\ **project** pour être reconnu
- Le fichier "taskweaver_config.json" en local: 
```Python
{
    "llm.api_base": "http://localhost:1234/v1",
    "llm.api_key": "anything",
    "llm.model": "local llm"
  }
```
- Installer aussi chainlit:
![Capture d'écran 2024-01-22 142201](https://github.com/jpbrasile/formationIA2.0/assets/8331027/11c8a1a5-2f88-4ea2-9177-78f7917d6172)


![Capture d'écran 2024-01-22 141630](https://github.com/jpbrasile/formationIA2.0/assets/8331027/58ee0298-aa10-44c2-b83e-1e2ca77eeac9)
```
- Taskweaver a la capacité de lire des fichiers locaux. En fait il crée le code ad hoc pour y arriver ! Malheureusement il perd du temps à itérer car les bibliothèques requises ne sont pas charger au départ ! Il perd donc quelques itérations à le constater et à faire les pip install nécessaire.
- Donc bien que très lent , taskweaver est très performant car s'il n'a pas une fonctionnalité il créer le code pour s'en doter et l'exécute ensuite... 
