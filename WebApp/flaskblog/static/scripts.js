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

    function updateTaskStatus(taskId, isDone) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/toggle_task_status/" + taskId, true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.onload = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var taskElement = document.querySelector("#checkbox-" + taskId);
                if (taskElement) {
                    taskElement.checked = isDone;
                }
            }
        };
        var data = JSON.stringify({ isDone: isDone });
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
