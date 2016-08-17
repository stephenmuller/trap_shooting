# **Score Keeper**

### Product Overview
The core focus of this app is to keep track of scores and information about trap shooting. It will allow a player to easily log scores and relavent details (eg. shells, weather, location) to look for trends that show over time. 

### Specific Functionality

**Main Page:**
  * login/username - advanced goal
  * Longest streak
  * Users last score

**Player page:**
  * Time-sorted list of rounds
  * Place to add shotgun/shell/location data
  * Basic statistics, hit %, average score, best score, longest streak

**Round Page:**
  * 5x5 grid of target pictures, clickable to set hit/miss, hit by default
  * Ability to just input a score by # EG. 23 or 4, 5, 3, 5, 5 without specific orders
  * Drop downs/menus/etc for relavent details
   * Shells
   * Gun
   * Location
   * Weather
   * External conditions/excuses (wind, lighting, busy day, etc)
   * save/autosave functionality?

**Group page:**
 * Ability to score 5 games simultaneously (the max amount of people in a squad)

## Data Model
The app will need to store a handful of very spefic things:
 * The 'player'/user
 * details about a specific round:
   * date/time
   * location
   * a score, represented by an integer or 25 booleans
   * type of shells used (TBD how specific this will get)
   * shotgun used

## Technical Components
In order to keep the front end simple, fast, and easy the pages will all be done in JS using basic HTML elements and images. For example the score input will take either a 5x5 grid of clay targets that are by default set to 'hit' (Eg an image like: [broken clay.jpg](http://mickleyhall.com/wp-content/uploads/2015/05/clay-pigeon-shooting.jpg))

Data Model

What are the persistent "nouns" you need to save across pages in your project MVP? What do they represent?

We'll be using a relational database which models things like a spreadsheet. There are fixed fields and every instance

How do you need to search for specific instances of nouns?

Technical Components

What are the "moving parts" of your MVP? What are the things like "modules" you're going to write? How do they talk to each other?

Make decisions here and now. Do research and prototyping to figure out what libraries and technologies will help you solve your problems. Write up which ones you'll use. It's okay if they end up not working and you have to change your plans.

This is more specific than "Django backend, CSS style, etc." Please specify what specific technical problems you'll have to solve and a guess at the solution.

Schedule

Write out the order in which you will tackle your technical components of your MVP.

What are the easy parts? What are the hard parts? Can you guess how long you'll take for each?

Work on the tough and crucial parts first.

Further Work

All of the above parts are just addressing your MVP. Here you should outline other features you'd like to implement if you get "done" early. Order them by importance towards your high-level goal and what order you'll work on them later.

Don't work on any of these features until all of MVP is complete.

