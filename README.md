
安装kivy：
下载kivy3.dmg拷贝kivy3.app到应用程序目录，改名kivy.app

建立 kivy.app 终端关联

ln -s /Applications/Kivy.app/Contents/Resources/script  /usr/local/bin/kivy

使用brew安装ta-lib库和mongodb：brew.sh去参考
安装brew管理：
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

安装talib库：
brew install ta-lib

安装mongodb数据库服务器环境：
brew install mongodb

开启终端安装配置环境
kivy后输入import kivy测试kivy环境是否正常。正常后下面配置

终端kivy环境配置：
kivy -m pip install -r kivy-m_pip_freeze.txt

kivy -m jupyter notebook 或 kivy -m jupyterlab进入web后开启终端

web终端虚拟环境python配置：
python -m pip install -r python-m_pip_freeze.txt

web终端环境配置：
pip install -r pip_freeze.txt
