class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, __object) -> None:
        if __object < 1:
            raise NonPositiveError
        super().append(__object)


positive_list = PositiveList()
positive_list.append(1)
positive_list.append(2)
positive_list.append(-1)
print(positive_list)