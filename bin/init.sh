#!/bin/bash

DATASET_DIR="dataset"
TRAIN_DIR="$DATASET_DIR/train"
TEST_DIR="$DATASET_DIR/test"

if [ ! -e "$DATASET_DIR" ]; then
    ZIP_FILE="affectnet-training-data.zip"

    kaggle datasets download -d noamsegal/affectnet-training-data
    mkdir -p "$DATASET_DIR"
    unzip -q "$ZIP_FILE" -d "$DATASET_DIR"

    rm "$ZIP_FILE"

    echo "L'archive a été téléchargée, extraite dans le dossier 'dataset' et supprimée."
fi

if [ -e "$TRAIN_DIR" ] || [ -e "$TEST_DIR" ]; then
    rm -rf "$TRAIN_DIR"
    rm -rf "$TEST_DIR"
    echo "Les ensembles d'entraînement et de test ont été supprimés."

else
    echo "Les ensembles d'entraînement et de test n'existent pas."
fi

echo "Création des dossiers test et train en cours :"
if [ -e "$TRAIN_DIR" ] || [ -e "$TEST_DIR" ]; then
    echo "Les ensembles d'entraînement et de test existent déjà."
    exit 1
fi

mkdir -p "$TRAIN_DIR"
mkdir -p "$TEST_DIR"

file_count=$(find "$DATASET_DIR" -maxdepth 1 -type d | wc -l)
progress=0

for SUB_DIR in "$DATASET_DIR"/*; do

    emotion=$(basename "$SUB_DIR" | cut -d'_' -f1)

    if [ -d "$SUB_DIR" ] && [ "$SUB_DIR" != "$TRAIN_DIR" ] && [ "$SUB_DIR" != "$TEST_DIR" ]; then
        TOTAL_FILES=$(find "$SUB_DIR" -type f | wc -l)
        
        TEST_COUNT=$((TOTAL_FILES * 20 / 100))
        
        if [ ! -d "$TEST_DIR/$emotion" ]; then
            mkdir -p "$TEST_DIR/$emotion"
        fi

        if [ ! -d "$TRAIN_DIR/$emotion" ]; then
            mkdir -p "$TRAIN_DIR/$emotion"
        fi

        ls "$SUB_DIR" | sort -R | head -n $((TOTAL_FILES - TEST_COUNT)) | xargs -I {} cp "$SUB_DIR/{}" "$TRAIN_DIR/$emotion"
        
        ls "$SUB_DIR" | sort -R | head -n $TEST_COUNT | xargs -I {} cp "$SUB_DIR/{}" "$TEST_DIR/$emotion"
    fi

    progress=$((progress + 1))
    percentage=$((progress * 100 / file_count))
    echo -ne "Progress: $percentage% \r"
done

echo "Le jeu de données a été divisé en ensembles d'entraînement et de test."

echo "Intallation des dépendances en cours :"
pip install -r requirements.txt

echo "Initialisation des hooks en cours :"
chmod +x bin/create_pre_commit_hook.sh
bash bin/create_pre_commit_hook.sh

echo "Initialisation terminée."
