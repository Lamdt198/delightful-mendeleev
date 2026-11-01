import sys

print(f"Python version: {sys.version}")
print("-" * 45)

packages = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "openpyxl"]

for pkg in packages:
    try:
        mod = __import__(pkg)
        version = getattr(mod, "__version__", "unknown")
        print(f"[OK] {pkg:15} : {version}")
    except ImportError as e:
        print(f"[FAILED] {pkg:15} : Not installed ({e})")

print("-" * 45)
print("Moi truong xu ly du lieu da san sang!")
