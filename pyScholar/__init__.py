from scholar import searchAuthor,Author

"""
pyScholar
Fetch author information from Google scholar

Originally forked from:
https://github.com/lbello/chalmers-web/commit/73bd99aef6ba0310d393c66e4fc3bce9e40e6bf5

At the moment, the module is mainly focus in authors information (aka
citations).

Search for authors (e.g. called "Bello" working for "Chalmers University"):
 >>> import scholar
 >>> l=scholar.searchAuthor('Bello Chalmers').next()
 >>> l.name
 <<< u'Luciano Bello'

Fetch all the information of an author:
 >>> l.fillIn()
 >>> l.affiliation
 <<< u'PhD Student of Computer Science, Chalmers University of Technology'

Get an author by id:
 >>> b=scholar.Author('L9Rk-_sAAAAJ')
 >>> b.fillIn()
 >>> b.citationIndex.all
 <<< 15
"""
__version__=  '0.1'