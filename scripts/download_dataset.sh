#!/bin/bash

URL='https://storage.googleapis.com/kaggle-data-sets/2812806/4860972/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231101%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231101T170844Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=51209e5118336058fd3f6fe045c9220260d4f824183f29158b98195ffa1282ef9c1a3e0617e72dde6362033a033f4700b950333d7959f36fe56a722698e396a6aad65b4f8507e5c863f2d326e69e4cd20a11c3db3b41a3a5b65e3f33c22d286108519eb51aeafed2ae428ca650c96a14d241493e0a1013442b487c198c200256b3252e6fff2715d78627b8aba0f7026c3c32f6fee91c63e3667c24afffb8bc3b8dc7288d7e7cce0d1ac0ddcc6893c70b358a859844cb0dc0dff9eaabc30f3a8bc8d0143c592efba5ce1d2a508b398ac1b9b0d8ad5787a0117ea414ae76edbf8a13a018a5f6a39d4c526305e73723376cf8a12df099c229eb498297fa79653396'
ZIP_FILE="archive.zip"
DESTINATION_DIR="dataset"

curl -o "$ZIP_FILE" "$URL"
mkdir -p "$DESTINATION_DIR"
unzip -q "$ZIP_FILE" -d "$DESTINATION_DIR"

rm "$ZIP_FILE"

echo "L'archive a été téléchargée, extraite dans le dossier 'dataset' et supprimée."