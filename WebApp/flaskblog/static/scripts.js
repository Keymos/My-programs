function confirmDelete(taskId) {
            var confirmMessage = "Are you sure you want to delete this task?";
            if (confirm(confirmMessage)) {
                // If user confirms, submit the form
                var form = document.querySelector('#delete-form-' + taskId);
                form.submit();
            }
        }


document.addEventListener("DOMContentLoaded", function () {
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