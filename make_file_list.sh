#!/bin/bash
tree -lfi | grep \.mp4 | sort -V > file_list
