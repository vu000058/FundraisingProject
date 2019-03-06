
$( document ).ready(function() {

    $('#deleteModal').on('show.bs.modal', function(e) {
         var sectionId = $(e.relatedTarget).data('id');
         var sectionName = $(e.relatedTarget).data('name');

         $(".modal-body #sectionName").text( sectionName );
         $(".modal-footer #deleteSection").attr("href", "/delete_section/" + sectionId);
    });
});