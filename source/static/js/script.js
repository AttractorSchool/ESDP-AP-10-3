const table = document.getElementById('tenderTable');
if(table){
const cells = table.getElementsByTagName('td');
for(let i = 0; i < cells.length; i++) {
    const cell = cells[i];
    if(cell.textContent.trim() === 'None') {
        cell.textContent = ' ';
    }
}
}
