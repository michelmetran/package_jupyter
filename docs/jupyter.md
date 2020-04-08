<h1>Sumário<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Introdução" data-toc-modified-id="Introdução-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introdução</a></span></li><li><span><a href="#Get-Jupyter-Notebook-filename" data-toc-modified-id="Get-Jupyter-Notebook-filename-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Get <em>Jupyter Notebook</em> filename</a></span></li><li><span><a href="#Export" data-toc-modified-id="Export-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Export</a></span></li><li><span><a href="#GitHub" data-toc-modified-id="GitHub-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>GitHub</a></span></li><li><span><a href="#Outros" data-toc-modified-id="Outros-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Outros</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Requirements</a></span></li><li><span><a href="#Erros" data-toc-modified-id="Erros-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Erros</a></span></li><li><span><a href="#Referêcias" data-toc-modified-id="Referêcias-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Referêcias</a></span></li></ul></div>

# Introdução

O *Jupyter Notebook* é a maneira que optei para escrever os códigos na linguagem *Python*, visto que além de rodar os códigos, é possível:
1. Documentar os *scripts*, escrevendo o singnificado e objetivo de cada conjunto de comandos;
2. Atualizar os meus repositórios na plataforma **GitHub**;
3. Trabalhar com uma diversidade de opções de exportação do arquivo em formatos diversos, adaptados até mesmo para as simples leitura, como PDFs e Markdowns.

É no procesos de exportação dos arquivos que eu me ative nessa publicação, pois um dos objetivos de longo prazo que busco é exportar relatórios padronizados, para distribuição geral e irrestrita, ou seja, quero algo que não seja inteligível apenas por pessoas que conhecem de programação.

Para isso foram aqui apresentados um diversidade de opções para exportação de um arquivo *.ipynb*, sendo possível incluir com campos determinados, tais como:
- Apenas as células que tenham determinada *tag*;
- Apenas as células de *markdown*;
- Excluindo as células de *outputs*.




```python
%run '../codes/files/create_folders.py'

create_folders('', folders=['docs'])
```

    Directory "docs" already exists...


# Get *Jupyter Notebook* filename

https://stackoverflow.com/questions/12544056/how-do-i-get-the-current-ipython-jupyter-notebook-name


```javascript
%%javascript

var kernel = IPython.notebook.kernel;
var body = document.body, attribs = body.attributes;
var command = 'ipynb_filename = ' + '"'+attribs['data-notebook-name'].value+'"';
kernel.execute(command);
```


    <IPython.core.display.Javascript object>



```python
ipynb_filename
```




    'jupyter.ipynb'




```python
#%run '../codes/files/get_jupyternotebook_name.py'
```


```python
#get_jupyternotebook_name()
```


```javascript
%%javascript

var kernel = IPython.notebook.kernel;
var nb = IPython.notebook;
var command = 'ipynb_pathname = "' + nb.base_url + nb.notebook_path + '"';
kernel.execute(command);
```


    <IPython.core.display.Javascript object>



```python
ipynb_pathname
```




    '/package_jupyter/jupyter.ipynb'



# Export


```python
%run '../codes/files/export_jupyter.py'

export_jupyter(ipynb_filename, 'docs', ['html', 'markdown', 'pdf', 'python'], False)
```

    Arquivo jupyter.ipynb exportado corretamente para o formato html sem usar prefixo da data.
    Arquivo jupyter.ipynb exportado corretamente para o formato markdown sem usar prefixo da data.
    Arquivo jupyter.ipynb exportado corretamente para o formato pdf sem usar prefixo da data.
    Arquivo jupyter.ipynb exportado corretamente para o formato python sem usar prefixo da data.



```python
#import os
#os.system('jupyter-nbconvert --to python jupyter.ipynb')
```


```python
#--stdout
#--TemplateExporter.exclude_input_prompt=True'
```


```python
!jupyter-nbconvert jupyter.ipynb\
--to markdown\
--TagRemovePreprocessor.enabled=True\
--ClearOutputPreprocessor.enabled=True\
--TemplateExporter.exclude_markdown=False\
--TemplateExporter.exclude_code_cell=True\
--TemplateExporter.exclude_output=True\
--TemplateExporter.exclude_raw=False\
--TemplateExporter.exclude_input_prompt=True\
--TagRemovePreprocessor.remove_cell_tags='["remove_cell"]'\
--output Teste
```

    [NbConvertApp] Converting notebook jupyter.ipynb to markdown
    [NbConvertApp] Writing 1710 bytes to Teste.md


Quero saber como exportar somente algumas células.
'https://stackoverflow.com/questions/57701538/jupyter-notebook-nbconvert-without-magic-commands-w-o-markdown


# GitHub


```python
import os
os.system('nbstripout --install --attributes .gitattributes')
```




    0




```python
!nbstripout --install --attributes .gitattributes
```


```python
%run '../codes/git/update_github.py'
```


```python
git_full('/home/michel/Geodata/SourceCode/package_jupyter', '.', 'Atualizando')
```

    b'' b''
    b'[master cbc3f02] Atualizando\n 7 files changed, 389 insertions(+), 319 deletions(-)\n create mode 100644 Teste.ipynb\n create mode 100644 Teste.pdf\n rewrite docs/jupyter.pdf (94%)\n' b''
    b'' b'To github.com:michelmetran/package_jupyter.git\n   cb45215..cbc3f02  master -> master\n'
    Done!!


# Outros

A partir do post [How to Git Jupyter Notebooks the Right Way](http://mateos.io/blog/jupyter-notebook-in-git), compreendi que é a partir da instalaçao do package _nbstripout_ que é possível fazer o git de arquivos _ipynb_.


# Requirements

O comando ```pip freeze``` é o mais difundido na internet para se obter os *requirements.txt*, ou seja, o arquivo com o qual é possível indicar quais os *packages* necessários para rodar um determinado *script*.


```python
pip freeze > requirements.txt
```

    Note: you may need to restart the kernel to use updated packages.


Tentei usar também o ```pipreqs```, porém ele não funciona em Juptyter Notebook.


```python
import pipreqs
```

eee


```python
conda env export > environment.yml
```

    
    Note: you may need to restart the kernel to use updated packages.



```python
import os
cwd = os.getcwd()
py = os.path.join(cwd, 'docs')
py
```




    '/media/Geodata/SourceCode/package_jupyter/docs'



# Erros

Em uma tentativa de exportar para pdf, tive problemas. Não exportava.

Descobri que é necessário ter o
'''sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended'''
ou
'''sudo apt-get install texlive-full'''

_nbconvert failed: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex._

# Referêcias

A partir do post <a title="Link do Folium" href="https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231" target="_blank">**_Jupyter Notebook Extensions_**</a>.

A partir do post <a title="Link do Folium" href="https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/" target="_blank">**_28 Jupyter Notebook Tips, Tricks, and Shortcuts_**</a>, 


A partir do post [Link do Folium](https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231)


```python

```
