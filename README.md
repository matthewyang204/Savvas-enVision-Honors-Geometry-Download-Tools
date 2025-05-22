# Savvas enVision Algebra 1 Textbook Download Tools
This is a set of scripts to show how easy it is to download the enVision Algebra 1 from Savvas as of March 21, 2025.

# Requirements
- Python 3.4-3.12
- wget
- all in requirements.txt - use `pip3 install -r requirements.txt` to install

# Steps to use
1. Open `https://assets.savvas.com/file-vault/flipbooks/floridareview/math/enV_FL_2020_SE_A1/html/html5forpc.html?page=0` in a web browser.
2. Click through all the pages until you reach all 658 pages.
3. Leave the page open in the web browser.
4. Clone the repo and `cd` into it
5. Run `./get` to download all images
6. `cd` into pages and then run `python3 ../buildpdf.py`.
7. Retrieve the result, a pdf at `new1.pdf` in the `pages` folder
