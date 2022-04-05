# DE Junior Portfolio
**Здесь я собрал работы которые я выполнил в процессе обучения и постарался оформить их в виде портфолио.**

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
