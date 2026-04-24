from typing import Callable, Any

class simple_property:
    def __init__(self, fget: Callable[[Any], Any]) -> None:
        self.fget = fget

    def __get__(self, instance: object | None, owner: type) -> Any:
        if instance is None:
            return self
        return self.fget(instance)
    
class User:

    def __init__(self, first:str, last:str) -> None:
        self.first = first
        self.last = last

    # full_name = simple_property(full_name) --> tiene un __get__ y es un atributo de clase (porque under the hood estamos haciendo full_name = simple_property(full_name))
    @simple_property
    def full_name(self) -> str:
        return f"{self.first} {self.last}"

def main() -> None:

    u = User("John", "Doe")
    # este u.full_name esta llamando al atributo full_name de la clase user que, al llamar al __get__ luego se llama a la función full_name con el valor instance = u
    print(u.full_name)

if __name__ == "__main__":
    main()