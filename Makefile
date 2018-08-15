FILE_LIST = ./.installed_files.txt

.PHONY: pull push clean generate-bindings install uninstall

default: | pull clean generate-bindings install

generate-bindings:
	@ pyxbgen -u xsds/weather.xsd -m dom --module-prefix=ferengi.openweathermap

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
