--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1 (Debian 15.1-1.pgdg110+1)
-- Dumped by pg_dump version 15.1 (Debian 15.1-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: modules_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.modules_info (
    id integer NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    code character varying(128) NOT NULL,
    description text NOT NULL,
    level character varying(32) NOT NULL
);


ALTER TABLE public.modules_info OWNER TO postgres;

--
-- Name: modules_info_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.modules_info_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.modules_info_id_seq OWNER TO postgres;

--
-- Name: modules_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.modules_info_id_seq OWNED BY public.modules_info.id;


--
-- Name: resources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resources (
    id integer NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    url character varying(256) NOT NULL,
    title character varying(128) NOT NULL
);


ALTER TABLE public.resources OWNER TO postgres;

--
-- Name: resources_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resources_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resources_id_seq OWNER TO postgres;

--
-- Name: resources_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resources_id_seq OWNED BY public.resources.id;


--
-- Name: resources_modules_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resources_modules_info (
    id integer NOT NULL,
    module_code character varying(64) NOT NULL,
    resource_id integer NOT NULL
);


ALTER TABLE public.resources_modules_info OWNER TO postgres;

--
-- Name: resources_modules_info_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resources_modules_info_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resources_modules_info_id_seq OWNER TO postgres;

--
-- Name: resources_modules_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resources_modules_info_id_seq OWNED BY public.resources_modules_info.id;


--
-- Name: modules_info id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modules_info ALTER COLUMN id SET DEFAULT nextval('public.modules_info_id_seq'::regclass);


--
-- Name: resources id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources ALTER COLUMN id SET DEFAULT nextval('public.resources_id_seq'::regclass);


--
-- Name: resources_modules_info id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources_modules_info ALTER COLUMN id SET DEFAULT nextval('public.resources_modules_info_id_seq'::regclass);


--
-- Data for Name: modules_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.modules_info (id, created_at, updated_at, code, description, level) FROM stdin;
6	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	modules_packages	Модули и пакеты. Модуль учит превращать набор файлов в организованный проект. Объясняется, как Python находит код, как разделять ответственность между модулями и правильно запускать приложения.	Структура и абстракции
7	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	oop_basics	Объектно-ориентированное программирование. Переход от написания кода к проектированию системы. Модуль учит моделировать предметную область, управлять состоянием и поведением объектов.	Структура и абстракции
8	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	oop_advanced	Продвинутое ООП. Углублённое понимание Python как объектной системы. Формируется навык чтения сложных библиотек и осознанного использования продвинутых абстракций.	Структура и абстракции
9	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	advanced_functions	Продвинутые функции. Функции становятся инструментами построения гибкой архитектуры. Модуль учит писать выразительный, лаконичный и мощный код.	Структура и абстракции
10	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	iterators_generators	Итераторы и генераторы. Формируется понимание ленивых вычислений и потоковой обработки данных — ключ к работе с большими объёмами данных.	Структура и абстракции
11	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	stdlib_essentials	Стандартная библиотека. Модуль учит решать задачи с помощью стандартной библиотеки, понимать идиомы Python и эффективно использовать встроенные инструменты.	Стандартная библиотека
12	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	files_os_basics	Файлы и ОС. Работа с файловой системой и операционной средой. Необходимый навык для автоматизации, серверных приложений и CLI-утилит.	Стандартная библиотека
13	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	text_encoding	Кодировки и текст. Модуль закрывает частые проблемы работы с Unicode и текстовыми данными, устраняя ошибки кодировок.	Стандартная библиотека
14	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	json_serialization	Сериализация данных. Модуль учит превращать данные в форматы обмена между системами — основа API, конфигураций и интеграций.	Стандартная библиотека
15	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	typing_mypy	Типизация. Формируется мышление «код как контракт». Модуль снижает количество ошибок и улучшает поддержку больших кодовых баз.	Качество кода
16	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	code_style_linters	Стиль кода. Модуль учит писать код, который удобно читать и поддерживать другим разработчикам.	Качество кода
17	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	logging_debugging	Логирование и отладка. Навык понимания поведения приложения после деплоя, а не только во время разработки.	Качество кода
20	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	concurrency_basics	Потоки и процессы. Модуль объясняет модель параллелизма Python и ограничения интерпретатора.	Асинхронность
21	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	asyncio_fundamentals	Asyncio. Обучение написанию высоконагруженных I/O-приложений и пониманию асинхронной экосистемы Python.	Асинхронность
22	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	async_io_patterns	Асинхронные паттерны. Проектирование устойчивых асинхронных систем, а не просто использование async/await.	Асинхронность
1	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	python_syntax_types	Синтаксис Python и типы. Этот модуль закладывает фундамент работы с Python как языком. Формируется понимание того, как код читается, исполняется и как данные существуют в программе. После него студент уверенно пишет простой код, понимает различие между типами данных и избегает типичных ошибок новичков, связанных с приведением типов и управлением значениями.	Базовый уровень
2	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	control_flow_basics	Управление потоком выполнения. Модуль учит управлять логикой программы: принимать решения, повторять действия и корректно завершать выполнение. Это ключевой шаг от линейных скриптов к программам, реагирующим на условия и входные данные.	Базовый уровень
3	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	collections_basics	Коллекции данных. Модуль учит работать с наборами данных: хранить, изменять, извлекать и комбинировать значения. Формируется интуиция выбора правильной структуры данных под задачу и база для дальнейшей работы с алгоритмами.	Базовый уровень
4	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	functions_basics	Функции. Модуль показывает, как структурировать код, избегать дублирования и мыслить в терминах подзадач. Код становится читаемым, переиспользуемым и тестируемым.	Базовый уровень
5	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	error_handling_basics	Обработка ошибок. Формируется правильное отношение к ошибкам как к управляемым сценариям. Модуль учит писать устойчивый код, корректно реагирующий на нештатные ситуации и упрощающий отладку.	Базовый уровень
18	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	unit_testing_basics	Тестирование. Формируется культура проверки кода и уверенность в изменениях — критично для командной разработки.	Качество кода
19	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	pytest_advanced	Продвинутое тестирование. Тестирование как инструмент проектирования и поддержки сложных систем.	Качество кода
23	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	async_web_clients	Асинхронные клиенты. Работа с внешними API: таймауты, ретраи, пулы соединений.	Асинхронность
24	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	http_rest_basics	HTTP и REST. Системное понимание взаимодействия сервисов в интернете.	Веб и бэкенд
25	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	web_framework_basics	Веб-фреймворки. Общие принципы веб-разработки независимо от конкретного фреймворка.	Веб и бэкенд
26	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	routing_request	Request/Response. Жизненный цикл HTTP-запроса и обработка ошибок.	Веб и бэкенд
27	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	validation_serialization	Валидация данных. Навык защиты приложения от некорректных данных и построения надёжных API.	Веб и бэкенд
30	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	sql_basics	SQL. Фундамент работы с реляционными базами данных.	Работа с данными
31	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	postgres_essentials	PostgreSQL. Использование БД как полноценного инструмента, а не просто хранилища.	Работа с данными
32	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	python_db_drivers	Драйверы БД. Эффективное и безопасное взаимодействие Python с базами данных.	Работа с данными
33	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	orm_basics	ORM. Понимание компромиссов между SQL и высокоуровневыми абстракциями.	Работа с данными
34	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	migrations_schema	Миграции. Управление эволюцией схемы данных без боли.	Работа с данными
35	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	backend_arch_patterns	Архитектура. Переход от написания кода к проектированию систем.	Продакшен и архитектура
36	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	caching_performance	Производительность. Поиск узких мест и масштабирование приложений.	Продакшен и архитектура
37	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	background_tasks_async	Фоновые задачи. Вынос тяжёлой работы из пользовательских запросов.	Продакшен и архитектура
38	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	task_queues_brokers	Очереди задач. Понимание распределённых систем и надёжной обработки задач.	Продакшен и архитектура
39	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	docker_python_apps	Docker. Подготовка Python-приложений к деплою и эксплуатации.	Продакшен и архитектура
28	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	auth_security_basics	Безопасность. Базовое понимание защиты веб-приложений и пользовательских данных.	Веб и бэкенд
29	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	advanced_auth_security	Продвинутая безопасность. Реальные схемы авторизации и управления доступом в продакшене.	Веб и бэкенд
40	2026-02-02 18:41:05.227875+00	2026-02-02 18:41:05.227875+00	ci_cd_basics	CI/CD. Автоматизация пути от коммита до продакшена.	Продакшен и архитектура
41	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	numpy_basics	NumPy: основы работы с многомерными массивами, векторизация вычислений, математические операции, индексирование массивов, работа с данными научных вычислений	Наука о данных
42	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	pandas_basics	Pandas: работа с DataFrame и Series, загрузка/сохранение данных из CSV/Excel/SQL, фильтрация, группировка, обработка пропущенных значений, объединение таблиц	Наука о данных
43	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	cli_tools	CLI-утилиты: создание консольных приложений с помощью argparse, click, typer. Парсинг аргументов командной строки, флаги, опции, подкоманды, валидация параметров	Инструменты разработчика
44	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	data_cleaning_pipelines	Очистка данных и пайплайны: автоматизация обработки данных, нормализация, удаление дубликатов, преобразование форматов, создание ETL-процессов, пайплайны с pandas	Наука о данных
45	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	env_poetry	Виртуальные окружения и Poetry: настройка venv, pyenv, poetry, управление зависимостями, pyproject.toml, poetry.lock, публикация пакетов в PyPI	DevOps и развертывание
46	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	context_managers	Контекстные менеджеры: протокол with, создание через class и @contextlib.contextmanager, работа с файлами, базами данных, блокировками, cleanup ресурсов	Синтаксис Python
47	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	automation_os_schedulers	Автоматизация с ОС и планировщиками: subprocess, os, shutil, cron, systemd timers, Windows Task Scheduler, автоматизация задач, скрипты развертывания	DevOps и развертывание
48	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	api_docs_openapi	Документация API и OpenAPI: автоматическая генерация Swagger/FastAPI docs, OpenAPI 3.0 спецификация, аннотации Pydantic, примеры запросов/ответов, интерактивная документация	Веб-разработка
49	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	packaging_distribution	Пакетирование и распространение: setuptools, pyproject.toml, wheel/sdist, манифесты, entry_points, публикация на PyPI/TestPyPI, CI/CD для пакетов Python	DevOps и развертывание
50	2026-02-02 21:58:59.713534+00	2026-02-02 21:58:59.713534+00	apis_integrations	API и интеграции с внешними сервисами: REST клиенты (httpx, aiohttp), OAuth2, Webhook'ы, rate limiting, retry логика, парсинг сложных ответов API, интеграции с Telegram/Discord	Веб-разработка
\.


--
-- Data for Name: resources; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.resources (id, created_at, updated_at, url, title) FROM stdin;
1	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/tutorial/introduction.html	Python Official Tutorial
2	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python-data-types/	RealPython: Python Data Types
3	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=_uQrJ0TkZlc	Corey Schafer: Python Tutorial
4	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://numpy.org/doc/stable/user/absolute_beginners.html	NumPy Beginner Guide
5	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/numpy-tutorial/	RealPython: NumPy Tutorial
6	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=QUT1VHiLmmI	Sentdex: NumPy Intro
7	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/library/typing.html	Python Typing Module
8	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://mypy.readthedocs.io/en/stable/	MyPy Documentation
9	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=-NFnkS9Qkk8	MyPy Tutorial
10	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/tutorial/classes.html	Python Classes Tutorial
11	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python3-object-oriented-programming/	RealPython: OOP Basics
12	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=ZDa-Z5JzLYM	OOP in Python
13	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/tutorial/controlflow.html#defining-functions	Defining Functions in Python
14	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/defining-your-own-python-function/	RealPython: Functions
15	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=9Os0ZawaO90	Functions Explained
16	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range	Python Collections
17	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python-data-structures/	RealPython: Data Structures
18	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=W8KRzm-HUcc	Collections Overview
19	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/tutorial/controlflow.html	Python Control Flow
20	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python-conditional-statements/	RealPython: Conditional Statements
21	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=XBmY0bcvHAc	Control Flow
22	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://pandas.pydata.org/docs/user_guide/10min.html	Pandas 10-Minute Guide
23	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.kaggle.com/learn/pandas	Kaggle: Learn Pandas
24	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=vmEHCJofslg	Pandas 10 Minutes
25	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.sqlalchemy.org/en/20/tutorial/	SQLAlchemy ORM Tutorial
26	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python-sqlalchemy-orm/	RealPython: SQLAlchemy
27	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=faFweYWkG7o	SQLAlchemy ORM
28	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/howto/descriptor.html	Python Descriptors HowTo
29	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python-metaclasses/	RealPython: Metaclasses
30	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=txY0BuBI0qc	Advanced OOP
31	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/library/threading.html	Python Threading Library
32	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python-concurrency/	RealPython: Concurrency
33	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=PJbtBKvXHu0	Threads & Processes
34	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/library/unittest.html	Python unittest Module
35	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.pytest.org/en/stable/	Pytest Documentation
36	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=DzWng5j-Oo8	Pytest Basics
37	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/library/argparse.html	Python argparse Module
38	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://click.palletsprojects.com/	Click Documentation
39	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=ngqGM3zUogk	CLI with Argparse
40	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/glossary.html#term-decorator	Python Decorators
41	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/primer-on-python-decorators/	RealPython: Decorators
42	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=FsAPt_9Bf3U	Decorators
43	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/tutorial/modules.html	Python Modules Tutorial
44	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python-modules-packages/	RealPython: Modules & Packages
45	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=jd9hAky1At0	Modules
46	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/tutorial/errors.html	Python Error Handling
47	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python-exceptions/	RealPython: Exceptions
48	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=NG5edO-InMU	Exceptions
49	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://pandas.pydata.org/docs/user_guide/missing_data.html	Pandas Missing Data Guide
50	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://scikit-learn.org/stable/modules/compose.html#pipeline	Scikit-learn Pipelines
51	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=A_4Tlvvo5HQ	Data Cleaning
52	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://docs.python.org/3/library/functools.html#lru_cache	functools lru_cache
53	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://realpython.com/python-caching/	Python Caching Techniques
54	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.youtube.com/watch?v=nmgLIPUv82M	Profiling
55	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://fastapi.tiangolo.com/tutorial/	FastAPI Tutorial
56	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://flask.palletsprojects.com/en/stable/quickstart/	Flask Quickstart
57	2026-02-02 21:40:22.755218+00	2026-02-02 21:40:22.755218+00	https://www.djangoproject.com/start/	Django Start Guide
58	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://alembic.sqlalchemy.org/en/latest/tutorial.html	Alembic Tutorial
59	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.djangoproject.com/en/stable/topics/migrations/	Django Migrations
60	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=qqPYuylpNlo	Alembic Video
61	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-design-patterns/	Python Design Patterns
62	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://refactoring.guru/design-patterns/python	Refactoring Guru Patterns
63	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=7iDLUqX0Pp8	Patterns Overview
64	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://fastapi.tiangolo.com/tutorial/security/	FastAPI Security Tutorial
65	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-jwt-json-web-tokens/	JWT in Python
66	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=mbsmsGFHwbU	JWT FastAPI
67	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/library/asyncio.html	Python asyncio
68	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/async-io-python/	AsyncIO RealPython
69	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=suy8_5DkeYM	Asyncio Fundamentals
70	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.pytest.org/en/stable/example/parametrize.html	Pytest Parametrize Examples
71	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/pytest-python-testing/	Advanced Pytest Tutorial
72	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=F2I9pse3wmo	Advanced Pytest Video
73	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/library/subprocess.html	Subprocess Module
74	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://apscheduler.readthedocs.io/	APScheduler Documentation
75	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=3qiF2rycX9c	Cron in Python
76	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://pep8.org/	PEP8 Style Guide
77	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://black.readthedocs.io/	Black Formatter
78	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=QQ_BoyJLnAI	Black & Flake8 Tutorial
79	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/tutorial/classes.html#generators	Python Generators
80	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/introduction-to-python-generators/	Generators Introduction
81	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=bD05uGo_sfc	Generators Video
82	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://python-poetry.org/docs/	Poetry Documentation
83	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-virtual-environments-a-primer/	Python Virtual Environments
84	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=1T2I0VfSlfE	Poetry Video
85	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/library/	Python Standard Library
86	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-standard-library/	Stdlib Essentials
87	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=YYeEDnhn8qM	Stdlib Tour
88	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/library/logging.html	Python Logging Module
89	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-logging/	Logging Guide
90	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=0sOvCWFmrtA	Logging Video
91	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/library/contextlib.html	Python Contextlib
92	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-context-managers/	Context Managers Guide
93	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=a9NpvSo9k6c	Context Managers Video
94	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.docker.com/language/python/build-images/	Docker Python Guide
95	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://pythonspeed.com/articles/docker-python-sample-hello/	Docker Python Example
96	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=ngqGM3zUogk	Docker Python Video
97	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://fastapi.tiangolo.com/tutorial/bigger-applications/	FastAPI Routing Tutorial
98	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://flask.palletsprojects.com/en/stable/patterns/urlroutes/	Flask URL Routes
99	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=0sOvCWFmrtA	Routing Video
100	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://fastapi.tiangolo.com/tutorial/schema-extra-example/	FastAPI OpenAPI Example
101	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://swagger.io/docs/specification/about/	Swagger / OpenAPI
102	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=J9we6xq4V0o	OpenAPI Video
103	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://fastapi.tiangolo.com/advanced/security/	Advanced FastAPI Security
104	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/lessons/security-best-practices-python/	Python Security Best Practices
105	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=mbsmsGFHwbU	Advanced Auth Video
106	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://fastapi.tiangolo.com/tutorial/background-tasks/	FastAPI BackgroundTasks
107	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html	Celery Periodic Tasks
108	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=7t2mw8aOqc8	Background Tasks Video
109	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/library/asyncio-task.html	Asyncio Tasks and Queues
110	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/async-io-python/#concurrency-and-parallelism	Async Patterns Guide
111	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=ZzfHjytDceU	Async Patterns Video
112	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.aiohttp.org/en/stable/client_quickstart.html	aiohttp ClientSession
113	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/async-io-python/#http-requests-with-aiohttp	Async HTTP Requests
114	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=suy8_5DkeYM	aiohttp Video
115	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://packaging.python.org/tutorials/packaging-projects/	Packaging Projects
116	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-project-structure/	Python Project Structure
117	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=_J8L1NSRBr4	Packaging Video
118	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/tutorial/inputoutput.html	Python File I/O
119	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-pathlib/	Pathlib Tutorial
120	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=EhXrL9Flqhw	Pathlib Video
121	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.github.com/en/actions/quickstart	GitHub Actions Quickstart
122	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/ci-cd-git-hub-actions/	CI/CD Basics
123	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=fLkNynozbDk	GitHub Actions Video
124	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.pydantic.dev/latest/	Pydantic Documentation
125	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.django-rest-framework.org/api-guide/serializers/	DRF Serializers
126	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=0sOvCWFmrtA	Pydantic Video
127	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html	Celery Getting Started
128	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/asynchronous-tasks-with-celery/	Asynchronous Tasks with Celery
129	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=7t2mw8aOqc8	Celery Video
130	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://requests.readthedocs.io/en/stable/user/quickstart/	Requests Library Quickstart
131	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-api/	Python API Calls
132	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=tb8gHvYlCFs	API Calls Video
133	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/library/json.html	JSON Module
134	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-json/	Python JSON Guide
135	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=0sOvCWFmrtA	JSON Video
136	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/howto/unicode.html	Python Unicode Guide
137	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-encodings-guide/	Text Encodings Guide
138	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=ngqGM3zUogk	Unicode Video
139	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://developer.mozilla.org/en-US/docs/Web/HTTP	HTTP Basics
140	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://realpython.com/python-http-library/	Python HTTP Library
141	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=GzVKtHg_34U	REST Video
142	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.psycopg.org/docs/	Psycopg2 Documentation
143	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://docs.python.org/3/library/sqlite3.html	SQLite3 Module
144	2026-02-02 21:48:51.87672+00	2026-02-02 21:48:51.87672+00	https://www.youtube.com/watch?v=faFweYWkG7o	DB Drivers Video
\.


--
-- Data for Name: resources_modules_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.resources_modules_info (id, module_code, resource_id) FROM stdin;
28	python_syntax_types	1
29	python_syntax_types	2
30	python_syntax_types	3
31	numpy_basics	4
32	numpy_basics	5
33	numpy_basics	6
34	typing_mypy	7
35	typing_mypy	8
36	typing_mypy	9
37	oop_basics	10
38	oop_basics	11
39	oop_basics	12
40	functions_basics	13
41	functions_basics	14
42	functions_basics	15
43	collections_basics	16
44	collections_basics	17
45	collections_basics	18
46	control_flow_basics	19
47	control_flow_basics	20
48	control_flow_basics	21
49	pandas_basics	22
50	pandas_basics	23
51	pandas_basics	24
52	orm_basics	25
53	orm_basics	26
54	orm_basics	27
55	oop_advanced	28
56	oop_advanced	29
57	oop_advanced	30
58	concurrency_basics	31
59	concurrency_basics	32
60	concurrency_basics	33
61	unit_testing_basics	34
62	unit_testing_basics	35
63	unit_testing_basics	36
64	cli_tools	37
65	cli_tools	38
66	cli_tools	39
67	advanced_functions	40
68	advanced_functions	41
69	advanced_functions	42
70	modules_packages	43
71	modules_packages	44
72	modules_packages	45
73	error_handling_basics	46
74	error_handling_basics	47
75	error_handling_basics	48
76	data_cleaning_pipelines	49
77	data_cleaning_pipelines	50
78	data_cleaning_pipelines	51
79	caching_performance	52
80	caching_performance	53
81	caching_performance	54
82	web_framework_basics	55
83	web_framework_basics	56
84	web_framework_basics	57
85	migrations_schema	58
86	migrations_schema	59
87	migrations_schema	60
88	backend_arch_patterns	61
89	backend_arch_patterns	62
90	backend_arch_patterns	63
91	auth_security_basics	64
92	auth_security_basics	65
93	auth_security_basics	66
94	asyncio_fundamentals	67
95	asyncio_fundamentals	68
96	asyncio_fundamentals	69
97	pytest_advanced	70
98	pytest_advanced	71
99	pytest_advanced	72
100	automation_os_schedulers	73
101	automation_os_schedulers	74
102	automation_os_schedulers	75
103	code_style_linters	76
104	code_style_linters	77
105	code_style_linters	78
106	iterators_generators	79
107	iterators_generators	80
108	iterators_generators	81
109	env_poetry	82
110	env_poetry	83
111	env_poetry	84
112	stdlib_essentials	85
113	stdlib_essentials	86
114	stdlib_essentials	87
115	logging_debugging	88
116	logging_debugging	89
117	logging_debugging	90
118	context_managers	91
119	context_managers	92
120	context_managers	93
121	docker_python_apps	94
122	docker_python_apps	95
123	docker_python_apps	96
124	routing_request	97
125	routing_request	98
126	routing_request	99
127	api_docs_openapi	100
128	api_docs_openapi	101
129	api_docs_openapi	102
130	advanced_auth_security	103
131	advanced_auth_security	104
132	advanced_auth_security	105
133	background_tasks_async	106
134	background_tasks_async	107
135	background_tasks_async	108
136	async_io_patterns	109
137	async_io_patterns	110
138	async_io_patterns	111
139	async_web_clients	112
140	async_web_clients	113
141	async_web_clients	114
142	packaging_distribution	115
143	packaging_distribution	116
144	packaging_distribution	117
145	files_os_basics	118
146	files_os_basics	119
147	files_os_basics	120
148	ci_cd_basics	121
149	ci_cd_basics	122
150	ci_cd_basics	123
151	validation_serialization	124
152	validation_serialization	125
153	validation_serialization	126
154	task_queues_brokers	127
155	task_queues_brokers	128
156	task_queues_brokers	129
157	apis_integrations	130
158	apis_integrations	131
159	apis_integrations	132
160	json_serialization	133
161	json_serialization	134
162	json_serialization	135
163	text_encoding	136
164	text_encoding	137
165	text_encoding	138
166	http_rest_basics	139
167	http_rest_basics	140
168	http_rest_basics	141
169	python_db_drivers	142
170	python_db_drivers	143
171	python_db_drivers	144
\.


--
-- Name: modules_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.modules_info_id_seq', 50, true);


--
-- Name: resources_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resources_id_seq', 144, true);


--
-- Name: resources_modules_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resources_modules_info_id_seq', 171, true);


--
-- Name: modules_info modules_info_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modules_info
    ADD CONSTRAINT modules_info_code_key UNIQUE (code);


--
-- Name: modules_info modules_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modules_info
    ADD CONSTRAINT modules_info_pkey PRIMARY KEY (id);


--
-- Name: resources_modules_info resources_modules_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources_modules_info
    ADD CONSTRAINT resources_modules_info_pkey PRIMARY KEY (id);


--
-- Name: resources resources_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources
    ADD CONSTRAINT resources_pkey PRIMARY KEY (id);


--
-- Name: resources_modules_info uid_resources_m_resourc_cc9938; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources_modules_info
    ADD CONSTRAINT uid_resources_m_resourc_cc9938 UNIQUE (resource_id, module_code);


--
-- Name: resources_modules_info resources_modules_info_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources_modules_info
    ADD CONSTRAINT resources_modules_info_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resources(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

