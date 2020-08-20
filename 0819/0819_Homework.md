# 0819_Homework

## 1. Model 반영하기

- python manage.py makemigrations

model을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용

- python manage.py showmigrations

migration이 DB에 반영이 됐는지 확인하는 명령어

- python manage.py migrate

마이그레이션을 DB에 반영하기 위해 사용

- python manage.py sqlmigrate

DB에 작동되는 SQL문을 확인할 때 쓰는 명령어



## 2. Model 변경사항 저장하기

```sqlite
CREATE TABLE "new__articles_articles" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL);       
INSERT INTO "new__articles_articles" ("id", "title", "content") SELECT "id", "title", "content" FROM "articles_articles";
DROP TABLE "articles_articles";
ALTER TABLE "new__articles_articles" RENAME TO "articles_articles";
COMMIT;
```



## 3. Python Shell

```bash
python manage.py shell
```





## 4. Django Model Field

- BooleanField
- CharField
- DateField
- DateTimeField
- DecimalField