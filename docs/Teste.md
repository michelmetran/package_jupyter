<h1>Sumário<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Introdução" data-toc-modified-id="Introdução-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introdução</a></span></li><li><span><a href="#Get-Jupyter-Notebook-filename" data-toc-modified-id="Get-Jupyter-Notebook-filename-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Get <em>Jupyter Notebook</em> filename</a></span></li><li><span><a href="#Export" data-toc-modified-id="Export-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Export</a></span></li><li><span><a href="#GitHub" data-toc-modified-id="GitHub-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>GitHub</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Requirements</a></span></li><li><span><a href="#Erros" data-toc-modified-id="Erros-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Erros</a></span></li><li><span><a href="#Referêcias" data-toc-modified-id="Referêcias-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Referêcias</a></span></li></ul></div>

# Export

Quero saber como exportar somente algumas células.
'https://stackoverflow.com/questions/57701538/jupyter-notebook-nbconvert-without-magic-commands-w-o-markdown


# GitHub

A partir do post [How to Git Jupyter Notebooks the Right Way](http://mateos.io/blog/jupyter-notebook-in-git), compreendi que é considerada como *best pratices* no git de projetos escritos em *Jupyter Notebook* a aplicação de um determinado código usando o package *nbstripout*, conforme segue. No vídeo [nbstripout: strip output from Jupyter and IPython notebooks](https://www.youtube.com/watch?v=BEMP4xacrVc) é explicado detalhadamente como o comando atua.

Criei uma 

# Requirements

O comando ```pip freeze``` é o mais difundido na internet para se obter os *requirements.txt*, ou seja, o arquivo com o qual é possível indicar quais os *packages* necessários para rodar um determinado *script*.

Tentei usar também o package ```pipreqs```, porém ele não funciona em *Juptyter Notebook*. Descobri ainda que o comando ``` conda env export > environment.yml``` pode auxiliar na criação destes parâmetros.

# Erros

Em uma tentativa de exportar o *Jupyter Notebook* para PDF tive problemas. O arquivo não era exportado e apresentava a seguinte mensagem de erro:
- *nbconvert failed: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex.*

Para solucionar, descobri que é necessário instalar, no Linux, akguns pacotes de aplicativos com os seguintes comandos:

```sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended```     # Versão Compacta

```sudo apt-get install texlive-full```      # Versão Completa

# Referêcias


[**Jupyter Notebook Extensions**](https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231)


A partir do post [**28 Jupyter Notebook Tips, Tricks, and Shortcuts**](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts)


A partir do post [Link do Folium](https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231)
