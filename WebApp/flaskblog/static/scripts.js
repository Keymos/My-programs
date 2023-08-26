function confirmDelete(taskId) {
    var confirmMessage = "Are you sure you want to delete this task?";
    if (confirm(confirmMessage)) {
        // If user confirms, submit the form
        var form = document.querySelector('#delete-form-' + taskId);
        form.submit();
    }
}

document.addEventListener("DOMContentLoaded", function () {
    // make the checked / uncheck update the Task.isDone accordingly on refresh
    var checkboxes = document.querySelectorAll(".task-checkbox");

    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {
            var taskId = this.id.split("-")[1];
            var isDone = this.checked;

            updateTaskStatus(taskId, isDone);
        });
    });

    // Function to update the status of a task (mark as done or not done)
    function updateTaskStatus(taskId, isDone) {
    // Create a new XMLHttpRequest object to make an HTTP request
    var xhr = new XMLHttpRequest();
    
    // Specify the HTTP method (POST) and the URL for the request
    xhr.open("POST", "/toggle_task_status/" + taskId, true);
    
    // Set the Content-Type header to specify that we're sending JSON data
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    
    // Define a function to run when the HTTP request is complete (onload)
    xhr.onload = function () {
        // Check if the request is complete and the response status is 200 (OK)
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Find the HTML element (checkbox) for the task by its ID
            var taskElement = document.querySelector("#checkbox-" + taskId);
            
            // If the task element exists in the HTML
            if (taskElement) {
                // Update the checked attribute of the checkbox based on isDone
                taskElement.checked = isDone;
            }
        }
    };
    
    // Create a JSON string containing the data to send in the request
    var data = JSON.stringify({ isDone: isDone });
    
    // Send the HTTP request with the JSON data
    xhr.send(data);
    }
});
    

// Preload the current time in the task adding part
document.addEventListener("DOMContentLoaded", function () {
    var currentDate = new Date();

    var dateInput = document.querySelector("[name='date_due_date']");
    var timeInput = document.querySelector("[name='date_due_time']");

    dateInput.value = (
        ("0" + currentDate.getDate().toString()).slice(-2) + "/" +
        ("0" + (currentDate.getMonth()+1).toString()).slice(-2) + "/" +
        currentDate.getFullYear().toString().substr(-2));
    timeInput.value = (
    ("0" + currentDate.getHours().toString()).slice(-2) + ":" +
    ("0" + currentDate.getMinutes().toString()).slice(-2)); // Months are 0-indexed
});
