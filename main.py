import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def run_script(script_name):
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error al ejecutar {script_name}:")
        print(result.stderr)
    else:
        print(f"Resultado de {script_name}:")
        print(result.stdout)


if __name__ == "__main__":
    # Lista de paquetes requeridos
    required_packages = ['pandas', 'numpy']

    # Instalar las bibliotecas necesarias
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            install(package)

    # Ejecutar los scripts
    scripts = ['combinaciones.py', 'convergencia.py']

    for script in scripts:
        print(f"Ejecutando {script}...")
        run_script(script)
        print(f"Finalizó la ejecución de {script}.\n")
