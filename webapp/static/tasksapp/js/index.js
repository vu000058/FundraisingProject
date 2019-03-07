
$( document ).ready(function() {

    $('#deleteModal').on('show.bs.modal', function(e) {
         var taskId = $(e.relatedTarget).data('id');
         var taskName = $(e.relatedTarget).data('name');

         $(".modal-body #taskName").text( taskName );
         $(".modal-footer #deleteTask").attr("href", "/delete_task/" + taskId);
    });

     $('#taskDetailsModal').on('show.bs.modal', function(e) {
         var taskNameDetail = $(e.relatedTarget).data('name');
         var taskCreator = $(e.relatedTarget).data('creator');
         var taskAssignee = $(e.relatedTarget).data('assignee');
         var taskDue = $(e.relatedTarget).data('due');
         var taskStatus = $(e.relatedTarget).data('status');
         var taskDelegator = $(e.relatedTarget).data('delegator');
         var taskUpdated = $(e.relatedTarget).data('updated');
         var taskDescription = $(e.relatedTarget).data('description');

         $("#taskDetailsModal #taskNameDetail").text('Name: ' + taskNameDetail );
         $("#taskDetailsModal #taskCreator").text( 'Creator: ' + taskCreator );
         $("#taskDetailsModal #taskAssignee").text('Assignee: ' + taskAssignee );
         $("#taskDetailsModal #taskDue").text('Due Date: ' + taskDue );
         $("#taskDetailsModal #taskStatus").text('Status: ' + taskStatus );
         $("#taskDetailsModal #taskDelegator").text('Delegator: ' + taskDelegator );
         $("#taskDetailsModal #taskUpdated").text('Updated on: ' + taskUpdated );
         $("#taskDetailsModal #taskDescription").text('Description: ' + taskDescription );

    });
});