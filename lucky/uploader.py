import subprocess
import json
import requests
import os

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

    @staticmethod
    def upload_to_pgyer(config_path, target_name):
        with open(config_path, 'r') as f:
            config = json.load(f)

        ipa_path = f"./build/{config['targets'][target_name]['scheme']}.ipa"
        pgy_api_key = config.get("pgy_api_key", "")

        if not pgy_api_key:
            print("Error: Missing Pgyer API key in config.")
            return

        if not os.path.exists(ipa_path):
            print(f"Error: IPA file does not exist at path {ipa_path}")
            return

        # Step 1: Get COS Token
        try:
            print("Fetching COS Token...")
            get_token_url = "https://www.pgyer.com/apiv2/app/getCOSToken"
            headers = {"enctype": "multipart/form-data"}
            data = {"_api_key": pgy_api_key, "buildType": "ios"}
            token_response = requests.post(get_token_url, data=data, headers=headers)
            if token_response.status_code != 200 or token_response.json().get("code") != 0:
                print(f"Failed to fetch COS Token: {token_response.json().get('message', 'Unknown error')}")
                return

            token_data = token_response.json().get("data", {})
            endpoint = token_data["endpoint"]
            upload_params = token_data["params"]
        except Exception as e:
            print(f"Error fetching COS Token: {e}")
            return

        # Step 2: Upload to COS
        try:
            print("Uploading file to COS...")
            with open(ipa_path, 'rb') as ipa_file:
                files = {"file": ipa_file}
                cos_response = requests.post(endpoint, data=upload_params, files=files, headers=headers)
                if cos_response.status_code != 204:  # COS 上传成功的状态码是 204
                    print(f"Failed to upload file to COS: {cos_response.text}")
                    return
                else:
                    print(f"Successfully uploaded to Pgyer.")
        except Exception as e:
            print(f"Error uploading to COS: {e}")
            return
