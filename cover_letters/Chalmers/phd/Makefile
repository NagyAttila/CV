NAME=main
PDF=$(NAME).pdf
all: build update

view:
	mupdf $(PDF)

build:
	texi2pdf --clean $(NAME).tex

update:
	exec kill -SIGHUP `pgrep mupdf`

