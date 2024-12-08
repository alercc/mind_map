# Mind map from source-target tables (in Excel)

Python code that generates an interactive HTML mind map, based on a source-target table. The table must follow the Excel template provided.

## Installation

Simply download the `draw.py` and `template.xlsx` files to a local directory.

## Usage

1. Open `template.xlsx` and fill the "source" and "target" columns with text. Visually, these texts will be rendered as nodes, connected with arrows. Whenever you repeat the exact same text in either column, the program will interpret it as the very same node.
2. Rename the worksheet (within `template.xlsx`) with a customized name, for example `map1`. If you wish, create another map in another worksheet, with a different name (say, `map2`).
3. Open the bash terminal in `my_dir` and issue the command
```bash
python c/path/to/my_dir/draw.py template.xlsx
```
As a result, there will be HTML files saved to `my_dir`. They will be as many as the number of worksheets you created in `template.xlsx`.
