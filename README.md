# 🚨🚗 Sinistralidade Rodoviária

**em desenvolvimento**

Dados de acidentes rodoviários com mortos e/ou feridos graves em Portugal Continental

## Fontes

[Relatórios de Sinistralidade](http://www.ansr.pt/Estatisticas/RelatoriosDeSinistralidade/Pages/default.aspx) da [ANSR](http://www.ansr.pt/).

Notas:  
- ~~embora haja um script para download dos PDFs (total de 429 PDFs a 08/Set/2018), o servidor tem rate-limiting agressivo~~ não usar sleep, há um espaço temporal antes de ser bloqueado que chega para fazer download de todos os relatórios PDFs
- relatórios anuais em PDF, por distrito de Portugal Continental
- entre os anos 2004 e 2017. Existem outros relatórios entre 1999 e 2003 (ainda a explorar)
- dois formatos de relatórios: vítimas a 24 horas e vítimas a 30 dias. 
	- Os dados a 30d começam a partir de 2010. Os dados a partir de 2011 estão tratados de forma semelhante aos das vítimas a 24h, numa tabela com todos os acidentes. Os dados de 2010 não estão tratados, dado que o respectivo relatório apenas inclui na tabela acidentes onde houve alterações no número de mortos entre as 24h e os 30 dias; para produzir a tabela completa, seria necessário cruzar a informação das duas tabelas. Caso necessite desta informação e tenha dificuldades, crie um [issue](https://github.com/centraldedados/sinistralidade/issues)
- tabela de 'Listagem dos Acidentes' extraída usando tabula-py (script disponível na pasta /scripts)  
- campos vazios têm um '-'

Scripts:
- `make pdf_download` para download dos PDFs para a pasta `pdfs`


## A fazer
- ~~Corrigir nomes inconsistentes dos csv causados por inconsistência do nome dos pdfs originais~~
- Nos ficheiros de 2007 para trás, há problemas nos cabeçalhos na conversão das tabelas. Em alguns casos, o título da página aparece na tabela convertida, pelo que o código procura pelo cabeçalho correcto nas primeiras linhas do ficheiro csv convertido. Há casos em que o cabeçalho não é convertido e o código acaba por não identificar nenhuma tabela de acidentes, apesar dela existir. É necessário fazer adaptações para este último caso. Existem por isso alguns ficheiros de dados de 2004 e 2005 vazios.
- Documentar scripts, makefile no final
- Acabar limpeza manual dos csv. Há ainda algumas inconsistências nas colunas e valores; infelizmente, as inconsistências são também ela inconsistentes. Situação atual:

Esta tabela indica os ficheiros cuja validação do número de colunas está confirmada.
Falta ainda verificar se as linhas estão corretas e bem preenchidas.

Distrito        | Limpo           
------------- |:-------------:
Aveiro | 2008-Fim
Beja | 2008-Fim
Braga | 2008-Fim
Bragança | 2008-Fim
Castelo Branco | 2008-Fim
Coimbra | 2008-Fim
Évora | 2008-Fim
Faro | 
Guarda | 2008-Fim
Leiria | 
Lisboa | 
Portalegre | 
Porto | 
Santarém | 
Setúbal | 
Viana do Castelo | 
Vila Real | 
Viseu | 
