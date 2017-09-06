    <!-- Footer -->
    <footer class="footer py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Musicality 2017</p>
      </div>
      <!-- /.container -->
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="static/vendor/jquery/jquery.min.js"></script>
    <script src="static/vendor/inputmask/jquery.inputmask.bundle.min.js"></script>
    <script src="static/vendor/popper/popper.min.js"></script>
    <script src="static/vendor/bootstrap/js/bootstrap.min.js"></script>

    <script>
      $(document).ready(function(){
        $('#bd').inputmask("99/99/9999");
      });

      $('#logout').click(function(e){
        e.preventDefault();
        $.ajax({
          type: 'post',
          url: 'logout',
          success: function(data){
            window.location.reload();
          }
        })
      });
    </script>