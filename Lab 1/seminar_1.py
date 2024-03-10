import re
import random
import string

import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# Өгөгдсөн хүснэгтээс нийт ялгаатай утгатай элемэнтүүдийн тоог ол.
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k = length))

def generate_random_dataframe(n):
    df = pd.DataFrame({'Col1': [generate_random_string(10) for _ in range(n)],
                       'Col2': [generate_random_string(10) for _ in range(n)]})
    return df

df = generate_random_dataframe(n = 30)

print(f"Randomly generated column 1 value counts:\n{df['Col1'].value_counts()}")
print(f"\nRandomly generated column 2 value counts:\n{df['Col2'].value_counts()}")
print("*"*64)

# Өгөгдсөн өгүүлбэрийн үг бүр нь хэдэн удаа давтагдсанг ол.
lorem_ipsum = "Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# 1. No puncts
text_no_punct = re.sub(r'[^\w\s\']', '', lorem_ipsum)

# 2. 's and s after numbers
text_no_suffix = re.sub(r'(?<=\d)s\b', '', text_no_punct)

# 3. Remove ' letters
text_no_apos = re.sub(r'\b\w+\'\w+\b', '', text_no_suffix)

# 4. contractions like e.g 're, 've
text_no_contractions = re.sub(r'\b\w+\'(?:re|ve|s|m|d|ll)\b', '', text_no_apos)

# 5. No extra space
clean_text = re.sub(r'\s+', ' ', text_no_contractions).strip()

word_cnt = pd.DataFrame({"words": [word.strip() for word in clean_text.split()]})
print(f"\nEach word cnt in sentence:\n{word_cnt['words'].value_counts()}")
print("*"*64)

# Өгөгдсөн хүснэгтээс 'xyz' тэмдэгт мөрийг агуулсан тэмдэгт мөрүүдийг хэвлэ.
def generate_random_string(length):
    prefix_length = random.randint(0, length - 3)
    suffix_length = length - prefix_length - 3
    
    xyz_pattern = 'xyz'
    prefix = ''.join(random.choices(string.ascii_letters + string.digits, k = prefix_length))
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k = suffix_length))

    random_number = np.random.randint(6)
    if random_number % 3 == 0:
        return prefix + xyz_pattern + suffix
    return prefix + suffix

xyz_objects = pd.DataFrame({'Col': [generate_random_string(15) for _ in range(100)]})
print(f"\nColumn values containing xyz:\n{xyz_objects[xyz_objects['Col'].str.contains('xyz')]}")
print("*"*64)

# Өгөгдсөн хүснэгтээс 'xyz' тэмдэгт мөрөөр эхэлсэн эсвэл төгссөн тэмдэгт мөрүүдийг хэвлэ.
xyz_objects = pd.DataFrame({'Col': [generate_random_string(15) for _ in range(1000)]})
print(f"\nColumn values startswith or endswith:\n{xyz_objects[(xyz_objects['Col'].str.endswith('xyz')) & (xyz_objects['Col'].str.startswith('xyz'))]}")
print("*"*64)

# Хамгийн эхний анхны 50 тоог олох функц бич.
def sieve(n):
    primes = []
    is_prime = [True] * (n * 10)

    for num in range(2, int(n * (n**0.5)) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, n * 10, num):
                is_prime[multiple] = False

    for num in range(max(2, int(n * (n**0.5)) + 1), n * 10):
        if is_prime[num]:
            primes.append(num)

    return primes[:n]

print("\nFirst 50 primes:")
print(sieve(50))