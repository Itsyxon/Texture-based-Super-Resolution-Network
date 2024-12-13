import os.path
from os import listdir
from os.path import isfile, join, dirname, abspath
import unittest
import numpy as np
from PIL import Image


class CompareImagesTestCase(unittest.TestCase):

    def test_two_images_correct(self):
        expected_im = Image.open(r"../resources/images/animated.png")
        actual_im = Image.open(r"../resources/output/images/animated.png")

        self.assertEqual(expected_im.height, actual_im.height)
        self.assertEqual(expected_im.width, actual_im.width)
        np_expected, np_actual = np.asarray(expected_im), np.asarray(actual_im)
        max_posiible_mean = 10
        actual_mean = np.mean(np.abs(np_expected - np_actual))

        self.assertLess(actual_mean, max_posiible_mean)


if __name__ == '__main__':
    unittest.main()
