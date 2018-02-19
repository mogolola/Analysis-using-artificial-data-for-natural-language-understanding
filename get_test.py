import random
#number_per_file = 100
dir = 'data/generation-projet-test/'


def save_test_file():
    with open(dir+'ask_for_recipe-newP-newV-test.bio','r') as f:
        a1 = f.read()
    text_a1 = a1.split('\n\n')


    with open(dir+'ask_for_recipe-newP-oldV-test.bio','r') as f:
        a2 = f.read()
    text_a2 = a2.split('\n\n')



    with open(dir+'ask_for_recipe-oldP-newV-test.bio','r') as f:
        a3 = f.read()
    text_a3 = a3.split('\n\n')


    with open(dir+'give_cat-ingredients-newP-newV-test.bio','r') as f:
        b1 = f.read()
    text_b1 = b1.split('\n\n')

    with open(dir+'give_cat-ingredients-newP-oldV-test.bio','r') as f:
        b2 = f.read()
    text_b2 = b2.split('\n\n')

    with open(dir+'give_cat-ingredients-oldP-newV-test.bio','r') as f:
        b3 = f.read()
    text_b3 = b3.split('\n\n')



    with open(dir+'give_ingredients-newP-newV-test.bio','r') as f:
        c1 = f.read()
    text_c1 = c1.split('\n\n')


    with open(dir+'give_ingredients-newP-oldV-test.bio','r') as f:
        c2 = f.read()
    text_c2 = c2.split('\n\n')

    with open(dir+'give_ingredients-oldP-newV-test.bio','r') as f:
        c3 = f.read()
    text_c3 = c3.split('\n\n')

    text = []
    text.extend(text_a1)
    text.extend(text_a2)
    text.extend(text_a3)
    text.extend(text_b1)
    text.extend(text_b2)
    text.extend(text_b3)
    text.extend(text_c1)
    text.extend(text_c2)
    text.extend(text_c3)

    random.shuffle(text)
    text_s = ''
    for i in text:
        text_s = text_s + i + '\n\n'
    print('Total Number of examples in test_file: ' + str(len(text)))
    print("Number of enamples of type 'ask_for_recipe_newP_newV': " + str(len(text_a1)))
    print("Number of enamples of type 'ask_for_recipe_newP_oldV': " + str(len(text_a2)))
    print("Number of enamples of type 'ask_for_recipe_oldP_newV': " + str(len(text_a3)))

    print("Number of enamples of type 'give_cat-ingredients_newP_newV': " + str(len(text_b1)))
    print("Number of enamples of type 'give_cat-ingredients_newP_oldV': " + str(len(text_b2)))
    print("Number of enamples of type 'give_cat-ingredients_oldP_newV': " + str(len(text_b3)))


    print("Number of enamples of type 'give_ingredients_newP_newV': " + str(len(text_c1)))
    print("Number of enamples of type 'give_ingredients_newP_oldV': " + str(len(text_c2)))
    print("Number of enamples of type 'give_ingredients_oldP_newV': " + str(len(text_c3)))
    print("saved to 'data/test.iob'")

    f = open('data/test.iob', 'w')
    f.write(text_s)
    f.close()

def save_test_file_newP_newV():
    with open(dir+'ask_for_recipe-newP-newV-test.bio','r') as f:
        a1 = f.read()
    text_a1 = a1.split('\n\n')

    with open(dir+'give_cat-ingredients-newP-newV-test.bio','r') as f:
        b1 = f.read()
    text_b1 = b1.split('\n\n')

    with open(dir+'give_ingredients-newP-newV-test.bio','r') as f:
        c1 = f.read()
    text_c1 = c1.split('\n\n')

    text = []
    text.extend(text_a1)
    text.extend(text_b1)
    text.extend(text_c1)

    random.shuffle(text)
    text_s = ''
    for i in text:
        text_s = text_s + i + '\n\n'
    print('Total Number of examples in test_file: ' + str(len(text)))
    print("Number of enamples of type 'ask_for_recipe_newP_newV': " + str(len(text_a1)))
    print("Number of enamples of type 'give_cat-ingredients_newP_newV': " + str(len(text_b1)))
    print("Number of enamples of type 'give_ingredients_newP_newV': " + str(len(text_c1)))
    print("saved to 'data/test.iob'")
    f = open('data/test.iob', 'w')
    f.write(text_s)
    f.close()


def save_test_file_newP_oldV():
    with open(dir + 'ask_for_recipe-newP-oldV-test.bio', 'r') as f:
        a1 = f.read()
    text_a1 = a1.split('\n\n')#[:number_per_file]

    with open(dir+'give_cat-ingredients-newP-oldV-test.bio', 'r') as f:
        b1 = f.read()
    text_b1 = b1.split('\n\n')

    with open(dir+'give_ingredients-newP-oldV-test.bio', 'r') as f:
        c1 = f.read()
    text_c1 = c1.split('\n\n')#[:number_per_file]

    text = []
    text.extend(text_a1)
    text.extend(text_b1)
    text.extend(text_c1)

    random.shuffle(text)
    text_s = ''
    for i in text:
        text_s = text_s + i + '\n\n'
    print('Total Number of examples in test_file: ' + str(len(text)))
    print("Number of enamples of type 'ask_for_recipe_newP_oldV': " + str(len(text_a1)))
    print("Number of enamples of type 'give_cat-ingredients_newP_oldV': " + str(len(text_b1)))
    print("Number of enamples of type 'give_ingredients_newP_oldV': " + str(len(text_c1)))
    print("saved to 'data/test.iob'")
    f = open('data/test.iob', 'w')
    f.write(text_s)
    f.close()


def save_test_file_oldP_newV():
    with open(dir + 'ask_for_recipe-oldP-newV-test.bio', 'r') as f:
        a1 = f.read()
    text_a1 = a1.split('\n\n')#[:number_per_file]

    with open(dir+'give_cat-ingredients-oldP-newV-test.bio', 'r') as f:
        b1 = f.read()
    text_b1 = b1.split('\n\n')

    with open(dir+'give_ingredients-oldP-newV-test.bio', 'r') as f:
        c1 = f.read()
    text_c1 = c1.split('\n\n')#[:number_per_file]

    text = []
    text.extend(text_a1)
    text.extend(text_b1)
    text.extend(text_c1)

    random.shuffle(text)
    text_s = ''
    for i in text:
        text_s = text_s + i + '\n\n'
    print('Total Number of examples in train_file: ' + str(len(text)))
    print("Number of enamples of type 'ask_for_recipe_oldP_newV': " + str(len(text_a1)))
    print("Number of enamples of type 'give_cat-ingredients_oldP_newV': " + str(len(text_b1)))
    print("Number of enamples of type 'give_ingredients_oldP_newV': " + str(len(text_c1)))
    print("saved to 'data/test.iob'")

    f = open('data/test.iob', 'w')
    f.write(text_s)
    f.close()

def save_test_file_little():
    with open(dir+'give_cat-ingredients-newP-newV-test.bio','r') as f:
        b1 = f.read()
    text_b1 = b1.split('\n\n')

    with open(dir+'give_cat-ingredients-newP-oldV-test.bio','r') as f:
        b2 = f.read()
    text_b2 = b2.split('\n\n')

    with open(dir+'give_cat-ingredients-oldP-newV-test.bio','r') as f:
        b3 = f.read()
    text_b3 = b3.split('\n\n')

    text = []
    text.extend(text_b1)
    text.extend(text_b2)
    text.extend(text_b3)

    random.shuffle(text)
    text_s = ''
    for i in text:
        text_s = text_s + i + '\n\n'
    print('Total Number of examples in train_file: ' + str(len(text)))
    print("Number of enamples of type 'give_cat-ingredients_newP_newV': " + str(len(text_b1)))
    print("Number of enamples of type 'give_cat-ingredients_newP_oldV': " + str(len(text_b2)))
    print("Number of enamples of type 'give_cat-ingredients_oldP_newV': " + str(len(text_b3)))
    print("saved to 'data/test.iob'")
    f = open('data/test.iob', 'w')
    f.write(text_s)
    f.close()