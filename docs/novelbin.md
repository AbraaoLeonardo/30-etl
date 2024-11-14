
# Primeiro Projeto - NovelBin
## ETL em Site de Novels Chinesas
O primeiro projeto consiste em um simples pipeline de ETL, desenvolvido para extrair dados de um site de novels chinesas chamado NovelBin. Utilizando a biblioteca requests para fazer a requisição HTTP e o BeautifulSoup (bs4) para realizar o parsing e extração das informações, o objetivo principal deste projeto é coletar os dados e salvá-los em um arquivo de texto.

## Passos do Processo:
- **Extração (Extract):** A partir do site NovelBin, são feitas requisições HTTP para capturar os dados das novels.
- **Transformação (Transform):** Utilizando o BeautifulSoup, os dados brutos extraídos são limpos e organizados, removendo as partes indesejadas.
- **Carga (Load):** O conteúdo processado é salvo em um arquivo .txt para futura utilização.

## Casos de Uso do Projeto
Apesar de ser um projeto simples, ele abre diversas possibilidades interessantes de aplicação. Abaixo, alguns casos de uso que podem ser explorados:

1. Treinamento de Inteligência Artificial
Com os dados extraídos, podemos alimentar modelos de IA para treiná-los a escrever novels chinesas. Utilizando ferramentas de aprendizado de máquina, seria possível criar um sistema capaz de gerar histórias e narrativas baseadas no estilo das obras coletadas.

2. Tradução Automática
Uma vez que os textos estejam coletados, podemos aplicar ferramentas de tradução automática, como o ChatGPT ou o AWS Translate, para traduzir as novels para outros idiomas. Isso possibilitaria a distribuição das histórias para um público mais amplo, que não tenha o domínio do inglês.

Com o uso de ferramentas de automação, como o cronjob ou o Apache Airflow, seria possível agendar a coleta de novos capítulos das novels, realizar a tradução automaticamente e, em seguida, realizar o upload desses textos traduzidos o bancos de dados. Isso permitiria uma atualização constante e automática do conteúdo, sem a necessidade de intervenção manual.

Esse primeiro projeto serve como uma introdução ao processo de ETL e demonstra como técnicas simples de scraping e automação podem ser aplicadas em diversos contextos.

## Como executar o projeto
1. Acesse o site [novelbin](https://novelbin.lanovels.net/), selecione um capítulo e copie a sua URL
2. execute no terminal o seguinte comando
```bash
cd projeto1-novelbin
python3 src/main.py --url '<url da novel>'
```

## Disclaimer

Este projeto utiliza dados extraídos do site **NovelBin** para fins educacionais e de prática de ETL. **Não possuo os direitos autorais sobre as novels ou qualquer outro conteúdo presente no site**, e este projeto **não tem nenhuma relação com o site NovelBin**.

O objetivo deste projeto é apenas demonstrar o processo de **extração, transformação e carga (ETL)** de dados. Nenhuma obra é distribuída ou monetizada através deste projeto.

Se você é o detentor dos direitos autorais de qualquer conteúdo usado e deseja que ele seja removido, entre em contato para que possamos tomar as providências necessárias.
