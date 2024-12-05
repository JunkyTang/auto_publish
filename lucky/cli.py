import argparse
from lucky.builder import Builder
from lucky.uploader import Uploader


def main():
    parser = argparse.ArgumentParser(description="lucky iOS Build and Upload Tool")

    # 定义可选的子命令
    subparsers = parser.add_subparsers(dest="command")

    # 打包命令
    build_parser = subparsers.add_parser("build", help="Build the iOS project")
    build_parser.add_argument("config", help="Path to the config file")
    build_parser.add_argument("target", help="Target name to build")
    build_parser.add_argument("--env", choices=["release", "debug"], default="release",
                              help="Build environment (default: release)")

    # 上传命令
    upload_parser = subparsers.add_parser("upload", help="Upload the iOS project")
    upload_parser.add_argument("config", help="Path to the config file")
    upload_parser.add_argument("target", help="Target name to upload")
    upload_parser.add_argument("--platform", choices=["pgy", "appstore"], required=True,
                               help="Upload platform: pgy or appstore")

    args = parser.parse_args()

    # 根据命令执行操作
    if args.command == "build":
        Builder.build_project(args.config, args.target, args.env)
    elif args.command == "upload":
        if args.platform == "pgy":
            Uploader.upload_to_pgyer(args.config, args.target)
        elif args.platform == "appstore":
            Uploader.upload_to_appstore(args.config, args.target)


if __name__ == "__main__":
    main()