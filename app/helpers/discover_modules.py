import importlib
import pkgutil


def discover_modules(package, base_class=None, attr_name=None, init_fn=None):
    results = []
    for info in pkgutil.iter_modules(package.__path__):
        if info.name.startswith("_"):
            continue
        mod = importlib.import_module(f".{info.name}", package.__name__)

        if attr_name:
            if hasattr(mod, attr_name):
                inst = getattr(mod, attr_name)
                if init_fn:
                    init_fn(inst)
                results.append(inst)
        elif base_class:
            for name in dir(mod):
                attr = getattr(mod, name)
                if (
                    isinstance(attr, type)
                    and issubclass(attr, base_class)
                    and attr is not base_class
                ):
                    inst = attr()
                    if init_fn:
                        init_fn(inst)
                    results.append(inst)
    return results
