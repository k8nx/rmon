
init:
	bower install
	cd rmon/assets/components/bootstrap && npm install recess && make bootstrap-css
	mkdir rmon/assets/libs
	cp -r rmon/assets/components/* rmon/assets/libs
	rm -rf rmon/assets/libs/bootstrap
	cp -r rmon/assets/components/bootstrap/bootstrap rmon/assets/libs/bootstrap

clean:
	rm -r bootstrap
