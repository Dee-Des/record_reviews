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
    - [Imagery](#imagery)
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

### Imagery

Images for the placeholder image on the Home Page and Paginated Pages and for the image on the Record Details with Reviews page were taken from pexels.com. User-generated images on the Home Page are taken from my own collection.

Placeholder image

![placeholder image](/documentation/imagery/placeholder-image.png)

Record Details with Reviews page image

![record details with Reviews page image](/documentation/imagery/image-on-record-details-with-reviews-page.png)

User generated images

![user generated images](/documentation/imagery/user-generated-images.png)

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
- Displays confirmation messages
- Logged in authenticated users can add, edit and delete their own reviews
- Site users can view approved reviews 
- Review moderation: reviews require admin approval before appearing

🔐 Register Page (/accounts/signup/)

- User registration form with Bootstrap styling
- Validation messages for incorrect or missing input
- Creates new user accounts stored in Postgres
- Displays confirmation message

🔑 Login Page (/accounts/login/)	

- Login form with username and password fields
- Error messages for invalid credentials
- Redirects to Home Page after successful login
- Displays confirmation message

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
- Displays confirmation messages

✨ Technical Features include:

- Bootstrap integration for responsive design
- Cloudinary for image hosting
- Postgres database for records, reviews, and users
- Django models (Record, Review) with relationships
- Pagination for record listings

</details>


## Improvements and Future Development

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

<details>

Manual Testing was carried out during the Development process and again after Deployments. Please see below Manual Testing Report which highlights key functionality testing.

# 📄 Manual Testing Report – RecordReviews Project

---

## 📌 Cover Page

**Project Title:** RecordReviews – Capstone Project  
**Author:** [Denise Desmond]  
**Date of Testing:** December 2025  
**Purpose of Testing:**  
To validate that all features of the RecordReviews project function correctly across multiple devices (Desktop and Android). Testing includes navigation, CRUD operations for Records and Reviews, authentication, permissions, access control, notifications, and non‑functional requirements (validation, responsiveness, accessibility).  

**Devices Tested:**  
- Desktop (Windows)  
- Android (Mobile)  

**Overall Result:**  
✅ All features tested successfully. Expected and actual results matched across devices.  

---

# 🧪 Consolidated Manual Testing Matrix

| **Page/Area** | **Feature** | **Test Performed** | **Expected Result** | **Actual Result** | **Devices Tested** | **Status** |
|---------------|-------------|--------------------|---------------------|-------------------|--------------------|------------|
| Home (`/`) | Navbar links | Click Home, Register, Login | Correct page loads | Correct page loads | Desktop, Android | ✅ Pass |
| Home (`/`) | Record listings | Verify records display with title, author, excerpt, image | Records visible with correct info | Records visible | Desktop, Android | ✅ Pass |
| Home (`/`) | Pagination | Click “Next” page | Loads next set of records | Records load on Page 2 | Desktop, Android | ✅ Pass |
| Home (`/`) | Footer links | Click social media icons | Redirects to external social sites | Redirects correctly | Desktop, Android | ✅ Pass |
| Paginated Listings (`/?page=2`) | Pagination continuity | Navigate between pages | Records continue to display correctly | Records display correctly | Desktop, Android | ✅ Pass |
| Record Detail (`/<id>/`) | Record info | Open record detail | Full record info displayed | Info displayed correctly | Desktop, Android | ✅ Pass |
| Record Detail (`/<id>/`) | Reviews section | View approved reviews | Reviews show reviewer, body, timestamp | Reviews display correctly | Desktop, Android | ✅ Pass |
| Record Detail (`/<id>/`) | Review form (signed in) | Submit review | Review saved, pending admin approval | Review saved, hidden until approved | Desktop, Android | ✅ Pass |
| Record Detail (`/<id>/`) | Review visibility (not signed in) | Visit record detail page while logged out | Approved reviews are visible | Reviews visible | Desktop, Android | ✅ Pass |
| Record Detail (`/<id>/`) | Review form (not signed in) | Attempt to submit review while logged out | Form not available / redirect to login | Form hidden, prompt to log in | Desktop, Android | ✅ Pass |
| Record Detail (`/<id>/`) | Review ownership – Add/Edit/Delete | User manages own review | Only own reviews editable/deletable | Works as expected | Desktop, Android | ✅ Pass |
| Record Detail (`/<id>/`) | Review ownership – Other users | Attempt to edit/delete another’s review | Permission denied | Options not visible | Desktop, Android | ✅ Pass |
| Register (`/accounts/signup/`) | Registration form | Submit valid details | Account created | Account created | Desktop, Android | ✅ Pass |
| Register (`/accounts/signup/`) | Validation | Submit invalid/missing details | Error messages displayed | Errors displayed | Desktop, Android | ✅ Pass |
| Login (`/accounts/login/`) | Login form | Enter valid credentials | User logged in, redirected to Home | Works as expected | Desktop, Android | ✅ Pass |
| Login (`/accounts/login/`) | Validation | Enter invalid credentials | Error message shown | Error shown | Desktop, Android | ✅ Pass |
| **Login (`/accounts/login/`)** | Login notification | Successful login | Confirmation message displayed | Message displayed | Desktop, Android | ✅ Pass |
| Logout (`/accounts/logout/`) | Logout action | Click logout | User logged out, confirmation shown | Works as expected | Desktop, Android | ✅ Pass |
| **Logout (`/accounts/logout/`)** | Logout notification | Successful logout | Confirmation message displayed | Message displayed | Desktop, Android | ✅ Pass |
| **Global (Navbar)** | Logged‑in state indicator | Check navbar when logged in/out | Shows “You are logged in” or “You are not logged in” | Correct state shown | Desktop, Android | ✅ Pass |
| **Templates** | HTML validation | Run templates through W3C validator | No validation errors | No errors found | Desktop | ✅ Pass |
| **CSS** | CSS validation | Run stylesheets through Jigsaw validator | No validation errors | No errors found | Desktop | ✅ Pass |
| **Global (Responsive Design)** | Responsiveness | Resize browser / test on Android | Layout adapts to screen width | Responsive across devices | Desktop, Android | ✅ Pass |
| **Global (Accessibility)** | Accessibility & performance | Test with Lighthouse/Wave | Meets minimum accessibility/performance | Requirements met | Desktop | ✅ Pass |
| **Records (Frontend Form)** | Record – Create | Logged‑in user submits record form | Record created and saved | Record created successfully | Desktop, Android | ✅ Pass |
| **Records (Frontend Form)** | Record – Create notification | After record creation | Confirmation message displayed | Message displayed | Desktop, Android | ✅ Pass |
| **Records (Frontend Form)** | Record – Edit | Logged‑in user edits own record | Changes saved and updated | Works as expected | Desktop, Android | ✅ Pass |
| **Records (Frontend Form)** | Record – Edit notification | After record edit | Confirmation message displayed | Message displayed | Desktop, Android | ✅ Pass |
| **Records (Frontend Form)** | Record – Delete | Logged‑in user deletes own record | Record removed | Works as expected | Desktop, Android | ✅ Pass |
| **Records (Frontend Form)** | Record – Delete notification | After record deletion | Confirmation message displayed | Message displayed | Desktop, Android | ✅ Pass |
| **Records (Frontend Form)** | Record manipulation (logged‑out) | Attempt to create/edit/delete while logged out | Access denied | Access denied | Desktop, Android | ✅ Pass |
| **Records (Restricted Access)** | Authorised access | Attempt to access restricted records/information | Only authorised users can access | Access correctly restricted | Desktop, Android | ✅ Pass |
| Admin (`/admin/`) | Authentication | Attempt login as non-admin | Access denied | Access denied | Desktop, Android | ✅ Pass |
| Admin (`/admin/`) | Record – Create | Add new record via admin | Record saved and visible on site | Record created successfully | Desktop, Android | ✅ Pass |
| Admin (`/admin/`) | Record – Read | View record list in admin | Records display with correct info | Records display correctly | Desktop, Android | ✅ Pass |
| Admin (`/admin/`) | Record – Update | Edit record details | Changes saved and reflected on site | Changes applied correctly | Desktop, Android | ✅ Pass |
| Admin (`/admin/`) | Record – Delete | Delete a record | Record removed from site | Record deleted successfully | Desktop, Android | ✅ Pass |
| Admin (`/admin/`) | Review – Create | Add new review via admin | Review saved and linked to record | Review created successfully | Desktop, Android | ✅ Pass |
| Admin (`/admin/`) | Review – Read | View review list in admin | Reviews display with correct info | Reviews display correctly | Desktop, Android | ✅ Pass |
| Admin (`/admin/`) | Review – Update | Edit review details | Changes saved and reflected on site | Changes applied correctly | Desktop, Android | ✅ Pass |
| Admin (`/admin/`) | Review – Delete | Delete a review | Review removed from site | Review deleted successfully | Desktop, Android | ✅ Pass |

---

# ✅ Summary

- All **functional tests** (login state, registration, authentication, CRUD for records and reviews, notifications, permissions) passed.  
- All **non‑functional tests** (HTML validation, CSS validation, responsiveness, accessibility & performance) passed.  
- Tested thoroughly on **Desktop (Windows)** and **Android mobile devices**.  
- **Status: Pass** for all features.

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







