#!/usr/bin/env python
# coding: utf-8

# # Introdução
# 
# A partir do post <a title="Link do Folium" href="http://mateos.io/blog/jupyter-notebook-in-git/" target="_blank">**_How to Git Jupyter Notebooks the Right Way_**</a>, compreendi que é a partir da instalaçao do package _nbstripout_ que é possível fazer o git de arquivos _ipynb_.
# 
# 
# Em uma tentativa de exportar para pdf, tive problemas. Não exportava.
# 
# Descobri que é necessário ter o
# sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended
# ou
# sudo apt-get install texlive-full
# 
# 
# _nbconvert failed: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex._

# # Get *Jupyter Notebook* filename
# 
# https://stackoverflow.com/questions/12544056/how-do-i-get-the-current-ipython-jupyter-notebook-name

# In[17]:


get_ipython().run_line_magic('run', "'../codes/files/create_folders.py'")

create_folders('', folders=['docs'])


# In[2]:


get_ipython().run_cell_magic('javascript', '', '\nvar kernel = IPython.notebook.kernel;\nvar body = document.body, attribs = body.attributes;\nvar command = \'ipynb_filename = \' + \'"\'+attribs[\'data-notebook-name\'].value+\'"\';\nkernel.execute(command);')


# In[3]:


ipynb_filename


# In[4]:


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

    display(Javascript('IPython.notebook.kernel.execute("theNotebook = " +     "\'"+IPython.notebook.notebook_name+"\'");'))

    # Result
    return theNotebook


# In[22]:


#get_jupyternotebook_name()


# In[6]:


get_ipython().run_cell_magic('javascript', '', '\nvar kernel = IPython.notebook.kernel;\nvar nb = IPython.notebook;\nvar command = \'ipynb_pathname = "\' + nb.base_url + nb.notebook_path + \'"\';\nkernel.execute(command);')


# In[7]:


ipynb_pathname


# # Export

# In[18]:


get_ipython().run_line_magic('run', "'../codes/files/export_jupyter.py'")

export_jupyter(ipynb_filename, 'docs', ['html', 'markdown', 'pdf', 'python'], False)


# Quero saber como exportar somente algumas células.
# 'https://stackoverflow.com/questions/57701538/jupyter-notebook-nbconvert-without-magic-commands-w-o-markdown
# 

# # GitHub

# In[19]:


get_ipython().run_line_magic('run', "'../codes/git/update_github.py'")


# In[20]:


git_full('/home/michel/Geodata/SourceCode/package_jupyter', '.', 'Atualizando')


# # Outros

# In[ ]:


import os
os.system('jupyter-nbconvert --to python jupyter.ipynb --stdout --TemplateExporter.exclude_input_prompt=True')


# In[21]:


import os
os.system('nbstripout --install --attributes .gitattributes')


# # Referêcias
# A partir do post <a title="Link do Folium" href="https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231" target="_blank">**_Jupyter Notebook Extensions_**</a>.
# 
# A partir do post <a title="Link do Folium" href="https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/" target="_blank">**_28 Jupyter Notebook Tips, Tricks, and Shortcuts_**</a>, 
