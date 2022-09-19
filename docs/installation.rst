Installation
===================================

Installing Conda 
-----------------
We are providing a conda env yaml file for easy installation of all the dependencies. Therefore, `Miniconda installation <https://docs.conda.io/en/latest/miniconda.html>`_ is recommended for using the UVRSABI package.

Installing Colmap
-----------------
Another dependency for the package is colmap which needs to be installed as follows: `Colmap Installation <https://colmap.github.io/install.html>`_

Installing the UVRSABI env
-----------------

Clone the `Github repository <https://github.com/UVRSABI/UVRSABI-Code.git>`_.
Once all the above dependencies have been installed, create a conda environment by running the following command:-

..  code-block:: bash

	$ cd UVRSABI-Code/
	$ conda env create -f uvrsabi.yaml
    

Now you should be able to use the package on your dataset :)

.. Follow the instructions mentioned on the `official website <https://docs.docker.com/get-docker>`_ 
.. to install Docker on your system. The installation can be verified by running the following commands in the terminal
 (Linux Systems and macOS) or in the command line (Windows)::
    
        docker --version
        docker-compose --version

.. For getting hands-on-experience with Docker, you can refer to some `basic tutorials .. <https://www.freecodecamp.org/news/the-docker-handbook/>`_.