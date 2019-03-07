
$( document ).ready(function() {

    $('#deleteModal').on('show.bs.modal', function(e) {
         var goalId = $(e.relatedTarget).data('id');

         $(".modal-footer #deleteGoal").attr("href", "/delete_goal/" + goalId);
    });
});