#!/usr/bin/env python


import subprocess


bib = {
    0: {
        "title": "Spaces Of Constant Curvature",
        "authors": ["Joseph A. Wolf"],
        "year": "1972",
        "doi": "10.1090/chel/372",
    },
    1: {
        "title": "A formula of Simons' type and hypersurfaces with constant mean curvature",
        "authors": ["Katsumi Nomizu", "Brian Smyth"],
        "year": "1969",
        "doi": "10.4310/jdg/1214429059",
    },
}


def getbib(doi):
    url = "https://api.crossref.org/works"
    app = "transform/application/x-bibtex"
    cmd = "curl -s {}/{}/{}".format(url, doi, app)
    bib = subprocess.check_output(cmd, shell=True)
    return bib.decode("utf-8")


def main():
    print("Writing bibliography to refs/main.bib.")
    with open("refs/main.bib", "w") as f:
        for i in [0, 1]:
            doi = bib[i]["doi"]
            print(getbib(doi), file=f)
    print("Done.")


if __name__ == "__main__":
    main()
