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

## Rsync的阅读和理解：看 > 对应了命令
    Fri Jan 10 2025 22:34:36 GMT+0800 (香港标准时间) syncing
    > rsync -rlptzv --progress --exclude=.vscode --exclude=.git --exclude=*.DS_Store --exclude=*.vtk --exclude=*.safetensor --exclude=*.pvd --exclude=*.mat --exclude=*.vtu -ahH --bwlimit=40000000 --partial --out-format='[%t] [%i] (Last Modified: %M) (bytes: %-10l) %-100n' jiashhu@ws9:/home/jiashhu/HarmonicMapping/ /Users/liubocheng/Documents/2024/HamonicMap/ 
    rsync error: received SIGINT, SIGTERM, or SIGHUP (code 20) at /AppleInternal/Library/BuildRoots/d9889869-120b-11ee-b796-7a03568b17ac/Library/Caches/com.apple.xbs/Sources/rsync/rsync/rsync.c(244) [receiver=2.6.9]

这条命令是对比。
    Fri Jan 10 2025 22:38:31 GMT+0800 (香港标准时间) comparing
    > rsync -nrlptzv --progress --exclude=.vscode --exclude=.git --exclude=*.DS_Store --exclude=*.vtk --exclude=*.safetensor --exclude=*.pvd --exclude=*.mat --exclude=*.vtu -ahH --bwlimit=40000000 --partial --out-format='[%t] [%i] (Last Modified: %M) (bytes: %-10l) %-100n' jiashhu@ws9:/home/jiashhu/HarmonicMapping/ /Users/liubocheng/Documents/2024/HamonicMap/ 
    receiving file list ... 
    100 files...
    200 files...
    239 files to consider
    '[2025/01/10 22:38:39] [.d..t....] (Last Modified: 2025/01/06-21:22:26) (bytes: 4096      ) CollocationMethod/                                                                                  '
    '[2025/01/10 22:38:39] [.d..t....] (Last Modified: 2024/12/11-18:49:50) (bytes: 108       ) CollocationMethod/.ipynb_checkpoints/                                                               '

    sent 129 bytes  received 8.69K bytes  1.04K bytes/sec
    total size is 9.03M  speedup is 1024.01

如何更新
在实际运行 rsync 时（不使用 -n 选项），rsync 会根据这些标志执行相应的操作：

如果标志中有 >，文件将被复制或更新到目标位置。
如果标志中有 c，文件的属性将被更新。
如果标志中有 t，文件的时间戳将被更新。

## 第一条是Compare local to remote可以看到的。对应的是将本地文件同步到远程服务器
* 如果你看到[<f+++++++]，就说明这个文件在远程服务器上不存在，rsync将会把它从本地复制到远程。
* [2024/08/18 12:31:52] [cd+++++++]：表示目录在本地不存在，且需要创建该目录及其内容。
* [2024/08/18 12:31:52] [>f+++++++]：表示文件在本地不存在，且需要从远程复制该文件。
* [2024/08/18 12:31:51] [.d..t....]：表示目录结构在远程和本地相同，但其时间戳不同，所以需要更新时间戳。
* [2024/08/18 12:31:52] [>f.st....]：表示文件内容不同，同时时间戳和权限也不同，所以需要更新文件。
* [2024/08/18 12:31:52] [>f..t....]：表示文件内容相同，但时间戳不同，所以需要更新时间戳。
