#!/bin/bash
# Write a script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s "$1" -H "X-School-User-Id: 98"
