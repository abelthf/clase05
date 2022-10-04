from saludo import saludo


def test_saludo(capfd):
    saludo("Fredy")

    out, err = capfd.readouterr()
    assert out == "Hola Fredy\n"
