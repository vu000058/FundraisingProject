
$( document ).ready(function() {

    $('#deleteModal').on('show.bs.modal', function(e) {
         var taskId = $(e.relatedTarget).data('id');
         var taskName = $(e.relatedTarget).data('name');

         $(".modal-body #taskName").text( taskName );
         $(".modal-footer #deleteTask").attr("href", "/delete_task/" + taskId);
    });
});