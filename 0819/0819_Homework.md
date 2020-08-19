# 0819_Homework

## 1. Model 반영하기

- makemigration

model을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용

- migrate

마이그레이션을 DB에 반영하기 위해 사용



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