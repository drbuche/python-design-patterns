# Padrão de Projeto Estrutural (Structural) - Facade:


<p align="center">
  <img src="https://i.imgur.com/dnJ9L4v.jpg" width="1440px" height="500px"/>
</p>

## Características Gerais: 

O Pattern Facade, também conhecido como Façade ou Fachada, é responsável por fazer a intermediação dos subsistemas com o cliente, criando uma "Fachada" (interface) entre essas entidades, assim o cliente não tem a necessidade de conhecer o sistema como um todo!

Caso você tenha uma ligação um tanto confusa entre classes e interações que o cliente **não necessariamente** precise ver, você pode criar uma interface que seja útil para o cliente, apresentando a ele apenas o necessário, concretizando assim o Pattern Facade!

 
# UML:

<p align="center">
  <img src="https://i.imgur.com/un8wwnE.jpg"/>
</p>


# Como Funciona?

*Que tal conceituarmos utilizando uma estalagem medieval?*

Digamos que você acabou de voltar de sua aventura, cansado, com sede e fome.Você entra em uma estalagem para comer, beber e depois descansar em algum quarto. Para isso você deve conversar com o estalajadeiro, especificando o que deseja comer, beber e pedindo um quarto.

O estalajadeiro, coletará seu pedido e distribuirá para cozinha, camareira e demais funcionários, que por sua vez o retornarão a ele e serão entregues a você.

- Cliente:
    - Neste exemplo, vemos que `Você` é a entidade `Cliente`, responsável por pedir um objeto característico e recebê-lo no final do processo. Além disso, nota-se que você não tem conhecimento total da cozinha, quartos, funcionários e estoque da estalagem, seu contato se resumo ao estalajadeiro.
    
- Facade:
    - Representado pelo `Estalajadeiro`, nossa interface responsável por intermediar o `Cliente` com os serviços (`System`) que serão prestados. Ele comunica as duas pontas, sem que uma saiba da organização da outra.
    
- System:
    - Cada `Funcionário` representa um `Subsystem` que unidos compõem o `System` da estalagem, são responsável por executar as tarefas que o estalajadeiro repassa.
   
   
 
 # Mãos a Obra!
 
Vamos utilizar o [exemplo](https://github.com/drbuche/python-design-patterns/blob/master/Structural/Facade/Facade.py) da estalagem, onde:

Você, nobre aventureiro, deseja apenas chegar na estalagem e tomar um Hidromel, comer uma enorme Wild Pie e depois descansar em um quarto quente.

Para começar, iniciaremos criando a nossa classe `Estalajadeiro`, que representa nossa interface `Facade`. O `Estalajadeiro` tem a função de facilitar a interação do `Cliente` com os `Subsistemas` da estalagem. 
 
A classe `Estalajadeiro` possui o `método trabalhando()`, que é responsável por acionar as ações dos `Subsistemas` desejados.

Agora criamos nossos `Subsistemas`:

- `Camareira`: Que verifica se o quarto está livre com o método `__verifica_vaga() `, se a resposta for `True`, ela consegue limpar o quarto com o método `prepara_quarto()`.

- `Cozinheiro`: Que acende o fogo e depois utiliza o método `preparando_comida()` para preparar o prato desejado.

- `Adega`: Que procura a bebida na adega, e atribui `hidromel` como `True` (pois uma estalagem que se preze sempre tem Hidromel!). Essa classe também possui o método `pegar_bebida()`, responsável por pegar o Hidromel.
 
Por fim criamos a classe que representa você, o `Cliente`, a qual nomeamos de `Aventureiro`.

Dentro da classe `Aventureiro`, colocamos um método chamado `fazer_pedido()` que irá se comunicar com o estalajadeiro e retornará apenas aquilo que precisamos.
- *Utilizamos o método mágico `__del__` apenas como um finalizador, para deixar um obrigado ao estalajadeiro, esse método é como um `__init__` ao contrário, pois ao invés de realizar as ações no inpicio de sua instanciação, ele as executa em seu término e as apaga da memória logo em seguida.* 

Agora é só atribuir a classe `Aventureiro` a uma variável e chamar o método `fazer_pedido()`. Isso nos retornará:

```
-------------------------------------------------------
'O aventureiro adentra a estalagem....'
Aventureiro: Olá estalajadeiro, eu gostaria de um Hidromel, uma Wild pie e um quarto para pernoitar.
-------------------------------------------------------
Estalajadeiro: Vou verificar se temos tudo, um segundo.
-------------------------------------------------------
Camareira: 'Verificando quartos...
Camareira: O quarto está vago!
Camareira: Inicia a limpeza do quarto.
Cozinheiro: Estou acendendo o fogo!
Cozinheiro:'Wild pie está sendo preparada.' 
Adega: 'Procurando a bebida...'
Adega: 'Retorna Hidromel.'
-------------------------------------------------------
Aventureiro: Obrigado pelo serviço!
-------------------------------------------------------

```

Tudo isso é possível pois a interface `Estalajadeiro` simplifica as coisas para o `Aventureiro`. Por sua vez o `Estalajadeiro` usa de composição (como visto no UML) com os `Subsistemas`, para criar objetos desejados pelo `Aventureiro`!

# Princípio do Conhecimento Mínimo e a Lei de Demeter:

- **Princípio do Conhecimento Mínimo:**
    - Analisar o design do sistema, observando atentamente quantas classes temos ligada a cada objeto criado e o modo que essa interação ocorre.
    - Observando o primeiro tópico, certifique-se que não exista diversas classes criadas e altamente acopladas entre si.
    - Caso o tópico dois seja falso, o sistema tem uma probabilidade alta de ser difícil de se manter. Qualquer alteração em uma classe pode causar uma mudança não intencional em outra parte, significando que o sistema possa sofrer uma regressão para só depois expandir.
 
- **Lei de Demeter:**
    - Cada unidade deve ter conhecimento limitado sobre outras unidades.
        - Apenas unidades próximas se relacionam. 
    
    - Cada unidade deve apenas conversar com seus amigos.
        - Não fale com estranhos. 
    
    - Apenas fale com seus amigos imediatos.
    

**O Princípio do Conhecimento Mínimo e a Lei de Demeter são iguais, apontando para a filosofia do baixo acoplamento.**


# FAQ:

- Posso ter várias `Facade` para um `Subsistema`? 
    - Sim. Mas devemos tomar cuidado! Tendo em vista que podemos ter várias interface para facilitar a comunicação do `Cliente`, uma má execução pode virar uma bola de neve, pois se começarmos a criar muitas interfaces desnecessárias, aumentamos a complexidade do código e reduzindo o desempenho em tempo de execução.
 
- O `Cliente` pode acessar os `Subsistemas` de forma independente?
    - Sim. Como os `Subsistemas` não são classes abstratas, podemos acessá-los diretamente.

- O `Facade` pode adicionar alguma funcionalidade própria?
    - Sim. Um `Facade` bem aplicado pode adicionar uma linearidade ao código, ditando a ordem das ações e invocações dos `Subsistemas`.

# Ligações:

O padrão [`Abstract Factory`](https://github.com/drbuche/python-design-patterns/tree/master/Creational/Factory#abstract-factory) pode ser usado com o `Facade` para fornecer uma interface responsavel por criar objetos de um `Subsistema` de forma independente. Pode também ser usado como uma alternativa ao `Facade` para esconder classes de alguma plataforma especifica.