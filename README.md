# FIPEZAP-Data-Analyzer

O projeto FIPEZAP Data Analyzer foi desenvolvido em resposta a uma solicitação do Professor Cesar Augusto Cardoso Caetano. Sua estrutura é orientada a objetos e dividida em três programas principais.

## Descrição dos Programas

### data_loader

O primeiro programa, chamado `data_loader`, utiliza as bibliotecas pandas, requests e io para fazer o download da planilha disponibilizada pelo FIPEZAP Residencial no site [FIPEZAP](https://www.fipe.org.br/pt-br/indices/fipezap/#indice-mensal). Em seguida, transforma os dados para trabalhar em um dataframe, além de converter as datas para o formato 'YYYY-MM-DD' e os valores de índice para duas casas decimais.

### Calculate_metrics

O programa `calculate_metrics` é responsável por calcular os valores estatísticos utilizando os dados do dataframe. Isso inclui média, desvio padrão, mediana, relação interquartil e coeficiente de variação. Além disso, ele também plota os gráficos relacionados aos dados, incluindo o desvio padrão, boxplot e curva do índice ao longo do tempo. Para realizar essas tarefas, foram utilizadas as bibliotecas pandas, matplotlib e seaborn.

### Main

O programa principal, denominado `main`, atua como o ponto de ligação entre os códigos e as chamadas de classe e método. Ele coordena a execução dos programas `data_loader` e `calculate_metrics`, garantindo que os dados sejam carregados corretamente e que as métricas sejam calculadas e visualizadas adequadamente.

## Objetivo e Contexto

O projeto está vinculado com a estrutura disponibilizada pelo FIPEZAP e foi desenvolvido para fins de obtenção de nota no curso de Análise e Desenvolvimento na Faculdade Impacta.

Este projeto foi desenvolvido como parte de um trabalho acadêmico e não possui relação oficial com o FIPEZAP ou suas afiliadas. O FIPEZAP é uma marca registrada e pertence aos seus respectivos proprietários.

## Como Contribuir 

Se você identificar erros nas soluções propostas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request. Todas as contribuições são bem-vindas!

## Contato 

Para mais informações ou dúvidas, entre em contato com Geovanni Barbosa Reis através do e-mail geovanni.dev@gmail.com.
