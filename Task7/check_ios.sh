#!/bin/bash

REQUIRED_IOS='16.9.1012'
VERSION_SEARCH_TEXT='version'

echo $(date +%d-%m-%Y) 
echo 
echo "STARTING IOS CHECK" 
for f in ios_configs/* 
do 
  cat $f | grep hostname  
  IOS_VERSION=$(cat $f | grep $VERSION_SEARCH_TEXT | cut -d' ' -f2)
  echo Current IOS version: $IOS_VERSION
  if [[ $IOS_VERSION == $REQUIRED_IOS* ]] 
  then
    echo No upgrade needed
  else 
    echo Upgrade IOS version to: $REQUIRED_IOS
  fi
  echo 
done
echo "ENDING IOS CHECK"