#!/bin/bash

DATASET_DIR="dataset"

TRAIN_DIR="$DATASET_DIR/train"

TEST_DIR="$DATASET_DIR/test"

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
    echo "Progress: $percentage%\r"
done

echo "Le jeu de données a été divisé en ensembles d'entraînement et de test."
