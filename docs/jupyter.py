#!/usr/bin/env python
# coding: utf-8

# <h1>Sumário<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introdução" data-toc-modified-id="Introdução-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introdução</a></span></li><li><span><a href="#Get-Jupyter-Notebook-filename" data-toc-modified-id="Get-Jupyter-Notebook-filename-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Get <em>Jupyter Notebook</em> filename</a></span></li><li><span><a href="#Export" data-toc-modified-id="Export-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Export</a></span></li><li><span><a href="#GitHub" data-toc-modified-id="GitHub-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>GitHub</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Requirements</a></span></li><li><span><a href="#Erros" data-toc-modified-id="Erros-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Erros</a></span></li><li><span><a href="#Referêcias" data-toc-modified-id="Referêcias-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Referêcias</a></span></li></ul></div>

# # Introdução
# 
# O *Jupyter Notebook* é a maneira que optei para escrever os códigos na linguagem *Python*, visto que além de rodar os códigos, é possível:
# 1. Documentar os *scripts*, escrevendo o singnificado e objetivo de cada conjunto de comandos;
# 2. Atualizar os meus repositórios na plataforma **GitHub**;
# 3. Trabalhar com uma diversidade de opções de exportação do arquivo em formatos diversos, adaptados até mesmo para as simples leitura, como PDFs e Markdowns.
# 
# É no procesos de exportação dos arquivos que eu me ative nessa publicação, pois um dos objetivos de longo prazo que busco é exportar relatórios padronizados, para distribuição geral e irrestrita, ou seja, quero algo que não seja inteligível apenas por pessoas que conhecem de programação.
# 
# Para isso foram aqui apresentados um diversidade de opções para exportação de um arquivo *.ipynb*, sendo possível:
# - Incluir apenas campos determinados;
# - Incluir apenas as células que tenham determinada *tag*;
# - Incluir apenas as células de *markdown*;
# - Excluir as células de *outputs*.

# In[1]:


get_ipython().run_line_magic('run', "'../codes/files/create_folders.py'")

create_folders('', folders=['docs'])


# # Get *Jupyter Notebook* filename
# 
# https://stackoverflow.com/questions/12544056/how-do-i-get-the-current-ipython-jupyter-notebook-name

# In[51]:


get_ipython().run_cell_magic('javascript', '', '\nvar kernel = IPython.notebook.kernel;\nvar body = document.body, attribs = body.attributes;\nvar command = \'ipynb_filename = \' + \'"\'+attribs[\'data-notebook-name\'].value+\'"\';\nkernel.execute(command);')


# In[52]:


ipynb_filename


# In[53]:


#%run '../codes/files/get_jupyternotebook_name.py'


# In[54]:


#get_jupyternotebook_name()


# In[55]:


get_ipython().run_cell_magic('javascript', '', '\nvar kernel = IPython.notebook.kernel;\nvar nb = IPython.notebook;\nvar command = \'ipynb_pathname = "\' + nb.base_url + nb.notebook_path + \'"\';\nkernel.execute(command);')


# In[56]:


ipynb_pathname


# # Export

# In[57]:


get_ipython().run_line_magic('run', "'../codes/files/export_jupyter.py'")

export_jupyter(ipynb_filename, 'docs', ['html', 'markdown', 'pdf', 'python'], False)


# In[58]:


#import os
#os.system('jupyter-nbconvert --to python jupyter.ipynb')


# In[59]:


#--stdout
#--TemplateExporter.exclude_input_prompt=True'


# In[60]:


get_ipython().system('jupyter-nbconvert jupyter.ipynb--to markdown--TagRemovePreprocessor.enabled=True--ClearOutputPreprocessor.enabled=True--TemplateExporter.exclude_markdown=False--TemplateExporter.exclude_code_cell=True--TemplateExporter.exclude_output=True--TemplateExporter.exclude_raw=False--TemplateExporter.exclude_input_prompt=True--TagRemovePreprocessor.remove_cell_tags=\'["remove_cell"]\'--output Teste')


# Quero saber como exportar somente algumas células.
# 'https://stackoverflow.com/questions/57701538/jupyter-notebook-nbconvert-without-magic-commands-w-o-markdown
# 

# # GitHub
# 
# A partir do post [How to Git Jupyter Notebooks the Right Way](http://mateos.io/blog/jupyter-notebook-in-git), compreendi que é considerada como *best pratices* no git de projetos escritos em *Jupyter Notebook* a aplicação de um determinado código usando o package *nbstripout*, conforme segue. No vídeo [nbstripout: strip output from Jupyter and IPython notebooks](https://www.youtube.com/watch?v=BEMP4xacrVc) é explicado detalhadamente como o comando atua.

# In[74]:


import os
os.system('nbstripout --install --attributes .gitattributes')


# In[73]:


import nbstripout
nbstripout
get_ipython().system('nbstripout --install --attributes .gitattributes')


# Criei uma 

# In[64]:


get_ipython().run_line_magic('run', "'../codes/git/update_github.py'")
git_full('/home/michel/Geodata/SourceCode/package_jupyter', '.', 'Atualizando')


# # Requirements

# O comando ```pip freeze``` é o mais difundido na internet para se obter os *requirements.txt*, ou seja, o arquivo com o qual é possível indicar quais os *packages* necessários para rodar um determinado *script*.

# In[65]:


pip freeze > requirements.txt


# Tentei usar também o package ```pipreqs```, porém ele não funciona em *Juptyter Notebook*. Descobri ainda que o comando ``` conda env export > environment.yml``` pode auxiliar na criação destes parâmetros.

# # Erros
# 
# Em uma tentativa de exportar o *Jupyter Notebook* para PDF tive problemas. O arquivo não era exportado e apresentava a seguinte mensagem de erro:
# - *nbconvert failed: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex.*
# 
# Para solucionar, descobri que é necessário instalar, no Linux, akguns pacotes de aplicativos com os seguintes comandos:
# 
# ```sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended```     # Versão Compacta
# 
# ```sudo apt-get install texlive-full```      # Versão Completa

# # Referêcias
# 
# 
# [**Jupyter Notebook Extensions**](https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231)
# 
# 
# A partir do post [**28 Jupyter Notebook Tips, Tricks, and Shortcuts**](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts)
# 
# 
# A partir do post [Link do Folium](https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231)
