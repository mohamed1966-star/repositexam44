class Wishlist:
    def __init__(self,items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, item):
        return self.items[item]

    def __add__(self, other):
        return self.items.append(other)

    def __str__(self):
        wishlist = []
        for index, item in enumerate(self.items):
            wishlist.append(f'{index + 1}. {item}')
        print('List of items in your wishlist :')
        print('-' * 30)
        return '\n'.join(wishlist)

my_wishlist = Wishlist(['Python 3 Object Oriented Programming','How to make mastikes in Python','Python Essential Reference'])

print(len(my_wishlist))

print((my_wishlist[0]))

my_wishlist + 'Think Python'

print(len(my_wishlist))
print((my_wishlist[3]))

print(my_wishlist)