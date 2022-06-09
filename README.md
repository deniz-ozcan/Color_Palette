<p align="center">
    <img src="Brand.png" alt="App Logo" width="289px" height="260px" />
  </p>
  <h1 align="center">Bank Application</h1>
 
  <!-- TABLE OF CONTENTS -->
  <h2 id="table-of-contents">:book: Table of Contents</h2>
  <details open="open">
    <summary>Table of Contents</summary>
    <ol>
      <li><a href="#about-the-project"> ➤ About The Project</a></li>
      <li><a href="#overview"> ➤ Overview</a></li>
      <li><a href="#howtoinstall"> ➤ Overview</a></li>
      <li>
        <a href="#project-files-description"> ➤ Project Files Description</a>
      </li>
      <li><a href="#Role_1"> ➤ Role 1: Manager </a></li>
      <li><a href="#Role_2"> ➤ Role 2: Representative </a></li>
      <li><a href="#Role_3"> ➤ Role 3: Customer </a></li>
      <li><a href="#Credits"> ➤ Credits</a></li>
    </ol>
  </details>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
  <!-- ABOUT THE PROJECT -->
  <h2 id="about-the-project">:pencil: About The Project</h2>
  
  <p align="justify">
    As using Python->PyQt5 and Mysql database of bank managing, banking,
    transactions of accounts and storing them in 3NF database.
  </p>
  
  <ul>
    <li>
      In order to use the roles, 3 panels (customer, representative, bank manager)
      is designed in the interface.
    </li>
    <li>
      All required information is stored in a relational database (MSSQL, MySQL,
      PostgreSQL).
    </li>
    <li>The database is designed with 3NF optimization.</li>
    <li>All performed operations can be viewed via a GUI(Python->PyQt5).</li>
    <li>
      It can be viewed by clicking the Bank icon on the home page of the ER
      design.
    </li>
  </ul>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
  <!-- OVERVIEW -->
  <h2 id="overview">:cloud: Overview</h2>
  
  <p align="justify">
    There are 3 roles in the bank system: customer, representative and bank
    manager. Required identifying information for customers and employees
    (Name-Surname, Telephone No, Citizenship No, Address, E-mail) is stored in the
    database. A customer can have multiple accounts. Accounts can be opened in any
    currency registered in the system (₺ should come by default). Currency
    conversion should be done automatically when necessary in money transfer
    between accounts. The actions performed by the roles are outlined below. All
    these actions must be displayed visually through a designed interface.
  </p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h2 id="howtoinstall">⛓️ How to install</h2>

  <p align="justify">
    There are two way to deal with it:
  <ol>
    <li>Build an executable file with Pylance</li>
      <ul>
         <li> Open the location where all the documents are located.</li>
         <li> Click the right button while pressing the Shift key.</li>
         <li> You can see "Open powershell window here" .</li>
         <li> pyinstaller --onefile -w -i .\palette.png .\palette.py</li>
         <li> Run this line of code with Shell.</li>
         <li> You can see executable file in dist folder in that folder</li>
      </ul>
    <li>Run Main(palette.py) file with IDE</li>
   </ol>
  </p>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  <!-- PROJECT FILES DESCRIPTION -->
  <h2 id="project-files-description">📝: Project Files Description</h2>
  
  <ul>
    <li><b>palette.py</b> - Where all the main classes.</li>
    <li>
      <b>colorpalette.py</b> - Where manager form implementation generated from
      reading ui file colorpalette.ui.
    </li>
  </ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

  <!-- CREDITS -->
  <h2 id="Credits">:scroll: Credits</h2>
  
[![GitHubBadge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/canthearwhatusay)[![LinkedInBadge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deniz-%C3%B6zcan-4aa4a8162/)
