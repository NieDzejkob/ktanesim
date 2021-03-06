from os.path import basename, dirname, join as path_join
from glob import glob
import importlib

VANILLA_MODULES = {}
MODDED_MODULES = {}

def register_module(module):
    category = VANILLA_MODULES if module.vanilla else MODDED_MODULES
    try:
        for identifier in module.identifiers:
            category[identifier] = module
    except AttributeError:
        # Assume we're dealing with an abstract class that doesn't need
        # to be registered.
        pass

# This has to be here to avoid cyclic imports.
from modules.base import Module, noparts, check_solve_cmd, gif_append, gif_output

for module_file in glob(path_join(dirname(__file__), "*.py")):
    module_name = basename(module_file)[:-3]
    importlib.import_module('modules.' + module_name)

async def cmd_modules(channel, author, parts):
    list_ = lambda d: ', '.join(f"`{x}`" for x in d)
    await channel.send(f"Available modules:\nVanilla: {list_(VANILLA_MODULES)}\nModded: {list_(MODDED_MODULES)}")
