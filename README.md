# Senior_Capstone_Project











Final Report 
for
Grocery Logger (Gro-Log)



Prepared by:
Zack Luckman
Olisa Omekam
Rehan Ayoub
Aaron Turner

ZORA


Table of Contents
1.0 Introduction	3
1.1 Purpose	3
1.2 Scope	3
1.3 Definitions, Acronyms, Abbreviations	3
1.3.1 Definitions	3
1.3.2 Acronyms	3
1.3.3 References	4
1.4 Overview	4
2.0 Design Details	5
2.1 System Decomposition	5
2.2 UML Diagrams	6
2.2.1 Class Diagram	6
2.2.2 Use Case Diagrams	7
2.2.3 Sequence Diagrams	9
3.0 Implementation Details	10
3.1 Implementation Overview	10
3.2 Hardware	10
3.3 Software	11
3.3.1 Development System	11
3.4 Implementing Gro-Log	11
3.5 Implementation Testbed	12
3.6 Completed Functionalities	13
3.6.1 GUI	13
3.6.2 Database	17
3.6.3 Online APIs	19
3.7 Removed Functionalities	20
3.8 Implementation Issues / Technical Issues	21
3.8.1 ListView and RecycleView	21
3.8.2 API Limitation	23
4.0 Detailed Contributions	23



Disclaimer: This document is written with the intention to help users and developers understand how Grocery Logger (Gro-Log) functions internally. Access to this document does not entitle you to the rights of the ideas set forth. All credit and rights belong to the creators of Grocery Logger on Team Zora.
1.0 Introduction
1.1 Purpose
This document is meant to give all existing and remaining information regarding the final demo and the associated Gro-Log application not covered in any previous documents. Any questions or details arising from the final demo and remaining functionalities to be implemented since the last demo are covered and explained within this document.

	1.2 Scope
This document explains any changes made throughout the semester on this project. Our team’s use of the agile development method in developing the Grocery Logger device.  Additionally, this document lays out a detailed representation of how Grocery Logger functions in a kitchen setting.This includes the key techniques implemented, as well as completed functionalities, remaining functionalities, implementation issues, and an analysis of team member contributions.

	1.3 Definitions, Acronyms, Abbreviations
1.3.1 Definitions
Graphical User Interface: The front-end portion of the program that the user views and interacts with directly using the touchscreen display.
Quick Response Code: A matrix barcode embedded with product details that can be scanned by the barcode scanner attached to the Raspberry Pi.
Dongle: A small piece of hardware that connects to another device to provide it with additional functionality.
Raspberry Pi 3: A lightweight, low-powered piece of hardware comprising of all the basic components of a full size computer motherboard including I/O ports for attachments.

	1.3.2 Acronyms
BDB: Barcode Database
FDB: Food Database
FR: Functional Requirements
GUI: Graphical User Interface
NFR: Non-Functional Requirements
OS: Operating System 
RP3: Raspberry Pi 3
SRS: Software Requirements Specification
UCD: Use Case Diagram
Gro-Log: Short for Grocery Logger

	1.3.3 References
GitHub Repository for Senior Capstone Project:
Gro-Log repository link

SQLite Database:
https://www.sqlite.org/docs.html

Raspberry Pi Setup and Configuration:
https://www.raspberrypi.org/documentation/

Barcode Lookup API:
https://www.barcodelookup.com/api

Recipe Search API:
https://developer.edamam.com/edamam-recipe-api

Kivy Doc:
https://kivy.org/doc/stable/gettingstarted/intro.html

1.4 Overview
Grocery Logger (Gro-Log) is a kitchen-friendly device granting the power of a grocery store inventory logger to the convenience of your home. It is comprised of an intuitive touch-screen interface, Raspberry Pi 3B, and a barcode scanner. 
Gro-Log was created with the intention to help individuals easily manage their inventory of food. This device stores the names of food items scanned in via barcode scanner or inputted via keyboard and prompts the user to enter its expiration dates. The device allows users to search recipes for the items that are selected in their inventory and display the ingredients of the recipe to the user. Gro-Log will also display to the user how many food items are expiring soon in an effort to prompt them to consume these items in a timely manner as to negate the loss of food due to expiration.
For the common scenario of having multiple roommates that want to keep track of their own distinct food items, there is the ability to create separate profiles each containing their own unique inventory. The item’s information is stored in the associated food database of the selected user’s.

2.0 Design Details

2.1 System Decomposition

Our system is comprised of five components: Python, Kivy, SQLite, Barcode Lookup API, and Edamam Recipe Search API. Python is used by importing both Kivy, an open source Python library used for developing multitouch application software with a natural user interface, and SQLite, a relational database management system which is embedded into the program and stored locally on the RP3. Kivy GUI events that invoke Kivy functions are also used to make queries to the SQLite database as well as invoking various created Python methods. Invoked Kivy functions also trigger API request calls to both the Barcode Lookup database as well as the Edamam Recipe Search database.
2.2 UML Diagrams


2.2.1 Class Diagram



Gro-Log class diagrams did not change that much over the the course of development but classes and methods were added. Our initial software design specifications were made such that the classes were abstract. The class that changed considerably during development was the database class, the core of the system. This class was made without taking into account mandatory functions that were added as we found out during the undertaking of development of the database for Gro-Log. The addition of the GUI class was added to the class diagram because of the interactions between the other classes allowed for much easier functionality. This screenshot of our class diagram better represents the system much closer to the actual implementation. Each of the five classes interact with the Food Database class and User Profile Database class, Recipe Search API class and Food Database class are displayed to the user by the GUI class now that the system is developed and functional.
2.2.2 Use Case Diagrams

This use case diagram has been created to show the functionalities the user has access to upon opening the application: creating a new profile, choosing an existing profile and possible options to use when viewing a food inventory.

This use case diagram has been created to further show the functionalities of what kind of manipulation the user can do with items in their database. If no items exist in the database, the user can add items in various ways: manually enter a barcode number, scan in an item barcode with a barcode scanner, or add a non-barcoded item (such as apples) and optionally entering in the expiration dates for each method. Once items exist in the database, the user has the ability to select one or more items and either search recipes containing these items or delete them from the inventory and the user’s subsequent food database.







2.2.3 Sequence Diagrams

In the first sequence, the user will press the New Profile button and choose to either enter the name of the profile or cancel. Cancel will return the user back to the Profile Screen. The Create Profile button will then query the SQLite Database to create a new profile and will return to the Profile Screen and repopulate the Profile Screen with the new profile. 
In the second sequence, the user can select a profile from the screen and press the Delete Profile button in the Main Menu Screen and will prompt the user with a confirmation screen. If the user still chooses to delete the profile, the button will query the SQLite Database to remove the profile and will return to the Profile Screen and repopulate the Profile Screen without the new profile. The user can also press Cancel on the Confirmation popup and will return to the Main Menu Screen of the selected profile.


In the first sequence, the user will press the Add Item button on the Main Menu Screen or Inventory Screen and the user can input a barcode number and press the Submit button. The Submit button will run the function that makes the Barcode Lookup API call and return the item name of the inputted barcode number and make a query to the SQLite database to add the item info and will update the displayed inventory. The user can also press the Other button and input the corresponding information which will make a query to the SQLite database to add the item info and will update the displayed inventory.
In the second sequence, the user will press the Delete button from the Inventory Screen and will make a query to the SQLite database to remove the item’s info which will update the displayed inventory.In the third sequence, the user will select item(s) from the displayed inventory in the Inventory Screen and press the Search Recipes button which will make an API call to the Edamam Recipe Lookup and display the results of the recipe in the View Recipe Screen.

3.0 Implementation Details
3.1 Implementation Overview
In an effort to complete the creation of Gro-Log, the following steps were taken to maximize efficiency and balance work responsibilities. 

The work was first divided between the members of Zora corresponding to their programming knowledge history with each section. The project was split into three main categories, those being GUI, Database, and Online API calls. The setup of the hardware was done first, a fairly simple task. Raspbian OS needed to be available to boot from on the RP3 and there were two options available: use a properly formatted, bootable flash drive with an OS installed or configure a microSD card to use as the boot drive. We went with the latter and formatted a microSD card to the correct format, transferred the OS files, and inserted the microSD card. Following on screen prompts finalized the OS installation. For the other hardware, an iPad with a server connection using VNC for the touch-input device and barcode scanner were both of a “plug and play” setup. After these steps had been made, we each worked on our respective sections independently and then integrated them to get one cohesive device that is suitable for a kitchen countertop.

3.2 Hardware
Raspberry Pi 3 B (RP3): This device computes the application side, connects to internet, hosts the VNC server (prototype only), connects to the barcode scanner, and stores the database and program source code locally on a microSD card
Touchscreen: Connects to, displays, and controls the RP3 (iPad for prototype)
Barcode scanner: Allows user to scan barcode rather than manually entering the barcode number
3.3 Software
Raspbian OS: Operating system for the Raspberry Pi 3 B
Python 3: The basis programming language for the project application side in which all functionality will be developed with
SQLite: Allows for the creation and manipulation of the users’ databases through Python, storing them in local files
Kivy: Allows for the project application side to be interacted with through a user interface with interactive buttons and data fields that handle data manipulation and pass data to the database
VNC Viewer: Allows for connection to the Raspberry Pi from touchscreen device through internet connection (prototype only)
3.3.1 Development System
VS Code: Text editor used in writing code as well as the ability to run a python debugger.
GitHub: A web-based repository hosting service with version control through the use of Git.
3.4 Implementing Gro-Log
Implementing our system requires Python 3, Kivy version 1.10.1 (GUI module), SQLite 3, a barcode scanner, touch screen interface, and a Raspberry Pi 3 B (RP3). The main middleware code connects all of these different modules, input devices.


Required Modules



The above picture indicates the libraries, packages, and modules in the Python file required to develop and run the Gro-Log application.

Commonly used imported libraries, packages, and modules are explained below:
kivy.app library allows for integration with the Python GUI framework Kivy
kivy.uix.button package allows for creating button widgets that can be bound to an action
kivy.uix.screenmanager package allows for our system to consist of multiple screens that can be traversed through
kivy.uix.popup package allows for creating popup screen-based widgets
kivy.uix.label package allows for creating label widgets to display text on screen or popup
kivy.uix.listview package allows for interaction with the ListView widget
kivy.adapter package allows for creating the ListView widget
json package converts the returned result from the online APIs to a json object
SQLite_test is the created module to help with the interaction between Python and SQLite

3.5 Implementation Testbed

For each new process and functionality created for the Gro-Log program, a simple pattern for testing was adopted by each member. The new addition was incrementally black box test by others to an agreed upon functionality, then eventually moved each addition into our implementation file and tested them together with the existing program.

Each new component being added to the program was first designed by a member of our team assigned to the delegated task. While creating their addition, each member tested their code as it was being created through means of negative testing. Checking for invalid inputs while making sure it met the necessary requirements.

Once they had validated to themselves that their addition met the requirements, they uploaded it to Github for others in the group to run black box testing on. In this stage, other members of the group took the potentially new addition and tested it randomly in attempts to crash or break their code into an unintended result. If an error was found, the creator of said code would fix their section to specifically handle that error, returning it to the black box testing phase.

After the code passed the black box testing phase it was then moved to the Implementation Testing folder in GitHub and integrated with the rest of the existing code. If the addition did not integrate fluidly with the rest of the program, the developer who created it was then responsible to meet with other team members who may understand why or where to integrate the new code. Eventually every module was added to the Integration Testing folder, resulting in a fully working program. 

For final testing, Gro-Log was implemented on the Raspberry Pi, connecting to an iPad through VNC viewer, and connection a barcode scanner over a USB cable. The application was then loaded and ran on the device running against different premade test cases conceived along the way during creation.

This system was then deemed suitable as our final prototype in which we presented for our final demonstration.

3.6 Completed Functionalities
	3.6.1 GUI
	Splash Screen
The Splash Screen is what a user first sees when launching the program after booting their device. It is used as a space to initialize any non existing databases if they are not already created as well as creating the screen manager class in which any necessary widgets are initially added. The screen is just one big button so a press on any part of it will pass the user to the Profile Select Screen.








Profile Select Screen
The Profile Selection Screen is able to add users, dynamically sizing the buttons to take up the entire screen in an attempt to appeal more to a touchscreen-based interface. When the Add New Profile button is pressed, the user is passed to the Profile Creation Screen. With database support through use of SQLite, the Profile Select Screen is created on entry based upon the current contents of the DB file.




Profile Creation Screen
The Profile Creation Screen is a simple popup featuring a text box, prompting the user to enter their name. On entering the Profile Creation Screen, the text box is cleared and focused on to allow the user to immediately begin typing their name. A Create button and Cancel button are also displayed which both switch back to the Profile Select Screen. They differ by having the Create button add the name to the profile database, and the Cancel button does not add the user to the profile database.




Main Menu Screen
The Main Menu Screen is able to be navigated to by selecting a profile from the Profile Select Screen. Upon entry, the chosen profile’s name is welcomed at the top to ensure the user that they are on the correct profile. On this screen, the user has access to two main buttons relating to their food items. The Add Item button takes the user to the Add Item Screen and the View Food Inventory button will take the user to the screen that shows all the food items that have currently been inputted by the user. The user also has the option to return to the Profile Select Screen by pressing on the Switch Profile button at the bottom of the screen. Next to the Switch Profile button, the Delete Profile button allows the user to delete the current profile along with their associated food database, triggering a confirmation popup if pressed. At the very bottom of the screen is a banner that displays to the user the number of items they have expiring in the next seven days.


View Food Inventory Screen
The View Food Inventory Screen displays to the user the current contents of their entered items. The Add button has the same functionality as the Add Item button on the Main Menu Screen, taking the user to the Add Item Screen. With a selected item or items, pressing the Delete button will remove the selection from the database while pressing the Search Recipe button will direct the user to the Search Recipe Screen, passing along the selected contents. Header buttons adorn the inventory table, indicating each columns’ contents. The Back to Main Menu button takes the user back to the main menu screen. 


Add Item Screen
The Add Item Screen is fully integrated with the Barcode Lookup API. The text input box for accepting the barcode either via scanning an item or manually inputting it is in place and the user is then optionally able to input an expiration date for this item. Pressing the Submit button transfers an inputted item’s information from the online Barcode Lookup API, granted that it exists in the API database, and adds it into the item database for that specific profile. If the user wishes to add a non-barcoded item to their inventory, pressing the Other button will take them to the Add Other Item Popup to input this information. The Cancel button functions by taking the user back to the View Food Inventory Screen without adding anything to the database.






Add Other Item Popup
The Add Other Item Popup allows the user to add a non-barcoded item to the database. The user is then optionally able to input the expiration date for this other item and then press the Submit button to pass it to the database which will then show on the View Inventory Screen. The Cancel button returns the user to the Add Item Screen.







Search Recipe Screen
The Search Recipe Screen is populated upon pressing the Search Recipes button with selected items in Inventory Screen. It references the selected item’s JSON object values and passes them through the search_recipes() function, creating an array of strings, each containing a different recipe. These are then displayed one at a time with each recipe’s name displayed at the top on a banner. The user is then able to navigate through the different recipes via the arrow buttons near the top of the screen. To go back to the inventory screen, the user simply presses the Back to Inventory button.



3.6.2 Database
Database Backend
The database backend has been created as well as any helper functions needed to access the data. The database will be created on first start up and stored as files on the RP3. The helper functions are written in python and will be called when necessary to manipulate and produce data for the front end GUI to display and interact with.
Functions created include:

create_connection() - Creates a connection to the database file, resulting creating one if the database file name does not exist  


profile_table_setup() - Initializes the necessary databases on first startup



create_profile(name) - Adds a user to the profiles database and creates them a corresponding user database


delete_profile(name) - Deletes a user from the profiles database given a username


select_all_profiles() - Selects the current contents of the profiles database


count_exp(name) - Query searches a user’s database for all items and tallies up the number of item


select_inventory(name) - Query selects the user’s database for all of its contents, creating a padded string and passing the array along as an array


add_inventory(name,item_info) - Adds an item’s barcode, name, and expiration date the user’s database


add_other_inventory(name,item_info) - Adds an “other” type item to a user’s database given the item name and expiration date 


delete_inventory(name, item_name) - Deletes an item from a user’s database given the corresponding barcode


select_profile_db(name) - Query searches the profile database for the corresponding user database name

3.6.3 Online APIs
Barcode Lookup API
Barcodes are able to be manually entered or scanned from the barcode scanner which acts as a input device. After the barcode number is entered, the user can press the Search button on the Add Item Screen. Using the function def search_item(self,barcode_number)that takes in the inputted barcode number from the text input field, a Get request is sent to the Barcode Lookup API. If the request call is successful and the status response is 200, the returned results are stored in a JSON object and then the item name is extracted.



Edamam Recipe Search API
The Recipe Search API was implemented successfully after creating a trial API account and adding the associated app ID and key for that account (which is required to make an API call) to the API calling function. As we now have it, the Recipe Search API transfers at most 10 recipes containing any items selected in the user’s inventory. The app ID and key used in the function def search_recipes(self) allows access for 500 calls to the API a year. Our system assumes the rest of the ingredients required for a listed recipe besides selected items are available. After successful requests with this API calling function, the results are again stored in a JSON object and each individual recipe is referred to on the Search Recipe Screen.



The below figure shows the graph for our API calls using the search recipe API. With this kind of metric and the more API calls requested, this data can be used to determine the most popular time of the year that people look up recipes, which is helpful for research purposes.

 



3.7 Removed Functionalities
Sorting Functionality
As time was not permitting, we did not implement the ability to sort items in a user’s inventory based on soonest expiring items and alphabetically by item name. The way that we would have done it would be to have the items sorted differently in the database first and then repopulate the inventory screen after a user presses one of the inventory header buttons to display the inventory items in a different order.


Expiring Items on Main Menu
We altered the ability for the user to be shown expiring items on the main menu screen. We initially planned to have an expiring item banner that showed the user various items in the inventory that would could loop through the names of the top 3 soonest expiring items and the date they would expire. Kivy does not have built-in functionality for a widget with scrolling text so an alternative option to implement this could possibly consist of the names and dates of the top 3 soonest expiring items populated on nicely formatted buttons or labels to display to the user. As of now, it only lists the number of items that will be expiring soon (within 7 days).

Triple ListView Implementation
We removed the triple ListView implementation of a user’s item inventory considering using a single ListView is more memory efficient than using three separate ListViews. Because of this, each item has a row dedicated to that item’s attributes and anywhere on the row is able to be selected so that item can be used to search recipes or be deleted. Using the triple ListView implementation gave the user the ability to select any combination of cells from the three different ListViews which would not make sense to do. A user would have been able to select the name of the first item in the inventory, the expiration date of the second item, and the barcode of the third item. 

Random Recipes based on Inventory
It would not be hard to implement but we did not have time to add the ability to show the user random recipes based on expiring food in their inventory. This would just require the top expiring items in the database to automatically be selected and search recipes containing those items either collectively or individually with an alternate search recipe button and show the user on the existing view recipes screen.

3.8 Implementation Issues / Technical Issues
3.8.1 ListView and RecycleView
Initial ListView Implementation
We initially implemented the inventory in three separate ListViews to contain all 3 item attributes for each item displayed to the user for their inventory of items. Even though each item in the cells of the ListViews would be nicely formatted and centered below their respective header button, populating three separate ListViews was a bit sluggish on the RP3 as each individual cell is a separate selectable widget. Because of this, we toyed with the idea of scrapping ListView (which is a deprecated module in Kivy 1.10 and later) and instead use RecycleView which is a bit more memory efficient and would benefit our system running on the low-powered RP3, especially if a user has a large amount of items in their inventory. 

Selection in RecycleView
Unfortunately, RecyleView acts more like an interactive Kivy label widget and does not come with native support for selecting items in a list as a widget like ListView does. The workaround was to create a function that enabled the ability to change the background color of a RecyleView item on pressing it so as to simulate the item being a selectable button. We ended up sticking with a single ListView which has fully native support for multiple item selection.


Selecting Multiple Items in ListView
With the initial implementation of ListView, only one item at a time could be selected, which posed a problem with a core functionality of our system: selecting multiple items in a user’s inventory to search recipes containing those items. After further testing and research, changing an attribute of ListView toggled the ability from selecting one item to multiple items. This resulted in the breaking of a few of the other function in which were meant to pull the selected items, forcing us to spend time fixing them.

Separating the Kivy Code
When it came to the GUI for our system, we had the option to embed Kivy code directly into the main Python file for our system. This required importing the Kivy Builder class and lengthened the overall Python file tremendously as the entire codebase existed in a single file. Separating the Kivy code out into its own .kv file seemed more ideal to be able to quickly view different screens and widgets without looking through Python code as well. This required a specific naming scheme to link the Kivy code automatically with the main Python file by naming it “GroceryLoggerApp.py” and the linked .kv file similarly named but without the “App” and all lowercase: “grocerylogger.kv” At first, the Python file defined classes and methods for the functionality on each of the different screens as well as building the screen manager class that handled the application itself; the Kivy file created and formatted the screens and widgets as well as called methods based on user interaction.

Populating Items in ListView
There was a small issue of figuring out how to display a different item database per user on the inventory screen so that an entirely different inventory would populate for one user versus another. Creating the ListView in the .kv file initialized the ListView to be static and built the inventory upon starting the application which would be problematic if more than one user existed. The solution to this problem was by embedding the Kivy code for creating a ListView into a Python method with slightly different syntax than in the .kv file. We then call that method upon entering the inventory screen. This allows the ListView to populate for that specific user and update the ListView with any new items that the database now contained for their profile.


Alternate Profile Screen Implementation with ListView
After coming up with the low-fidelity prototype of the Application, we initially tried to implement the profile screen identically to this first version. Using the Kivy BoxLayout layout to format widgets in a certain layout, buttons were arranged and adjusted in size on screen depending on how many profiles were in the database. We ran into some problems with how the application handles creating these buttons for new profiles and adjusting the pre-existing buttons for other profiles, as well as handling how the application gives the user a prompt for a creating a new profile. In the initial design, a user would press the Add New Profile button on the Profile Selection screen and be greeted with a popup that prompted them to enter a profile name. Upon pressing submit, a new entry would be made in the profile database, a new empty inventory would be created for that profile, and the Profile Selection screen would update to reflect this new profile with a button that would adjust in size to fit with the other buttons on screen. Being able to repopulate the Profile Selection screen after pressing submit on this popup proved problematic so an alternate profile screen with an entirely different layout was made, implemented in ListView. With this implementation, profiles were no longer buttons but selectable widgets in a scrollable list and a user would simply select their profile and press the Select Profile button above the list to enter their profile. A new profile textbox existed at the top of the screen that had immediate focus on opening the application, prompting the user to enter a new profile name if it did not already exist and a corresponding create button. The user would also have the option to select a profile and then hit a small delete button at the bottom of the screen to remove their profile and corresponding inventory from the database.

3.8.2 Recipe Search API Limitation

Determining Keywords from Item Name
The current Barcode Lookup API that we are currently using passes very specific item names to to the database. As a result, using them is hard for the Recipe Search API to find a match in some cases. This was the best API we could use (accounting for limited project budget and using a free API trial account). Since there was limited time to complete the project, it was not possible to develop an algorithm to single out any keywords in a scanned in item in the string returned from the Barcode Lookup API. Therefore, the string was parsed as is and transferred into the database. When a Recipe Search API call is used on that item, the item name element of the JSON object is passed to the Recipe Search API which is able to recognize the inputted item and return all the recipes containing that specific item, with more specific item names returning less recipes.

4.0 Detailed Contributions

Zachariah Luckman:

Set up of Python and Kivy on the RP3 to allow for the program to run
Creation of all Python functions that allow for SQLite database connection, creation, data selection, and data manipulation used throughout the program
Profile Screen data refreshing
Profile delete functionality
Main Menu expiration banner data counting
Add item submission functionality
ListView population and alteration for inventory screen per user
Inventory Screen data referencing
Inventory Screen string creation
Inventory Screen data parser to pass to outside functions
Data manipulation and passing between Inventory Screen and API requests
VNC Viewer Setup
Ordering of the hardware


Olisa Omekam: 

Setup and installed Kivy on the RP3
Setup Python 3 on RP3
Profile Screen
Profile Screen functionality
Create New Profile Screen
Create New Profile functionality
Search Recipe Screen
Search Recipe Screen functionality
Functionality to take recipe names and recipe ingredients into a data structure
Splash Title Screen
Item Expiration Banner
Welcome Banner
Welcome Banner functionality
Add Profile functionality
Profile Delete Confirmation functionality
Current User functionality


Rehan Ayoub:
Integrating the search_item() function with the Search button in the GUI using Barcode Lookup API
Adding the url and concatenation of item to the URL
Error handling of the API calls such as checking for the right input string format 
Checking status codes such as Status 200, 201,404 (Not Found)
Changing the content of returned result to json format in order to parse to other function such as the GUI and database.
Integrating the search_recipes() function to the Search Recipes button using the Edamam Recipe Search API
Concatenating app ID and app key with an inputted item to the URL
Converting the returned results to a JSON object
Looping through the JSON object and printing recipes with the dishname

David (Aaron) Turner:
Initialization of RP3 and microSD card 
Configuration with Raspbian OS
VNC Viewer testing
Alternate Profile Screen (type A)
Alternate Profile Screen functionality
Main Menu Screen layout
Main Menu Screen transition
Inventory Screen layout 
Development with search_recipe API function 
Development with search_item API function
Add Item Screen layout
Add Item Screen functionality 
Item Expiration date functionality
Add Item Popup layout
Add Item Popup functionality
Other Item Expiration date functionality
