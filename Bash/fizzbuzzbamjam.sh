#!/bin/bash

for ((i=1; i<=100; i++))
do
  output=""

  if (( i % 3 == 0 ))
  then
    output+="Fizz"
  fi

  if (( i % 5 == 0 ))
  then
    output+="Buzz"
  fi

  if (( i % 7 == 0 ))
  then
    output+="Bam"
  fi

  if (( i % 11 == 0 ))
  then
    output+="Jam"
  fi

  if [ -z "$output" ]
  then
    echo "$i"
  else
    echo "$output"
  fi

done