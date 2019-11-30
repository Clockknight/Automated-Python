This program doesn't ask for any arguments in cmd, everything it needs it asks you for when it runs.

The only real restriction is that you can't select anything when it composes the mail, or it'll select something unrelated.

Enjoy!

PLAN:

Take multiple strings as inputs
 - Ask user to input text
 - Store it as a variable for later
 - Do the above twice

Using Selenium to log onto the email account
- Open up selenium to mail.com
- Enter address "https://www.gmail.com/"
- Enter the account "AutotheBoring"
- Enter the password "Idontcare"
- Submit

Composing an email
- Click "compose email" button

Applying the strings to fields like target address and message
- Apply target email variable to To field
- Apply "Sent thanks to Automated Python" in Subject
- Apply message to body field

Sending the email
- Click send button
