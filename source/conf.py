# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = 'myresearch'
copyright = '2024, jiash'
author = 'jiash'
release = '0.1'

# Jupyter notebook 配置
nbsphinx_execute = 'never'  # 控制是否在构建时执行 Jupyter Notebook，可以设为 'always' 或 'never'

# 其他可能需要的配置
source_suffix = ['.rst', '.md']

# 扩展配置
extensions = [
    "nbsphinx",
    "myst_parser"
]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# conf.py
html_baseurl = 'https://<your-username>.github.io/<your-repository-name>/'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_use_index = True
html_domain_indices = True
    
# html_theme_options = {
#     "description": "A light, configurable Sphinx theme",
#     "github_user": "sphinx-doc",
#     "github_repo": "sphinx_rtd_theme",
#     "fixed_sidebar": True,
#     "github_banner": True,
# }
