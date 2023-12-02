# TravelerView API in DRF

**Developer: Mustafa Habet**

[Live link](https://traveler-view-90e3792ff7f0.herokuapp.com/)

This repository contains the API set up using Django REST Framework for the TravelerView front-end application ([repostiory link]
(enter link here) and [Live Link](enter link here))

## Table of Contents
- [User Stories](#user-stories)
- [Database](#database)
- [Technologies Used](#technologies-used)
- [Validation](#validation)
- [Testing](#testing)
- [Credits](#credits)

## User Stories
The project's backend section centers on its administrative aspect and covers one user story:
- As an admin, I want to be able to create, edit and delete users, posts, comments and likes. This allows the admin to exercise control over the application's content and swiftly remove any inappropriate material.

## Database

The following models were created to represent the database model structure of the application:
<Insert Image here>


#### User Model

- The User Model contains information about the user. It is part of the Django allauth library.
- One-to-one relation with the Profile model owner field.
- ForeignKey relation with the Follower model owner and followed fields.
- ForeignKey relation with the Post model owner field.
- ForeignKey relation with the Comment model owner field.
- ForeignKey relation with the Like model owner field.

#### Profile Model

- The Profile Model contains the following fields: owner, name, description, created_on, updated_on and image.
- One-to-one relation between the owner field and the User Model ID field.

#### Post Model

- The Post model contains the following fields: owner, created_on, updated_on, title, description, country and image.
- ForeignKey relation with the Comment Model post field.
- ForeignKey relation with the Like Model post field.

#### Follower Model

- The Follower Model contains the following fields: owner, followed and created_on.
- ForeignKey relation between the owner field and the User Model id field.
- ForeignKey relation between the followed field and the User Model post field.

#### Comment Model

- The Comment Model contains the following fields: owner, post, created_on, updated_on and content.
- ForeignKey relation between the owner field and the User Model ID field.
- ForeignKey relation between the post field and the User Model post field.

#### Like Model

- The Like Model contains the following fields: owner, post and created_on
- ForeignKey relation between to the User Model ID field
- ForeignKey relation between the owner field and the User Model ID field
- ForeignKey relation between the post field and the Post Model post field

## Technologies Used

### Language & Frameworks

### Libraries & Tools

## Validation

## Testing

### Manual Testing

### Automated Testing

## Credits

### Images

### Code