# autonomousAJ_spotifyAPI/run.py
import importlib
from autonomousAJ_spotifyAPI.config import global_config

app_run_input = global_config.prompt_app_run_choices()

if app_run_input == "all":
    for script_name in global_config.find_all_scripts():
       module = importlib.import_module(f'autonomousAJ_spotifyAPI.{script_name}')
else:
    module = importlib.import_module(f'autonomousAJ_spotifyAPI.{app_run_input}')