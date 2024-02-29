import random

def generate_username(keyword=None):
    syllables = ['li', 'on', 'ex', 'en', 'zer', 'ia', 'trix', 'or', 'max', 'um', 'phy', 'ra', 'ze', 'ki', 'ta', 'te', 'di', 'co', 'va', 'be', 'ka', 'do', 'ju', 'lo', 'wi', 'zi']
    shades = ['_', '-', '.', '']
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'black', 'white']
    username = ''.join(random.sample(syllables, random.randint(3, 5))).capitalize() + random.choice(shades) + random.choice(colors) + str(random.randint(10, 99))

    if keyword:
        username += keyword.lower()

    return username

# Example usage:
print(generate_username())
print(generate_username("tech"))
