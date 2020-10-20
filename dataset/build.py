""""
    Making a synthetic dataset.
    Based on the examples in https://github.com/opennars/opennars/wiki/
"""

def f1(a, b):
    # A is a type of B.
    text = f"{a} is a type of {b}."
    a = a.lower()
    b = b.lower()
    narsese = f"<{a} --> {b}>."
    return text,narsese

def f2(a, b):
    # A is probably not a type of B.
    text = f"{a} is probably not a type of {b}."
    a = a.lower()
    b = b.lower()
    narsese = f"<{a} --> {b}>. %0.10;0.60%"
    return text, narsese

def f3(a, b):
    # Is A a type of B?
    text = f"Is {a} a type of {b}?"
    a = a.lower()
    b = b.lower()
    narsese = f"<{a} --> {b}>?"
    return text,narsese

def f4(a):
    # What is a type of A?
    text = f"What is a type of {a}?"
    a = a.lower()
    narsese = f"<?x --> {a}>?"
    return text, narsese

def f5(a):
    # What is the type of A?
    text = f"What is the type of {a}?"
    a = a.lower()
    narsese = f"<{a} --> ?1>?"
    return text, narsese

def f6(a, b):
    # A is similar to B.
    text = f"{a} is similar to {b}."
    a = a.lower()
    b = b.lower()
    narsese = f"{a} <-> {b}>."
    return text, narsese

def f7(a, b):
    # I think A is not similar to B.
    text = f"I think {a} is not similar to {b}."
    a = a.lower()
    b = b.lower()
    narsese = f"<{a} <-> {b}>. %0.10;0.60% "
    return text, narsese

def f8(a, b):
    # A is probably similar to B
    text = f"{a} is probably similar to {b}."
    a = a.lower()
    b = b.lower()
    narsese = f"<{a} <-> {b}>. %0.87;0.91%"
    return text, narsese

def f9(a, b):
    # I guess that A is similar to B
    text = f"I guess that {a} is similar to {b}."
    a = a.lower()
    b = b.lower()
    narsese = f"<{a} <-> {b}>. %0.90;0.45%"
    return text, narsese

def f10(a):
    # What is A?
    text = f"What is a {a}?"
    a = a.lower()
    narsese = "<{?1}" + f" --> {a}>?"
    return text, narsese

def f11(a, b):
    # A is different from B.
    text = f"{a} is different from {b}."
    a = a.lower()
    b = b.lower()
    narsese = f"<{a} <-> {b}>. %0.10;0.81%'"
    return text, narsese

def f12(a, b):
    # A is similar to B.
    text = f"{a} is similar to {b}."
    a = a.lower()
    b = b.lower()
    narsese = f"<{a} <-> {b}>. %0.10;0.81%'"
    return text, narsese

def writepair(pair):
    text, narsese = pair
    text += '\n'
    narsese += '\n'
    print((text, narsese))
    with open('dataset.txt', 'a') as fd:
        fd.write(text)
        fd.write(narsese)

# def genwritepair()

if __name__ == "__main__":
    # overwrite file
    with open('dataset.txt', 'w') as fd:
        pass
    # random animals
    animals = ['Owl', 'Wolf', 'Dog', 'Cat', 'Bear', 'Horse', 'Chicken',
               'Rooster', 'Cow', 'Elephant', 'Mouse', 'Bird', 'Pig']
    def af1(a, b):
        # A is a type of B.
        text = f"{a} is an {b}."
        a = a.lower()
        b = b.lower()
        narsese = f"<{a} --> {b}>."
        return text,narsese
    
    for animal in animals:
        a = animal
        b = 'animal'
        pair = f1(a, b)
        writepair(pair)
        pair = f3(a, b)
        writepair(pair)
        pair = f5(a)
        writepair(pair)
        pair = af1(a, b)
        writepair(pair)
        
    # random colors
    colors = ['red', 'green', 'blue', 'yellow', 'black', 'white', 'brown']
    
    def cf1(a, b):
        # A is a type of B.
        text = f"{a} is a {b}."
        a = a.lower()
        b = b.lower()
        narsese = f"<{a} --> {b}>."
        return text,narsese
    
    for color in colors:
        a = color
        b = 'color'
        pair = f1(a, b)
        writepair(a, b)
        pair = cf1(a, b)
        writepair(a, b)


    # random countries
    countries = ['Austria', 'Brazil', 'China', 'Russia', 'Germany', 'Australia', 'Czechia', 'Estonia',
                 'Latvia', 'Denmark', 'France', 'Greece', 'Hungary', 'Poland', 'Slovakia', 'Sweden', 'Switzerland', 'Ukraine']
    for country in countries:
        a = country
        b = 'country'
        pair = f1(a, b)
        writepair(pair)
        pair = f3(a, b)
        writepair(pair)
        pair = f5(a)
        writepair(pair)
