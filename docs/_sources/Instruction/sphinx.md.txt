### 注意事项
* 错误表现：deploy的网页没有正确的显示配置
    原因：Jekyll和sphinx的干扰
    处理方式：在docs文件夹中写入一个.nojekyll的文件
    - name: Create .nojekyll to avoid Jekyll processing
        run: |
          touch docs/.nojekyll
* Pages页面需要设置是将根目录或者是docs文件夹作为部署点，而sphinx编译的文件在build中
    处理方式：将build/html/*下的所有文件copy到docs/文件夹中
    - name: Deploy to GitHub Pages (docs folder)
        run: |
          mkdir -p docs
          cp -r build/html/* docs/
* 错误表现：ipynb遇到问题（没有title等）
    处理方式：修改conf.py文件，在下面的配置中不要写 .ipynb
    # 其他可能需要的配置
    source_suffix = ['.rst', '.md']
* 错误表现：编译错误，找不到文件等
    处理方式：检查build的命令，文件架构中，source文件夹和.github同一层级
    - name: Build Sphinx Docs
        run: |
          sphinx-build -b html source build/html
* 本地编写了之后，远程提交之后因为Pages和Action中修改了html文件。因此本地提交的build文件不是最新的，需要先pull下来，merge然后再提交。
git fetch origin 
git merge origin/main  
git add .                 
git commit
git push origin main  