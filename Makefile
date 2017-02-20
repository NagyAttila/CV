NAME=CV_Attila_Nagy_simple
PDF=$(NAME).pdf
all: build update

view:
	mupdf $(PDF)

build:
	texi2pdf $(NAME).tex
	rm $(NAME).{aux,log}

update:
	exec kill -SIGHUP `pgrep mupdf`

clean:
	rm $(NAME).{aux,log,pdf}
