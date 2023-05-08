from dataclasses import dataclass, field, fields, asdict, astuple, KW_ONLY


@dataclass
class Person:
    _: KW_ONLY
    name: str
    age: int
    skills: list[str] = field(default_factory=list)

    def __str__(self):
        return self.name


p = Person(name="Vova", age=40)
print(astuple(p))

