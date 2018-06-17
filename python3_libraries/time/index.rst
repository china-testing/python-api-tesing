====================
 time --- Clock Time
====================

.. module:: time
    :synopsis: Clock time

:Purpose: Functions for manipulating clock time.

The ``time`` module provides access to several different types of
clocks, each useful for different purposes. The standard system calls
like ``time()`` report the system "wall clock" time. The
``monotonic()`` clock can be used to measure elapsed time in a
long-running process because it is guaranteed never to move backwards,
even if the system time is changed. For performance testing,
``perf_counter()`` provides access to the clock with the highest
available resolution to make short time measurements more
accurate. The CPU time is available through ``clock()``, and
``process_time()`` returns the combined processor time and system
time.

.. note::

  The implementations expose C library functions for manipulating
  dates and times.  Since they are tied to the underlying C
  implementation, some details (such as the start of the epoch and
  maximum date value supported) are platform-specific.  Refer to the
  library documentation for complete details.

Comparing Clocks
================

Implementation details for the clocks varies by platform. Use
``get_clock_info()`` to access basic information about the current
implementation, including the clock's resolution.

.. literalinclude:: time_get_clock_info.py
   :caption:
   :start-after: #end_pymotw_header

This output for Mac OS X shows that the monotonic and perf_counter
clocks are implemented using the same underlying system call.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'time_get_clock_info.py'))
.. }}}

.. code-block:: none

	$ python3 time_get_clock_info.py
	
	clock:
	    adjustable    : False
	    implementation: clock()
	    monotonic     : True
	    resolution    : 1e-06
	    current       : 0.046796
	
	monotonic:
	    adjustable    : False
	    implementation: mach_absolute_time()
	    monotonic     : True
	    resolution    : 1e-09
	    current       : 716028.526210432
	
	perf_counter:
	    adjustable    : False
	    implementation: mach_absolute_time()
	    monotonic     : True
	    resolution    : 1e-09
	    current       : 716028.526241605
	
	process_time:
	    adjustable    : False
	    implementation: getrusage(RUSAGE_SELF)
	    monotonic     : True
	    resolution    : 1e-06
	    current       : 0.046946999999999996
	
	time:
	    adjustable    : True
	    implementation: gettimeofday()
	    monotonic     : False
	    resolution    : 1e-06
	    current       : 1521404584.966362
	

.. {{{end}}}

Wall Clock Time
===============

One of the core functions of the ``time`` module is ``time()``,
which returns the number of seconds since the start of the "epoch" as
a floating point value.

.. literalinclude:: time_time.py
    :caption:
    :start-after: #end_pymotw_header

The epoch is the start of measurement for time, which for Unix systems
is 0:00 on January 1, 1970. Although the value is always a float,
actual precision is platform-dependent.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'time_time.py'))
.. }}}

.. code-block:: none

	$ python3 time_time.py
	
	The time is: 1521404585.0243158

.. {{{end}}}

The float representation is useful when storing or comparing dates,
but not as useful for producing human readable representations. For
logging or printing time ``ctime()`` can be more useful.

.. literalinclude:: time_ctime.py
    :caption:
    :start-after: #end_pymotw_header

The second ``print()`` call in this example shows how to use
``ctime()`` to format a time value other than the current time.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'time_ctime.py'))
.. }}}

.. code-block:: none

	$ python3 time_ctime.py
	
	The time is      : Sun Mar 18 16:23:05 2018
	15 secs from now : Sun Mar 18 16:23:20 2018

.. {{{end}}}

.. _time-monotonic:

Monotonic Clocks
================

Because ``time()`` looks at the system clock, and the system clock
can be changed by the user or system services for synchronizing clocks
across multiple computers, calling ``time()`` repeatedly may produce
values that go forwards and backwards. This can result in unexpected
behavior when trying to measure durations or otherwise use those times
for computation. Avoid those situations by using ``monotonic()``,
which always returns values that go forward.

.. literalinclude:: time_monotonic.py
   :caption:
   :start-after: #end_pymotw_header

The start point for the monotonic clock is not defined, so return
values are only useful for doing calculations with other clock
values. In this example the duration of the sleep is measured using
``monotonic()``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'time_monotonic.py'))
.. }}}

.. code-block:: none

	$ python3 time_monotonic.py
	
	start : 716028.72
	end   : 716028.82
	span  :      0.10

.. {{{end}}}

Processor Clock Time
====================

While ``time()`` returns a wall clock time, ``clock()`` returns
processor clock time.  The values returned from ``clock()`` reflect
the actual time used by the program as it runs.

.. literalinclude:: time_clock.py
    :caption:
    :start-after: #end_pymotw_header

In this example, the formatted ``ctime()`` is printed along with
the floating point values from ``time()``, and ``clock()`` for
each iteration through the loop.

.. note::

  If you want to run the example on your system, you may have to add
  more cycles to the inner loop or work with a larger amount of data
  to actually see a difference in the times.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'time_clock.py'))
.. }}}

.. code-block:: none

	$ python3 time_clock.py
	
	Sun Mar 18 16:23:05 2018 : 1521404585.328 0.051
	Sun Mar 18 16:23:05 2018 : 1521404585.632 0.349
	Sun Mar 18 16:23:05 2018 : 1521404585.935 0.648
	Sun Mar 18 16:23:06 2018 : 1521404586.234 0.943
	Sun Mar 18 16:23:06 2018 : 1521404586.539 1.244

.. {{{end}}}

Typically, the processor clock does not tick if a program is not doing
anything.

.. literalinclude:: time_clock_sleep.py
    :caption:
    :start-after: #end_pymotw_header

In this example, the loop does very little work by going to sleep
after each iteration. The ``time()`` value increases even while
the application is asleep, but the ``clock()`` value does not.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u time_clock_sleep.py'))
.. }}}

.. code-block:: none

	$ python3 -u time_clock_sleep.py
	
	Sun Mar 18 16:23:06 2018 - 1521404586.89 - 0.04
	Sleeping 3
	Sun Mar 18 16:23:09 2018 - 1521404589.90 - 0.04
	Sleeping 2
	Sun Mar 18 16:23:11 2018 - 1521404591.90 - 0.04
	Sleeping 1
	Sun Mar 18 16:23:12 2018 - 1521404592.90 - 0.04

.. {{{end}}}

Calling ``sleep()`` yields control from the current thread and
asks it to wait for the system to wake it back up. If a program has
only one thread, this effectively blocks the app and it does no work.

Performance Counter
===================

It is important to have a high-resolution monotonic clock for
measuring performance. Determining the best clock data source requires
platform-specific knowledge, which Python provides in
``perf_counter()``.

.. literalinclude:: time_perf_counter.py
   :caption:
   :start-after: #end_pymotw_header

As with ``monotonic()``, the epoch for ``perf_counter()`` is
undefined, and the values are meant to be used for comparing and
computing values, not as absolute times.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'time_perf_counter.py'))
.. }}}

.. code-block:: none

	$ python3 time_perf_counter.py
	
	Sun Mar 18 16:23:13 2018 : 0.378 0.378
	Sun Mar 18 16:23:13 2018 : 0.376 0.754
	Sun Mar 18 16:23:14 2018 : 0.372 1.126
	Sun Mar 18 16:23:14 2018 : 0.376 1.502
	Sun Mar 18 16:23:14 2018 : 0.376 1.879

.. {{{end}}}

Time Components
===============

Storing times as elapsed seconds is useful in some situations, but
there are times when a program needs to have access to the individual
fields of a date (year, month, etc.). The ``time`` module defines
``struct_time`` for holding date and time values with components
broken out so they are easy to access. There are several functions
that work with ``struct_time`` values instead of floats.

.. literalinclude:: time_struct.py
    :caption:
    :start-after: #end_pymotw_header

The ``gmtime()`` function returns the current time in
UTC. ``localtime()`` returns the current time with the current
time zone applied. ``mktime()`` takes a ``struct_time`` and
converts it to the floating point representation.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'time_struct.py'))
.. }}}

.. code-block:: none

	$ python3 time_struct.py
	
	gmtime:
	  tm_year : 2018
	  tm_mon  : 3
	  tm_mday : 18
	  tm_hour : 20
	  tm_min  : 23
	  tm_sec  : 14
	  tm_wday : 6
	  tm_yday : 77
	  tm_isdst: 0
	
	localtime:
	  tm_year : 2018
	  tm_mon  : 3
	  tm_mday : 18
	  tm_hour : 16
	  tm_min  : 23
	  tm_sec  : 14
	  tm_wday : 6
	  tm_yday : 77
	  tm_isdst: 1
	
	mktime: 1521404594.0

.. {{{end}}}



Working with Time Zones
=======================

The functions for determining the current time depend on having the
time zone set, either by the program or by using a default time zone
set for the system. Changing the time zone does not change the actual
time, just the way it is represented.

To change the time zone, set the environment variable ``TZ``, then
call ``tzset()``.  The time zone can be specified with a lot of
detail, right down to the start and stop times for daylight savings
time. It is usually easier to use the time zone name and let the
underlying libraries derive the other information, though.

This example program changes the time zone to a few different values
and shows how the changes affect other settings in the time module.

.. literalinclude:: time_timezone.py
    :caption:
    :start-after: #end_pymotw_header

The default time zone on the system used to prepare the examples is
US/Eastern. The other zones in the example change the tzname, daylight
flag, and timezone offset value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'time_timezone.py'))
.. }}}

.. code-block:: none

	$ python3 time_timezone.py
	
	Default :
	  TZ    : (not set)
	  tzname: ('EST', 'EDT')
	  Zone  : 18000 (5.0)
	  DST   : 1
	  Time  : Sun Mar 18 16:23:14 2018
	
	GMT :
	  TZ    : GMT
	  tzname: ('GMT', 'GMT')
	  Zone  : 0 (0.0)
	  DST   : 0
	  Time  : Sun Mar 18 20:23:14 2018
	
	Europe/Amsterdam :
	  TZ    : Europe/Amsterdam
	  tzname: ('CET', 'CEST')
	  Zone  : -3600 (-1.0)
	  DST   : 1
	  Time  : Sun Mar 18 21:23:14 2018
	

.. {{{end}}}

Parsing and Formatting Times
============================

The two functions ``strptime()`` and ``strftime()`` convert
between ``struct_time`` and string representations of time
values. There is a long list of formatting instructions available to
support input and output in different styles. The complete list is
documented in the library documentation for the ``time`` module.

This example converts the current time from a string to a
``struct_time`` instance and back to a string.

.. literalinclude:: time_strptime.py
    :caption:
    :start-after: #end_pymotw_header

The output string is not exactly like the input, since the day of the
month is prefixed with a zero.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'time_strptime.py'))
.. }}}

.. code-block:: none

	$ python3 time_strptime.py
	
	Now: Mon Jan  2 16:17:27 2017
	
	Parsed:
	  tm_year : 2017
	  tm_mon  : 1
	  tm_mday : 2
	  tm_hour : 16
	  tm_min  : 17
	  tm_sec  : 27
	  tm_wday : 0
	  tm_yday : 2
	  tm_isdst: -1
	
	Formatted: Mon Jan 02 16:17:27 2017

.. {{{end}}}

.. seealso::

   * :pydoc:`time`

   * :ref:`Python 2 to 3 porting notes for time <porting-time>`

   * :mod:`datetime` -- The ``datetime`` module includes other classes
     for doing calculations with dates and times.

   * :mod:`calendar` -- Work with higher-level date functions to
     produce calendars or calculate recurring events.
