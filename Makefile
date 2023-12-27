collect_translations:
	 pygettext3.11 -d base -o locales/base.pot handlers/*

mo:
	msgfmt -o locales/uz/LC_MESSAGES/base.mo locales/uz/LC_MESSAGES/base
	msgfmt -o locales/ru/LC_MESSAGES/base.mo locales/ru/LC_MESSAGES/base
