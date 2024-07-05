#!/bin/bash
# display only the status code of a response
curl -so /dev/null --write-out "%{http_code}" "$1"
