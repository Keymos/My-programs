# Thrive Program

## Description
A todo web app basically. The point is to learn flask, and other webdev technlogies needed for the project.
The main thing is the versatility and the ability for me personally to gather my data and analyse it seperately.


## Planned

- Make a minimum viable product. So that I can start using it, putting in todos and such.

**Tasks:**
what it should contain:
  - ~~id~~
  - mother task (if needed)
  - sub-tasks
  - ~~title~~
    - add validation for title
  - ~~description~~
  - due time
    - ~~add the attribute~~ 
    - ~~If both date and time are empty, they both don't register~~
    - ~~If only time is filled, then check if it is still not too late today, if yes, add today's date automatically~~
    - ~~If only date is filled, then the time is automatically set to 00:00~~
    - so that you can't make todo.date_due.time() == time(0, 0) → validation 
    - ~~status (done/no)~~
    - add:
      - If both date and time are empty, they both don't register
      - If only time is filled, then check if it is still not too late today, if yes, add today's date automatically
      - If only date is filled, then the time is automatically set to 00:00
  - reminder
    - add the reminder attribute
      - yes / no (reminder), checkbox
      - if yes, show an add reminder buttom (each click add a reminder)
        - when clicked, displays the date and time of the reminder
        - later make it show something like "1 day before", "15 minutes before"...
        - small delete cross to remove if needed
  - make a big drop down window that show the advanced options:
    - Repeat (y/n) → on _[days]_ or _x_ times every _y_ * _u_ (units [days, weeks, months])
    - reward (skill xp + pts)
    - skills
      - add the skills idea in general first
      - drop down menu to choose from skills (skill attribute is optional)
    - include duration
    - tags = categories ( might not need?)

- Make is so that when clicking on a title, a page open up to edit the task
- Something like a drop down menu, where only like the last 10 tasks done show.

  **Skills**
  - option to manage skills:
    - add skills
    - edit skills
    - delete skills
      - confirmation
  - each skill has a level and and xp bar
  - the xp ammount needed to level up from level 2 to 3 is the x1.5 ammount needed to rise from level 1 to 2
  - show the skills graph in the left winow
=======
>>>>>>> parent of 0f4bc15 (Update README.md)
=======
>>>>>>> parent of 0f4bc15 (Update README.md)
