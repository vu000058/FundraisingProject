
$( document ).ready(function() {

    $('#deleteModal').on('show.bs.modal', function(e) {
         var userId = $(e.relatedTarget).data('id');
         var username = $(e.relatedTarget).data('name');

         $(".modal-body #username").text( username );
         $(".modal-footer #deleteUser").attr("href", "/delete_user/" + userId);
    });
});