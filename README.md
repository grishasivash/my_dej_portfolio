# My DE Junior Portfolio
**Здесь я собрал в виде портфолио работы которые выполнил в процессе обучения.**

------------

### ✅ Проектирование DWH
**Задача:** описать предметную область и спроектировать хранилище данных по трем методологиям: Dimensional modeling, Data Vaulth, Anchor Modeling.

**Результат:**
1. [**Описание предматной области**](https://github.com/grishasivash/my_dej_portfolio/blob/39ea6649f7ed5cf61fe004fe56ae2db6b8236bd4/dwh_design/%D0%9F%D1%80%D0%B5%D0%B4%D0%BC%D0%B5%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%20%D0%A0%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B3%D1%80%D0%B0%D0%BD%D1%82%D0%BE%D0%B2%20%D0%B2%20%D0%A4%D0%BE%D0%BD%D0%B4%D0%B5.pdf "**Описание предматной области**")
2. ER-диаграммы: [**Dimensional modeling**](https://github.com/grishasivash/my_dej_portfolio/blob/39ea6649f7ed5cf61fe004fe56ae2db6b8236bd4/dwh_design/Dimensional%20modeling.jpg "**Dimensional modeling**"), [**Data Vault**](https://github.com/grishasivash/my_dej_portfolio/blob/39ea6649f7ed5cf61fe004fe56ae2db6b8236bd4/dwh_design/Data%20Vaulth.jpg "**Data Vault**"), [**Anchor modeling**](https://github.com/grishasivash/my_projects/blob/7e71e021c1e55ac36b403147c51db2f851fc0234/dwh_design/Anchor%20Modeling.png "Anchor modeling")

------------

### ✅  Создание витрины данных (Hadoop. YARN, MapReduce)

**Задача:** в облачном кластере скопировать в свой S3-бакет открытый датасет [NYC Yellow Taxi](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page "NYC Yellow Taxi") и написать map-reduce приложение, использующее скопированные в бакет данные и вычисляющее отчет на каждый месяц 2020 года с тремя колонками: Payment type, Month, Tips average amount.

**Результат:** [**map-reduce приложение**](https://github.com/grishasivash/my_dej_portfolio/tree/main/mapreduce "**map-reduce приложение**")

**Пояснение:** задача решалась в облачном кластере yandex.cloud

------------

### ✅  Создание витрины данных (Spark)

**Задача:** в облачном кластере скопировать в свой S3-бакет открытый датасет [NYC Yellow Taxi](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page "NYC Yellow Taxi") и написать spark приложение, использующее скопированные в бакет данные и вычисляющее отчет на каждый месяц 2020 года с тремя колонками: Payment type, Month, Average trip cost, Avg trip km cost.

**Результат:** [**spark приложение**](https://github.com/grishasivash/my_dej_portfolio/blob/cee623f91119f721614cac1ccc8e1e8f64548481/spark_job_datamart_nytaxi.py "**spark приложениее**")

**Пояснение:** задача решалась в облачном кластере yandex.cloud

------------

### ✅  Создание DAG и Operator (Airflow)

**Задача #1:** Создать DAG, который : работает с понедельника по субботу, но не по воскресеньям, ходит в GreenPlum, забирает из таблицы articles значение поля heading из строки с id, равным дню недели, складывает получившееся значение в XCom.

**Результат:** [**DAG**](https://github.com/grishasivash/my_dej_portfolio/blob/f674fc5de6371e693303778d2dcc55d56c76b34d/airflow/get_value_from_gp.py "**DAG**")

**Задача #2:** Создать DAG, который : cоздает в GreenPlum'е таблицу с названием "<название>" с полями id, name, type, dimension, resident_cnt. С помощью API (https://rickandmortyapi.com/documentation/#location) находит три локации сериала "Рик и Морти" с наибольшим количеством резидентов. Записывает значения соответствующих полей этих трёх локаций в таблицу. 

**Результат:** [**DAG**](https://github.com/grishasivash/my_dej_portfolio/blob/f674fc5de6371e693303778d2dcc55d56c76b34d/airflow/write_to_gp_from_api.py "**DAG**"), [**Operator**](https://github.com/grishasivash/my_dej_portfolio/blob/f674fc5de6371e693303778d2dcc55d56c76b34d/airflow/g_sivash_4_top3_operator.py "**Operator**")

------------

### ✅  Обучение модели для банковского скоринга и оценки заемщика (SparkML)

**Задача #1:** Используя шаблон реализовать пропущенную логику по обучению модели, для оценки благонадежности клиентов банка. Для оценки использовать метрику accuracy. Булевский тип данных необходимо привести к числовому формату.

**Результат:** [**spark приложение**](https://github.com/grishasivash/my_dej_portfolio/blob/661159d48b9ce6dcabb839ac4c52c8cb1ec022ab/spark_ml/bank_scoring.py "**spark приложениее**")

**Задача #2:** Используя шаблон реализовать пропущенную логику по обучению модели для прогнозирования значения максимальной суммы кредита, которую банк может предложить клиенту, на основе данных о нем.  Для оценки используйте метрику RMSE.

**Результат:** [**spark приложение**](https://github.com/grishasivash/my_dej_portfolio/blob/661159d48b9ce6dcabb839ac4c52c8cb1ec022ab/spark_ml/bank_credit_count.py "**spark приложениее**")

**Пояснение:** в шаблоне был построен каркас, мною был дополнен код в функциях.

------------

### ✅  Идентификация ботов среди пользовательских сессий (SparkML)

**Задача:** Есть исходный датасет с перечнем пользовательских сессий, поставлена задача реализовать классификатор таких сессии для того, чтобы отсеивать ботов показывая им капчу, но для этого необходимо понимать идентификатор подозрительной сессии (session_id). 

**Результат:** [**Обучение модели**](https://github.com/grishasivash/my_dej_portfolio/blob/661159d48b9ce6dcabb839ac4c52c8cb1ec022ab/spark_ml/bot_finder_fit.py "**Обучение модели**"),  [**Применение модели**](https://github.com/grishasivash/my_dej_portfolio/blob/661159d48b9ce6dcabb839ac4c52c8cb1ec022ab/spark_ml/bot_finder_predict.py "**Применение модели**")

------------

### ✅  Логирование эксперемента (MLFlow)

**Задача:** Сделать разметку эксперимента для трекинга процесса обучения модели в MLFlow. В разметку включены 4 метрики, 10 параметров 1 залогированная модель.

**Результат:** [**Обучение модели**](https://github.com/grishasivash/my_dej_portfolio/blob/661159d48b9ce6dcabb839ac4c52c8cb1ec022ab/mlflow/PySparkFit.py "**Обучение модели**"),  [**Применение модели**](https://github.com/grishasivash/my_dej_portfolio/blob/661159d48b9ce6dcabb839ac4c52c8cb1ec022ab/mlflow/PySparkPredict.py "**Применение модели**")

------------

### ✅  Разработать задачу по анализу данных (Data Quality) (SparkML, PyDeequ)

**Задача:** От внешней системы-источника вам поставляются данных о доступных товаров обуви. Используя возможности pydeequ разработайте задачу по анализу данных (используя AnalyzerContext) и сохранения отчета с анализом в папку (согласно report_path).

Проанализируйте следующие  условия:
1) Размер датасета
2) Полноту всех колонок (x9)
3) Уникаольность id
4) Присутствуют ли записи со скидкой меньше 0
5) Присутствуют ли записи со скидкой больше 100
6) Присутствуют ли записи с доступным количеством на складе меньше 0
7) Присутствуют ли записи с количеством предзаказов меньше 0

**Результат:** [**Процесс анализа**](https://github.com/grishasivash/my_dej_portfolio/blob/661159d48b9ce6dcabb839ac4c52c8cb1ec022ab/pydeequ/PySparkAnalayzer.py "**Процесс анализа**")

------------
