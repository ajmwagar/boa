#!/bin/sh
echo 'Installing Python dependcies'
pip3 install simplejson

echo 'Please install:\n ship\nnetcat\nairmon-ng\nmdk3'

echo 'Installing boa'
pip3 install -e .
