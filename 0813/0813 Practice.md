# 0813 Practice

## Responsive Web

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <link rel="stylesheet" href="shop.css">
  <link href="https://fonts.googleapis.com/css2?family=Baloo+Tamma+2:wght@800&display=swap" rel="stylesheet">
  <title>Title</title>
</head>
<body>
  <!-- nav -->
  <nav class="navbar d-flex navbar-light bg-white fixed-top">
    <a class="navbar-brand flex" href="#">
      SAMSUNG
    </a>
    <ul class="d-flex align-items-center mb-0 list-unstyled">
      <li class="mx-3"><a class="text-dark font-weight-bold text-decoration-none" href="" style="font-family : 'Baloo Tamma 2'">Contact</a></li>
      <li class="mx-3"><a class="text-dark font-weight-bold text-decoration-none" href="" style="font-family : 'Baloo Tamma 2'">Cart</a></li>
      <li class="mx-3"><a class="text-dark font-weight-bold text-decoration-none" href="" style="font-family : 'Baloo Tamma 2'">Login</a></li>
    </ul>
  </nav>

  <div class="container">
    <!-- section -->
    <section class="d-flex justify-content-center pt-3">
      <img class="img-fluid" src="./images/main.png" alt="main">
    </section>

    <!-- article -->
    <article class="d-flex flex-column align-items-center">
      <p class="font-weight-bold text-center display-5 m-5">Our New Products</p>
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
        <div class="col mb-4">
          <div class="card justify-content-center mb-0">
            <a href="">
              <img src="./images/buds.jpg"
              class="card-img-top" alt="...">
            </a>
            <div class="card-body">
              <h5 class="card-title text-center">Buds</h5>
              <p class="card-text text-center">179,000</p>  
            </div>
          </div>
        </div>
        <div class="col mb-4">
          <div class="card justify-content-center mb-0">
            <a href="">
              <img src="./images/buds.jpg"
              class="card-img-top" alt="...">
            </a>
            <div class="card-body">
              <h5 class="card-title text-center">Buds</h5>
              <p class="card-text text-center">179,000</p>  
            </div>
          </div>
        </div>
        <div class="col mb-4">
          <div class="card justify-content-center mb-0">
            <a href="">
              <img src="./images/buds.jpg"
              class="card-img-top" alt="...">
            </a>
            <div class="card-body">
              <h5 class="card-title text-center">Buds</h5>
              <p class="card-text text-center">179,000</p>  
            </div>
          </div>
        </div>
        <div class="col mb-4">
          <div class="card justify-content-center mb-0">
            <a href="">
              <img src="./images/buds.jpg"
              class="card-img-top" alt="...">
            </a>
            <div class="card-body">
              <h5 class="card-title text-center">Buds</h5>
              <p class="card-text text-center">179,000</p>  
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- footer -->
    <footer class="d-flex justify-content-center mt-4 mb-5 p-0 fixed-bottom">
      <a class="mx-2" href="https://instagram.com">
        <img src="./images/instagram.png" alt="" width="45">
      </a>
      <a class="mx-2" href="https://facebook.com">
        <img src="./images/facebook.png" alt="" width="45">
      </a>
      <a class="mx-2" href="https://twitter.com">
        <img src="./images/twitter.png" alt="" width="45">
      </a>
    </footer>
  </div>
  
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/5opper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>

```



```css
/* 아래에 코드를 작성하시오. */

body {
    height: 1000px;
    margin-top: 80px;
    margin-bottom: 150px;
}

.section {
    height: 600px;
    background-image: url(./images/main.png);
    background-position: center;
    background-size: cover;
}
```





![](practice/result.JPG)