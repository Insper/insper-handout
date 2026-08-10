from importlib import resources
from pathlib import Path
import argparse
import shutil
import subprocess
import sys
import time


ASSET_FILES = {
    "InsperTemplate.tex": "",
    "InsperTemplate.html": "",
    "logo.pdf": "",
    "logo.png": "",
    "cabecalho.png": "",
    "box.lua": "",
    "include.py": "filters",
    "pandoc-svg.py": "filters",
    "filterBox.py": "filters",
}


def install_runtime_assets(script_home):
    script_home = Path(script_home)
    package_files = resources.files("data_files")

    for filename, subdir in ASSET_FILES.items():
        destination_dir = script_home / subdir
        destination_dir.mkdir(parents=True, exist_ok=True)
        destination = destination_dir / filename

        if not destination.exists():
            source = package_files / filename
            with resources.as_file(source) as source_path:
                shutil.copy2(source_path, destination)


def check_pandoc_version():
    try:
        resp = subprocess.run(
            ["pandoc", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except FileNotFoundError:
        print("pandoc not found. Install pandoc before running insper_handout.py.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        print(exc.stderr or "Could not run pandoc --version.", file=sys.stderr)
        sys.exit(exc.returncode)

    first_line = resp.stdout.splitlines()[0]
    version = int(first_line.split(" ")[1].split(".")[0])
    if version < 2:
        return "latex-engine"
    return "pdf-engine"


def build_pandoc_command(arguments, name, script_home, pdf_engine):
    script_home = Path(script_home)

    if arguments.format == "latex":
        if not name.endswith(".pdf"):
            name += ".pdf"
        return [
            "pandoc",
            "-f",
            "markdown+tex_math_double_backslash+fenced_divs",
            "-t",
            "latex",
            "-o",
            name,
            arguments.filename,
            f"--data-dir={script_home}",
            "--filter",
            "include.py",
            "--filter",
            "filterBox.py",
            f"--lua-filter={script_home / 'box.lua'}",
            f"--variable=logo={script_home / 'logo.pdf'}",
            f"--variable=header={script_home / 'cabecalho.png'}",
            "--template",
            str(script_home / "InsperTemplate.tex"),
            f"--{pdf_engine}=xelatex",
        ]

    if arguments.format == "html":
        if not name.endswith(".html"):
            name += ".html"
        return [
            "pandoc",
            "-f",
            "markdown+tex_math_double_backslash+fenced_divs",
            "-s",
            "--self-contained",
            "-o",
            name,
            arguments.filename,
            f"--data-dir={script_home}",
            "--filter",
            "include.py",
            "--filter",
            "filterBox.py",
            f"--lua-filter={script_home / 'box.lua'}",
            "--template",
            str(script_home / "InsperTemplate.html"),
        ]

    if arguments.format == "tex":
        if not name.endswith(".tex"):
            name += ".tex"
        return [
            "pandoc",
            "-f",
            "markdown+tex_math_double_backslash+fenced_divs",
            "-t",
            "latex",
            "-o",
            name,
            arguments.filename,
            f"--data-dir={script_home}",
            "--filter",
            "include.py",
            "--filter",
            "filterBox.py",
            f"--lua-filter={script_home / 'box.lua'}",
            f"--variable=logo={script_home / 'logo.pdf'}",
            f"--variable=header={script_home / 'cabecalho.png'}",
            "--template",
            str(script_home / "InsperTemplate.tex"),
        ]

    print("Unknown format:", arguments.format, file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(prog="Insper Handout")
    parser.add_argument("filename")
    parser.add_argument("--format", action="store", default="latex")
    parser.add_argument("--output", action="store", default=None)
    parser.add_argument("-c", "--continuous", action="store_true", default=False)

    arguments = parser.parse_args()
    name = Path(arguments.filename).with_suffix("").as_posix()
    if arguments.output is not None:
        name = arguments.output

    script_home = Path.home() / ".insper_handout"
    install_runtime_assets(script_home)

    pdf_engine = check_pandoc_version()
    cmd_line = build_pandoc_command(arguments, name, script_home, pdf_engine)

    if not arguments.continuous:
        return subprocess.run(cmd_line).returncode

    while True:
        subprocess.run(cmd_line)
        time.sleep(1)


if __name__ == "__main__":
    sys.exit(main())
