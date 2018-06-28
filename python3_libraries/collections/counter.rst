====================================
 Counter --- Count Hashable Objects
====================================

A ``Counter`` is a container that keeps track of how many times
equivalent values are added.  It can be used to implement the same
algorithms for which other languages commonly use bag or multiset data
structures.

Initializing
============

``Counter`` supports three forms of initialization.  Its
constructor can be called with a sequence of items, a dictionary
containing keys and counts, or using keyword arguments that map string
names to counts.

.. literalinclude:: collections_counter_init.py
   :caption:
   :start-after: #end_pymotw_header

The results of all three forms of initialization are the same.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_init.py'))
.. }}}

.. code-block:: none

	$ python3 collections_counter_init.py
	
	Counter({'b': 3, 'a': 2, 'c': 1})
	Counter({'b': 3, 'a': 2, 'c': 1})
	Counter({'b': 3, 'a': 2, 'c': 1})

.. {{{end}}}

An empty ``Counter`` can be constructed with no arguments and
populated via the ``update()`` method.

.. literalinclude:: collections_counter_update.py
   :caption:
   :start-after: #end_pymotw_header

The count values are increased based on the new data, rather than
replaced.  In the preceding example, the count for ``a`` goes from ``3`` to
``4``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_update.py'))
.. }}}

.. code-block:: none

	$ python3 collections_counter_update.py
	
	Initial : Counter()
	Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
	Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})

.. {{{end}}}

Accessing Counts
================

Once a ``Counter`` is populated, its values can be retrieved
using the dictionary API.

.. literalinclude:: collections_counter_get_values.py
   :caption:
   :start-after: #end_pymotw_header

``Counter`` does not raise ``KeyError`` for unknown items.
If a value has not been seen in the input (as with ``e`` in this
example), its count is ``0``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_get_values.py'))
.. }}}

.. code-block:: none

	$ python3 collections_counter_get_values.py
	
	a : 3
	b : 2
	c : 1
	d : 1
	e : 0

.. {{{end}}}

The ``elements()`` method returns an iterator that produces all of
the items known to the ``Counter``.

.. literalinclude:: collections_counter_elements.py
   :caption:
   :start-after: #end_pymotw_header

The order of elements is not guaranteed, and items with counts less
than or equal to zero are not included.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_elements.py', break_lines_at=65))
.. }}}

.. code-block:: none

	$ python3 collections_counter_elements.py
	
	Counter({'e': 3, 'x': 1, 't': 1, 'r': 1, 'm': 1, 'l': 1, 'y': 1, 
	'z': 0})
	['e', 'e', 'e', 'x', 't', 'r', 'm', 'l', 'y']

.. {{{end}}}

Use ``most_common()`` to produce a sequence of the *n* most
frequently encountered input values and their respective counts.

.. literalinclude:: collections_counter_most_common.py
   :caption:
   :start-after: #end_pymotw_header

This example counts the letters appearing in all of the words in the
system dictionary to produce a frequency distribution, then prints the
three most common letters.  Leaving out the argument to
``most_common()`` produces a list of all the items, in order of
frequency.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_most_common.py'))
.. }}}

.. code-block:: none

	$ python3 collections_counter_most_common.py
	
	Most common:
	e:  235331
	i:  201032
	a:  199554

.. {{{end}}}

Arithmetic
==========

``Counter`` instances support arithmetic and set operations for
aggregating results. This example shows the standard operators for
creating new ``Counter`` instances, but the in-place operators
``+=``, ``-=``, ``&=``, and ``|=`` are also supported.

.. literalinclude:: collections_counter_arithmetic.py
   :caption:
   :start-after: #end_pymotw_header

Each time a new ``Counter`` is produced through an operation, any
items with zero or negative counts are discarded.  The count for ``a``
is the same in ``c1`` and ``c2``, so subtraction leaves it at
zero.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_counter_arithmetic.py',
..                    break_lines_at=74, line_break_mode='wrap'))
.. }}}

.. code-block:: none

	$ python3 collections_counter_arithmetic.py
	
	C1: Counter({'b': 3, 'a': 2, 'c': 1})
	C2: Counter({'a': 2, 'l': 1, 'p': 1, 'h': 1, 'b': 1, 'e': 1, 't': 1})
	
	Combined counts:
	Counter({'a': 4, 'b': 4, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})
	
	Subtraction:
	Counter({'b': 2, 'c': 1})
	
	Intersection (taking positive minimums):
	Counter({'a': 2, 'b': 1})
	
	Union (taking maximums):
	Counter({'b': 3, 'a': 2, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})

.. {{{end}}}
