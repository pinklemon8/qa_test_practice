## Вот основные команды Git для работы с репозиторием через консоль:

Настройка Git:

git config --global user.name "Your Name": Установить имя пользователя для всех репозиториев.
git config --global user.email "youremail@example.com": Установить email пользователя для всех репозиториев.
git config --list: Просмотреть все настройки Git.
Создание и клонирование репозитория:

git init: Инициализировать новый локальный репозиторий Git.
git clone <URL>: Клонировать репозиторий с удаленного сервера.
Работа с изменениями:

git status: Показать состояние рабочего каталога и индекса.
git add <файлы>: Добавить изменения в индекс для подготовки к коммиту.
git commit -m "Ваше сообщение": Фиксировать изменения в локальном репозитории.
git commit --amend: Изменить последний коммит.
git reset <файл>: Отменить добавление файла в индекс.
git checkout -- <файл>: Отменить изменения в файле до последнего коммита.
Ветвление и слияние:

git branch: Показать список веток.
git branch <название_ветки>: Создать новую ветку.
git checkout <название_ветки>: Переключиться на другую ветку.
git merge <название_ветки>: Слить указанную ветку с текущей.
Удаление и переименование:

git rm <файл>: Удалить файл из индекса и рабочего каталога.
git mv <старый_файл> <новый_файл>: Переименовать файл и отследить изменение.
Работа с удаленным репозиторием:

git remote -v: Показать список удаленных репозиториев.
git remote add <название> <URL>: Добавить новый удаленный репозиторий.
git push <удаленный_репозиторий> <ветка>: Отправить изменения на удаленный репозиторий.
git pull <удаленный_репозиторий> <ветка>: Получить и объединить изменения с удаленного репозитория.
Просмотр истории и логов:

git log: Показать историю коммитов.
git log --oneline: Показать компактный список коммитов.
git diff: Показать разницу между коммитами, индексом и рабочим каталогом.
Дополнительные команды:

git help <команда>: Получить справку по конкретной команде Git.
git stash: Скрыть временные изменения.
git stash pop: Применить последний скрытый изменения.
Это основные команды Git для работы с репозиторием через консоль.