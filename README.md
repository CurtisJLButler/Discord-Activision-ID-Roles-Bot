# Discord-Activision-ID-Roles-Bot
Creates roles for users to display Activion IDs

### /setid (ActivisionID)
This saves the username of the account you use the command along with your Activision ID (replace "(ActivisionID)" with your actual Activision ID)

### /getid (optional:username)
This grabs the Activision ID of the discord user if it is in the database (Has to be someone in this server that has set their Activision ID using /setid as above)  
if you type /getid without specifying a user, it will return your Activision ID instead of someone elses

### /updateid (ActivisionID)
This allows users to update their Activision ID's if they were incorrectly inputted into the database, or if they have updated their username on Call of Duty

### /delid (ActivisionID)
This allows users to delete their Activision ID's from the database.  
In this case you still have to enter your Activision ID so that you don't accidentaly delete your username. It's just a little accident prevention

## Future stuff
I plan to add a semi feature rich log applet to this
  
The server I'm hosting this on has a free option, but to prevent going over the monthly limits
I will be setting a limit on how many times a day someone can access the database (i.e. setting their Activision ID, getting an Activision ID...)
This will not effect accessing logs as the logs will be stored locally on the server
##

All of the app files are stored in the app folder  
Anything outside of that is for a server website to load the bot (Haven't gotten that part working quite yet)
