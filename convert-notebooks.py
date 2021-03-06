from pathlib import Path
import re 
from subprocess import run
from shutil import rmtree


def convert(notebook_file):
    notebook = Path(notebook_file)
    name = notebook.stem
    blog_root = Path("content/blog/")
    if not blog_root.is_dir():
        blog_root.mkdir()
    dest_dir = blog_root / name
    files_dir = notebook.with_name(notebook.stem + "_files")

    if dest_dir.is_dir():
        print(f"Rebuilding {dest_dir}")
        rmtree(dest_dir)
        
    run(["jupyter", "nbconvert", str(notebook), "--to", "markdown"])


    print(files_dir)

    if files_dir.is_dir():
        files_dir.replace(dest_dir)
    else:
        dest_dir.mkdir()

    md_path = notebook.with_suffix(".md")
    md = md_path.read_text()
    yaml = notebook.with_suffix(".yml").read_text()

    output_text = "\n".join(["---", yaml, "---", md])
    replaced = output_text.replace(f"![png]({name}_files/", "![png](")
    (dest_dir / "index.md").write_text(replaced)
    md_path.unlink()
    

if __name__ == "__main__":
    notebook_path = Path() / "notebooks"
    for notebook in notebook_path.glob("*.ipynb"):
        print(f"Converting {notebook}")
        convert(notebook)