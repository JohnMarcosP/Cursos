#!/bin/bash
for i in {0..254}
do
    ping -c 1 "$i.$i" | grep ttl | cut -d " " -f 4 | sed "s/.$//" &
done
