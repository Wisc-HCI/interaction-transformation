# Interaction Transformation

This is a tool that repairs social robot programs based on user data from a social context. Given a robot program whose behaviors are expressed as a transition system, and a set of user execution paths (traces) through this system, this tool will search for edits that maximize acceptance of traces with positive user experience, and minimize acceptance of traces with negative user experience.

# Software and Hardware

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Software Prerequisites and Installation

This software has been tested on OSX and Ubuntu, and should work fine on either system. Python3 is also required to use this software. Use pip to install any libraries that python3 requires.

### Note about PyNuSMV
At the time that the research article associated with this repository was submitted and published, this software required the use of the PyNuSMV model checker [1][2]. PyNuSMV required OSX 10.14 or Ubuntu 16.04 -- we did not find a way to install PyNuSMV on other versions of Ubuntu or OSX. Thus, we have removed all dependencies for PyNuSMV and removed the copy that we previously included in this repository. A custom model checker to replace PyNuSMV is under development.
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
