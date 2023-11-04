function displayEditForm(taskId) {
    const form = document.getElementById('editForm-' + taskId);
    form.style.display = form.style.display == 'none' ? 'block' : 'none';
}
