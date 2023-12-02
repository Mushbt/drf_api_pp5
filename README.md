# TravelerViews API in DRF

**Developer: Mustafa Habet**

[Live link](https://traveler-view-90e3792ff7f0.herokuapp.com/)

This repository contains the API set up using Django REST Framework for the TravelerViews front-end application ([repostiory link]
(enter link here) and [Live Link](enter link here))
<hr>

## Table of Contents
- [User Stories](#user-stories)
- [Database](#database)
- [Technologies Used](#technologies-used)
- [Validation](#validation)
- [Testing](#testing)
- [Credits](#credits)
<hr>

## User Stories
The project's backend section centers on its administrative aspect and covers one user story:
- As an admin, I want to be able to create, edit and delete users, posts, comments and likes. This allows the admin to exercise control over the application's content and swiftly remove any inappropriate material.
<hr>

## Database

The following models were created to represent the database model structure of the application:
<Insert Image here>
<hr>


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

- The Like Model contains the following fields: owner, post and created_on.
- ForeignKey relation between to the User Model ID field.
- ForeignKey relation between the owner field and the User Model ID field.
- ForeignKey relation between the post field and the Post Model post field.

## Technologies Used

### Language & Frameworks

- Python
- Django

### Libraries & Tools

- [APITestCase](https://www.django-rest-framework.org/api-guide/testing/) - Django Rest Framework APITestCase was used for automated testing.
- [Cloudinary](https://cloudinary.com/) to store static files.
- [Dbdiagram.io](https://dbdiagram.io/home) used for the database schema diagram.
- [GitHub](https://github.com/) was used as a remote repository to store project code.
- [Gitpod)](https://gitpod.io/workspaces) - a virtual IDE workspace used to build this site.
- [Heroku](https://Heroku.com) was used to deploy the project into live environment.
- [Django REST Framework](https://www.django-rest-framework.org/) was used to build the back-end API.
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for user authentication.
- [Pillow](https://pillow.readthedocs.io/en/stable/) was used for image processing and validation.
- [Psycopg2](https://www.psycopg.org/docs/) was used as a PostgreSQL database adapter for Python.
- [ElephantSQL](https://www.elephantsql.com//) – This was used as the deployed project on Heroku uses an ElephantSQL database.

## Validation

### PEP8 Validation
[PEP8CI](https://pep8ci.herokuapp.com/) Validation Service was used to check the code for PEP8 requirements. All the code passes with no errors or warnings.

## Testing
The following tests were carried out on the app:
1. Manual testing
2. Automated testing

### Manual Testing

- As an admin, I want to be able to create, edit and delete users, posts, comments and likes. This allows the admin to exercise control over the application's content and swiftly remove any inappropriate material.

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User | Create, update & delete user | A user can be created, edited or deleted | Works as expected
User | Change permissions | User permissions can be updated | Works as expected
Profile | Create, update & delete | User profile can be created, edited or deleted | Works as expected
Post | Create, update & delete | A post can be created, edited or deleted | Works as expected
Comment | Create, update & delete | A comment can be created, edited or deleted | Works as expected
Like | Create & delete | A like can be created or deleted (like / unlike post) | Works as expected
Follower | Create & delete | Follow or unfollow user | Works as expected

In addition, posts, comments, likes and following can be created by logged-in users only. Users can only update or delete the content which was created by themselves.

### Automated Testing

Even though automated testing was not required for this project, I decided to go ahead with it and I can say that it was a huge help! It helped me to discover a few errors in my code before I started to manually test all the different functions.

Automated testing was done using the Django Rest Framework APITestCase.

A total of 34 tests were created and they all passed.

<details><summary>Automated Testing</summary>
<img src="docs/testing/automated_testing.png">
</details>


### The automated tests that were taken are as followed:

#### Comments Testing

- Test to ensure users can't create comments if not logged in.
- Test to ensure logged in users can create comments
- Test to ensure users can retrieve existing comments
- Test to ensure non existing comments can't be retrieved
- Test to ensure users can update their own comments
- Test to ensure user can't update other user's comments
- Test to ensure user can delete their own comments
- Test to ensure users can't delete other users comments

#### Followers Testing

- Test to ensure users who are not logged in can't follow other users
- Test to ensure logged in user can follow other users
- Test to ensure user can retrieve existing following using valid ID
- Test to ensure user can not retrieve a following from a non valid ID
- Test to ensure user can unfollow other users
- Test to ensure user can not remove other users followers

#### Likes Testing

- Test to ensure users who are not logged in not able to like posts
- Test to ensure logged in users can like posts
- Test to ensure user can retrieve existing likes using valid ID
- Test to ensure user can't retrieve likes with no valid ID
- Test to ensure user can unlike a post they have liked
- Test to ensure user can't remove other users likes

##### Posts Testing

- Test to ensure logged out users can't create posts
- Test to ensure logged in users can create posts
- Test to ensure all fields are filled before uploading post
- Test to ensure users can view posts
- Test to ensure existing posts can be retrieved
- Test to ensure non existing posts can't be retrieved
- Test to ensure user can delete their own posts
- Test to ensure users can't delete other users posts

#### Profiles Testing

- Test to ensure user can view other user profiles
- Test to ensure user can not view non existing profiles
- Test to ensure user can update their own profile
- Test to ensure user can't update other users profiles
- Test to ensure users can't update their profiles if not logged in
- Test to ensure user can delete their own profile


## Credits

### Images

- User avatar default image taken from [Code Institute](https://codeinstitute.net/) Django REST Framework walkthrough.
- Default post image was taken from [Code Institute](https://codeinstitute.net/) Django REST Framework walkthrough.

### Code

This project was created based on the Code Institute's Django REST API walkthrough project. [DRF API](https://github.com/Code-Institute-Solutions/drf-api)