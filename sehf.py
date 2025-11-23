import os
from datetime import datetime

def patch_runtime_lavamoat(base_path):
    target_filename = "runtime-lavamoat.js"
    search_text = 'scuttleGlobalThis":{"enabled":true'
    replace_text = 'scuttleGlobalThis":{"enabled":false'
    log_entries = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
