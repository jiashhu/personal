# 创建一个新的 Conda 环境并安装 Sphinx

# 创建一个新的 Conda 环境
conda create --name sphinx-env -y

# 激活新创建的环境
conda activate sphinx-env

# 在激活的环境中安装 Sphinx
conda install -c conda-forge sphinx -y

# 验证 Sphinx 是否安装成功
sphinx-build --version