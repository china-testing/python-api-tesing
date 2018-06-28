.. _deque:

==============================
 deque --- Double-Ended Queue
==============================

A double-ended queue, or ``deque``, supports adding and removing
elements from either end of the queue. The more commonly used stacks and queues are
degenerate forms of deques, where the inputs and outputs are
restricted to a single end.

.. literalinclude:: collections_deque.py
    :caption:
    :start-after: #end_pymotw_header

Since deques are a type of sequence container, they support some of
the same operations as ``list``, such as examining the contents
with ``__getitem__()``, determining length, and removing elements
from the middle of the queue by matching identity.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque.py'))
.. }}}

.. code-block:: none

	$ python3 collections_deque.py
	
	Deque: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
	Length: 7
	Left end: a
	Right end: g
	remove(c): deque(['a', 'b', 'd', 'e', 'f', 'g'])

.. {{{end}}}

Populating
==========

A deque can be populated from either end, termed "left" and "right" in the
Python implementation.

.. literalinclude:: collections_deque_populating.py
    :caption:
    :start-after: #end_pymotw_header

The ``extendleft()`` function iterates over its input and performs
the equivalent of an ``appendleft()`` for each item. The end result
is that the ``deque`` contains the input sequence in reverse order.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_populating.py'))
.. }}}

.. code-block:: none

	$ python3 collections_deque_populating.py
	
	extend    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
	append    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
	extendleft: deque([5, 4, 3, 2, 1, 0])
	appendleft: deque([6, 5, 4, 3, 2, 1, 0])

.. {{{end}}}

Consuming
=========

Similarly, the elements of the ``deque`` can be consumed from
both ends or either end, depending on the algorithm being applied.

.. literalinclude:: collections_deque_consuming.py
    :caption:
    :start-after: #end_pymotw_header

Use ``pop()`` to remove an item from the "right" end of the
``deque`` and ``popleft()`` to take an item from the "left" end.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_consuming.py'))
.. }}}

.. code-block:: none

	$ python3 collections_deque_consuming.py
	
	From the right:
	gfedcba
	
	From the left:
	012345

.. {{{end}}}


Since deques are thread-safe, the contents can even be consumed from
both ends at the same time from separate threads.

.. literalinclude:: collections_deque_both_ends.py
    :caption:
    :start-after: #end_pymotw_header

The threads in this example alternate between each end, removing items
until the ``deque`` is empty.

.. NOT RUNNING
.. cog.out(run_script(cog.inFile, 'collections_deque_both_ends.py'))

.. code-block:: none

	$ python3 collections_deque_both_ends.py
    
        Left: 0
       Right: 4
       Right: 3
        Left: 1
       Right: 2
        Left done
       Right done

Rotating
========

Another useful aspect of the ``deque`` is the ability to rotate it in
either direction, so as to skip over some items.

.. literalinclude:: collections_deque_rotate.py
    :caption:
    :start-after: #end_pymotw_header

Rotating the ``deque`` to the right (using a positive rotation)
takes items from the right end and moves them to the left
end. Rotating to the left (with a negative value) takes items from the
left end and moves them to the right end.  It may help to visualize
the items in the deque as being engraved along the edge of a dial.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_rotate.py'))
.. }}}

.. code-block:: none

	$ python3 collections_deque_rotate.py
	
	Normal        : deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	Right rotation: deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
	Left rotation : deque([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])

.. {{{end}}}

Constraining the Queue Size
===========================

A ``deque`` instance can be configured with a maximum length so
that it never grows beyond that size. When the queue reaches the
specified length, existing items are discarded as new items are
added. This behavior is useful for finding the last *n* items in a
stream of undetermined length.

.. literalinclude:: collections_deque_maxlen.py
   :caption:
   :start-after: #end_pymotw_header

The deque length is maintained regardless of which end the items are
added to.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_maxlen.py'))
.. }}}

.. code-block:: none

	$ python3 collections_deque_maxlen.py
	
	n = 17
	D1: deque([17], maxlen=3)
	D2: deque([17], maxlen=3)
	n = 72
	D1: deque([17, 72], maxlen=3)
	D2: deque([72, 17], maxlen=3)
	n = 97
	D1: deque([17, 72, 97], maxlen=3)
	D2: deque([97, 72, 17], maxlen=3)
	n = 8
	D1: deque([72, 97, 8], maxlen=3)
	D2: deque([8, 97, 72], maxlen=3)
	n = 32
	D1: deque([97, 8, 32], maxlen=3)
	D2: deque([32, 8, 97], maxlen=3)

.. {{{end}}}



.. seealso::

    * `Wikipedia: Deque <https://en.wikipedia.org/wiki/Deque>`_ -- A
      discussion of the deque data structure.

    * `Deque Recipes <https://docs.python.org/3.5/library/collections.html#deque-recipes>`_
      -- Examples of using deques in algorithms from the standard
      library documentation.
