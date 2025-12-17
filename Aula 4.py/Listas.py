#Listas

#Em python, uma lista (list) é uma sequência ordenada de valores, que são identificadas por um indice. Estes valores, que compõem uma lista, são chamdos de elementos ou itens. Listas são estruturas de dados muito similares às strings, que por sua vez são sequência de caracteres, apenas. A diferença é que os elementos de uma lista podem ser de qualquer tipo, ou seja, podem ser homogeneos(todos os valores do mesmo tipo) e heterogêneos (valores com tipos distintos).
#Diferentes das strings, uma lista é também uma sequência mutável e dinâmica. Uma vez que sejam criadas, é possivel:

# Alterar o valor de um ou mais elementos. 
#Os elementos podem ser adicionados, removidos ou substituidos.

# A sintaxe para acessar os elementos de uma lista é por meio do operador ([]), especificados o índice (posição) do elemento a ser acessado (ex.: [0] e [1]) e sempre com o primeiro elemento no índice 0. Também podemos utilizar indices negativos e o conceito de slicing (faixa de indices), que nos retorna uma sub-lista.

lista_de_compras = ['Arroz',
                    20,
                    2.40,
                    True,
                    None]

print(lista_de_compras)
type(lista_de_compras[4])

print(len(lista_de_compras))
