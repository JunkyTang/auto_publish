import subprocess
import json

class Builder:
    @staticmethod
    def build_project(config_path, target_name, configuration="release"):
        with open(config_path, 'r') as f:
            config = json.load(f)

        workspace_path = config.get('workspace_path')
        scheme = config['targets'][target_name]['scheme']
        export_options_path = config['export_options']

        # 根据输入选择配置
        build_config = "Release" if configuration.lower() == "release" else "Debug"

        try:
            # Archive 阶段
            subprocess.run(
                [
                    "xcodebuild",
                    "-workspace", workspace_path,
                    "-scheme", scheme,
                    "-configuration", build_config,  # 添加配置
                    "-archivePath", f"{scheme}.xcarchive",
                    "archive"
                ],
                check=True
            )
            # 导出 IPA 阶段
            subprocess.run(
                [
                    "xcodebuild",
                    "-exportArchive",
                    "-archivePath", f"{scheme}.xcarchive",
                    "-exportPath", "./build",
                    "-exportOptionsPlist", export_options_path
                ],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Build failed: {e}")
            raise