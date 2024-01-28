#!/bin/bash

remove_eggs() {
  # The directory path is sent as the first argument
  cd "$1" || exit
  rm -rf build
  # shellcheck disable=SC2035
  rm -rf *.egg-info
  rm -rf dist
  cd ..
}

# remove build files from components
remove_eggs api
remove_eggs app_platform
remove_eggs block_visualizer
remove_eggs simple_visualizer
remove_eggs train_data_source
remove_eggs airport_data_source

# remove db
cd graph_explorer || exit
# shellcheck disable=SC2035
rm -f *.sqlite3  # Use -f flag to prevent error if no matching files are found
cd ..