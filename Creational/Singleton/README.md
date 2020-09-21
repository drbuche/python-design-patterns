# Padrão de Projeto Criacional ([Creational](https://github.com/drbuche/python-design-patterns/tree/master/Creational)) - Singleton:

![N|Solid](https://i.imgur.com/TIb0XaS.jpg)
## Características Gerais: 
O padrão Singleton é considerado um dos Padrões  Criacionais mais simples. Seu principal objetivo é garantir que uma classe possa instanciar apenas um objeto, além de disponibilizar um ponto de acesso global.

# UML:

![N|Solid](https://www.patrickschadler.com/wp-content/uploads/2019/08/2000px-Singleton_UML_class_diagram-e1565094559716.png)

# Como Funciona?

Como observamos no UML, deixamos o construtor privado e criamos um método estático responsável pela instanciação do objeto, tal metodo será o nosso único modo de instanciar um objeto.

Ao chamar esse método temos 2 alternativas:
- Se é a primeira vez ou a classe não possui um objeto - O objeto é criado.
- Se já existe um objeto pertencente a esta classe - O método retorna o objeto já existente.

# Em Python:

A implementação em Python é um pouco diferente, tendo em vista que não existem construtores privados, diferente de linguagens como Java, temos apenas um recurso de *Name Mangling*, usando underscore antes do atributo.

### [Singleton Tracidional](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Singleton/01_Singleton_Tradicional.py):
Utilizamos o método `__new__`, um método especial para instanciar objetos no momento que chamamos a classe. Além disso, utilizamos uma estrutura condicional chamando o método `hasattr`, responsável por saber se um objeto tem as propriedades descritas. 

`if not hasattr(cls, 'instancia')` -> Se a class não possuir a propriedade `instancia`, ele realizara a ação:
- Criar um objeto desta classe, nomeado de `instancia`.

Caso a afirmativa acima seja falsa, ele apenas retorna o objeto já existente.

### [Singleton Monostate](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Singleton/02_Monostate_Borg.py):
O modo Monostate, também conhecido como Borg, é levemente diferente do Singleton tradicional. Diferente do Singleton, ele cria mais de um objeto da mesma classe, mas todos os objetos compartilham os mesmos dados.

Utilizamos o método `__dict__`, que armazena o estado de todos os objetos da classe, atribuimos a ele a variável `__compartilhado`, sendo assim, sempre que chamarmos a classe MonostateBorg(), instanciaremos um novo objetos, mas todos os objetos compartilharão os mesmos dados. Se um objeto for modificado, o outro também mudará, da mesma forma de uma Shallow copy.

### [Singleton Lazy Instantiation](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Singleton/03_Singleton_Lazy_Instantiation.py):
A instanciação preguiçosa garante que o objeto será criado apenas se chamarmos o método `@classmetod -> get_instancia`. Isso evita que o objeto seja instanciado quando iniciamos a Classe, apenas realizando a instanciação perante ao método.

### [Singleton MetaCLass](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Singleton/04_Singleton_MetacLass.py):

Uma metaclasse é uma classe de outra classe. Isso significa que a classe é uma instanciação de sua metaclasse.

Meio confuso?

Então, o método `__call__` é chamado quando um objeto precisa ser criado para uma classe já existente. Então, no momento que chamamos a classe `Controlada`, automaticamente chamamos o método `__call__` da metaclasse, que é responsável por instanciar o objeto e também por garantir que exista apenas um dele.

# Mundo real:

Indicado para casos em que queremos ter apenas um objeto, como em:

- Pools threads (padrão para obter simultaneidade de execução em um programa de computador.)
- Caches
- Caixas de diálogos
- Configuração de registro
- Conexão com banco de dados

No exemplo [Singleton_Mundo_Real.py](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Singleton/Singleton_Mundo_Real.py), temos uma verificação de sanidade para infraestrutura. Onde precisamos gerenciar a criação e remoção de servidores.
 
Temos as referência `obj1` e `obj2`, mas apenas um objeto é criado.

Como `obj1` e `obj2` são referências ao mesmo objeto, a ação cometida por um ou por outro resulta em uma interação com o mesmo objeto. Pois eles são apenas referências ao objeto e não o objeto em si.

# Desvantagens:

- Variáveis globais podem ser alteradas por engano.

- Várias referências podem ser criadas para o mesmo objeto.

- Classes que dependem de variáveis globais são altamentes acopladas, sendo assim, uma mudança em uma classe global pode impactar outra classe.
