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

      $('#ava').change(function(){
        var ava = $('#ava').val();
        var expression = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi;
        var regex = new RegExp(expression);

        if(!ava.match(regex)){
          $('#probtn').attr('disabled', true);
          alert("Please enter valid URL!");
        }else{
          $('#probtn').removeAttr('disabled');
        }
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