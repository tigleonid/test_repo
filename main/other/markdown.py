"""
Модуль, отвечающий за генерацию html из markdown
"""


import re
import markdown
from markdown_grid_tables import GridTableExtension
from django.template import Template, Context

# взял несколько полезных официальных расширений отсюда:
# https://python-markdown.github.io/extensions/#third-party-extensions
#
# tables — вот это превратится в таблицу:
# 
# First Header  | Second Header
# ------------- | -------------
# Content Cell  | Content Cell
# Content Cell  | Content Cell
# 
# sane_lists — по умолчанию markdown корректирует нумерацию 
# (1. … 2. … 4. … — исправит 4 на 3), sane_lists отключает это
#
# footnotes — позволяют делать нумерованные ссылки на концовку (как в статьях на источники)
# Контент[^1] (вместо 1 можно поставить любое выражение)
# (в конце) [^1]: Пояснение к контенту
#
# nl2br — по умолчанию markdown "проглатывает" новые строки, чтобы создать,
# нужно две пустых строки. Неопытным пользователям это тяжело, поэтому это расширение это отключает
# 
# GrifTableExtension — неофициальное расширение, позволяющее рендерить более сложные таблицы:
# +-------+----------+------+
# | Table Headings   | Here |
# +-------+----------+------+
# | Sub   | Headings | Too  |
# +=======+==========+======+
# | cell  | column spanning |
# + spans +----------+------+
# | rows  | normal   | cell |
# +-------+----------+------+
# | multi | cells can be    |
# | line  | *formatted*     |
# |       | **paragraphs**  |
# | cells |                 |
# | too   |                 |
# +-------+-----------------+

markdown_extensions = ['tables', 'sane_lists', 'footnotes', 'nl2br', GridTableExtension()]


# регулярка, помогающая найти парные знаки доллара (вида $…$, математические выражения)
DOLLAR = re.compile(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)')  # "?" stands for being lazy
# регулярка для двойной долларификации (вида $$…$$) — математические блоки
DOUBLE_DOLLAR = re.compile(r'(?<!\$)\$\$(?!\$)([\S\s]*?)(?<!\$)\$\$(?!\$)', re.MULTILINE)

# экранирует внутренности выражения
# (например, …*<что-то там…>*… может восприняться как выделение курсивом)
# поэтому заменяем "*" на "\*" и тп
def escape_math(text):
    # the problem is that markdown needs escaping to these chars, so we replace user's smth with \smth
    return re.sub(r'[\\\{\}\[\]\$_\*]', lambda match: '\\' + match.group(0), text)


# заменяет более удобный формат $…$ на стандартный для mathjax-а \(…\)
# + экранирует внутренности выражения
def replace_linear_math(match):
    text = f'\\({match.group(1)}\\)'

    return escape_math(text)

# экранирует внутренности математического блока
def replace_block_math(match):

    # can't include dollars, otherwise they will be also escaped
    return '$$' + escape_math(match.group(1)) + '$$'

# основной вызываемый метод генерации
def generate_html(md_text):

    # предварительно экранируем математику
    md_text = re.sub(DOLLAR, replace_linear_math, md_text)
    md_text = re.sub(DOUBLE_DOLLAR, replace_block_math, md_text)

    # а теперь вызываем готовую функцию конвертации с расширениями
    md_text = markdown.markdown(md_text, extensions=markdown_extensions)
    return Template(md_text).render(Context({})) # возвращаем строку в формате Template
