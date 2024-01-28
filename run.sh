#!/bin/bash

# This script is used to build all necessary python components
# and runt django website.

lay_egs() {
  # The directory path is sent as the first argument
  pip install $1
}

run_server() {
  # The Django website path is sent as the first argument
  cd "$1" || exit
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
}


# build components
lay_egs ./api
lay_egs ./app_platform
lay_egs ./simple_visualizer
lay_egs ./block_visualizer
lay_egs ./train_data_source
lay_egs ./airport_data_source



run_server graph_explorer
