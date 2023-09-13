{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>
{% block title %}{% endblock title %}
    
  </title>
  <meta content="ecommerce website we deliver product in 1 hours" name="description">
  <meta content="ecommerce" name="amazon,flipkart,selling,products">

 
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="{% static '/assets/vendor/bootstrap/css/bootstrap.min.css' %}" rel="stylesheet">
  <link href="{% static '/assets/vendor/bootstrap-icons/bootstrap-icons.css' %}" rel="stylesheet">
  <link href="{% static '/assets/vendor/boxicons/css/boxicons.min.css' %}" rel="stylesheet">
  <link href="{% static '/assets/vendor/glightbox/css/glightbox.min.css' %}" rel="stylesheet">
  <link href="{% static '/assets/vendor/remixicon/remixicon.css' %}" rel="stylesheet">
  <link href="{% static '/assets/vendor/swiper/swiper-bundle.min.css' %}" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="{% static '/assets/css/style.css' %}" rel="stylesheet">


</head>

<body>

  <!-- ======= Header ======= -->
  <header id="header" class="fixed-top ">
    <div class="container d-flex align-items-center justify-content-between">


      <!-- Uncomment below if you prefer to use an image logo -->
<a href="/" class="logo"><img src="{% static 'assets/img/logo.png' %}" alt="" class="img-fluid">ShopSage</a>

      <nav id="navbar" class="navbar">
        <ul>
          <li><a class="nav-link scrollto active" href="/">Home</a></li>
          <li><a href="/blog">Blog</a></li>
          <li><a class="nav-link scrollto" href="/about">About</a></li>
          <li><a class="nav-link scrollto" href="/about">Orders</a></li>
          <li><a class="nav-link scrollto" href="/about">My Profile</a></li>
          <li class="dropdown"><a href="#"><span>SignIn</span> <i class="bi bi-chevron-down"></i></a>
            <ul>
              <li><a href="/auth/signup/">Sign Up</a></li>
              <li><a href="/auth/login/">Login</a></li>
              <li><a href="/auth/logout/">Logout</a></li>
            </ul>
          </li>
          <li><a class="nav-link scrollto bg-danger p-2 m-2" href="/contact">Cart</a></li>
          <li><a class="nav-link scrollto bg-dark p-2 m-2" href="/contact">Contact</a></li>
          
        </ul>
        <i class="bi bi-list mobile-nav-toggle"></i>
      </nav><!-- .navbar -->

    </div>
  </header><!-- End Header -->

  <!-- ======= Hero Section ======= -->
  <section id="hero">
    <div class="hero-container">

      {% block content %}
      
      
      
      {% endblock content %}
    </div>
  </section><!-- End Hero -->

  <main id="main">

    {% block body %}
    

    {% endblock body %}

  
  </main><!-- End #main -->

  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Vendor JS Files -->
  <script src="{% static '/assets/vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>
  <script src="{% static '/assets/vendor/glightbox/js/glightbox.min.js' %}"></script>
  <script src="{% static '/assets/vendor/isotope-layout/isotope.pkgd.min.js' %}"></script>
  <script src="{% static '/assets/vendor/swiper/swiper-bundle.min.js' %}"></script>
  <script src="{% static '/assets/vendor/php-email-form/validate.js' %}"></script>

  <!-- Template Main JS File -->
  <script src="{% static '/assets/js/main.js' %}"></script>

</body>

</html>