import argparse
import os
import zipfile
from pathlib import Path


def make_rel_archive(a_args):

    archive: zipfile = zipfile.ZipFile(a_args.name + ".zip", "w", zipfile.ZIP_DEFLATED)

    v_path: str = os.path.join(a_args.src_dir, "resources")
    for path in Path(v_path).rglob('*.png'):
        archive.write(path, os.path.join("SKSE/Plugins/resources/", path.relative_to(v_path)))

    archive.write(os.path.join(a_args.src_dir, "config", "LamasTinyHUD.ini"),
                  "MCM/Settings/LamasTinyHUD.ini")


def parse_arguments():
    parser = argparse.ArgumentParser(description="archive build artifacts for distribution")
    parser.add_argument("--name", type=str, help="the project name", required=True)
    parser.add_argument("--src-dir", type=str, help="the project root source directory", required=True)
    return parser.parse_args()


def main():
    out: str = "artifacts"
    try:
        os.mkdir(out)
    except FileExistsError:
        pass
    os.chdir(out)

    args = parse_arguments()
    make_rel_archive(args)


if __name__ == "__main__":
    main()
