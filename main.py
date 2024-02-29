import random

def generate_username(keyword=None):
    syllables = ['li', 'on', 'ex', 'en', 'zer', 'ia', 'trix', 'or', 'max', 'um', 'phy', 'ra', 'ze', 'ki', 'ta', 'te', 'di', 'co', 'va']
    username = ''.join(random.sample(syllables, random.randint(3, 5))).capitalize() + str(random.randint(10, 99))

    if keyword:
        username += keyword.lower()

    return username

print(generate_username())
