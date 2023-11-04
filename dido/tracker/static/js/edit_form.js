function displayEditForm(taskId) {
    var form = document.getElementById('editForm-' + taskId);
    form.style.display = form.style.display == 'none' ? 'block' : 'none';
}
