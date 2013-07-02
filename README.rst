simple Gettext merge tool
~~~~~~~~~~~~~~~~~~~~~~~~~

:license: GPL2+ (in case of doubt, same as mercurial)
:copyright: 2013 by Ronny Pfannschmidt


This is a simple merge tool for gettext files with line number comments.
It extends Merge3Text from mercurial.simplemerge to just
return the local change for line number comment changes.

It's not yet smart about bigger changes.






Git usage
---------

::
  [mergetool "gettext"]
      name = gettext
      cmd = python $HG_MERGE_GETTEXT_CHECKOUT/mergegettext.py "$BASE" "$LOCAL" "$REMOTE" --store "$MERGED"
