# llm-backend

## 准备环境
### Python 环境
1. 安装 [anaconda](https://www.anaconda.com/download)（Python版 nvm）
2. `conda create -n reaio python=3.10`
3. `conda activate reaio`
4. 项目根目录下：`pip install -r requirements.txt`

### OpenAI api key
1. `echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc`
2. `source ~/.zshrc`
3. 检查一下：`echo $OPENAI_API_KEY`

## 运行
`flask run -p 3002 --debug`
