.. _OrderedDict:

===================================================================
 OrderedDict --- Remember the Order Keys are Added to a Dictionary
===================================================================

An ``OrderedDict`` is a dictionary subclass that remembers the
order in which its contents are added.

.. literalinclude:: collections_ordereddict_iter.py
   :caption:
   :start-after: #end_pymotw_header

Before Python 3.6 a regular ``dict`` did not track the insertion order, and
iterating over it produced the values in order based on how the keys
are stored in the hash table, which is in turn influenced by a random
value to reduce collisions.  In an ``OrderedDict``, by contrast,
the order in which the items are inserted is remembered and used when creating
an iterator.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_ordereddict_iter.py',
..                    interpreter='python3.5'))
.. }}}

.. code-block:: none

	$ python3.5 collections_ordereddict_iter.py
	
	Regular dictionary:
	c C
	b B
	a A
	
	OrderedDict:
	a A
	b B
	c C

.. {{{end}}}

Under Python 3.6, the built-in ``dict`` does track insertion order,
although this behavior is a side-effect of an implementation change
and should not be relied on.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_ordereddict_iter.py',
..                    interpreter='python3.6'))
.. }}}

.. code-block:: none

	$ python3.6 collections_ordereddict_iter.py
	
	Regular dictionary:
	a A
	b B
	c C
	
	OrderedDict:
	a A
	b B
	c C

.. {{{end}}}

Equality
========

A regular ``dict`` looks at its contents when testing for equality.
An ``OrderedDict`` also considers the order in which the items were
added.

.. literalinclude:: collections_ordereddict_equality.py
   :caption:
   :start-after: #end_pymotw_header

In this case, since the two ordered dictionaries are created from
values in a different order, they are considered to be different.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_ordereddict_equality.py'))
.. }}}

.. code-block:: none

	$ python3 collections_ordereddict_equality.py
	
	dict       : True
	OrderedDict: False

.. {{{end}}}

Reordering
==========

It is possible to change the order of the keys in an
``OrderedDict`` by moving them to either the beginning or the end
of the sequence using ``move_to_end()``.

.. literalinclude:: collections_ordereddict_move_to_end.py
   :caption:
   :start-after: #end_pymotw_header

The ``last`` argument tells ``move_to_end()`` whether to move the
item to be the last item in the key sequence (when ``True``) or the
first (when ``False``).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_ordereddict_move_to_end.py'))
.. }}}

.. code-block:: none

	$ python3 collections_ordereddict_move_to_end.py
	
	Before:
	a A
	b B
	c C
	
	move_to_end():
	a A
	c C
	b B
	
	move_to_end(last=False):
	b B
	a A
	c C

.. {{{end}}}



.. seealso::

   * `PYTHONHASHSEED
     <https://docs.python.org/3.5/using/cmdline.html#envvar-PYTHONHASHSEED>`__
     -- Environment variable to control the random seed value added to
     the hash algorithm for key locations in the dictionary.
