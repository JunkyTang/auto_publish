import subprocess
import json

class Uploader:
    @staticmethod
    def upload_to_appstore(config_path, target_name):
        with open(config_path, 'r') as f:
            config = json.load(f)

        ipa_path = f"./build/{config['targets'][target_name]['scheme']}.ipa"

        try:
            subprocess.run(
                [
                    "xcrun",
                    "altool",
                    "--upload-app",
                    "-f", ipa_path,
                    "--type", "ios",
                    "--asc-provider", config.get("asc_provider", ""),  # 可选 ASC Provider
                ],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"App Store upload failed: {e}")
            raise