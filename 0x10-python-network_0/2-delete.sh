#!/bin/bash
# DELETE req to $1 URL and response body
curl -s "$1" -X DELETE
