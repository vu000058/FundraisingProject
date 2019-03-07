
$( document ).ready(function() {

    $('#deleteModal').on('show.bs.modal', function(e) {
         var eventId = $(e.relatedTarget).data('id');
         var eventName = $(e.relatedTarget).data('name');

         $(".modal-body #eventName").text( eventName );
         $(".modal-footer #deleteEvent").attr("href", "/delete_event/" + eventId);
    });
});