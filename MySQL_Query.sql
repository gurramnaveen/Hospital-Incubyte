CREATE TABLE <country_name>(
	CustomerName VARCHAR(255) NOT NULL,
	CustomerID VARCHAR(18) PRIMARY KEY,
	CustomerOpenDate DATE NOT NULL,
	LastConsultedDate DATE,
	VaccinatedType CHAR(5),
	DoctorConsulted CHAR(255),
	State CHAR(5),
	PostCode INT(5),
	DateOfBirth DATE,
	ActiveCustomer CHAR(1));