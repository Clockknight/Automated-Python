This program should:

Take two strings, one for a target email address, one for a message.

Use Selenium to log onto a prepared email and send the message string to the target email address.



Needed:

Take multiple strings as inputs
 - Ask user to input text
 - Store it as a variable for later
 - Do the above twice

Using Selenium to log onto the email account
- Open up selenium to mail.com
- Enter address "https://www.mail.com/"
- Click log in button
- Enter the account "AutotheBoring"
- Enter the password "Idontcare"
- Submit

Composing an email
- Click "compose email" button

Applying the strings to fields like target address and message
- Apply target email variable to To field
- Apply message to body field
- Apply "Sent thanks to Automated Python" in Subject

Sending the email
- Click send button
