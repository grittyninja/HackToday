 <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="/roro">Musicality</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item <?php echo empty($_GET['p']) || $_GET['p'] === 'home' ? 'active':''; ?>">
              <a class="nav-link" href="/roro">Home</a>
            </li>
            <li class="nav-item <?php echo $_GET['p'] === 'popular' ? 'active':''; ?>">
              <a class="nav-link" href="#">Popular</a>
            </li>
            <?php if(!$islogin): ?>
              <li class="nav-item <?php echo $_GET['p'] === 'login' ? 'active':''; ?>">
                <a class="nav-link" href="login">Login</a>
              </li>
              <li class="nav-item <?php echo $_GET['p'] === 'register' ? 'active':''; ?>">
                <a class="nav-link" href="register">Register</a>
              </li>
            <?php else: ?>
              <li class="nav-item <?php echo $_GET['p'] === 'profile' ? 'active':''; ?>">
                <a class="nav-link" href="profile">Profile</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="logout" id="logout">Logout</a>
              </li>
            <?php endif; ?>
          </ul>
        </div>
      </div>
    </nav>