# OCR Demo

以 Vue+ElementPlus作为前端，Django为后端集成 Paddle OCR模型; 实现 OCR 识别+敏感词检测

项目功能预览
- ✔️PaddleOCR 图片识别
- ✔️账号登录注册、及注销
- ✔️OCR 文本敏感词检测与过滤
- ✔️保留识别历史记录 并保存

## 项目启动流程 -- Django 端

python 3.9 以上

```bash
cd django-backen
```

- macOS 环境

```bash
brew install openssl swig mysql-client
```

- 创建虚拟环境(可选)

```bash
# 创建文件夹
mkdir venv

# 创建虚拟环境
python -m venv venv
```

- 安装 python 依赖

```bash
pip install -r requirements.txt
```

- 检查数据库迁移

```bash
# 请修改数据库配置，在 dlIntegrated/settings.py 文件中

python manage.py makemigrations
```

- 数据库迁移

```bash
python manage.py migrate
```

- 项目启动

```shell
python manage.py runserver
```


## 前端

首先需要确保你的电脑中安装了 nodeJs 18

```bash
cd vue-front
```

- 安装依赖

```bash
pnpm i
```
- 前端启动

```bash
pnpm serve
```
