from src.printf import *
import importlib
import os

class ModuleLoader:
    def __init__(self, modules_dir="modules", debug=1):
        self.modules_dir = modules_dir
        self.modules = {}
        self.debug = debug

    def load_modules(self):
        for filename in os.listdir(self.modules_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                module_path = f"{self.modules_dir}.{module_name}"
                try:
                    module = importlib.import_module(module_path)
                    if hasattr(module, module_name.capitalize()):
                        module_class = getattr(module, module_name.capitalize())
                        instance = module_class()
                        self.modules[module_name] = instance
                        print_info(f"Module '{module_name}' has been loaded successfully")
                    else:
                        print_fatal(f"Class '{module_name.capitalize()}' cannot be found in module '{module_name}'")
                except Exception as e:
                    print_fatal(f"Error occurred while module loading: '{module_name}': {e}")

    def list_module_functions(self, module_name):
        if module_name in self.modules:
            module = self.modules[module_name]
            functions = [func for func in dir(module) if callable(getattr(module, func)) and not func.startswith("_")]
            return functions
        else:
            return []

    def call_module_function(self, module_name, function_name, *args, **kwargs):
        if module_name in self.modules:
            module = self.modules[module_name]
            func = getattr(module, function_name, None)
            if callable(func):
                return func(*args, **kwargs)
            else:
                result = f"Function '{function_name}' cannot be found in module '{module_name}'"
                if debug == 1:
                    print_error(result)
                return result
        else:
            if debug == 1:
                print_fatal(f"Module '{module_name}' is not loaded")

    def list_loaded_modules(self):
        return self.modules

    def name_by_fcn(self, module_name):
        if module_name in self.modules:
            module = self.modules[module_name]
            functions = {}
            for func_name in dir(module):
                func = getattr(module, func_name)
                if callable(func) and hasattr(func, 'display_name'):
                    functions[func_name] = func.display_name
            return functions
        return {}

    def fcn_by_name(self, module_name, display_name, *args):
        if module_name in self.modules:
            module = self.modules[module_name]
            for func_name in dir(module):
                func = getattr(module, func_name)
                display_name = getattr(func, 'display_name', None)
                if callable(func) and display_name == display_name:
                    return func(*args)
        result = f"Function named as '{display_name}' cannot be found in module '{module_name}'"
        if debug == 1:
            print_error(result)
        return result

    def kb_markup(self, display_name):
        for module_name, module_instance in self.modules.items():
            for func_name in dir(module_instance):
                func = getattr(module_instance, func_name)

                if callable(func) and getattr(func, 'display_name', None) == display_name:
                    markup = getattr(func, 'display_markup', None)
                    if markup == None:
                        if self.debug == 1:
                            print_warn(f"Module {module_name} with function {func_name} doesn't have a configured attribute 'display_markup'")
                        markup = f"Enter arguments for function '{func_name}'"
                    return [module_name, func_name, markup]
        return None
