#!/bin/bash

DATASET_TRAIN_DIR="dataset/train"
DATASET_TEST_DIR="dataset/test"

if [ -e "$DATASET_TRAIN_DIR" ] || [ -e "$DATASET_TEST_DIR" ]; then
    rm -rf "$DATASET_TRAIN_DIR"
    rm -rf "$DATASET_TEST_DIR"
    echo "Les ensembles d'entraînement et de test ont été supprimés."
    exit 1
else 
    echo "Les ensembles d'entraînement et de test n'existent pas."
    exit 1
fi