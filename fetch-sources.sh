#!/bin/bash

VERSION=8.1.1-ga
URL=https://github.com/openjdk/jmc/archive/refs/tags/$VERSION.tar.gz

# if a jmc tarball already exists, remove it prior to downloading a new one
if [ -f $TARBALL_NAME ]; then
    rm $VERSION.tar.gz
fi

wget $URL
