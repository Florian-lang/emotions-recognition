import unittest
from train import train_generator, validation_generator, model


class TestTrain(unittest.TestCase):

    def test_train_generator(self):
        self.assertIsNotNone(train_generator)
        self.assertEqual(train_generator.directory, 'dataset/train')
        self.assertEqual(train_generator.target_size, (96, 96))
        self.assertEqual(train_generator.batch_size, 32)
        self.assertEqual(train_generator.class_mode, 'categorical')

    def test_validation_generator(self):
        self.assertIsNotNone(validation_generator)
        self.assertEqual(validation_generator.directory, 'dataset/test')
        self.assertEqual(validation_generator.target_size, (96, 96))
        self.assertEqual(validation_generator.batch_size, 32)
        self.assertEqual(validation_generator.class_mode, 'categorical')

    def test_model(self):
        self.assertIsNotNone(model)
        self.assertEqual(len(model.layers), 90)
        self.assertEqual(
            model.layers[-1].output_shape,
            (None, train_generator.num_classes)
        )
        self.assertEqual(model.optimizer, 'adam')
        self.assertEqual(model.loss, 'categorical_crossentropy')
        self.assertEqual(model.metrics, ['accuracy'])


if __name__ == '__main__':
    unittest.main()
