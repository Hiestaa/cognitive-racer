# -*- coding: utf8 -*-

from conf import conf
from _en import en
from _fr import fr

labels = {
	'en': en,
	'fr': fr
}


def i18n(label):
	"""
	Returns the translated label.
	label -- name of the label to translate. It should have the syntax:
			 `cat/subcat/subsubcat/[...]/name`. See one of the language
			 file to see the tree structure.
	"""
	arb = label.split('/')
	translated = labels[conf['resources']['language']]
	for next in arb:
		if next in translated:
			translated = translated[next]
		else:
			translated = ("UNTRANSLATED: lang=%s: label=%s" 
					% (conf['resources']['language'], label))
			break
	return translated