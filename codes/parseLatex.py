import subprocess
import codes.parameters as pt

async def parseExpression(latexExpression):
    f = open('tex/expression.tex', 'w')
    f.write(f"""
\\documentclass[preview]{{standalone}}

\\usepackage[english]{{babel}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage{{lmodern}}
\\usepackage{{amsmath}}
\\usepackage{{amssymb}}
\\usepackage{{dsfont}}
\\usepackage{{setspace}}
\\usepackage{{tipa}}
\\usepackage{{relsize}}
\\usepackage{{textcomp}}
\\usepackage{{mathrsfs}}
\\usepackage{{calligra}}
\\usepackage{{wasysym}}
\\usepackage{{ragged2e}}
\\usepackage{{xcolor}}
\\usepackage{{framed}}
\\usepackage{{microtype}}
\\DisableLigatures{{encoding = *, family = * }}
\\linespread{{1}}
\\begin{{document}}

\\textcolor{{{pt.getTextcolour()}}}{{
""")
    f.close()
    f = open('tex/expression.tex', 'a')
    f.write(latexExpression)
    f.write(r"""
}
\end{document}
        """)
    f.close()
    bashCommand1 = "texliveonfly tex/expression.tex"
    bashCommand2 = "mv expression.pdf expression.aux expression.log expression.synctex.gz texput.log tex/"
    bashCommand3 = f"pdfcrop --margins {pt.getMargin()} tex/expression.pdf tex/expression.pdf"
    bashCommand4 = "dvisvgm --pdf --stdout tex/expression.pdf"
    bashCommand5 = f"inkscape --export-type=png --export-dpi={pt.getResolution()} --export-background-opacity={pt.getOpacity()} --export-background={pt.getBackgroundColour()} --export-filename=png/expression.png svg/expression.svg"
    process = subprocess.Popen(bashCommand1.split())
    output, error = process.communicate()
    process.terminate()
    print("Moving files...")
    process = subprocess.Popen(bashCommand2.split())
    output, error = process.communicate()
    process.terminate()
    print("Cropping pdf...")
    process = subprocess.Popen(bashCommand3.split())
    output, error = process.communicate()
    process.terminate()
    process = subprocess.Popen(bashCommand4.split(), stdout=open('svg/expression.svg', 'w'))
    output, error = process.communicate()
    process.terminate()
    process = subprocess.Popen(bashCommand5.split())
    output, error = process.communicate()
    process.terminate()