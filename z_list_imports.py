import pkgutil
import importlib

def list_imports(package):
    package = importlib.import_module(package)
    return {name for _, name, _ in pkgutil.walk_packages(package.__path__)}

if __name__ == "__main__":
    imports = set()
    with open("main.py", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("import") or line.startswith("from"):
                parts = line.replace(",", " ").split()
                if parts[0] == "import":
                    imports.update(parts[1:])
                elif parts[0] == "from":
                    imports.add(parts[1])
    
    additional_imports = set()
    for imp in imports:
        try:
            additional_imports.update(list_imports(imp))
        except:
            pass
    
    all_imports = imports.union(additional_imports)
    with open("active_imports.txt", "w", encoding="utf-8") as f:
        for imp in sorted(all_imports):
            f.write(f"{imp}\n")

    print(f"Detected imports: {sorted(all_imports)}")
