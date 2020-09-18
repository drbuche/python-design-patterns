# Padrão de Projeto Criacional ([Creational](https://github.com/drbuche/python-design-patterns/tree/master/Creational)) - Factory:

<p align="center">
  <img src="https://i.imgur.com/O7MSnfM.jpg">
</p>

## Características Gerais: 
O pattern Factory é considerado um dos padrẽos mais utilizados!

Ele é caracterizado por uma classe que é responsável por criar objetos de outros tipos. Normalmente uma Factory é associada a um objeto e métodos. No momento em que o usuário chama esses métodos, utilizando certos parâmetros, a Factory instancia o objeto de acordo com esses especificidades e retorna ao usuário.

Temos diferentes representações deste pattern, sendo elas:
 - [Simple Factory](#simple-factory).
 - [Polymorphic Factory Method](#polymorphic-factory-method).
 - [Abstract Factory](#abstract-factory).

## Por que usar uma Factory e não instanciar o objeto direto na classe do usuário?
Essa é uma questão muito levantada no primeiro contato com esse pattern , pois não parece tão prático criar uma interface só para instanciar novos objetos, mas quando olhamos mais atentamente, vemos suas vantagens, como:

- Baixo acoplamento, tendo em vista que a criação do objeto pode acontecer mesmo sem a implementação da classe.
- O usuário não necessita conhecer a classe que cria o objeto, ele precisa conhecer apenas os parâmetros e métodos responsáveis por instanciar o objeto desejado naquele momento.
- Poder de adicionar novos objetos na Factory, apenas adicionando novos parâmetros, tornando-a facilmente expansível.

# Variações de Factory:

## [Simple Factory](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Factory/01_Simple_Factory.py)
<p align="center">
  <img src="https://i.imgur.com/HDxavUq.jpg">
</p>
Essa versão é considerada mais como um conceito básico para dar um norte de como o pattern Factory se comporta.

Possui como premissa a possibilidade da interface criar novos objetos sem expor a lógica por trás de sua criação.

Inicialmente, necessitamos de uma classe abstrata para armazenar métodos e atributos genericos. Então vem o primeiro problema, pois python por si só, não nos fornece classes abstratas, então devemos importar os módulos `ABC` e `abstractclassmethod` do pacote `abc` com o comando `from abc import ABC, abstractclassmethod`. 

Com os modulos em mãos, podemos dar inicio ao nosso pattern.

Em nosso [exemplo](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Factory/01_Simple_Factory.py), primeiramente criamos nossa classe abstrata chamada de `Sociedade`, que por ser abstrata, não possui a função de instanciar objetos, ela apenas possui atributos e métodos que serão passadas para suas classes filhas, em forma de herança.

Após termos criado a classe abstrata, com todos os métodos e parâmetros genéricos que as classes filhas necessitam, devemos criar nossas classes concretas, que serão responsáveis por ditar as especificidades de cada objeto criado.

*Mas se todas herdam da mesma classe, como faremos para diferenciar os objetos instanciados pelas classes filhas?*

Utilizamos do polimorfismo para sobrescrever os métodos e parâmetros herdados que desejamos que sejam diferentes entre as classes. No exemplo, temos classes que representam personagens distintos, mas que herdam o método `fala()` da classe abstrata `Sociedade`. Tendo em vista que a fala desses personagens não são iguais, devemos sobrescrever estes métodos, adequando a realidade de cada classe `Personagem`.

Por fim, devemos criar uma interface, representada pela classe `FabricaDeFalas`. Essa classe funciona como um vendedor de uma taberna, ela será responsável por conversar com o usuário, e após entender as características da bebida que ele deseja, o taberneiro se vira, pega a bebida correspondente e a entrega ao usuário.

Neste caso, a nossa `FabricaDeFalas` possui um método estático chamado de `crie_fala()`. O `@staticmethod` possibilita a execução do método `crie_fala()` sem a necessidade de utilizar um objeto do tipo `FabricaDeFalas` como parâmetro.

Este método estatico vai receber um input do usuário, que será transformado em uma expressão, utilizando o método python - `eval`.
 
Com isso, o método `Personagem().fala()` é chamdo , criando nosso objeto desejado.


## [Polymorphic Factory Method](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Factory/02_Factory_Method.py)
<p align="center">
  <img src="https://i.imgur.com/oKvvML5.png">
</p>

A criação do Polymorphic Factory Method não é feita pela instanciação, mas por sua herança (isso ficará mais claro no final do exemplo).
 
1 - No UML acima, temos a classe `Produto`, que é representada pela classe `Armamento` em nosso [exemplo](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Factory/02_Factory_Method.py). Ela é nossa classe abstrata responsável por definir como será uma arma genérica.

2 - Em seguida, criamos várias classes `ConcreteProduct`, representada pelas classes:
- `Machado`
- `Espada`
- `Arco`
- `Escudo`
- `Flecha`
- `Adaga`

Essas classes concretas implementam o método abstrato que herdamos da classe `Projeto` e exibe o respectivo nome do armamento. 

3 - Agora, do outro lado do UML, começamos pela classe abstrata `Creator`, que foi nomeada de `Personagem`. Essa classe fornece o método `criar_personagem()`, que tem a função genérica de criar um personagens.

*Lembrando que a Classe `Personagem` não tem conhecimento das armas que cada `Personagem` pode ter.*

Criamos também métodos que:
- `get_nome_das_armas()` - retorna uma lista de armas do `Personagem`.
- `adicionar_arma()` - que adicionam as armas em uma lista chamada `equipamentos` que pertencem ao `Personagem`.

4 - Por fim, criamos as classes `ConcreterCreator`, nomeadas de:
- `Guerreiro`
- `Arqueiro`
- `Barbaro`

Cada uma dessas classes implementa o método abstrato `criar_personagem()`, o qual instância várias armas desse `Personagem` em tempo de execução. Assim fazendo uma relação com o termo usado acima, onde dissemos que a criação é feita por herança.

### Vantagens:
- Esse modelo nos garante uma enorme flexibilidade, deixando o código mais genérico. 

- Temos também um baixo acoplamento, tendo em vista que a parte que cria objetos está separada da parte que o utiliza.

- No exemplo acima podemos criar várias ramificações de novas armas e novos tipos de personagem utilizando várias combinações, tudo isso de maneira facilitada!
    - Facilidade para adicionar um novo tipo de produto à aplicação, só será necessário criar uma nova subclasse criadora e substituir o método Factory utilizando polimorfismo.

## [Abstract Factory](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Factory/03_Abstract_Factory.py)
<p align="center">
  <img src="https://i.imgur.com/9sN3y4H.png">
</p>

### O que é?
O Abstract Factory é uma extensão do [Polymorphic Factory Method](#polymorphic-factory-method), ele cria mais níveis de abstração, oferecendo uma interface que gera famílias de objetos relacionados sem especificar a classe concreta.

### Quando usar?

Esse método é indicado quando temos vários objetos interdependentes e você não deseja colocar essas características direto na classe que concretiza a entrega do objeto, removendo assim o acoplamento de camadas mais superficiais e deixando na interface apenas aquilo que importa.

### Mãos à Obra!

O [exemplo](https://github.com/drbuche/python-design-patterns/blob/master/Creational/Factory/03_Abstract_Factory.py) se trata de uma aventura! Queremos criar um grupos de aventureiros para desbravarem uma Caverna e uma Masmorra. Cada localidade deve ter um grupo de aventureiros específicos, tais grupos podem receber a ajuda de curandeiros ou não.

Iniciamos criando a nossa classe `LocalFactoryAbstrato`, uma classe abstrata responsável por moldar dois métodos, `criar_grupo_sem_healer()` e `criar_com_healer()`.

A partir desta classe, nós criamos as respectivas classes concretas:
- `CavernaConcreto(LocalFactoryAbstrato)` - que possui os métodos:
    - `criar_grupo_sem_healer()` - que retorna um grupo com Guerreiro e Ladino .
    - `criar_com_healer()` - que adiciona um Sacerdote no grupo.

- `MasmorraConcreto(LocalFactoryAbstrato)` - que possui os métodos:
    - `criar_grupo_sem_healer()` - que retorna um grupo com Mago e Barbaro.
    - `criar_com_healer()` - que adiciona um Druida no grupo.

Agora damos início ao nosso Produto abstrato, com as classes `SemCura` e ` ComCura`, essas classes possuem os métodos abstratos de `grupo_basico()` e `cura_adicional()`.
Esses métodos abstratos são modificados em suas classes concretas, sendo elas:
- `GuerreiroLadino(SemCura)`  e  `Sacerdote(ComCura)`. 
    - Que se relacionam com a Factory Concreta de de Grupo `CavernaConcreto`.

- `MagoBarbaro(SemCura)` e `Druida(ComCura)`.
    - Que se relacionam com a Factory Concreta de de Grupo `MasmorraConcreto`.

Por fim, criamos a interface `CriarGrupo`, que é responsável por chamar a nossa `Factory Concreta de Grupos` desejada e unir com as especificidades que desejamos do `Produto Concreto` (com ou sem cura).

Isso nos retornará:

```
Um Grupo sem cura entrará na MasmorraConcreto, ele é formado por : MagoBarbaro
Ao adentrar na MasmorraConcreto vocês receberão a ajuda de um Druida
Um Grupo sem cura entrará na CavernaConcreto, ele é formado por : GuerreiroLadino
Ao adentrar na CavernaConcreto vocês receberão a ajuda de um Sacerdote
```

**Assim conseguimos criar famílias de objetos relacionado!**

### Onde posso encontrá-lo?
O Abstract Factory é muito comum em projetos de interface gráfica do usuário (GUI), como:
- Motif
- GTK+(GNOME)
- Qt(KDE)

Um exemplo é quando criamos um objeto da Factory para a GUI que estamos utilizando e, a partir deste ponto, quando chamar um menu, botão, slider, etc... ele criará automaticamente a versão apropriada desse item para o GUI.


### Desvantagens:
Um "problema" do Abstract Factory é que ele é pouco utilizado, comparado com o [Polymorphic Factory Method](#polymorphic-factory-method), dificultando sua visualização por pessoas que não tem muita familiaridade com o pattern. Isso se deve por ele ter um nível de complexidade elevado e conseguir ter várias camadas de abstrações adicionais.


# [Polymorphic Factory Method](#polymorphic-factory-method) VS [Abstract Factory](#abstract-factory).

|   [Polymorphic Factory Method](#polymorphic-factory-method)️      |    [Abstract Factory](#abstract-factory)  |
|:---:|:------:|
|  Expõe um método ao cliente para criar os objetos. |  Contém um ou mais métodos de fábrica para criar uma família de objetos relacionados.   |
|  Usa herança e subclasses para definir o objeto a ser criado. |     Usa composição para delegar a responsabilidade de criar objetos de outra classe.  |
|  O Factory Method é usado para criar um produto.  |  O método Abstract Factory diz respeito a criar famílias de produtos relacionados.   |


