// Wait for the DOM content to fully load before executing the script
document.addEventListener("DOMContentLoaded", function () {
    fetchCompanies();  // Fetch and display company data
    fetchEmployees(); // Fetch and display employee data
});
// Function to fetch company data from the server and populate the company table
function fetchCompanies() {
    fetch("/companies/") // Make a request to the companies endpoin
        .then(response => response.json()) // Convert the response to JSON
        .then(data => {
            let tableBody = document.getElementById("companyTableBody"); // Get table body element
            tableBody.innerHTML = ""; // Clear existing table content

             // Loop through the received company data and add rows to the table
            data.forEach(company => {
                tableBody.innerHTML += `
                    <tr>
                        <td>${company.name}</td>
                        <td>${company.location}</td>
                        <td>${company.type}</td>
                    </tr>
                `;
            });
        })
        .catch(error => console.error("Error fetching companies:", error)); // Handle errors
}

// Function to fetch employee data from the server and populate the employee table
function fetchEmployees() {
    fetch("/employees/") // Make a request to the employees endpoint
        .then(response => response.json()) // Convert the response to JSON
        .then(data => {
            let tableBody = document.getElementById("employeeTableBody"); // Get table body element
            tableBody.innerHTML = ""; // Clear existing table content

            // Loop through the received employee data and add rows to the table
            data.forEach(employee => {
                tableBody.innerHTML += `
                    <tr>
                        <td>${employee.name}</td>
                        <td>${employee.email}</td>
                        <td>${employee.company}</td>
                    </tr>
                `;
            });
        })
        .catch(error => console.error("Error fetching employees:", error)); // Handle errors
}
}
