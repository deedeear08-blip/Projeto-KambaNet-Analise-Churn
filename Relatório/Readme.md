
📊 Relatório de Análise de Customer Churn — KambaNet

Contexto

A KambaNet identificou um nível preocupante de cancelamento dos seus serviços. O objetivo desta análise foi compreender o comportamento dos clientes, identificar segmentos com maior risco de churn, avaliar o impacto financeiro dos cancelamentos e encontrar possíveis fatores associados à saída dos clientes.

> Nota: Os dados utilizados são simulados e foram desenvolvidos para fins educacionais e de demonstração de competências em análise de dados.




---

1. Situação atual dos clientes

A base analisada possui 30 clientes, dos quais:

16 estão ativos, representando 53,3%;

14 cancelaram o serviço, representando 46,7%.


Isso significa que quase metade dos clientes da amostra deixou de utilizar o serviço, indicando um nível elevado de churn que merece investigação.


---

2. Distribuição dos clientes por plano

O plano Básico possui a maior quantidade de clientes, com 11 clientes, seguido pelo Premium, com 10, e pelo Standard, com 9.

Apesar de possuir a maior quantidade de clientes, o plano Básico também apresenta o maior índice de cancelamento.

Plano	Clientes	Churn

Básico	11	63,6%
Premium	10	40,0%
Standard	9	33,3%


O resultado indica que os clientes do plano Básico representam um segmento prioritário para investigação e ações de retenção.


---

3. Receita por plano

O plano Premium é o principal gerador de receita mensal, mesmo possuindo menos clientes que o plano Básico.

Isso ocorre porque sua mensalidade é significativamente maior.

Atualmente:

Básico → 60.000 Kz/mês

Standard → 150.000 Kz/mês

Premium → 210.000 Kz/mês


Esse resultado demonstra que quantidade de clientes não determina necessariamente a maior geração de receita.


---

4. Concentração geográfica

A maior parte dos clientes está concentrada em Luanda, com 16 clientes.

As restantes províncias possuem bases significativamente menores:

Benguela → 6 clientes

Huambo → 4 clientes

Huíla → 4 clientes


Entretanto, quando analisamos churn proporcional, o cenário muda.

Churn por província

Huambo → 100%

Benguela → 100%

Huíla → 75%

Luanda → 6,25%


Huambo e Benguela apresentam os maiores índices de churn da amostra. Contudo, como possuem poucos clientes, esses resultados devem ser interpretados com cautela e investigados com uma base maior.


---

 5. Impacto financeiro do churn

Os clientes cancelados representam aproximadamente:

320.000 Kz de receita mensal perdida

Enquanto a receita atualmente gerada pelos clientes ativos é de:

420.000 Kz/mês

Considerando a receita potencial de toda a base, os resultados correspondem a:

56,8% → receita atual

43,2% → receita perdida


Portanto, o churn não representa apenas uma perda de clientes, mas também um impacto financeiro significativo para a empresa.


---

 6. Reclamações e cancelamento

Os clientes cancelados apresentam uma quantidade significativamente maior de reclamações.

Na amostra analisada:

Clientes ativos → aproximadamente 0,7 reclamação por cliente

Clientes cancelados → aproximadamente 5,2 reclamações por cliente


Além disso, os clientes com maior número de reclamações concentram-se entre aqueles que posteriormente cancelaram o serviço.

Isso indica uma forte associação entre reclamações e churn, embora os dados disponíveis não permitam afirmar que as reclamações sejam, por si só, a causa dos cancelamentos.


---

 7. Pagamentos atrasados

Também foi identificada uma diferença importante entre clientes ativos e cancelados.

Os clientes cancelados apresentam maior quantidade de pagamentos atrasados, enquanto a maioria dos clientes ativos apresenta poucos ou nenhum atraso.

Esse comportamento sugere que atrasos nos pagamentos podem funcionar como um sinal de risco, especialmente quando aparecem juntamente com um elevado número de reclamações.


---

 8. Tempo de permanência e risco de churn

Este foi um dos principais insights da análise.

O churn está fortemente concentrado entre os clientes com até 9 meses de permanência.

Na amostra:

> 14 dos 15 clientes com até 9 meses de permanência cancelaram o serviço, correspondendo a 93,3%.



Em contrapartida, não foram observados cancelamentos entre os clientes com 10 meses ou mais de permanência.

Além disso, existe uma forte correlação negativa entre:

Tempo como cliente × Reclamações → -0,86

e

Tempo como cliente × Pagamentos atrasados → -0,75

Isso significa que, nesta amostra, clientes com maior tempo de permanência tendem a apresentar menos reclamações e menos pagamentos atrasados.


---

 9. Relação entre reclamações e pagamentos atrasados

Foi identificada uma correlação de:

0,92

entre reclamações e pagamentos atrasados.

Isso representa uma correlação positiva muito forte.

Na prática, clientes que apresentam mais reclamações também tendem a apresentar mais pagamentos atrasados.

Entretanto, correlação não significa causalidade. É necessário obter dados adicionais para determinar o motivo dessa relação.


---

 10. Score de risco

Foi criado um Score de Risco utilizando:

número de reclamações;

número de pagamentos atrasados.


A regra utilizada foi:

Score = Reclamações + 2 × Pagamentos Atrasados

O peso maior atribuído aos pagamentos atrasados foi utilizado como uma regra de priorização dentro deste projeto.

A distribuição do score revela dois grupos principais:

clientes com risco baixo;

clientes com risco elevado.


Os clientes Luís, Bruno e Carlos apresentaram os maiores scores, com 12 pontos, tornando-se os clientes prioritários para uma possível ação de retenção.

> Importante: esse score é uma métrica heurística criada para este projeto; não representa um modelo estatístico de previsão validado.




---

 Insight principal

A análise indica que o principal risco de churn está concentrado nos primeiros meses da relação com o cliente.

Os clientes com menor tempo de permanência apresentam simultaneamente:

maior número de reclamações;

maior quantidade de pagamentos atrasados;

maior score de risco;

maior probabilidade de cancelamento na amostra analisada.


Isso sugere que os primeiros 9–10 meses representam uma janela crítica para retenção de clientes.


---

 Plano de ação recomendado

Se eu estivesse responsável pela análise da KambaNet, recomendaria inicialmente três frentes de ação:

1. Criar um programa de retenção para clientes novos

Monitorar especialmente clientes nos primeiros 9–10 meses.

Clientes com:

muitas reclamações;

pagamentos atrasados;

baixo tempo de permanência;

score de risco elevado


deveriam receber atenção prioritária.

2. Investigar as causas do churn em Huambo e Benguela

As duas províncias apresentam 100% de churn na amostra.

Entretanto, antes de atribuir o problema ao marketing, concorrência ou qualidade do serviço, a empresa deveria investigar:

qualidade da conexão;

cobertura;

atendimento;

preços;

concorrência;

motivos declarados pelos clientes no cancelamento.


3. Melhorar o acompanhamento de reclamações

Clientes que acumulam várias reclamações devem ser identificados antes de cancelarem.

A empresa poderia criar um sistema de alerta:

 Poucas reclamações → risco baixo
Muitas reclamações + atrasos → risco elevado



Isso permitiria à empresa agir antes do cancelamento, em vez de apenas reagir depois que o cliente sai.


---

 Conclusão

 A análise da KambaNet revela uma taxa de churn de 46,7%, com impacto estimado de 320.000 Kz em receita mensal perdida. O risco está particularmente concentrado nos clientes com até 9 meses de permanência, que apresentam maior número de reclamações, pagamentos atrasados e scores de risco. O plano Básico apresenta a maior taxa de churn, enquanto Huambo e Benguela apresentam os maiores índices de cancelamento na amostra.

Os resultados sugerem que a KambaNet deve concentrar seus esforços de retenção nos primeiros meses da relação com o cliente, monitorando reclamações e pagamentos atrasados e investigando as causas específicas do churn por plano e região. Para confirmar as hipóteses identificadas, seria necessário analisar uma base de clientes maior e incorporar informações adicionais, como motivos de cancelamento, qualidade do serviço, atendimento, preços da concorrência e histórico de campanhas de marketing.




---

Ferramentas utilizadas

Python · Pandas · SQLite · SQL · NumPy · Matplotlib · 

 Autor

Pedro João

📁 Projeto

Customer Churn Analysis — KambaNet

Nível: Data Analyst Junior — em formação


