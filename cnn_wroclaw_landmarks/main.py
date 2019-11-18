from keras.applications import MobileNet

mobilenet = MobileNet(weights='imagenet')

import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt

filename = 'Archikatedra_Jana_Chrzciciela.jpg'
orginal = load_img(filename, target_size=(224, 224))
plt.imshow(orginal)
plt.show()

numpy_image = img_to_array(orginal)
image_batch = np.expand_dims(numpy_image, axis=0)

from keras.applications.imagenet_utils import decode_predictions
from keras.applications.mobilenet import preprocess_input

processed_image = preprocess_input(image_batch.copy())
predictions = mobilenet.predict(processed_image)
label = decode_predictions(predictions)
print(label)

# transfer learning

from keras.layers import Dense, GlobalAveragePooling2D

base_model = MobileNet(weights='imagenet', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(512, activation='relu')(x)
preds = Dense(6, activation='softmax')(x)

from keras.models import Model
model = Model(inputs=base_model.input, outputs=preds)
model.summary()

# train additional 5 layers

for layer in model.layers[:-5]:
    layer.trainable = False

# add photos to train and change to training dataset

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
train_generator = train_datagen.flow_from_directory(
    'wroc_landmarks_images/',
    target_size=(224, 224),
    color_mode='rgb',
    batch_size=32,
    class_mode='categorical',
    shuffle=True
)

# compile model

model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# train model

model.fit_generator(
    generator=train_generator,
    steps_per_epoch=train_generator.n/train_generator.batch_size,
    epochs=1
)

# check predictions for new skytower examples

print(train_generator.class_indices)

filename = 'Archikatedra_Jana_Chrzciciela.jpg'
orginal = load_img(filename, target_size=(224, 224))
plt.imshow(orginal)
plt.show()

numpy_image = img_to_array(orginal)
image_batch = np.expand_dims(numpy_image, axis=0)

processed_image = preprocess_input(image_batch.copy())
predictions = model.predict(processed_image)

print(np.argmax(predictions))
