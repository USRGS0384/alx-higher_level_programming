#!/bin/bash
# write ascript that display the size of byte
curl -Is "$1" | -w "cotent length"
