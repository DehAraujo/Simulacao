import pytest
from src.frete import calcular_frete
from hypothesis import given
import hypothesis.strategies as st

#Teste classe de equivalência dados válidos
@pytest.mark.parametrize("peso, destino, valor_pedido, frete_esperado",
[
    #peso <= 1 
    (1, "mesma_regiao", 50.0, 10.0),
    (1, "outra_regiao", 100, 15.0),
    (1, "internacional", 205, 0.0),
    #peso <=5
    (3.0, "mesma_regiao", 100.0, 15.0),
    (3.0, "outra_regiao", 100.0, 22.5),
    (3.0, "internacional", 100.0, 30.0),
    #peso <= 20
    (10.0, "mesma_regiao", 100.0, 25.0),
    (10.0, "outra_regiao", 100.0, 37.5),
    (10.0, "internacional", 100.0, 50.0),
    
])
def test_calcular_frete_dados_validos(peso, destino, valor_pedido, frete_esperado):
    assert calcular_frete(peso, destino, valor_pedido) == frete_esperado

#teste classe de equivalência dados inválidos
@pytest.mark.parametrize("peso, destino, valor_pedido",
[
    (-1.0, "mesma_regiao", 50.0),        # peso negativo
    (0.0, "outra_regiao", 50.0),         # peso zero
    (25.0, "mesma_regiao", 50.0),        # peso > 20
    (5.0, "sul", 50.0),                  # destino inválido
    (5.0, "mesma_regiao", -10.0),        # valor pedido negativo
])
def test_calcular_frete_dados_invalidos(peso, destino, valor_pedido):
    with pytest.raises(ValueError):
        calcular_frete(peso, destino, valor_pedido)

#teste de valores limite
@pytest.mark.parametrize("peso, destino, valor_pedido, frete_esperado", [
    (0.9, "mesma_regiao", 50.0, 10.0),
    (1, "outra_regiao", 70, 15.0),
    (1.1, "internacional", 230, 0.0),

    (4.9, "mesma_regiao", 150, 15.0),
    (5, "outra_regiao", 96, 22.5),
    (5.1, "internacional", 200, 50.0),

    (19.9, "mesma_regiao", 157.0, 25.0),
    (20.0, "outra_regiao", 250, 0.0),
    (20.1, "internacional", 22.0, 50.0),
    (-1, "internacional", 0, 150.0),
    (0.0, "12345", 18.0, 98.0),

])
def test_calcular_frete_valores_limite(peso, destino, valor_pedido, frete_esperado):
    if(peso <= 0 or peso > 20 or destino not in ["mesma_regiao", "outra_regiao", "internacional"] or valor_pedido <= 0):
        with pytest.raises(ValueError):
            calcular_frete(peso, destino, valor_pedido)
    else:
        assert calcular_frete(peso, destino, valor_pedido) == frete_esperado

#test e com hypothesis
@given(
    peso=st.floats(min_value=0.1, max_value= 20.0),
    destino=st.sampled_from(["mesma_regiao", "outra_regiao", "internacional"]),
    valor_pedido=st.floats(min_value=0, max_value=200),
)
def test_frete_nunca_negativo(peso, destino, valor_pedido):
    frete = calcular_frete(peso, destino, valor_pedido)
    assert frete >= 0