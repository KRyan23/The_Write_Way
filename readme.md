<h1 align="center">The Write Way</h1>

- [View the live project here ](https://the-write-way.herokuapp.com/)
<p align="center">The Write Way is a service that allows budding authors to submit and share short stories.</p>

<p align="center">The stories are accessible to casual readers as well as other writers.</p>


&nbsp;
&nbsp;

<p align="center">
  <img width="30%" height="30%" src="/assets/images/the_write_way_front_page.png">
</p>


----
## User Experience
----

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I would like to browse the sites content without signing up or logging in.
        
    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I would like create my own login profile to allow me create content.
        2. As a Returning Visitor, I would like to easily connect with the sites social media channels.
        

    -   #### Frequent User Goals
        
        1. As a Frequent Visitor, I would like create another short story.
        2. As a Frequent Visitor, I would like read back over one of my recently added short stories.
        3. As a Frequent Visitor, I would like edit one of my recently added short stories.
        4. As a Frequent Visitor, I would like remove one of my recently added short stories.

-   ### Design
    -   #### Colour Scheme
        -   The colour palette used for the site is listed below.
            - ![#59A52C](https://via.placeholder.com/15/59A52C/000000?text=+) `Green Transistion`
            - ![#0F0F0F](https://via.placeholder.com/15/0F0F0F/000000?text=+) `Black Transistion`
            - ![#FFFFFF](https://via.placeholder.com/15/FFFFFF/000000?text=+) `White`
            - ![#6FCA3A](https://via.placeholder.com/15/6FCA3A/000000?text=+) `Light Green Transistion`
            - ![#437D21](https://via.placeholder.com/15/437D21/000000?text=+) `Dark Green Transistion`
            - ![#282828](https://via.placeholder.com/15/282828/000000?text=+) `Charcoal Transistion`
            
    -   #### Typography
        -   The 'SOMETHING OR OTHER' font is used as the main font used throughout the site with Sans Serif as the fall-back font. 'SOMETHING OR OTHER' was chosen to enhance the sites content by giving a 'Top Secret' / 'Spy' feel.

    -   #### Imagery
        - The imagery of the website was chosen to convey a functional feel to fit in with the overall Spy theme.


*   ### Wireframes

    - Desktop Wireframes - [View here](/assets/docs/TheWriteWay-Desktop&SiteMap.pdf)
    - Tablet Wireframes - [View here](/assets/docs/TheWriteWay-Tablet&SiteMap.pdf)
    - Mobile Wireframes - [View here](/assets/docs/TheWriteWay-Mobile&SiteMap.pdf)


    *   ### Screenshots

        - [View here](/assets/docs/screenshots.pdf)


## Features

-   Responsive on all device sizes

-   Interactive elements

-   Create Your Own login

-   CRUD functionality for valid users

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [MongoDb](https://en.wikipedia.org/wiki/MongoDB)
-   [Heroku](https://en.wikipedia.org/wiki/Heroku)


### Frameworks, Libraries & Programs Used

1. [Materialize:](https://materializecss.com/)
    - Materialize instead of Bootstrap was used on this project to assist with the responsiveness and styling of the website.
2. [JQuery:](https://code.jquery.com/)
    - Some JQuery was used to simplify frontend deployment.  
3. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the "Saria Stencil One" font into the style.css file which is used on all pages throughout the site.
4. [Font Awesome v5.15.4:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
5. [Git](https://git-scm.com/)
    - Git was used for version control to push to GitHub.
6. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
7. [GitPod](https://www.gitpod.io/)
    - GitPod was used as the main development platform, this was linked to my GitHub repository.
8. [Paint.net:](https://www.getpaint.net/doc/latest/index.html)
    - Paint.net was used for resizing images and editing photos for the website.
9. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq 4.2.1 was used to create the WireFraming during the design process.


## Testing

The W3C Mark-up Validator and W3C CSS Jigsaw Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Mark-up Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](/assets/docs/Html-Css-results.pdf)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](/assets/docs/Html-Css-results.pdf)
-   [JSHint ](https://jshint.com/) - [Results](/assets/docs/JSHint.pdf)


### Testing User Stories from User Experience Section

### Users Stories
-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site.

        1. Upon landing on the main page users are greeted with a clean site whose imagery and text convey a message that the sites primary goal revolves around writing and storytelling.
        

    2. As a First Time Visitor, I would like to browse the sites content without signing up or logging in.

        1. The site has been designed to give a good and unimpeded flow from start to end.
        2. The sites categories and most of its content are freely availible to unregistered users. 


    
-   #### Returning Visitor Goals

    1. As a Returning Visitor, I would like create my own login profile to allow me create content.

        1. A returning visitor to the site can choose the 'Signup' button or 'Login' from the main navigation menu. From here they are invited to complete the signup process.

    
    2. As a Returning Visitor, I would like to easily connect with the sites social media channels.

        1. A returning visitor can use the social media links at the bottom of the page to connect with a larger audience.

-   #### Frequent User Goals

    1. As a Frequent Visitor, I would like create another short story.

        1. The user first needs a valid logon. Once logged in they can go to their profile page and choose the 'Create New' button. They then shoose a category for their story along with a public or private setting, lastly when they are finshed writing, they can submit the short story by clicking the 'Submit' button. 
        
    2. As a Frequent Visitor, I would like read back over one of my recently added short stories.

        1. The user in this case can be either logged in or not. From here they can browse the caterogries and find their story, or if they do login they cna view their work from within the profile.

    3. As a Frequent Visitor, I would like edit one of my recently added short stories.

        1. The user will need to be logged in for this task also, once logged in they can go to their profile page, locate the peice of work that there interested in changing and choose the edit function, once happy with the changes they can click the 'Submit' button.
    
    4. As a Frequent Visitor, I would like remove one of my recently added short stories.

        1. The user again will need to be logged in for this task. From here they can go to their profile page, locate the peice of work that there interested in and choose the delete button to remove it.
        
### Further Testing

-   The Website was tested on Google Chrome, Opera, Internet Explorer 11, Microsoft Edge and Firefox browsers.
- The website was continually checked on a variety of emulated devices under Chromes Developer tools, these included Desktop, Moto4, GalaxyS5, Pixel, IPhones5,6,7,8,X, IPad/Pro and the Surface Duo.
-   Internal and external linking were continually tested throughout the project to ensure functionality.
-   Family members were asked to review the site and to give their initial thoughts and feedback. Their input was used to make small design changes to all 3 games.

### Known Bugs

-  [Results](/assets/docs/known-bugs.pdf)

## Deployment
&nbsp;

The project was deployed using the steps below.


### MongoDb

[Steps to setup MongoDb](assets/docs/setting_up_mongo_db.pdf)

### GitHub

[Steps to setup GitHub](assets/docs/github-setup-and-instructions.pdf)

### GitPod

[Steps to setup GitPod](assets/docs/setting_up_gitpod.pdf)

### Heroku

[Steps to deploy to Heroku](assets/docs/deploying_to_heroku.pdf)



## Credits

### Code

- All code written by myself except for .....


### Content

-   Privacy Policy - Some of the privacy policy was borrowed from [this link](https://www.booksie.com/member/privacy-policy) to save time on the project. 
-   The remaining content was written by myself with some minor contributions by family and friends.

&nbsp;
# README DONE TO HERE !
### Media




Images

The images on the index page were chosen from the following sources.

[1 - Big Red Button A](https://pixabay.com/photos/button-light-bright-symbol-icon-2816448/)

[2 - ]()

[3 -  ]()

[4 - ]()

[5 - ]()

The images on the 'X' page were chosen from the following sources.

[1 - Big Red Button A](https://pixabay.com/photos/button-light-bright-symbol-icon-2816448/)

[2 - ]()

[3 - ]()

[4 - ]()

[5 - ]()

The images on the 'X' page were chosen from the following sources.

[1 - Big Red Button A](https://pixabay.com/photos/button-light-bright-symbol-icon-2816448/)

[2 - ]()

[3 - ]()

[4 - ]()

[5 - ]()

The images on the 'X' page were chosen from the following sources.

[1 - Big Red Button A](https://pixabay.com/photos/button-light-bright-symbol-icon-2816448/)

[2 - ]()

[3 - ]()

[4 - ]()

[5 - ]()

### Acknowledgements
- My Mentor
- Friends and family for input and site testing.
