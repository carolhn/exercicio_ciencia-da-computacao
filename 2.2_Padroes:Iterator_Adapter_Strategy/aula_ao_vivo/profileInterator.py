from collections.abc import Iterable, Iterator


class ProfileInterator(Iterator):
    def __init__(self, frends):
        self._frends = frends
        self._index = 0

    def __next__(self):
        try:
            currente_value = self._frends[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return currente_value


class SocialNetworking(Iterable):
    def __init__(self, frends):
        self._frends = frends

    def __iter__(self):
        return ProfileInterator(self._frends)

    if __name__ == "__main__":
        redesocial = SocialNetworking(["Cris", "Joao", "Carol"])
        for user in redesocial:
            print(user)
