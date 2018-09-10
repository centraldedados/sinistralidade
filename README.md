# 🚨🚗 Sinistralidade Rodoviária

**em desenvolvimento**

## Fontes

[Relatórios de Sinistralidade](http://www.ansr.pt/Estatisticas/RelatoriosDeSinistralidade/Pages/default.aspx) da [ANSR](http://www.ansr.pt/).

Notas:  
- ~~embora haja um script para download dos PDFs (total de 429 PDFs a 08/Set/2018), o servidor tem rate-limiting agressivo~~ não usar sleep, há um espaço temporal antes de ser bloqueado que chega para fazer download de todos os relatórios PDFs
- relatórios anuais em PDF, por distrito de Portugal Continental
- entre os anos 2004 e 2017. Existem outros relatórios entre 1999 e 2003 (ainda a explorar).
- dois formatos de relatórios: vítimas a 24h, vítimas a 30 dias  
- tabela de 'Listagem dos Acidentes' extraida usando tabula-py (script disponível na pasta /scripts)  
- campos vazios têm um '-'

Scripts:
- `make pdf_download` para download dos PDFs para a pasta `pdfs`


## A fazer
- Adaptar script de conversão das tabelas para csv para relatórios anteriores a 2013
- Corrigir nomes inconsistentes dos csv causados por inconsistência do nome dos pdfs originais
- Documentar scripts, makefile no final
