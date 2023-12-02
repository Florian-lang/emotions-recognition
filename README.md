# Documentation

## Configuration 
- Installer le gestionnaire pip des packages python :
    > `sudo apt update` 

    > `sudo apt install python3-pip`

- Créer un compte kaggle afin de pouvoir télécharger le dataset : https://www.kaggle.com/

- Se rendre dans les paramètres de votre compte : https://www.kaggle.com/settings

- Descendre dans la troisième section de la page nommée API et cliquer sur "Create New Token".
Un fichier kaggle.json sera téléchargé

- Vérifier si le dossier kaggle existe en faisant la commande :
    > `ls -l ~/.kaggle`

- Si le répertoire existe vous pouvez insérer votre fichier kaggle.json à l'emplacement suivant 
    > `cp 'chemin vers la position actuelle de votre kaggle.json' '~/.kaggle/kaggle.json'`

- Si le répertoire n'existe pas faite la commande :
    > `mkdir ~/.kaggle`

    > `cp 'chemin vers la position actuelle de votre kaggle.json' '~/.kaggle/kaggle.json'`

## Installer Kaggle
- Faire la commande :
    > `pip install kaggle`

## Télécharger le dataset
- Positionnez vous dans le répertoire du projet 'emotions-recognition' et faite la commande :
    > `./bin/init.sh`

- Si vous rencontrez des problèmes à lancer le script, faite la commande :
    > `sudo chmod 777 scritpts/init.sh`

- Attendez que le terminal vous infome que "Le jeu de données a été divisé en ensembles d'entraînement et de test."

## Exécuter l'applicaiton
- Pour lancer le projet vous devez avoir docker d'installé sur votre machine

- Lorsque votre docker a démarré, rentrez la commande :
    > `docker compose up`

