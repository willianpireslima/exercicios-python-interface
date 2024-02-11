# exercicios-python-interface
 Exercícios em java que usam a interface gráfica Custom Tkinter

A interface gráfica usada foi a customtkinter que é uma versão aprimorada de tkinter\
![imgr_00](https://github.com/willianpireslima/exercicios-python-interface/assets/158337302/162ea058-c65a-413d-91b3-653357e39513)

A janela é inicializada da seguinte forma\
![imgr_01](https://github.com/willianpireslima/exercicios-python-interface/assets/158337302/0debd830-dc5b-4b88-ac84-389b9e69a71b)

A interface gráfica possui o seguinte elementos: entrada, botão é rotulo (label)\
![imgr_02](https://github.com/willianpireslima/exercicios-python-interface/assets/158337302/95acd39a-8870-4084-a8b9-4d8df7b5be72)

Para a organização desses elementos em tela e usando grid disposto na tela por meio das coordenadas de colunas\
![imgr_03](https://github.com/willianpireslima/exercicios-python-interface/assets/158337302/cc3f93cc-2b29-45db-bbab-5ee18009aadd)

Para acionar o evento do início do programa usando a interface é usando o botão, para isso é usada uma função a ser passada para o método command do widget, dentro da função são método para extrair os dados do widget entrada é passar dados para a label de saída
![imgr_04](https://github.com/willianpireslima/exercicios-python-interface/assets/158337302/af53dd26-954a-4ca5-9118-93cbf20c3cb0)

## 1ª Lista de Exercícios: Estrutura Sequencial <h2>

1) O coração humano bate em média uma vez por segundo. Desenvolva um algoritmo para calcular e escrever quantas vezes o coração de uma pessoa baterá se viver X anos. 
Dado de entrada: idade da pessoa (inteiro em anos). Considerações: 1 ano = 365,25 dias, 1 dia = 24 horas, 1 hora = 60 minutos e 1 minuto = 60 segundos.\

2) Um fabricante de latas deseja desenvolver um algoritmo para calcular o custo de uma lata cilíndrica dealumínio. O custo do alumínio é de R$ 100,00 por m<sup>2</sup>
 e é fixo. Dados de Entrada: raio e altura da lata (em metros). Área da lata = área da base e topo(π∗raio2∗2)+ área do lado(2∗π∗raio∗altura).\

3) No Teorema de Pitágoras, onde o quadrado da hipotenusa é igual à soma dos quadrados dos catetos
   H<sup>2</sup>=L1<sup>2</sup>+ L2<sup>2</sup>), para se criar triângulos retângulos com os três lados inteiros, são utilizadas as seguintesfórmulas: L1=∣M<sup>2</sup>−N<sup>2</sup>∣, L2=2∗M∗N e H=M<sup>2</sup>+ N<sup>2</sup>, onde M e N são dois valores inteiros positivos.Desenvolver um algoritmo que leia dois números inteiros positivos, calcule e escreva o tamanho dos
catetos e da hipotenusa do triângulo retângulo gerado\

4) Muitos países estão passando a utilizar o sistema métrico. Fazer um algoritmo para executar as seguintes
conversões: 
• Ler uma temperatura dada em graus Fahrenheit e imprimir o equivalente em Celsius.Farenheit=9/5∗C+ 32
• Ler uma quantidade de chuva dada em polegadas e imprimir o equivalente em milímetros.(1 polegada=25,4mm)

5) Fazer um algoritmo para ler os valores dos coeficientes A, B e C de uma equação quadrática. Calcular e imprimir o
valor do discriminante (delta). Δ=B2−4∗A∗C.

6) O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos
impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 12% do preço de fábrica e
os impostos de 30% do preço de fábrica, fazer um algoritmo para ler o custo de fábrica de um carro e imprimir o custo
ao consumidor.\

7) Desenvolver um algoritmo para ler os comprimentos dos três lados de um triângulo (L1, L2 e L3) e calcular a área do
triângulo de acordo com a fórmula: Área=√T∗(T−L1)∗(T−L2)∗(T−L3), onde T=L1+ L2+ L3/2\

8) Dados os pontos A e B, cujas coordenadas A ( x1, y 1) e B( x2, y 2) serão informadas via teclado, desenvolver um
algoritmo que calcule a distância entre A e B, onde: Distância=√( x 2−x 1)<sup>2</sup>+ ( y2−y 1)<sup>2</sup> \

9) Fazer um algoritmo que, dados os 4 elementos de uma matriz 2x2, calcule e escreva o valor do determinante desta
matriz.Determinante =∣a11 a12 a21 a22∣= a11∗a22 − a21∗a1\

10) Dada a base e a altura de uma pirâmide, fazer um algoritmo que calcule e escreva o seu volume.
 Volume=1/3∗base∗altura. \

11) Fazer um algoritmo que obtenha o raio e a altura de um cilindro e que calcule e escreva o seu volume e sua área.
 Área=2∗π∗raio∗(altura+ raio) e Volume=π∗raio<sup>2</sup>∗altura\

12) Uma locadora de charretes cobra R$ 8,50 de taxa, para cada 3 horas de uso destas, e R$ 3,50 para cada hora abaixo
destas 3 horas. Fazer um algoritmo que, dado a quantidade de horas que a charrete foi usada, calcule e escreva quanto o
cliente tem de pagar.\

13) Escrever um algoritmo que leia 3 valores a, b, c e os escreva. Encontre, a seguir, o maior dos 3 valores
e o escreva com a mensagem: “É O MAIOR”. Utilize a fórmula:Maior =x+ y+ ∣ x− y ∣ /2 \

14) Escreva um algoritmo que leia três números inteiros positivos (A, B, C) e calcule a seguinte e xpressão:
D =R+ S<sup>2</sup>, onde R=(A+ B)<sup>2</sup> e S=(B+ C)<sup>2</sup>.

## 2ª LISTA DE EXERCÍCIOS: ESTRUTURA CONDICIONAL  <h2>

1) Fazer um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par
ou ímpar.
2) Fazer um algoritmo que calcule a média aritmética das três notas de um aluno e mostre, além do valor da
média do aluno, a mensagem “Aprovado”, caso a média seja igual ou superior a 6, ou a mensagem
“Reprovado”, caso contrário.
3) Escrever um algoritmo que leia o nome completo de um aluno e suas três notas; calcule a média
ponderada do aluno, considerando que o peso para a maior nota é 4 e, para as duas restantes, 3; mostre o
nome do aluno, suas três notas, a média calculada e uma mensagem "APROVADO", se a média for maior
ou igual a 5 e "REPROVADO", caso contrário.
4) Desenvolver um algoritmo que leia um número inteiro e verifique se este é divisível por 5 e por 3 ao mesmo tempo.
5) Dados quatro números distintos, desenvolver um algoritmo que determine e imprima a soma dos três
menores.
6) Desenvolver um algoritmo que leia os coeficientes (a, b e c) de uma equação do segundo grau ( y=ax<sup>2</sup>+ bx+ c) e
que calcule suas raízes. O algoritmo deve mostrar, quando possível, o valor das raízes calculadas e a classificação das
mesmas: “RAÍZES IMAGINÁRIAS”, “RAIZ ÚNICA” ou “RAÍZES DISTINTAS”.

7) Desenvolver um algoritmo para ler um número X e calcular e imprimir o valor de Y de acordo com as
condições a seguir: Y=X , se X< 1; Y=0, se X=1 e Y=X<sup>2</sup>, se X> 1.

8) Escrever um algoritmo que leia três números inteiros e que mostre o maior deles, supondo que todos sejam distintos.

9) Fazer um algoritmo que calcule e imprima o salário reajustado de um funcionário de acordo com as
seguintes regras:
• salário de até R$ 1500,00, reajuste de 50%;
• salários maiores que R$ 1500,00, reajuste de 30%.

10) O número 3.025 possui a seguinte característica:
{30 + 25 = 55
552 = 3.025
Fazer um algoritmo que, dado um número de 4 dígitos, calcule e escreva se ele possui ou não esta
característica. 

12) Fazer um algoritmo que, dado três valores A, B e C, verifique se eles formam um triângulo. Formando
um triângulo, dizer se ele é equilátero, isósceles ou escaleno. 

13) Fazer um algoritmo que, dado os lados de um triângulo A, B e C, onde A é o maior lado, dizer se os mesmos
formam um triângulo retângulo (A<sup>2</sup>=B<sup>2</sup>+ C<sup>2</sup>), obtusângulo (A<sup>2</sup>> B<sup>2</sup>+ C<sup>2</sup>) ou acutângulo (A<sup>2</sup>< B<sup>2</sup>+ C<sup>2</sup>).

13) Número capicua é aquele que escrito da direita para esquerda ou da esquerda para direita tem o mesmo
valor. Exemplos: 929, 44, 97379. Fazer um algoritmo que, dado um número de 5 dígitos, calcule e escreva
se o mesmo é ou não capicua.

14) Desenvolver um algoritmo que leia o mês e o ano de uma data e que exiba o número de dias constantes no mês do
ano lido.

15) Desenvolver um algoritmo que determine o imposto de renda cobrado de um funcionário pelo governo.
Seu programa deverá ler o número de dependentes, o salário do funcionário e o imposto normal pago. O
imposto bruto é de 20% do salário do funcionário se o funcionário ganha mais de 12 salários mínimos; o
imposto bruto é de 8% do salário do funcionário se o funcionário ganha mais de 5 e até 12 salários
mínimos; e de quem ganha 5 salários mínimos ou menos não é cobrado o imposto de renda. Sabe-se qugoverno cobra
4% de taxa adicional sobre o imposto bruto. Determine o imposto líquido a ser pago pelofuncionário subtraindo R$ 300,00
para cada dependente do mesmo, no imposto bruto. O programacalculará e imprimirá o imposto a ser pago ou devolvido, que é
a diferença entre o imposto normaldescontado e o imposto líquido. Se a diferença for negativa mostrar a mensagem “imposto a pagar”, caso
contrário “imposto a receber”. Considere o salário mínimo como uma constante no seu programa.

16) Quadrado perfeito é o número cuja raiz quadrada é um valor inteiro. Exemplo 144. Fazer um algoritmo que, dado
um número inteiro positivo, calcule e escreva se o mesmo é ou não um quadrado perfeito. 

17) Desenvolver um algoritmo para receber uma data e consisti-la. Consistir uma data significa verificar se
a mesma é válida.

18) Desenvolver um algoritmo para calcular a conta de água para a SANEAGO. O custo da água varia dependendo do
tipo do consumidor – residencial, comercial ou industrial. A regra para calcular a conta é:
• Residencial: R$ 5,00 de taxa mais R$ 0,05 por m<sup>3</sup> consumido;
• Comercial: R$ 500,00 para os primeiros 80 m<sup>3</sup> consumidos mais R$ 0,25 por m<sup>3</sup> excedente;
• Industrial: R$ 800,00 para os primeiros 100 m<sup>3</sup> mais R$ 0,04 por m3 excedente;
O algoritmo deverá ler a conta do cliente, seu tipo (residencial, comercial ou industrial) e o seu consumo de
água em metros cubos. Como resultado, imprimir a conta do cliente e o valor em reais a ser pago pelo mes

19) A distribuidora de combustíveis Ave Maria irá aumentar o preço do combustível em função da
quantidade comprada anualmente por seus clientes. Os postos, que consomem em média até 50.000 litros
de combustível por mês, terão aumento de 20%. Os postos, que consomem acima desta média, 12% de
aumento. A distribuidora irá fornecer o nome do posto e seu consumo anual. Faça um algoritmo que leia os
dados fornecidos pela distribuidora, calcule e escreva o nome do posto e qual será o preço do litro de
combustível para o mesmo, considerando-se que hoje a distribuidora cobra R$ 4,95 por litro.

20) Uma locadora de filmes tem as seguintes regras para aluguel de DVDs:
• às segundas, terças e quintas (2, 3 e 5): desconto de 40% em relação ao preço normal;
• às quartas, sextas, sábados e domingos (4, 6, 7 e 1): preço normal;
• locação de DVDs comuns: preço normal;
• locação de lançamentos: acréscimo de 15% em relação ao preço normal.
Desenvolver um algoritmo para ler o preço normal do DVD alugado (em R$), sua categoria (comum ou
lançamento), o dia da semana da locação e calcular e imprimir o preço final que será pago pela locação do DVD.

21) Elabore um algoritmo que leia dois números inteiros e a operação aritmética desejada; calcule, então, a
resposta adequada. Utilize os símbolos da tabela a seguir para saber qual a operação aritmética escolhida.
Símbolo Operação Aritmética
+ Adição
– Subtração
* Multiplicação
/ Divisão

22) Desenvolver um algoritmo com as opções de calcular e imprimir o volume e a área da superfície de um cone reto,
de um cilindro ou de uma esfera. O algoritmo deverá ler a opção da figura desejada (cone/cilindro/esfera) e, de acordo
com a opção escolhida, calcular e escrever o volume e a área da superfície da figura pedida.
Fórmulas:
• Cone Reto: Volume =π∗raio<sup>2</sup>∗altura\3 e Área = π∗raio∗√raio<sup>2</sup>+ altura2
• Cilindro: Volume = π∗raio<sup>2</sup>∗altura e Área = 2∗π∗raio∗altura
• Esfera: Volume =4\3∗π∗raio\3 e Área = 4∗π∗raio<sup>2</sup>

23) Fazer um algoritmo que receba a idade e o nome de um nadador e imprima o seu nome, a sua idade e a
categoria do mesmo, de acordo com as regras a seguir:
Categoria Faixa Etária
Infantil A 5 a 7 anos
Infantil B 8 a 10 anos
Juvenil A 11 a 13 anos
Juvenil B 14 a 17 anos
Sênior A partir de 18 anos

24) Elabore um algoritmo que calcule o valor a ser pago por um produto considerando o preço normal de etiqueta e a
escolha da condição de pagamento. Utilize os códigos da tabela a seguir para saber qual a condição de pagamento
escolhida e efetuar o cálculo adequado.
Código Condição de Pagamento
1 À vista, dinheiro ou cheque, 10% de desconto.
2 À vista, cartão de crédito, 5% de desconto.
3 Em 2 vezes, preço normal da etiqueta sem juros.
4 Em 3 vezes, preço normal da etiqueta + 10% de juros.

25) Um usuário deseja um algoritmo onde ele possa escolher o tipo de média que deseja calcular a partir de
3 notas. Faça um algoritmo que leia as notas, sua opção escolhida e calcule a média. 
(1) aritmética; (4) geométrica;
(2) ponderada (3, 3, 4); (5) quadrática.
(3) harmônica

26) Escreva um algoritmo que descubra se um ano lido é bissexto. Um ano é bissexto se ele for múltiplo de 4, exceto
quando ele for múltiplo de 100. Os anos múltiplos de 100 somente são bissextos quando são múltiplos de 400, usado a
partir de 1752 (por exemplo 1800 não é bissexto, mas 2000 é). 

27) Fazer um algoritmo que leia os dados de um usuário de telefonia de uma empresa de telecomunicações:
bairro e número completo do telefone; e verifique se o número do telefone (Exemplo: 32121212) está
correto, ou seja, se o prefixo (4 primeiros dígitos) é correspondente ao bairro especificado. Sabendo-se que
os prefixos existem nos bairros conforme a tabela a seguir: 
Bairro Prefixo
Oeste 3223, 3225, 3212
Centro 3223, 3224, 3212
Sul 3241, 3242, 3243, 3281
Bueno 3251, 3285
Campinas 3233, 3291

28) Escrever um algoritmo que leia o nome de um aluno, as 3 notas obtidas por ele nas 3 verificações e a média dos
exercícios que fazem parte da avaliação. Calcular a média de aproveitamento do aluno, usando a fórmula:
Média de Aproveitamento =nota1+ nota2∗2+ nota3∗3+ média dos exercícios\7 e o seu conceito, utilizando a tabela a seguir:
Média de Aproveitamento Conceito
9,0 < média ≤ 10,0 A
7,5 < média ≤ 9,0 B
6,0 < média ≤ 7,5 C
4,0 < média ≤ 6,0 D
média ≤ 4,0 E
O algoritmo deve escrever o nome do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o
conceito correspondente e a mensagem: APROVADO se o conceito for A, B ou C e REPROVADO, se o conceito for D
ou E.

30) A cidade de Perdiz das Cruzes possui um único posto telefônico. Por este posto são feitas todas as
ligações interurbanos da cidade. O valor a ser pago é calculado de acordo com as seguintes regras:
• Taxa de R$ 2,00 pela ligação mais R$ 1,00 para os 3 primeiros minutos;
• Acima dos três primeiros minutos, a taxa é de R$ 2,15, para cada intervalo de 5 minutos, e
R$ 0,85, para cada minuto abaixo disto.
A telefonista irá fornecer o nome do usuário e o tempo da ligação em minutos. O algoritmo deverá
calcular o valor a ser pago e escrever o nome do usuário e o valor da conta

31) Criar um algoritmo que leia o nome, a conta e o saldo bancário total do semestre de uma pessoa e que
calcule a tarifa bancária em que o mesmo se enquadra:
• Básica (saldo médio mensal inferior a R$ 1.000,00) tarifa de R$ 25,00;
• Prata (saldo médio mensal entre R$ 1.000,01 e R$ 2.000,00) tarifa de R$ 20,00;
• Ouro (saldo médio mensal entre R$ 2.000,01 e R$ 3.500,00) tarifa de R$ 13,00;
• Prêmio (saldo médio mensal superior a R$ 3.500,00) tarifa isenta.

32) Criar um algoritmo que leia a idade de uma pessoa e que mostre a sua classe eleitoral:
• Não-eleitor – abaixo de 16 anos;
• Eleitor Obrigatório – de 18 a 65 anos;
• Eleitor facultativo – de 16 a 18 e de 65 anos em diante.

33) Um posto de combustível vende três tipos de combustíveis: álcool, diesel e gasolina. O preço por litro
de combustível é apresentado na tabela a seguir. Faça um algoritmo que leia um caractere que representa o
tipo de combustível comprado (a, d ou g) e a quantidade em litros. O programa deve imprimir o valor em
reais a ser pago pelo combustível.
Combustível Preço por Litro
A - Álcool R$ 1,799
D - Diesel R$ 1,899
G - Gasolina R$ 2,799

34) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes expressões:
• Para homens: 72,7∗h−58 ;
• Para mulheres: 62,1∗h−44,7 ;

## 3ª LISTA DE EXERCÍCIOS – ESTRUTURAS DE REPETIÇÃO  <h2>

1) faça um algortimo que ao ser digitado um numero imprima ate esse numero em uma lista

2) Fazer um algoritmo que calcule o volume de uma esfera em função do raio R.
 O raio deverá variar de 0 a 20 cm de 0,5 em 0,5 cm em imprima em lista

3) Número capicuas são aqueles que escritos da direita para esquerda ou da esquerda para direita têm o mesmo
valor. Exemplo: 929, 44, 97379. Fazer um algoritmo, que dado um número inteiro positivo, calcule e escreva
se o mesmo é ou não capicua

4) Um número inteiro positivo é triangular se este for o resultado do produto de três números naturais consecutivos. Por exemplo, o número 120 é triangular porque 120 = 4*5*6.
Fazer um algoritmo que:leia um número inteiro; verifique se o número é ou não triangular. Se for imprimir: “Número Triangular” senão imprimir:"Número não Triangular”

5) Fazer um algoritmo que leia um número inteiro positivo, calcule e escreva o seu fatorial.
Exemplo: Fatorial de 5 → 5! = 5*4*3*2*1. Obs.: Fatorial de 0, por definição: 0! = 1.

6) Fazer um algoritmo que calcule e escreva a multiplicação de dois números N1 e N2 lidos do teclado.
Obs.: a máquina que executará este algoritmo somente sabe: adicionar e subtrair.

7) Fazer um algoritmo que leia um número inteiro positivo, calcule e escreva se o número lido é perfeito ou não.
Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, é igual ao número. Exemplo: 6 é um número perfeito porque 1 + 2 + 3 = 6.

8) Número primo é aquele que somente é divisível por ele mesmo e pela unidade. Fazer um algoritmo que leia
um número inteiro positivo, calcule e escreva se este é um número primo ou não

9) Fazer um algoritmo que leia um número inteiro positivo, calcule e escreva todos os seus divisores

10)  Fazer um algoritmo que:
• Leia dois números inteiros positivos;
• Calcule e escreva, para este par de números, o máximo divisor comum.
Obs.: Utilizar o método das divisões sucessivas (Algoritmo de Euclides).

## 4ª Lista de Exercícios N. 04 - POO  <h2>

QUESTÃO 01 - Desenvolva uma classe que modele um objeto cone em conformidade com o paradigma orientado a objeto.
Posteriormente implemente esta classe. A classe deverá ter as seguintes características: raio, altura e cálculo da geratriz,
área lateral, área total e o volume. Obs.: os valores do raio e da altura não podem ser negativos. O cálculo da geratriz é
(sqrt((altura*altura)+(raio*raio))), da área lateral é (3.14*raio*geratriz), da área total é (3.14*raio*(geratriz()+raio)) e do volume
é (1.0/3.0*3.14*raio*raio*altura).

QUESTÃO 02 - Desenvolva uma classe que modele um objeto triângulo em conformidade com o paradigma orientado a
objeto. Posteriormente implemente esta classe. A classe deverá ter as seguintes características: três lados ( L1, L2 e L3 ),
cálculo da área e encontrar os tipos do triângulo. Obs. os valores dos três lados não podem ser negativos e têm que formar
um triângulo.O triângulo possui três lados, nem todo conjunto de três valores numéricos formam um triângulo. Os triângulos podem ser
classificados ( tipos ):
• quanto aos lados: equilátero ou isósceles ou escaleno;
• quanto aos ângulos: acutângulo(A2<B2+C2
) ou obtusângulo(A2>B2+C2
) ou retângulo(A2=B2+C2
);

QUESTÃO 03 - Desenvolva uma classe que modele um objeto equação do segundo grau (ax2 + bx + c) em conformidade
com o paradigma orientado a objeto. Esta classe deve conter como atributos os coeficientes a, b e c. E os métodos para
definir a, b e c, para retorná-los, para calcular as raízes da equação caso elas existam.

QUESTÃO 04 - Criar uma classe Estoque definido a seguir:
 class Estoque
 {
 private:
 string descricao;
 int prodNum;
 int qde;
 double preco;
 public:
 void setEstoque();
 void getEstoque();
};
Faça um programa ( função principal ) para usar esta classe. Este programa deve:
• Criar um vetor de 10 objetos do tipo Estoque.
• Solicitar do usuário o preenchimento dos 10 objetos.
• Mostrar no vídeo os 10 objetos.

QUESTÃO 05 - Uma agenda de contatos de um celular normalmente pode armazenar até 256 contatos. Cada objeto do tipo
Contato tem um nome, um telefone e um e-mail. A class Contato deve conter os códigos para manipulação das
informações, ou seja, as funções membro: setContato(), modificarContato(), buscarContato() e getContato(). Faça um
programa em C++ para implementar uma agenda. A classe Agenda, que contém um vetor de registros do tipo Contato
para armazenar até 256 contatos e uma variável para controlar a ocupação deste vetor. A classe Agenda deverá ter as
seguintes funções membros: setContato(), getContato(), excluirContato(), buscarContato() e modificarContato().
O programa deve fornecer na função principal um menu de escolhas com as seguintes opções:
1. Para Inserir Contato.
2. Para Excluir Contato.
3. Para Buscar Contato.
4. Para Modificar Contato.

QUESTÃO 06 - Faça um programa em C++ para solicitar do usuário os coeficientes da equação do 2
0 grau (f(x) = ax2 + bx +
c) e calcular o ponto de inflexão (ponto de mínimo ou de máximo) usando a derivada. Calcular e armazenar num vetor uma
quantidade de coordenadas determinada pelo usuário mais um ponto de inflexão.
• Calculo do ponto de inflexão usando a derivada.
• f’(x) = 2ax + 2 = 0 -----> xi = -b / (2*a)
• aplica-se o resultado de xi em f(x) = ax2 + bx + c
• Tome a metade das coordenadas para o eixo X menores do que o ponto de inflexão, igualmente espaçadas de 1 em
1 unidade, e calcule a sua correspondente no eixo Y.
• Tome a metade coordenadas para o eixo X maiores do que o ponto de inflexão, igualmente espaçadas de 1 em 1
unidade, e calcule a sua correspondente no eixo Y.

QUESTÃO 07 - Criar uma classe Fracao que contenha dois membros de dados do tipo inteiro: numerador e denominador,
e as funções membro: setNumerador(), setDenominador(), soma(), subtrai(), divide(), multiplica(), mdc() e simplifica().
Faça um programa para implementar uma calculadora de frações com as operações de adicionar, multiplicar, subtrair e dividir,
onde todas as frações devem ser armazenadas em objetos do tipo Fracao.

QUESTÃO 08 - Criar uma classe Tempo que contenha três membros de dados do tipo inteiro: horas, minutos e segundos,
e cinco funções membro: validaTempo(), converteTempoSgundos(), converteSegundosTempo(), setTempo() e
getTempo(). A função converteSegundosTempo() deve retornar um registro do tipo Tempo. A função
converteTempoSgundos() deve retornar um long long. O tempo deve ser obtido e mostrado no formato h:min:seg ( 12:43:25
)
Fazer um’programa para:
• Solicitar do usuário pelo menos dois tempos e armazená-los em objetos do tipo Tempo.
• Mostrar os tempos no vídeo.
• Determinar o total de segundos de cada tempo e mostrá-los no vídeo.
• Determinar a diferença entre dois tempos, transformando-os em segundos e fazendo a diferença, e converte-la para
o formato h:min:seg. Exibir na tela esta diferença convertida para h:min:seg.

QUESTÃO 09 - Criar uma classe Data que contenha três membros de dados do tipo inteiro: dia, mes e ano, e cinco funções
membro: setData(), getData(), validaData(), determinaDiaSemana() e calculaDiasEntreDatas(). A data deve ser obtida e
mostrada no formato dia/mês/ano ( por exemplo: 31/12/2007 ). Para o cálculo do número de dias entre duas datas e a
determinação do dia da semana faça uma pesquisa ( biblioteca ou internet ). Fazer um programa para:
• Solicitar do usuário pelo menos duas datas e armazená-las em objetos do tipo Data.
• Determinar o dia da semana de cada data.
• Mostrar as datas no vídeo com os respectivos dias da semana.
• Determinar e mostrar no vídeo o número de dias entre as duas datas.

QUESTÃO 10 - Escreva um programa em C++ que implemente o jogo da forca. Você deve pesquisar as regras na internet
e adotar claramente estas regras segundo uma das fontes encontras ( sites ). Indicar a fonte ( site ) das regras adotadas
no seu programa com comentário no início do arquivo de código do seu programa. Usar necessariamente funções e arrays
( vetores e/ou matrizes ).
