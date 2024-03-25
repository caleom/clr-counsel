# Clr Counsel

![Clr Counsel]()

___

Site description

It is a fullstack diary site that allows users to make diary entries, create an account and see them later.

Link to live site - [https://clr-counsel-eeabdf94020e.herokuapp.com/](https://clr-counsel-eeabdf94020e.herokuapp.com/)

## CONTENTS

- [CONTENTS](#contents)
  - [Site Objectives](#site-objectives)
- [User Experience/UX](#user-experienceux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
    - [New Visitor Goals](#new-visitor-goals)
    - [Existing Visitor Goals](#existing-visitor-goals)
- [Design Choices](#design-choices)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Logo and Favicon](#logo-and-favicon)
  - [Wireframes](#wireframes)
  - [Database Plan](#database-plan)
- [Features](#features)
  - [Future Features](#future-features)
  - [Features Not Included](#features-not-included)
- [Technologies Used](#technologies-used)
- [Programming Languages, Frameworks and Libraries Used](#programming-languages-frameworks-and-libraries-used)
- [Agile](#agile)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [User](#user)
  - [Bugs](#bugs)
  - [Lighthouse](#lighthouse)
  - [Validation Testing](#validation-testing)
    - [HTML \& CSS](#html--css)
  - [Python Testing](#python-testing)
  - [Deployment](#deployment)
    - [Github Deployment](#github-deployment)
    - [Creating a Fork or Copying](#creating-a-fork-or-copying)
    - [Clone](#clone)
    - [Repository deployment via Heroku](#repository-deployment-via-heroku)
    - [Deployment of the app](#deployment-of-the-app)
  - [Credits](#credits)
  - [Media](#media)
  - [Acknowledgments and Thanks](#acknowledgments-and-thanks)

___

## Site Objectives

Design and create a patient diary that keeps a single point of record while someone is getting 1-2-1 help from a counselor.

My three main objectives were:

- ### Create a readable, clean and responsive front end

  I wanted to make the site easily accessible and intuitively navigated for the users. Django and Bootstrap were used to create and style the front end.

- ### Make use of available backend functionality

  The use of the backend framework allows users to create a profile, creating diary entries and going back to read them later 

- ### Store data on an external cloud database

  I used ElephantSQL to store the PostgreSQL database for this project.

___

# User Experience/UX

## Target Audience

- Patients going through counselling sessions

## User Stories

### New Visitor Goals

- I want patients to be able browse available counsellors to select one they may wish to use for treatment

### Existing Visitor Goals

- have a quick log in process to create and update their diary entries to later show to their counsellors
___

# Design Choices

## Colour Scheme

I used coolors.co to generate the colour scheme, I drew inspiration from other clinical sites such as local dentists and GP's. This I felt would look clean and professional to any site visitors.

<div align="center">
  <img src="./Readme/Images/Clr-Counsel pallette.png">
</div>

## Typography

Work Sans was selected for a clear and no frills look. This is hosted by Google Fonts.

## Logo and Favicon

The logo was created using chatGPT and Bing. I initially used chatGPT to generate a list of common counselling imagery and then selected several options to put into Bings image generator, i then selected one and took out the couch element and edited it in paint to put it in front of a circle of my choosing.

<div align="center">
  <img src="./Readme/Images/clr-logo.png">
</div>

## Wireframes

- Mobile Homepage Wireframe

![Mobile Homepage Wireframe]()

- Mobile Post Detail Wireframe

![Mobile Post Detail Wireframe]()

- Desktop Homepage Wireframe

![Desktop Homepage Wireframe]()

- Desktop Post Detail Wireframe

![Desktop Post Detail Wireframe]()


## Database Plan

The database plan is fairly simple, but it shows the information that is stored within the database, the type of data and if it is logged as a Primary or Foreign key where applicable.

![Database plan](documentation/diagrams/database_plan.png)

# Features

## Future Features

- 

## Features Not Included

- 

___

# Technologies Used

Here are the technologies used to build this project:

- [Github](https://github.com) To host and store the data for the site.
- [PEP8 Validator](https://pep8ci.herokuapp.com/) Used to check python code for errors
- [ElephandSQL](https://www.elephantsql.com/) Used to store PostgreSQL database.
- [Cloudinary](https://cloudinary.com/) Used as cloud storage for images uploaded as part of the blog posts
- [Heroku](https://id.heroku.com/) Used to deploy the project

# Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

# Agile

This project was designed using Agile methodology, utilising the Project Board and Issues sections in GitHub

- [Project Board](https://github.com/users/caleom/projects/6/views/1)

# Testing

As each section or Function/Model was built during this project, I was testing for functionality and styling issues that may have arisen (see table below), which were corrected or fixed before continuing. I also had friends test the site by signing up, adding and deleting comments using various devices on varying platforms (IOS, Android, Mobile, Tablet etc) and reporting back any issues they encountered with functionality or styling.

## Manual Testing

*For any Fails, there is a more detailed description below the table*

ADMIN
| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Blog Post | Post successfully created and displayed | Pass |
| Edit Blog Post | Error thrown when editing post title & slug (*) | FAIL |
| Edit Blog Post (after fix) | Post content and category updated successfully | Pass |
| Delete User Comments | Comment deleted successfully | Pass |
| Delete Blog Post | Post deleted successfully | Pass |
| Create 7 Test Posts to check Pagination | Next/Previous Page Appears at bottom of screen | Pass |

(*) - While testing the ability to edit posts (Limited to Admin only), I had a problem when editing the title and slug of the post. This was due to the URL not being able to find the original slug of the post (because it had been changed during the edit) to route it after the editing was complete. At this stage, I felt the easiest fix was to remove the ability to edit the post title and slug in the browser, but this functionality is still available via the django admin panel.

## User

| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Account | Created successfully | Pass |
| Error Check - Error page when signing up with email address | Unable to replicate(*) | Closed |
| Login | Login Successful | Pass |
| Logout | Logout Successful | Pass |
| Read Full Blog Post | PostDetail page loaded successfully | Pass |
| Add Comment under Blogpost | Comment Added Successfully | Pass |
| Delete Comment | Comment Deleted | Pass |
| Filter Posts by category | Posts marked as selected category displayed successfully | Pass |
| Create User Account to check access to restricted pages (add_post, add_category)| Page displayed correct error message, with no access to restricted content | Pass |

(*) See Bugs below

## Bugs



## Lighthouse

The performance scores appear to be low, and I believe this is due to the images uploaded for each blog post being hosted on a third-party cloud-based platform.

Mobile

![Lighthouse Mobile Score](documentation/images/lighthouse_mobile.png)

Desktop

![Lighthouse Desktop Score](documentation/images/lighthouse_desktop.png)

## Validation Testing

### HTML & CSS

HTML & CSS testing was completed using [W3 Validator](https://validator.w3.org/)

![HTML Validation - Descendant Error]()

Fixed:

![HTML Validation Complete- base.html]()

## Python Testing

Python pep8 validation was done via [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)

The only errors recieved here were where some lines of text exceeded the limit of 79 characters, but these have now been rectified.

Python Files Tested:

- models
- forms
- views
- urls

___

## Deployment

### Github Deployment

The website was stored using GitHub for storage of data and version control. To do this I did the following;

After each addition, change or removal of code, in the terminal within your IDE type:

- git add .
- git commit -m "meaningful commit message"
- git push

The files are now available to view within your github repository.

### Creating a Fork or Copying

To clone/fork/copy the repository you click on the fork tab which is situated next to unwatch tab in the top right corner of the page

### Clone

To create a clone you do the following;

1. Click on the code tab, left of the Gitpod tab
2. To the right of the repository name, click the clipboard icon
3. In the IED open GitBash
4. Change the working directory to the location you prefer
5. Add Git Clone with the copy of the repository name
6. Clone has been created

### Repository deployment via Heroku

- On the [Heroku Dashboard](https://dashboard.heroku.com) page, click New and then select Create New App from the drop-down menu.
- When the next page loads insert the App name and Choose a region. Then click 'Create app'
- In the settings tab click on Reveal Config Vars and add the key Port and the value 8000. The credentials for this app were:

1. Cloudinary URL
2. Postgres Database URL
3. Port (8000)

- Below this click Add buildpack and choose python and nodejs in that order.

### Deployment of the app

- Click on the Deploy tab and select Github-Connect to Github.
- Enter the repository name and click Search.
- Choose the repository that holds the correct files and click Connect.
- A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub.
- Once the deployment method has been chosen the app will be built and can be launched by clicking the Open app button which should appear below the build information window, alternatively, there is another button located in the top right of the page.

___

## Credits


___

## Media



___

## Acknowledgments and Thanks

