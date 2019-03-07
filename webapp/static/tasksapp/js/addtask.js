
$( document ).ready(function() {

    var $assigneeDropdown = $("#assignee");

    $("#section").change(function () {
        $assigneeDropdown.prop("disabled", true);
        var sectionId = $(this).val();
        var url = '/assignees/';

          $.ajax({
              type: 'GET',
              url: url,
              data: {
                  'sectionId': sectionId
              },
              success: function (data) {
                  $assigneeDropdown.html(data);
                  $assigneeDropdown.prop("disabled", false);
              }
          });
    });
});