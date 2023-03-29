class Set:
    def __init__(self, items=()):
        self.items = set(items)

    def complement(self, other):
        return Set([item for item in other.items if item not in self.items])

    def union(self, other):
        return Set(self.items | other.items)

    def intersection(self, other):
        return Set(self.items & other.items)

    def difference(self, other):
        return Set(self.items - other.items)

    def symmetric_difference(self, other):
        return Set(self.items ^ other.items)

    def __str__(self):
        if len(self.items) == 0:
            return "{}"
        return str(self.items)

    def __eq__(self, other):
        return self.items == other.items


if __name__ == '__main__':
    A = Set([1, 2, 3, 4, 5])
    B = Set([3, 4, 5, 6, 7])
    print(f"A = {str(A)}")
    print(f"B = {str(B)}")
    print(f"доповнення:    Aᶜ ∩ B = {str(A.complement(B))}")
    print(f"об'єдання:     A ∪ B = {str(A.union(B))}")
    print(f"перетин:       A ∩ B = {str(A.intersection(B))}")
    print(f"різниця:       A \ B = {str(A.difference(B))}")
    print(f"сим. різниця:  A Δ B = {str(A.symmetric_difference(B))}")
