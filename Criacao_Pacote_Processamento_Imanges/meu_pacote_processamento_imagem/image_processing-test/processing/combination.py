# Author: Karina Tiemi Kato
import numpy as np
from skimage.color import rgb2gray  # Corrigido
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Especifique duas imagens com o mesmo tamanho."
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similaridade das imagens:", score)
    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))
    return normalized_difference_image

def transfer_histogram(image1, image2):  # Corrigido
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image
