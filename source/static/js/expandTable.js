let tenderCells = document.querySelectorAll('.tender-cell');

tenderCells.forEach(function(cell) {
    cell.addEventListener('click', function() {
        if (this.classList.contains('expanded')) {
            this.classList.remove('expanded');
        } else {
            this.classList.add('expanded');
        }
    });
});
