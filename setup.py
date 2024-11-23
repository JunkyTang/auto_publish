from setuptools import setup, find_packages

setup(
    name="Lucky",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "git+https://github.com/yourusername/Lucky.git@v0.1.0#egg=Lucky",
    ],
    entry_points={
        "console_scripts": [
            "lucky-build=Lucky.builder:main",
            "lucky-upload=Lucky.uploader:main"
        ]
    },
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