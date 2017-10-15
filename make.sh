!/bin/bash
$pdf_previewer = 'start okular';
latexmk -pvc -f -pdf -jobname=Rulebook Rulebook.tex
latexmk -c 