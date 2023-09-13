{% extends 'base.html' %}
{% block title %}Signup{% endblock title %}
{% block content %}


<h1 class="text-dark">welcome</h1>

<div class="card bg-light p-5">
  {% for message in messages %}
  <div class="alert alert-{{messages.tags}}  alert-dismissible fade show" role="alert" role="alert">
    <strong>{{message}}</strong>
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
  {% endfor %}
  
  <h3 class="text-dark">Signup</h3>

  <form action="/auth/signup/" method="post">
    {% csrf_token %}
    <br />

    <label for="email">Email</label>
    <div class="form-group">
      <input
        type="email"
        class="form-control p-1"
        id="email"
        name="email"
        required
      />
    </div>
    <label for="pass1">Password</label>
    <div class="form-group">
      <input
        type="password"
        class="form-control p-1"
        id="pass1"
        name="pass1"
        required
      />
    </div>

    <label for="pass2">Password</label>
    <div class="form-group">
      <input
        type="password"
        class="form-control p-1"
        id="pass2"
        name="pass2"
        required
      />
    </div>
    <br />
    <button type="submit" class="btn btn-dark">SignIn</button>
    <br />
    Already User? <a href="/auth/login/">Login</a>
    <br />
  </form>
</div>

{% endblock content %}
