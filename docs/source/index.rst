.. _spectral-processing:

spectralProcessing Documentation
=============================================
Common mistakes / Issues
--------------------------
Note: When using 'hann' windowing, the DC component of the spectrum will not be
the same as the mean, due to spectral leakage. Spectral leakage of the DC
component does not occur when using boxcar filtering, but does occur when using
hann windowing. The total DC power is still the same, but it is spread over
multiple bins near zero (~approx 3).

component (mean)

.. automodule:: spectral_processing
    :members:
    :undoc-members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
