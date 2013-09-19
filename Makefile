all: build view

view:
	mupdf cv-plaincv-howtotex.pdf


build:
	texi2pdf cv-plaincv-howtotex.tex
	rm cv-plaincv-howtotex.{aux,log}


clean:
	rm cv-plaincv-howtotex.{aux,log,pdf}
