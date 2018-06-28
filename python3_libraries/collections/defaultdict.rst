=====================================================
 defaultdict --- Missing Keys Return a Default Value
=====================================================

The standard dictionary includes the method ``setdefault()`` for
retrieving a value and establishing a default if the value does not
exist. By contrast, ``defaultdict`` lets the caller specify the
default up front when the container is initialized.

.. literalinclude:: collections_defaultdict.py
    :caption:
    :start-after: #end_pymotw_header

This method works well as long as it is appropriate for all keys to
have the same default. It can be especially useful if the default is a
type used for aggregating or accumulating values, such as a
``list``, ``set``, or even ``int``. The standard
library documentation includes several examples in which
``defaultdict`` is used in this way.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_defaultdict.py', line_break_mode='wrap'))
.. }}}

.. code-block:: none

	$ python3 collections_defaultdict.py
	
	d: defaultdict(<function default_factory at 0x101341950>,
	{'foo': 'bar'})
	foo => bar
	bar => default value

.. {{{end}}}

.. seealso::

    * `defaultdict examples
      <https://docs.python.org/3.5/library/collections.html#defaultdict-examples>`__
      -- Examples of using ``defaultdict`` from the standard library
      documentation.

    * `Evolution of Default Dictionaries in Python
      <http://jtauber.com/blog/2008/02/27/evolution_of_default_dictionaries_in_python/>`_
      -- James Tauber's discussion of how ``defaultdict``
      relates to other means of initializing dictionaries.
