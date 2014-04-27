NAME=CV_Attila_Nagy
all: build

view:
	mupdf $(NAME).pdf

build:
	texi2pdf $(NAME).tex
	rm $(NAME).{aux,log}

clean:
	rm $(NAME).{aux,log,pdf}
