document.addEventListener('DOMContentLoaded', () => {
    const datasetSelect = document.getElementById('dataset-select');
    const dataDisplay = document.getElementById('data-display');
    const yearRange = document.getElementById('year-range');
    const yearValue = document.getElementById('year-value');

    datasetSelect.addEventListener('change', updateDataDisplay);
    yearRange.addEventListener('input', updateYearValue);

    function updateDataDisplay() {
        const selectedDataset = datasetSelect.value;
        let displayContent = '';

        switch(selectedDataset) {
            case 'organized-crime':
                displayContent = '<p>Data from the Organized Crime Index will be displayed here...</p>';
                break;
            case 'theft-rate':
                displayContent = '<p>Data from the Theft Rate By Country will be displayed here...</p>';
                break;
            default:
                displayContent = '<p>Please select a dataset to view the data.</p>';
        }

        dataDisplay.innerHTML = displayContent;
    }

    function updateYearValue() {
        yearValue.textContent = yearRange.value;
        // Update data display based on year range filter
    }

    // Initialize with the default dataset
    updateDataDisplay();
});
