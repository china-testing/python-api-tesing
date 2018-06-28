===========================================
 ChainMap --- Search Multiple Dictionaries
===========================================

The ``ChainMap`` class manages a sequence of dictionaries, and
searches through them in the order they are given to find values
associated with keys. A ``ChainMap`` makes a good "context" container,
since it can be treated as a stack for which changes happen as the stack
grows, with these changes being discarded again as the stack shrinks.

Accessing Values
================

The ``ChainMap`` supports the same API as a regular dictionary
for accessing existing values.

.. literalinclude:: collections_chainmap_read.py
   :caption:
   :start-after: #end_pymotw_header

The child mappings are searched in the order they are passed to the
constructor, so the value reported for the key ``'c'`` comes from the
``a`` dictionary.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_chainmap_read.py'))
.. }}}

.. code-block:: none

	$ python3 collections_chainmap_read.py
	
	Individual Values
	a = A
	b = B
	c = C
	
	Keys = ['c', 'b', 'a']
	Values = ['C', 'B', 'A']
	
	Items:
	c = C
	b = B
	a = A
	
	"d" in m: False

.. {{{end}}}

Reordering
==========

The ``ChainMap`` stores the list of mappings over which it
searches in a list in its :attr:`maps` attribute. This list is mutable,
so it is possible to add new mappings directly or to change the order
of the elements to control lookup and update behavior.

.. literalinclude:: collections_chainmap_reorder.py
   :caption:
   :start-after: #end_pymotw_header

When the list of mappings is reversed, the value associated with
``'c'`` changes.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_chainmap_reorder.py'))
.. }}}

.. code-block:: none

	$ python3 collections_chainmap_reorder.py
	
	[{'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}]
	c = C
	
	[{'b': 'B', 'c': 'D'}, {'a': 'A', 'c': 'C'}]
	c = D

.. {{{end}}}

Updating Values
===============

A ``ChainMap`` does not cache the values in the child mappings.
Thus, if their contents are modified, the results are reflected when the
``ChainMap`` is accessed.

.. literalinclude:: collections_chainmap_update_behind.py
   :caption:
   :start-after: #end_pymotw_header

Changing the values associated with existing keys and adding new
elements works the same way.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_chainmap_update_behind.py'))
.. }}}

.. code-block:: none

	$ python3 collections_chainmap_update_behind.py
	
	Before: C
	After : E

.. {{{end}}}

It is also possible to set values through the ``ChainMap``
directly, although only the first mapping in the chain is actually
modified.

.. literalinclude:: collections_chainmap_update_directly.py
   :caption:
   :start-after: #end_pymotw_header

When the new value is stored using ``m``, the ``a`` mapping is
updated.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_chainmap_update_directly.py'))
.. }}}

.. code-block:: none

	$ python3 collections_chainmap_update_directly.py
	
	Before: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
	After : ChainMap({'a': 'A', 'c': 'E'}, {'b': 'B', 'c': 'D'})
	a: {'a': 'A', 'c': 'E'}

.. {{{end}}}

``ChainMap`` provides a convenience method for creating a new
instance with one extra mapping at the front of the :attr:`maps` list
to make it easy to avoid modifying the existing underlying data
structures.

.. literalinclude:: collections_chainmap_new_child.py
   :caption:
   :start-after: #end_pymotw_header

This stacking behavior is what makes it convenient to use ``ChainMap``
instances as template or application contexts. Specifically, it is
easy to add or update values in one iteration, then discard the
changes for the next iteration.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_chainmap_new_child.py', line_break_mode='wrap'))
.. }}}

.. code-block:: none

	$ python3 collections_chainmap_new_child.py
	
	m1 before: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
	m2 before: ChainMap({}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c':
	'D'})
	m1 after: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
	m2 after: ChainMap({'c': 'E'}, {'a': 'A', 'c': 'C'}, {'b': 'B',
	'c': 'D'})

.. {{{end}}}

For situations where the new context is known or built in advance, it
is also possible to pass a mapping to ``new_child()``.

.. literalinclude:: collections_chainmap_new_child_explicit.py
   :caption:
   :start-after: #end_pymotw_header

This is the equivalent of

.. code-block:: none

  m2 = collections.ChainMap(c, *m1.maps)

and produces

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_chainmap_new_child_explicit.py'))
.. }}}

.. code-block:: none

	$ python3 collections_chainmap_new_child_explicit.py
	
	m1["c"] = C
	m2["c"] = E

.. {{{end}}}

