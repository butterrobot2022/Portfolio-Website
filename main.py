from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
    
    
# Html Code
# Index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Personal Portfolio Website!</title>
    <link rel=”stylesheet” href=”https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css”>
    <link rel="stylesheet" href="static/styles.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
</head>

<body>
{% block nav %}
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{{ url_for('home') }}">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{{ url_for('about') }}">About</a>
        </li>
          </ul>
  </div>
      </nav>
{% endblock %}
    <div class="head text-secondary">

<!--    <img src="https://th.bing.com/th/id/R.584fe37bf550e0f873d29a45a4e483d8?rik=bSDPO%2btLIv1gBw&riu=http%3a%2f%2fgetwallpapers.com%2fwallpaper%2ffull%2f8%2fe%2f4%2f375689.jpg&ehk=2N%2f%2bJg%2fKfuvAjQZk8jP9eTtoq2X29gNM5ukP1vYVDBs%3d&risl=&pid=ImgRaw&r=0" height="150">-->

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.min.js" integrity="sha384-IDwe1+LCz02ROU9k972gdyvl+AESN10+x7tBKgc9I5HFtuNz0wWnPclzo6p9vxnk" crossorigin="anonymous"></script>
    <br>
    <br>
    <br>
    <br>
    <br>
        <h1>Welcome!</h1>
        <h1>I'm Tlotlo.</h1>
        <h1>Nice to meet you!</h1>
</div>
<div class="body">
    <div class="first">
<!--        <img src="static/R (1)-modified.png" height="150" class="image">-->
        <h3>Projects that I've built😊:</h3>
    </div>

    <div class="container text-center">
  <div class="row">
    <div class="col order-last">
      <img src="static/data-modified.png" height="150" class="image">
        <h3>Data Science:</h3>
            <li><a href="#"><span>Linear Regression to Predict housing prices in Boston</span></a></li>
            <li><a href="#"><span>Multivariate Regression analysis on crime data</span></a></li>
            <li><a href="#"><span>Image color extractor website</span></a></li>
            <li><a href="#"><span>Numpy array Manipulation and Image Processing</span></a></li>
    </div>
    <div class="col">
      <img src="static/html-modified.png" height="150" class="image">
        <h3>Web Development:</h3>
            <li><a href="#"><span>Blog Website built with Flask</span></a></li>
            <li><a href="#"><span>Portfolio Website</span></a></li>
            <li><a href="#"><span>Cafe and Wi-Fi Website</span></a></li>
            <li><a href="#"><span>Image color extractor website</span></a></li>
            <li><a href="#"><span>Tindog Website-i.e Tinder for dogs!</span></a></li>
    </div>
    <div class="col order-first">
      <img src="static/OIP (2)-modified.png" height="150" class="image">
        <h3>Python:</h3>
            <li><a href="#"><span>Automated forex news tracker</span></a></li>
            <li><a href=""><span>Automated Data Job entry bot</span></a></li>
            <li><a href="#"><span>Text-to-Morse code converter</span></a></li>
            <li><a href="#"><span>Typing speed test GUI with Python tkinter</span></a></li>
            <li><a href="#"><span>Converting PDF file to audiobook with Python</span></a></li>
            <li><a href="#"><span>Breakout Shooting Game with Python Turtle</span></a></li>
    </div>

  </div>
</div>
</div>

<div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">

      <div class="carousel-item active">
      <img src="https://th.bing.com/th/id/R.32a5a951f98fbe0273fcb50e56147311?rik=n25JDICrcJ4fHQ&pid=ImgRaw&r=0" height="500" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Trading news and Data Entry Bot!</h5>
      </div>
    </div>
    <div class="carousel-item">
      <img src="https://th.bing.com/th/id/R.01310a0a61ccf43b96d062886a30fed2?rik=pbeZ%2fl3PMbhrhQ&pid=ImgRaw&r=0&sres=1&sresct=1" height="500" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Blog website</h5>
      </div>
    </div>
      <div class="carousel-item">
      <img src="https://opengameart.org/sites/default/files/sample_57.png" height="500" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Breakout Game!</h5>
      </div>
    </div>

  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
<br>
<br>

<div class="touch">
    <h2 class="git">Get in touch!</h2>
    <div class="container text-center">
  <div class="row">
    <div class="col">
       <svg xmlns="http://www.w3.org/2000/svg" width="30" height="25" fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16">
 <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
    </svg>
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="25" fill="currentColor" class="bi bi-facebook" viewBox="0 0 16 16">-->
        <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>-->
        </svg>
         <svg xmlns="http://www.w3.org/2000/svg" width="30" height="25" fill="currentColor" class="bi bi-instagram" viewBox="0 0 16 16">
  <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"/>
    </svg>

    <a href="#"><i class="bi bi-twitter"></i></a>
        <a href="#"><i class="bi bi-facebook"></i></a>
        <a href="#"><i class="bi bi-instagram"></i></a>
    </div>
  </div>
</div>




</div>


</body>
</html>

#About.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About me</title>
  <link rel=”stylesheet” href=”https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css”>
    <link rel="stylesheet" href="static/styles.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
</head>

<body>
   <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{{ url_for('home') }}">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{{ url_for('about') }}">About</a>
        </li>
          </ul>
  </div>
      </nav>
<div class="about_me text-secondary">
        <h1>A few interesting facts</h1>
        <h1>about me!</h1>


</div>
   <div class="body">
    <div class="first">
        <h3>About Me:</h3>
    </div>
    <div class="description">
    <p class=>I am fluent in Hebrew and semi-fluent in Japanese!</p>
    <p>My hobbies include: playing guitar and practising martial arts.</p>
    <p>I am a Python Developer, and an aspiring machine learning engineer, and data scientist.</p>
    <p>"The journey of a thousand miles begins with a single step" Let's get in touch!</p>
        </div>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.min.js" integrity="sha384-IDwe1+LCz02ROU9k972gdyvl+AESN10+x7tBKgc9I5HFtuNz0wWnPclzo6p9vxnk" crossorigin="anonymous"></script>
<br>
<br>
 </div>

<div class="touch">
    <h2 class="git">Get in touch!</h2>
    <div class="container text-center">
  <div class="row">
    <div class="col">
       <svg xmlns="http://www.w3.org/2000/svg" width="30" height="25" fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16">
 <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
    </svg>
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="25" fill="currentColor" class="bi bi-facebook" viewBox="0 0 16 16">-->
        <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>-->
        </svg>
         <svg xmlns="http://www.w3.org/2000/svg" width="30" height="25" fill="currentColor" class="bi bi-instagram" viewBox="0 0 16 16">
  <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"/>
    </svg>

    <a href="#"><i class="bi bi-twitter"></i></a>
        <a href="#"><i class="bi bi-facebook"></i></a>
        <a href="#"><i class="bi bi-instagram"></i></a>
    </div>
  </div>
</div>
</div>
</body>
</html>


# Css Code
#Styles.css

.about {
    text-align: left;
    margin-left: 1300px;
    font-family: 'Comic sans MS';
    background-color: transparent !important;
}

.head {
    text-align: center;
    background-image: url('https://backiee.com/static/wpdb/wallpapers/1920x1080/179836.jpg');
    background-attachment: fixed;
    background-size: cover;
    height: 600px;
}

h1{
    font-size: 450% !important;
    font-family: 'Brush Script MT', cursive;
    margin-top: 50;
    text-align: center;
    color: white;
    font-weight: bold;
}

body {
    margin: 0;
}
.info {
    text-align: right;
    margin-right: 20px;
    color: white;
    font-weight: bold;
}

.first {
    text-align: center;
    margin-top: 30px;

}
.body {
    background-color: #64C8FA;
    padding-top: 25px;
}
.work {
    text-align:center;
}
.p1 {
    margin-right: 500px;
}
 h3 {
    text-align: center;
 }

h5 {
    text-align: center;
    margin-top: 70px;
}

.touch {
    background-color: #6495ED;
    color: white;
    margin-top: -48px;
}

.git {
    text-align:center;
}

.ul {
    margin-right: 500px;
}

.about_me{
    text-align: center;
    background-image: url('https://th.bing.com/th/id/R.2176426d741e02302479c4c917d0a7b9?rik=I5s2x%2bkSrF4%2blA&riu=http%3a%2f%2fwallpapercave.com%2fwp%2fwp1833712.jpg&ehk=b1B4BkU763xYNt321pDjNZv5ms15p27V3PAopfKPuJE%3d&risl=&pid=ImgRaw&r=0');
    background-attachment: fixed;
    background-size: cover;
    height: 600px;
}

.description {
    text-align: center;
}

.ico {
    display: block;
}

.navbar-brand{
    text-align: right;
}
    
