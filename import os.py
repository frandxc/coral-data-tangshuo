import os

# 定义目录结构
structure = {
    'coral-data-tangshuo': {
        'app': ['__init__.py', 'routes.py', 'utils.py'],
        'static': ['styles.css'],
        'templates': ['index.html', 'visualize.html'],
        'data': [],
        'requirements.txt': None,
        'README.md': None,
        'run.py': None
    }
}

# 创建目录和文件
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                with open(os.path.join(path, file), 'w') as f:
                    pass
        else:
            with open(path, 'w') as f:
                pass

# 在当前目录下生成结构
create_structure('.', structure)

print("目录结构已生成。")