

// Xóa tìm kiếm gần đây
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.btn-remove').forEach(button => {
        button.addEventListener('click', function () {
            this.closest('li').remove();
        });
    });
});

function previewImage(event) {
    const input = event.target;
    const preview = document.getElementById('imagePreview');
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        }
        reader.readAsDataURL(input.files[0]);
    } else {
        preview.src = '#';
        preview.style.display = 'none';
    }
}