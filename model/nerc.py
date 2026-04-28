from dataclasses import dataclass

@dataclass
class Nerc:
    _id: int
    _value: str

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value

    def __eq__(self, other):
        return self.id == other.id


    def __str__(self):
        return self._value

    def __hash__(self):
        return hash(self._id)


