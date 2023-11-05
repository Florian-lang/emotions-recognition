# Documentation

## requirement
- obtenir le token sur 
    > https://www.kaggle.com/settings/account
- fichier kaggle.json téléchargé en même temps que la création du token.
- il faut le gestionnaire de package python (pip)

## First Time
Etape 1 le dataset.

- _Il faut se créer un compte sur kaggle.com afin de récupérer son token et son username._
- Installer kaggle avec la commande :
    > `pip install kaggle`
- Déplacer le fichier kaggle.json dans ~/.kaggle

- Il faut utiliser la commande :
    > `chmod 777 scritpts/init.sh` 

pour élever les privilèges et pour pouvoir executer ce script.  Faire pareil sur les 2 autres fichiers ".sh" en cas de besoin.

- Setup notre dataset grâce à la commande inscrite dans la partie suivante.

## Setup du dataset
Il faut executer la commande :
> `./scripts/init.sh`

Pour rénitialiser les data rééxécuter la commande ci-dessus.

## Docker
**A réfléchir**

Il n'est pas nécessaire d'utiliser Docker mais si ça vous chante voici ce qu'il faut faire :

1/ Download Docker Desktop sur internet

2/ Utiliser la commande suivante pour lancer le conteneur avec le script de l'IA : 
>`docker-compose up` -> tout se lance automatiquement

3/ Pour arrêter et supprimer le conteneur lancé 
> `docker-compose down`

 une fois que tout s'est terminé

4/ Il faut aussi supprimer l'image dans le logiciel docker desktop.


## Documentation
- Pour télécharger le dataset on lance la commande 
> `./script/download_dataset.sh`
- Pour créer nos dossiers test et train on lance la commande 
> `./script/split_dataset.sh`
- Pour reset le dataset lancer la commande 
> `./scripts/reset_dataset.sh`

**A savoir :** Le fonctionnement est entièrement automatisé tous les scripts s'appellent entre eux. Juste executer "download_dataset.sh"

