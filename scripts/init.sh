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

    if [ -d "$SUB_DIR" ] && [ "$SUB_DIR" != "$TRAIN_DIR" ] && [ "$SUB_DIR" != "$TEST_DIR" ]; then
        TOTAL_FILES=$(find "$SUB_DIR" -type f | wc -l)
        
        TEST_COUNT=$((TOTAL_FILES * 20 / 100))
        
        ls "$SUB_DIR" | sort -R | head -n $((TOTAL_FILES - TEST_COUNT)) | xargs -I {} cp "$SUB_DIR/{}" "$TRAIN_DIR"
        
        ls "$SUB_DIR" | sort -R | head -n $TEST_COUNT | xargs -I {} cp "$SUB_DIR/{}" "$TEST_DIR"
    fi

    progress=$((progress + 1))
    percentage=$((progress * 100 / file_count))
    echo "Progress: $percentage"
done

echo "Le jeu de données a été divisé en ensembles d'entraînement et de test."