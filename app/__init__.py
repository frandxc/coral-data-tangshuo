from flask import Flask

app = Flask(__name__)

# 其他初始化代码...
from app import routes
