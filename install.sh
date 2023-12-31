#!/bin/bash

# Устанавливаем дополнительный репозиторий x11
pkg install x11-repo

# Обновляем пакеты и устанавливаем нужные программы
apt update
apt upgrade -y
apt update
apt install -y python wget curl nano git which mc geckodriver clang libxml2 libxslt
pip install selenium beautifulsoup4 requests cython lxml

echo "Установка завершена!"


echo "HISTSIZE=10000 #сохранять историю команд
HISTFILESIZE=1000 #размер истории в текущей сессии

export HISTTIMEFORMAT='%d.%m.%Y %H:%M:%S' #отображать дату введённой команды в истории (проверка --> $ history)

PS1='"\[\e[1;32m\] ╭──[\[\e[31m\]\u\[\e[36m\]@\[\e[32m\]TERMUX]────\[\e[31m\][\t]\[\e[32m\]────\[\e[33m\][\!]\n\[\e[1;32m\][\#]\n\[\e[1;32m\] ╰──[\[\e[34m\]\W\[\e[32m\]]──\[\e[31m\]➤\$ \[\e[m\]"'
export EDITOR=nano #сделать nano — редактором по умолчанию
" > ~/.bashrc

# выводим сообщение об успешном выполнении скрипта
echo "Текст добавлен в ~/bashrc"
# создаем строку с текстом для добавления в файл
echo "terminal-transcript-rows=10000 #отображать в CLI 10к строк вместо 2к (доступно с v0.114+)

terminal-onclick-url-open = true #понимать url(s) в CLI (доступно с v0.118+)
" >> ~/.termux/termux.properties

# выводим сообщение об успешном выполнении скрипта
echo "Текст добавлен в ~/.termux/termux.properties"
