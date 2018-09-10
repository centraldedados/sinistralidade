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
- Corrigir erros nas tabelas, mais frequentes e inconsistentes de 2012 para trás
- Documentar scripts, makefile no final
