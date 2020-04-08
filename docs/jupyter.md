# Introdução

A partir do post <a title="Link do Folium" href="http://mateos.io/blog/jupyter-notebook-in-git/" target="_blank">**_How to Git Jupyter Notebooks the Right Way_**</a>, compreendi que é a partir da instalaçao do package _nbstripout_ que é possível fazer o git de arquivos _ipynb_.


Em uma tentativa de exportar para pdf, tive problemas. Não exportava.

Descobri que é necessário ter o
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended
ou
sudo apt-get install texlive-full


_nbconvert failed: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex._

# Get *Jupyter Notebook* filename

https://stackoverflow.com/questions/12544056/how-do-i-get-the-current-ipython-jupyter-notebook-name


```python
%run '../codes/files/create_folders.py'
```


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
# %load '../codes/files/get_jupyternotebook_name.py'
def get_jupyternotebook_name():
    """
    Returns the name of the current notebook as a string
    From https://mail.scipy.org/pipermail/ipython-dev/2014-June/014096.html
    :return: Returns the name of the current notebook as a string
    """
    # Import Packages
    from IPython.core.display import Javascript
    from IPython.display import display

    display(Javascript('IPython.notebook.kernel.execute("theNotebook = " + \
    "\'"+IPython.notebook.notebook_name+"\'");'))

    # Result
    return theNotebook

```


```python
get_jupyternotebook_name()
```


    <IPython.core.display.Javascript object>



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-0fd729895b36> in <module>
    ----> 1 get_jupyternotebook_name()
    

    <ipython-input-4-440559a4d7cf> in get_jupyternotebook_name()
         14 
         15     # Result
    ---> 16     return theNotebook
    

    NameError: name 'theNotebook' is not defined



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

export_jupyter(ipynb_filename, '', ['html', 'markdown', 'pdf', 'python'], False)
```

    Arquivo jupyter.ipynb exportado corretamente para o formato html sem usar prefixo da data.
    Arquivo jupyter.ipynb exportado corretamente para o formato markdown sem usar prefixo da data.
    Arquivo jupyter.ipynb exportado corretamente para o formato pdf sem usar prefixo da data.
    Arquivo jupyter.ipynb exportado corretamente para o formato python sem usar prefixo da data.


Quero saber como exportar somente algumas células.
'https://stackoverflow.com/questions/57701538/jupyter-notebook-nbconvert-without-magic-commands-w-o-markdown


# GitHub


```python
%run '../codes/git/update_github.py'
```


```python
git_full('/home/michel/Geodata/SourceCode/package_jupyter', '.', 'Atualizando')
```

    b'' b''
    b'[master 3b09637] Atualizando\n 1 file changed, 370 deletions(-)\n delete mode 100644 .ipynb_checkpoints/jupyter-checkpoint.ipynb\n' b''
    b'' b'To github.com:michelmetran/package_jupyter.git\n   19645a5..3b09637  master -> master\n'
    Done!!


# Outros


```python

```


```python
import os
os.system('jupyter-nbconvert --to python jupyter.ipynb --stdout --TemplateExporter.exclude_input_prompt=True')
```


```python
import os
os.system('nbstripout --install --attributes .gitattributes')
```


```python
!git add --all
!git commit -m "Initial commit"
!git push -u origin master
```

# Referêcias
A partir do post <a title="Link do Folium" href="https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231" target="_blank">**_Jupyter Notebook Extensions_**</a>.

A partir do post <a title="Link do Folium" href="https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/" target="_blank">**_28 Jupyter Notebook Tips, Tricks, and Shortcuts_**</a>, 
