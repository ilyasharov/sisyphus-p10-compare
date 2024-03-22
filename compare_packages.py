import json

def main(package_names):
   """
   Функция сравнения пакетов.

   Args:
       package_names: Список имен пакетов для сравнения.

   Returns:
       None.
   """

   # Загрузка пакетов Sisyphus
   with open("sisyphus_packages.json", "r") as f:
       sisyphus_packages = json.load(f)

   # Загрузка пакетов P10
   with open("p10_packages.json", "r") as f:
       p10_packages = json.load(f)

   # Сравнение пакетов
   missing_packages = []
   for package_name in package_names:
       if package_name not in p10_packages:
           missing_packages.append(package_name)

   # Вывод результата
   if missing_packages:
       print(f"В P10 отсутствуют следующие пакеты Sisyphus:")
       for package_name in missing_packages:
           print(f" - {package_name}")
   else:
       print("Все пакеты Sisyphus присутствуют в P10.")


if __name__ == "__main__":
   with open("packages.json", "r") as f:
       package_names = [package["name"] for package in json.load(f)]
   main(package_names)