#!bin/bash
other_processes=$(($1+9989))
for i in $(seq 9990 $other_processes); do
  if [ $i -ne $other_processes ]; then
    sh compile.sh $i &
  fi
done

sh compile.sh 9999
