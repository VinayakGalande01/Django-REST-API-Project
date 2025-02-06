document.addEventListener("DOMContentLoaded", function () {
    fetchCompanies();
    fetchEmployees();
});

function fetchCompanies() {
    fetch("/companies/")
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("companyTableBody");
            tableBody.innerHTML = "";
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
        .catch(error => console.error("Error fetching companies:", error));
}

function fetchEmployees() {
    fetch("/employees/")
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("employeeTableBody");
            tableBody.innerHTML = "";
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
        .catch(error => console.error("Error fetching employees:", error));
}
