from src.frete import validar_peso, validar_destino, calcular_frete
import pytest

#Testes calcular frete com peso válido
@pytest.mark.parametrize("peso, frete_esperado", [
(0.2, 10), #menor que 1
(1.5, 15), #menor que 5
(10, 25), #menor que 20
])
def test_calcular_frete_peso_valido(peso, frete_esperado):
        assert validar_peso(peso) == frete_esperado

@pytest.mark.parametrize("peso", [
    (-2),
    (0),
])
def test_calcular_frete_peso_invalido(peso):
        with pytest.raises(ValueError):
            validar_peso(peso)