#!/bin/bash
# write ascript that display the size of byte
curl -ls "$1" | wc -c
