import collections
import math
from array import array

Card = collections.namedtuple("Card", ["rank", "suite"])


class Deck:
    ranks = [str(single_rank) for single_rank in range(2, 11)] + ["J", "Q", "K", "A"]
    suites = ["spades", "diamonds", "clubs", "hearts"]

    def __init__(self):
        self._card = [Card(rank, suite) for rank in self.ranks for suite in self.suites]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, idx):
        return self._card[idx]


#
# suites order for sorting
#
suites_order = dict(spades=3, hearts=2, diamonds=1, clubs=0)


# rank: 2,3,4,5,6,7,8,9,10,11, J,Q,K,A
# suite: spades, hearts, diamonds, clubs
def spades_highest(single_card: Card):
    return (
            Deck.ranks.index(single_card.rank) * len(suites_order)
            + suites_order[single_card.suite]
    )


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":

    colors = ["red", "green", "blue"]
    sizes = ["S", "M", "L"]

    for val in (f'{color} {size}'
                for color in colors
                for size in sizes):
        print(val)
