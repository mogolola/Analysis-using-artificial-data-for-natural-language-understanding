import random
#number_per_file = 1000
dir = 'data/generation-projet-trn/'
def save_train_file(number_per_file):
    with open(dir+'ask_for_recipe-trn.bio','r') as f:
        a = f.read()

    text_1 = a.split('\n\n')[:number_per_file]

    with open(dir+'give_cat-ingredients-trn.bio','r') as f:
        b = f.read()
    text_2 = b.split('\n\n')

    with open(dir+'give_ingredients-trn.bio','r') as f:
        c = f.read()
    text_3 = c.split('\n\n')[:number_per_file]

    text = []
    text.extend(text_1)
    text.extend(text_2)
    text.extend(text_3)




    random.shuffle(text)
    text_s = ''
    for i in text:
        text_s = text_s + i + '\n\n'


    print ('Total Number of examples in train_file: ' + str(len(text)))
    print ("Number of enamples of type 'ask_for_recipe': " + str(len(text_1)) )
    print ("Number of enamples of type 'give_cat-ingredients': " + str(len(text_2)))
    print ("Number of enamples of type 'give_ingredients': " + str(len(text_3)))
    print("saved to 'data/train.iob'")

    f = open('data/train.iob', 'w')
    f.write(text_s)
    f.close()

'''
f = open('train.ibo', 'w')
f.write(a+b+c)
f.close()
'''