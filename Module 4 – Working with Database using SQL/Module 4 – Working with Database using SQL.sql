CREATE DATABASE MarketCo;
USE MarketCo;

CREATE TABLE Company (
  CompanyID INT PRIMARY KEY AUTO_INCREMENT,
  CompanyName VARCHAR(45) NOT NULL,
  Street VARCHAR(45),
  City VARCHAR(45),
  State VARCHAR(2),
  Zip VARCHAR(10)
);

INSERT INTO Company (CompanyName, Street, City, State, Zip) VALUES
('Toll Brothers', '250 Gibraltar Rd', 'Horsham', 'PA', '19044'),
('Urban Outfitters, Inc.', '5000 S Broad St', 'Philadelphia', 'PA', '19112'),
('Apple', '1 Apple Park Way', 'Cupertino', 'CA', '95014'),
('Tesla', '3500 Deer Creek Rd', 'Palo Alto', 'CA', '94304');


CREATE TABLE Contact (
  ContactID INT PRIMARY KEY AUTO_INCREMENT,
  CompanyID INT,
  FirstName VARCHAR(45),
  LastName VARCHAR(45),
  Street VARCHAR(45),
  City VARCHAR(45),
  State VARCHAR(2),
  Zip VARCHAR(10),
  IsMain BOOLEAN,
  Email VARCHAR(45),
  Phone VARCHAR(12),
  CONSTRAINT fk_contact_company
		FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

INSERT INTO Contact (CompanyID, FirstName, LastName, Street, City, State, Zip, IsMain, Email, Phone) VALUES
(1, 'Dianne', 'Connor', '10 Pine St', 'Horsham', 'PA', '19044', TRUE,  'dianne@tollbrothers.com', '215-555-1111'),
(1, 'Mark',   'Hill',   '12 Pine St', 'Horsham', 'PA', '19044', FALSE, 'mark@tollbrothers.com',   '215-555-2222'),
(2, 'Nora',   'Smith',  '50 Broad St','Philadelphia','PA','19112', TRUE,'nora@urban.com',        '215-555-3333'),
(3, 'Rahul',  'Patel',  '1 Infinite','Cupertino','CA','95014', TRUE,'rahul@apple.com',          '408-555-4444');

CREATE TABLE Employee (
  EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
  FirstName VARCHAR(45),
  LastName VARCHAR(45),
  Salary DECIMAL(10,2),
  HireDate DATE,
  JobTitle VARCHAR(25),
  Email VARCHAR(45),
  Phone VARCHAR(12)
);

INSERT INTO Employee (FirstName, LastName, Salary, HireDate, JobTitle, Email, Phone) VALUES
('Jack',   'Lee',   65000, '2022-01-10', 'Sales Rep',   'jack.lee@marketco.com',   '215-555-7777'),
('Lesley', 'Bland', 72000, '2021-09-15', 'Account Mgr', 'lesley.bland@marketco.com','215-555-0000'),
('Maya',   'Shah',  80000, '2020-03-05', 'Manager',     'maya.shah@marketco.com',  '215-555-9999');


CREATE TABLE ContactEmployee (
  ContactEmployeeID INT PRIMARY KEY AUTO_INCREMENT,
  ContactID INT,
  EmployeeID INT,
  ContactDate DATE,
  Description VARCHAR(100),
  CONSTRAINT fk_ce_contact
    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID),
  CONSTRAINT fk_ce_employee
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

INSERT INTO ContactEmployee (ContactID, EmployeeID, ContactDate, Description) VALUES
(1, 1, '2024-01-05', 'Intro call regarding new housing project'),
(1, 2, '2024-01-08', 'Pricing discussion and follow-up'),
(2, 1, '2024-02-01', 'Sent proposal via email'),
(3, 3, '2024-02-10', 'Partnership meeting scheduled'),
(1, 1, '2024-03-01', 'Follow-up call - Dianne with Jack');  -- We'll delete this in Q6

/*4*/
UPDATE Employee
SET Phone = '215-555-8800'
WHERE FirstName = 'Lesley' AND LastName = 'Bland';

SELECT * FROM Employee WHERE FirstName='Lesley' AND LastName='Bland';
    
/*5*/    
UPDATE Company
SET CompanyName = 'Urban Outfitters'
WHERE CompanyName = 'Urban Outfitters, Inc.';

SELECT * FROM Company WHERE CompanyID = 2;

/*6*/
SELECT CE.ContactEmployeeID, C.FirstName, C.LastName, E.FirstName, E.LastName, CE.ContactDate, CE.Description
FROM ContactEmployee CE
JOIN Contact C ON CE.ContactID = C.ContactID
JOIN Employee E ON CE.EmployeeID = E.EmployeeID
WHERE C.FirstName='Dianne' AND C.LastName='Connor'
  AND E.FirstName='Jack' AND E.LastName='Lee';
  
DELETE FROM ContactEmployee
WHERE ContactEmployeeID = 5;

/*7*/
SELECT DISTINCT E.FirstName, E.LastName
FROM Employee E
JOIN ContactEmployee CE ON E.EmployeeID = CE.EmployeeID
JOIN Contact C ON CE.ContactID = C.ContactID
JOIN Company Co ON C.CompanyID = Co.CompanyID
WHERE Co.CompanyName = 'Toll Brothers';

/*8*/

SELECT * FROM Employee WHERE FirstName LIKE 'J%';  -- starts with J
SELECT * FROM Employee WHERE FirstName LIKE '_a%'; -- second letter is a


/*10*/

SELECT C.FirstName, C.LastName, Co.CompanyName
FROM Contact C
JOIN Company Co ON C.CompanyID = Co.CompanyID;

/*12*/
SELECT E.FirstName, E.LastName, CE.ContactDate
FROM Employee E
LEFT JOIN ContactEmployee CE ON E.EmployeeID = CE.EmployeeID;
