from math import sqrt
import numpy as np

ratings = np.array(
    [
        [3, 3, 4, 0, 4, 2, 3, 0],
        [3, 5, 4, 3, 3, 0, 0, 4],
        [0, 4, 0, 5, 0, 0, 2, 1],
        [2, 0, 0, 4, 0, 4, 4, 5],
    ]
)
Ub = (ratings >= 3).astype(int)
print(Ub)


def jaccard_distance_bits(bit_pattern1, bit_pattern2):
    """
    Calculate Jaccard distance between two bit patterns.

    Parameters:
    - bit_pattern1, bit_pattern2: Integers representing binary patterns.

    Returns:
    - Jaccard distance (a float between 0 and 1).
    """
    intersection_size = bin(bit_pattern1 & bit_pattern2).count("1")
    union_size = bin(bit_pattern1 | bit_pattern2).count("1")

    if union_size == 0:
        return 0  # Handle the case where both bit patterns are zero

    return intersection_size / union_size


# Example usage:
bit_pattern_a = 0b11101010
bit_pattern_b = 0b01010000

distance = jaccard_distance_bits(bit_pattern_a, bit_pattern_b)
print(f"Jaccard Distance between bit_pattern_a and bit_pattern_b: {distance}")


def find_n2(arr):
    result = 0
    for i in arr[:]:
        result += i**2

    return sqrt(result)


fire = [3, 3, 4, 0, 4, 2, 3, 0]
mike = [2, 0, 0, 4, 0, 4, 5]
fire2 = find_n2(fire)
mike2 = find_n2(mike)
print((sum(fire) * sum(mike)) / (fire2 * mike2))

import math


def cosine_similarity(vector1, vector2):
    """
    Calculate cosine similarity between two vectors.

    Parameters:
    - vector1, vector2: Lists or arrays representing the vectors.

    Returns:
    - Cosine similarity (a float between -1 and 1).
    """
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(a**2 for a in vector1))
    magnitude2 = math.sqrt(sum(b**2 for b in vector2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0  # Handle the case where one or both vectors have zero magnitude

    return dot_product / (magnitude1 * magnitude2)


def cos(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Example usage:
vector_a = [3, 3, 4, 0, 4, 2, 3, 0]
vector_b = [3, 5, 4, 3, 3, 0, 0, 4]

similarity = cos(vector_a, vector_b)
print(f"Cosine Similarity between vector_a and vector_b: {similarity}")
