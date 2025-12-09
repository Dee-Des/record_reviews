# RecordReviews
### By Denise Desmond

live site - https://capstone-project-recordreviews-5a6a26926cda.herokuapp.com/

project board - https://github.com/users/Dee-Des/projects/11

![Website landing page](/documentation/RecordReviews%20-%20landing-page.png)

## Index
1. [Overview](#overview)
2. [UX Design Process](#ux-design-process)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [ERD](#erd)
    - [Color Schemes](#color-schemes)
    - [Fonts](#fonts)
3. [Features](#features)
4. [Improvements](#improvments-and-future-development)
5. [Deployment](#deployment)
6. [Testing and Validation](#testing-and-validation)
7. [AI implementation](#ai-implementation)
8. [Database](#database)
9. [References](#references)
10. [Tech used](#tech-used)
11. [Learning points](#learning-points)

## Overview

A website built using Django which allows users to share and review vinyl records.

## UX Design Process
<details>

project board - https://github.com/users/Dee-Des/projects/11/views/1

### User stories
<details>
Must Haves

- As a Site User I can view a paginated list of records so that I can select which record I want to view (Must Have)
- As a Site User I can click on a record so that I can read the full text (Must Have)
- As a Site User/Admin I can view reviews on an individual record So that I can read the conversation (Must Have)
- As a Site User I can register an account so that I can review a record (Must Have)
- As a Site User I can leave reviews on a record so that I can be involved in the conversation (Must Have)
- As a Site User I can modify or delete my review on a record so that I can be involved in the conversation (Must Have)
- As a Site Admin I can create, read, update and delete records so that I can manage my record content (Must Have)
- As a Site Admin I can create draft records so that I can finish writing the content later (Must Have)
- As a Site Admin I can approve or disapprove reviews so that I can filter out objectionable reviews (Must Have)

Should Haves

- As a Site User I can click on the About link so that I can read about the site (Should Have)
- As a Site Admin I can create or update the about page content so that it is available on the site (Should Have)

Could Haves

- As a Site User I can fill in a contact request form so that I can submit a request for contact (Could Have)
- As a Site Admin I can store contact requests in the database so that I can review them (Could Have)
- As a Site Admin I can mark contact requests as "read" so that I can see how many I still need to process (Could Have)
</details>

### Wireframes

<details>

Home Page

![home page wireframes](/documentation/wireframes/home_page/mobile-tablet-and-desktop.png)

Join Page
![join page wireframes](/documentation/wireframes/join_page/mobile-tablet-and-desktop.png)

Login Page
![login page wireframes](/documentation/wireframes/login_page/mobile-tablet-and-desktop.png)

Logout Page
![logout page wireframes](/documentation/wireframes/logout_page/mobile-tablet-and-desktop.png)
</details>

### Color schemes

<details>

![color schemes](/documentation/color_schemes/color-schemes.png)
</details>

### Fonts

<details>
For the fonts I used sans‑serif fonts
</details>
</details>


## Features

<details>
Key features of the website include:

📋 Project Features by Webpage

🏠 Home Page (/)	
- Responsive Bootstrap layout with grid system
- Navbar with links: Home, Register, Login/Logout
- Paginated record listings (title, author, featured image, excerpt)
- Each record card links to its detail page
- Footer with social media links (Facebook, Twitter, Instagram, YouTube)

📑 Paginated Listings (/?page=2, /?page=3, …)	
- Continuation of record listings with pagination controls
- Same layout and features as Home Page
- Ensures scalability for large record collections

🎼 Record Detail Page (//)	
- Full record information: title, artist, genre, year, record label, content
- Featured image (via Cloudinary)
- Author attribution (user who created the record)
- Reviews section: reviewer name, body, timestamp
- Review form (visible to logged‑in users)
- Review moderation: reviews require admin approval before appearing

🔐 Register Page (/accounts/signup/)
- User registration form with Bootstrap styling
- Validation messages for incorrect or missing input
- Creates new user accounts stored in Postgres

🔑 Login Page (/accounts/login/)	
- Login form with username and password fields
- Error messages for invalid credentials
- Redirects to Home Page after successful login

🚪 Logout Page (/accounts/logout/)	
- Logs out the user
- Displays confirmation message
- Navbar updates to show “You are not logged in.”

⚙️ Admin Dashboard (/admin/)	
- Authentication required (staff/superuser only)
- Manage Record model: create, edit, delete records; set status (Draft/Published)
- Manage Review model: approve/disapprove reviews, edit/delete reviews
- Manage User model: assign staff/superuser permissions
- Built‑in search and filters
- Full CRUD operations for all models

✨ Technical Features include

- Bootstrap integration for responsive design
- Cloudinary for image hosting
- Postgres database for records, reviews, and users
- Django models (Record, Review) with relationships
- Pagination for record listings

</details>


## Improvements and Future Developement

<details>
In my future enhancements I would add in the full scope as mentioned in the UX Design Process section of this README document. This would include the Should Have and Could Have User Stories mentioned in this README document.


</details>

## Testing and Validation

<details>

### HTML Validation

Home page
![home page](/documentation/validation/html/home_page/home-page.png)

Home page - page 2

![home page page 2](/documentation/validation/html/home_page/home-page-page-2.png) 

Record details page with reviews

![record details and reviews page](/documentation/validation/html/record_details_and_reviews_page/record-details-and-reviews-page.png)

### CSS Validation

![css validation](/documentation/validation/css/css-validation.png)

### Python Validation

admin.py

![admin.py](/documentation/validation/python/admin.py.png)

apps.py
![apps.py](/documentation/validation/python/apps.py.png)

forms.py
![forms.py](/documentation/validation/python/forms.py.png)

models.py - Alot of lines of code so I took two screenshots to try capture it all in the Linter

![models.py - 1st screenshot](/documentation/validation/python/models.py%20-%201st%20screenshot.png)

![models.py - 2nd screenshot](/documentation/validation/python/models.py%20-%202nd%20screenshot.png)

urls.py - one file in record and one in record_reviews

![urls.py - record](/documentation/validation/python/record%20urls.py.png)

![urls.py - record_reviews](/documentation/validation/python/record_reviews%20urls.py.png)

views.py - Alot of lines of code so I took three screenshots to try capture it all in the Linter

![views.py - 1st screenshot](/documentation/validation/python/views.py%20-%201st%20screenshot.png)

![views.py - 2nd screenshot](/documentation/validation/python/view.py%20-%202nd%20screenshot.png)

![views.py - 3rd screenshot](/documentation/validation/python/views.py%20-%203rd%20screenshot.png)


### JS Validation

No errors were displayed in JSHint - only warnings which could be ignored.

![js validation](/documentation/validation/js/js-validation.png)


### Lighthouse

Home Page

![lighthouse validation home page](/documentation/validation/lighthouse/home-page.png)

Home Page - page 2

![lighthouse validation home page - page 2](/documentation/validation/lighthouse/home-page-page-2.png)

Record Details page with Reviews

![lighthouse validation record details page with reviews](/documentation/validation/lighthouse/record-details-page-with-reviews.png)

### Testing

</details>


</details>

## AI Implementation

<details>

### Code Creation


### Debugging


### Performance and Experience


### Development Process

</details>

## Database
<details>
The database is a Postgres database hosted by Code Insitute.


###      table


###     table
</details>

## References
<details>

</details>

## Tech
<details>
- CSS
- HTML
- Django
- Bootstrap
- Copilot
- Postgres
</details>

## Learning Points

<details>
</details>







