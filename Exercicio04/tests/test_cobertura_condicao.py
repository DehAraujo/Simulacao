import pytest
from src.cobertura_condicao import acesso

#Testes caminhos independentes C0, cobertura de ramos C1 e cobertura de condições CC
@pytest.mark.parametrize("idade, membro, resultado_esperado", [
<<<<<<< HEAD
    (20, "True", "Permitido"),
    (15, "False", "Negado"),
    (17, "True", "Negado"),
=======
    (20, True, "Permitido"),
    (18, False, "Negado"),
    (17, True, "Negado"),
    (15, False, "Negado"),
>>>>>>> 6ac98827f8ff4e5a658841ee91c0b00ba7d214e6
])
def test_ciclo(idade, membro, resultado_esperado):
    assert acesso(idade, membro) == resultado_esperado

<<<<<<< HEAD
#Em C1 são necessarios dois testes pois ele analisa a condicao V ou F
#Em CC são necessários 3 testes pois ele analisa cada condição individualmente
=======
#Para a cobertura de ramos C1 são necessários dois casos de testes, um para cobrir o ramo verdadeiro e outro para cobrir o ramo falso
#Para a cobertura de condição CC são necessários quatro casos de testes para cobrir todas as condições possíves de cada ramo.
#Eles se diferem, pois C1 cobre apenas o ramo verdadeiro e o ramo falso e CC cobre cada condição do ramo verdadeiro e cada condição do ramo falso.
>>>>>>> 6ac98827f8ff4e5a658841ee91c0b00ba7d214e6
