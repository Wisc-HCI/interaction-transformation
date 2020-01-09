#!/bin/bash

javac -cp ".:prism-4.4-linux64/lib/colt.jar:prism-4.4-linux64/lib/jhoafparser.jar:prism-4.4-linux64/lib/pepa.zip:prism-4.4-linux64/lib/prism.jar" RunPrism.java

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:prism-4.4-linux64/lib

/usr/lib/jvm/java-8-openjdk-amd64/bin/java -Djava.library.path=prism-4.4-linux64/lib -Dfile.encoding=UTF-8 -classpath ".:prism-4.4-linux64/lib/colt.jar:prism-4.4-linux64/lib/jhoafparser.jar:prism-4.4-linux64/lib/pepa.zip:prism-4.4-linux64/lib/prism.jar" RunPrism $1
