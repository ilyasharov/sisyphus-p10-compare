Sisyphus vs. P10 Package Comparison Tool

This tool compares the packages available in Sisyphus with those available in P10 for Alt Linux 10.
Requirements

    Alt Linux 10
    Python 3

Installation

    Clone this repository:

git clone https://github.com/user/sisyphus-p10-compare.git

    Install Python 3 and the json package:

sudo apt install python3 python3-json

Usage

    Run the following command to compare the packages:

python3 compare_packages_cli.py -p packages.json

    The output will be a JSON report with the following information:

    Missing in P10: List of packages that are in Sisyphus but not in P10.
    Missing in Sisyphus: List of packages that are in P10 but not in Sisyphus.
    Version mismatch: List of packages with different versions in Sisyphus and P10.

Notes

    The package lists for comparison are stored in the packages.json file.
    You can edit the packages.json file to add or remove packages from the comparison.
    The tool can be used to compare packages for different architectures.

