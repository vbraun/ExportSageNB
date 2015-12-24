
tox:
	tox

watch-%:
	while true ; do \
	    $(MAKE) $* ; \
	    inotifywait -e close_write -r . --exclude '.*~' --exclude '#.*' ; \
	done

.PHONY: tox
