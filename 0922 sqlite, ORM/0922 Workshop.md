# 0922 Workshop

## 1번.

```sqlite
CREATE TABLE countries(
    id INTEGER PRIMARY KEY, 
    room_num TEXT NOT NULL,
    check_in TEXT NOT NULL,
    check_out TEXT NOT NULL,
    grade TEXT NOT NULL,
    price INTEGER NOT NULL
);
```



## 2번.

```sqlite
INSERT INTO countries
VALUES
(1,'B203','2019-12-31','2020-01-03','suite',900),
(2,'1102','2020-01-04','2020-01-08','suite',850),
(3,'303','2020-01-01','2020-01-03','deluxe',500),
(4,'807','2020-01-04','2020-01-07','superior',300);
```



## 3번.

```sqlite
ALTER TABLE countries
RENAME TO hotels;
```



## 4번.

```sqlite
SELECT room_num, price
FROM hotels
ORDER BY price DESC
LIMIT 2;
```



## 5번.

```sqlite
SELECT COUNT(*)
FROM hotels
GROUP BY grade
ORDER BY COUNT(*) DESC;
```



## 6번.

```sqlite
SELECT *
FROM hotels
WHERE room_num LIKE 'B%' OR grade='deluxe';
```



## 7번.

```sqlite
SELECT price
FROM hotels
WHERE room_num NOT LIKE 'B%' and check_in='2020-01-04'
ORDER BY price ASC;
```

