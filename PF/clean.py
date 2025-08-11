import os
import shutil

# Borra todos los .pyc
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".pyc"):
            os.remove(os.path.join(root, file))

# Borra todas las carpetas _pycache_
for root, dirs, files in os.walk("."):
    for dir in dirs:
        if dir == "_pycache_":
            shutil.rmtree(os.path.join(root, dir))

print("✅ ¡Archivos .pyc y _pycache_ eliminados correctamente!")