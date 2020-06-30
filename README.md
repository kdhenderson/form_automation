# form_automation
This project tests the functionality of an online form using Selenium as a tool for browser automation.

This is what the program does step-by-step:
  - Creates an instance of the browser with a webdriver using the Selenium package.
  - Navigates to the URL to test with the get method.
  - Uses assert method to confirm the html contains expected text via the title and page_source properties.
  - Locates the user input box, clears it and automates typing a message, with the find_element_by_id, clear and send_keys methods.
  - Locates a button by class name and simulates clicking it.
  - Uses the CSS selector to grab the output, and asserts that the text is correct.
  - Pauses briefly for demo purposes and then closes the browser window.


Dependencies:
  - Install the requirements using pip install -r requirements.txt.
	- Make sure you use Python 3.
	- You may want to use a virtual environment for this.
  - You will also need the chromedriver.

Usage:
  - Run the program from the command line.