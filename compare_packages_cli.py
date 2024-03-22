import argparse
import json

def compare_packages(sisyphus_packages, p10_packages):
   """
   Функция сравнения пакетов.

   Args:
       sisyphus_packages: Список пакетов Sisyphus.
       p10_packages: Список пакетов P10.

   Returns:
       Словарь JSON с результатами сравнения.
   """

   # Сравнение пакетов
   missing_in_p10 = []
   missing_in_sisyphus = []
   version_mismatch = []

   for package in sisyphus_packages:
       if package["name"] not in p10_packages:
           missing_in_p10.append(package)
       else:
           sisyphus_version = package["version"]
           p10_version = p10_packages[package["name"]]["version"]
           if sisyphus_version > p10_version:
               version_mismatch.append(
                   {
                       "name": package["name"],
                       "sisyphus_version": sisyphus_version,
                       "p10_version": p10_version,
                   }
               )

   for package in p10_packages:
       if package["name"] not in sisyphus_packages:
           missing_in_sisyphus.append(package)

   # Формирование JSON-отчета
   report = {
       "missing_in_p10": missing_in_p10,
       "missing_in_sisyphus": missing_in_sisyphus,
       "version_mismatch": version_mismatch,
   }

   return report


def main():
   """
   Функция сравнения пакетов.

   Args:
       None.

   Returns:
       None.
   """

   # Обработка аргументов командной строки
   parser = argparse.ArgumentParser(description="Сравнение пакетов Sisyphus и P10")
   parser.add_argument(
       "-p",
       "--packages",
       dest="packages_file",
       metavar="FILE",
       help="Файл JSON со списком пакетов для сравнения",
       required=True,
   )
   args = parser.parse_args()

   # Загрузка данных из packages.json
   with open(args.packages_file, "r") as f:
       data = json.load(f)

   # Списки пакетов
   sisyphus_packages = data["sisyphus_packages"]
   p10_packages = data["p10_packages"]

   # Сравнение пакетов по архитектурам
   for arch in data["architectures"]:
       report = compare_packages(
           [package for package in sisyphus_packages if package["arch"] == arch],
           [package for package in p10_packages if package["arch"] == arch],
       )
       print(f"**{arch}**")
       print(json.dumps(report, indent=2))


if __name__ == "__main__":
   main()