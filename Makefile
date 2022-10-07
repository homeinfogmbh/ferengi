FILE_LIST = ./.installed_files.txt

.PHONY: pull push clean bindings install uninstall

default: | pull clean bindings install

bindings:
	#@ pyxbgen -u xsds/facebook.xsd -m dom --module-prefix=ferengi.facebook
	@ pyxbgen -u xsds/openligadb/openligadb.xsd -m dom --module-prefix=ferengi.openligadb
	@ pyxbgen -u xsds/weather.xsd -m dom --module-prefix=ferengi.openweathermap
	@ pyxbgen -u xsds/welt.xsd -m dom --module-prefix=ferengi.weltnews

install:
	@ ./setup.py install --record $(FILE_LIST)

uninstall:
	@ while read FILE; do echo "Removing: $$FILE"; rm "$$FILE"; done < $(FILE_LIST)

clean:
	@ rm -Rf ./build

pull:
	@ git pull

push:
	@ git push
