# plotblock (Under development)

Python tool to make latex code of block diagrams and render it into PDF and PNG. This tool is available for use under the MIT license.

# Installation

# Usage Example

Running the code shown below generate [this](tmp/latex.pdf) file

```
from block import Block

block = Block()
block.add_text('Hello World!')
block.convert_pdf()
```
