from keras.applications import MobileNet
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator

# Création de paginateur pour normaliser les pixels entre 0 et 1
train_datagen = ImageDataGenerator(rescale=1. / 255)
test_datagen = ImageDataGenerator(rescale=1. / 255)

# Création des données d'entrainement
train_generator = train_datagen.flow_from_directory(
    'dataset/train',
    target_size=(96, 96),
    batch_size=32,
    class_mode='categorical')

# Création des données de test
validation_generator = test_datagen.flow_from_directory(
    'dataset/test',
    target_size=(96, 96),
    batch_size=32,
    class_mode='categorical')

# Création du modèle
base_model = MobileNet(
    weights='imagenet',
    include_top=False,
    input_shape=(96, 96, 3)
)

# On ajoute les couches de classification
x = base_model.output
x = GlobalAveragePooling2D()(x)

x = Dense(1024, activation='relu')(x)

predictions = Dense(train_generator.num_classes, activation='softmax')(x)

# On définit le modèle custom
model = Model(inputs=base_model.input, outputs=predictions)

# On compile le modèle notre optimiseur,
# notre fonction de perte et nos métriques
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Entrainement du modèle
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size,
    verbose=2
)

# Sauvegarde du modèle
model.save('data/emotion_recognition_model.keras')
