\# Лабораторная работа №6



\## Веб-программирование на Python (Flask и FastAPI)



\*\*ФИО:\*\* Кочетова Виктория Александровна  

\*\*Группа:\*\* 221141  

\*\*Вариант:\*\* 6



\---



\## Задания



| Уровень | № | Задание | Файл / Маршрут |

|---------|---|---------|----------------|

| Средн.1 | 6 | FastAPI «Hello» | `fastapi\_app.py`, `GET /` |

| Средн.2 | 8 | FastAPI параметр | `fastapi\_app.py`, `GET /greet/{name}` |

| Средн.3 | 2 | Flask форма приветствия | `flask\_app.py`, `POST /greet` |

| Повыш.1 | 4 | Flask загрузка файла | `flask\_app.py`, `POST /upload` |

| Повыш.2 | 10 | Тестирование API | `test\_api.py` |



\---



\## Установка зависимостей



pip install -r requirements.txt



\---



\## Запуск приложений



\### FastAPI

uvicorn fastapi\_app:app --reload  

Документация Swagger доступна по адресу: http://127.0.0.1:8000/docs



\### Flask

python flask\_app.py  

Приложение доступно по адресу: http://127.0.0.1:5000



\---



\## Запуск тестов



pytest test\_api.py

