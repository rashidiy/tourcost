collect_translations:
	 /usr/share/doc/python3.11/examples/i18n/pygettext.py -d base -o locales/base.pot handlers/*

mo:
	msgfmt -o locales/uz/LC_MESSAGES/base.mo locales/uz/LC_MESSAGES/base
	msgfmt -o locales/ru/LC_MESSAGES/base.mo locales/ru/LC_MESSAGES/base
