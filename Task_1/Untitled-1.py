#!/bin/bash

# Список вебсайтів для перевірки
websites=(
  "https://google.com"
  "https://facebook.com"
  "https://twitter.com"
)

# Назва файлу логів
log_file="website_status.log"

# Чистимо файл логів перед записом нових результатів
> $log_file

# Перевірка кожного сайту за допомогою curl
for site in "${websites[@]}"
do
  # Виконуємо HTTP GET запит із curl, зберігаючи HTTP статус в змінну
  http_status=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 10 $site)

  # Перевіряємо HTTP статус для визначення доступності сайту
  if [ $http_status -eq 200 ]; then
    status="[${site}] is UP"
  else
    status="[${site}] is DOWN (HTTP Status: $http_status)"
  fi

  # Записуємо результати у файл логів
  echo $status >> $log_file

  # Вивід на екран
  echo $status
done

# Повідомлення про успішне завершення та назву файлу логів
echo "Результати записано у файл логів: $log_file"
