nuitka --no-cache --mingw64 --show-progress --standalone --enable-plugin=pyside6 --onefile --remove-output --lto -optimize=2 app.py 
nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --onefile --remove-output --lto app.py
nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --onefile --remove-output --optimize=2 app.py
nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --onefile --lto=yes --onefile-tempdir-spec="%TEMP%" --remove-output --include-data-file=cfg.yaml=cfg.yaml --include-data-file=rule.db=sqlite.db app.py

nuitka  --mingw64 --show-progress --standalone --enable-plugin=pyside6 --onefile --lto=yes --onefile-tempdir-spec="%TEMP%" --remove-output --include-data-file=cfg.yaml=cfg.yaml --include-data-file=rule.db=sqlite.db app.py
.idea 文件夹的内容不会被打包或跟踪，cfg.yaml 和 rule.db 文件也不会被打包到可执行文件中，而是可以放在可执行文件所在的目录中并通过相对路径访问。
nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --onefile --lto=yes --onefile-tempdir-spec="%TEMP%" --remove-output --nofollow-import-to=.idea app.py


nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --onefile --lto=yes --remove-output app.py

nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --onefile --lto=yes --remove-output --no-cache app.py


nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --onefile --remove-output --lto -optimize=2 app.py 

nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --plugin-enable=pandas --onefile --remove-output --lto --optimize=2 app.py
使用peewee， 排除sqlalchemy 

nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --exclude-package=sqlalchemy --onefile --remove-output --lto --optimize=2 app.py

nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 --lto=yes app.py

nuitka --mingw64 --show-progress --standalone --enable-plugin=pyside6 app.py

nuitka --standalone --windows-disable-console --mingw64 --nofollow-imports --show-memory --show-progress --plugin-enable=qt-plugins --include-qt-plugins=sensible,styles --follow-import-to=need --output-dir=o 你的.py

--include-module=PySide6.QtWidgets --include-module=PySide6.QtGui --include-module=PySide6.QtCore \

python -m nuitka --mingw64 --standalone --enable-plugin=pyside6 --show-progress --output-dir=dist --follow-imports --assume-yes-for-downloads --include-qt-plugins=sensible,qml,styles app.py

python -m nuitka --output-dir=app --mingw64 --lto=yes --standalone --enable-plugin=pyside6 --show-progress --follow-imports --assume-yes-for-downloads --include-qt-plugins=sensible,qml,styles,sqldrivers --nofollow-import-to=scipy app.py

单个文件
python -m nuitka --onefile --output-dir=app --mingw64 --lto=yes --standalone --enable-plugin=pyside6 --show-progress --follow-imports --assume-yes-for-downloads --include-qt-plugins=sensible,qml,styles,sqldrivers --nofollow-import-to=scipy app.py

nuitka --standalone --remove-output --exclude-module=pandas.io.clipboard,pandas.plotting app.py

图标
python -m nuitka --onefile --output-dir=app --mingw64 --lto=yes --enable-plugin=pyside6 --show-progress --follow-imports --assume-yes-for-downloads --include-qt-plugins=sensible,qml,styles,sqldrivers --windows-icon-from-ico=./resource/logo.png app.py

无console，打包package
python -m nuitka --company-name=COMPANY_NAME --onefile --output-dir=app --mingw64 --lto=yes --enable-plugin=pyside6 --show-progress --follow-imports --assume-yes-for-downloads --include-qt-plugins=sensible,qml,styles,sqldrivers --windows-icon-from-ico=./resource/logo.png app.py

python -m nuitka --config-file=nuitka.cfg app.py

添加信息
python -m nuitka --onefile --output-dir=app --mingw64 --lto=yes --enable-plugin=pyside6 --show-progress --show-memory --follow-imports --assume-yes-for-downloads --include-qt-plugins=sensible,qml,styles,sqldrivers --windows-icon-from-ico=.\resource\logo.png --company-name="小岚岚有限公司" --product-name="IT Tools" --file-version=2.3.0.0 --product-version=2.3.0.0 --file-description="IT Tools by 小岚岚 hikari021004@gmail.com" --copyright="© 2024 Hikari" --trademarks="Hikari Trademark" --nofollow-import-to=numpy app.py


--windows-disable-console
--include-package-data=PySide6
--follow-import-to=need
--include-qt-plugins=sensible,qml,styles,sqldrivers
--mingw64 #默认为已经安装的vs2017去编译，否则就按指定的比如mingw(官方建议)
--standalone 独立环境，这是必须的(否则拷给别人无法使用)
--windows-disable-console 没有CMD控制窗口
--output-dir=out 生成exe到out文件夹下面去
--show-progress 显示编译的进度，很直观
--show-memory 显示内存的占用
--enable-plugin=pyside6
--plugin-enable=tk-inter 打包tkinter模块的刚需
--plugin-enable=numpy 打包numpy,pandas,matplotlib模块的刚需
--plugin-enable=torch 打包pytorch的刚需
--plugin-enable=tensorflow 打包tensorflow的刚需
--windows-icon-from-ico=./resource/logo.png
--windows-company-name=Windows下软件公司信息
--windows-uac-admin=Windows下用户可以使用管理员权限来安装
--linux-onefile-icon=Linux下的图标位置
--onefile 像pyinstaller一样打包成单个exe文件(2021年我会再出教程来解释)
--include-package=复制比如numpy,PyQt5 这些带文件夹的叫包或者轮子
--include-module=复制比如when.py 这些以.py结尾的叫模块