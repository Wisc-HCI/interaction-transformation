# Interaction Transformation

This is a tool that repairs social robot programs based on user data from a social context. Given a robot program whose behaviors are expressed as a transition system, and a set of user execution paths (traces) through this system, this tool will search for edits that maximize acceptance of traces with positive user experience, and minimize acceptance of traces with negative user experience.

# Software and Hardware

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Software Prerequisites and Installation

This software has been tested on OSX 10.14 and Ubuntu 16.04. Python3 is also required to use this software. Use pip to install any libraries that python3 requires.

### PyNuSMV
This software requires that you use the PyNuSMV model checker. We have provided a copy of the PyNuSMV source code in this repository. Versions installed using other means will not work with this software. For more information, see the source of PyNuSMV [1][2]. Install PyNuSMV by running the following:

On OSX:
```
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:<path_to_local_repo>/src/verification/pynusmv/src/lib/
```

On Ubuntu:
```
LD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:<path_to_local_repo>/src/verification/pynusmv/src/lib/
```

### d3 and Dagre
To visualize the transformation process, d3 and Dagre are both required. Download them both, and place the node_modules folder in src.

# Running the software

Run the following:

```
./bfs.sh
```

# Citing this code

More to come about this later.

# References

[1] https://github.com/sbusard/pynusmv

[2] Busard, S., & Pecheur, C. (2013, May). PyNuSMV: NuSMV as a python library. In NASA Formal Methods Symposium (pp. 453-458). Springer, Berlin, Heidelberg.
