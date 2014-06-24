binary=build/douban.popclipextz
all_files=douban.popclipext/Config.plist \
		   douban.popclipext/douban.png  \
		   douban.popclipext/douban.py   \
		   douban.popclipext/douban.sh

$(binary): $(all_files)
	zip -r $(binary) douban.popclipext

install: $(binary)
	open -a popclip $(binary)
