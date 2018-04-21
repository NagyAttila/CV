NAME=CV_Attila_Nagy
PDF=$(NAME).pdf
all: build update clean

view:
	mupdf $(PDF)

build:
	texi2pdf $(NAME).tex

update:
	exec kill -SIGHUP `pgrep mupdf`

clean:
	rm $(NAME).{aux,log}
