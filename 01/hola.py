# programa que saluda mediante un objeto definido en una clase (nombre)


class ClaseHola:
    def __init__(self, name):
        self.name = name

    def hola(self):
        print(f"Hola, {self.name}")


def main():
    saludo = ClaseHola("Abel")
    saludo.hola()


if __name__ == "__main__":
    main()
