from setuptools import setup, find_packages

setup(
    name="lucky",
    version="0.1.5",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="lucky",
    author_email="Luck@where.com",  # 作者邮箱
    description="A short description of your package",  # 包的简短描述
    long_description="A long description of your package",  # 包的详细描述
    long_description_content_type="README.md",  # 描述格式，支持 reStructuredText、Markdown 等
    url="https://github.com/JunkyTang/auto_publish",  # 包的主页或 GitHub 地址
    classifiers=[  # 用于分类包的类别标签（用于 PyPI）
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',  # 指定支持的 Python 版本
    entry_points={
        "console_scripts": [
            "lucky=lucky.cli:main",  # 这将使得 'lucky' 命令触发 cli.py 中的 main 函数
        ]
    }

    # include_package_data=True,  # 如果你有额外的文件（如图片、配置文件等）需要包含在包内
    # package_data={  # 通过包的目录结构来指定额外的文件
    #     'your_package': ['data/*.dat'],
    # },
    # zip_safe=False,  # 如果你的包是纯 Python 包，可以设置为 True


)



# {
#     "project_path": "path/to/your/ios_project.xcodeproj",
#     "export_options": "path/to/exportOptions.plist",
#     "pgy_api_key": "your_pgyer_api_key",
#     "asc_provider": "your_team_id_here",  // 这里填写你的 Team ID
#     "targets": {
#         "Target1": {
#             "scheme": "Target1Scheme"
#         },
#         "Target2": {
#             "scheme": "Target2Scheme"
#         }
#     }
# }


# lucky build config.json Target1 --env release
# lucky upload config.json Target1 --platform pgy
# lucky upload config.json Target1 --platform appstore
