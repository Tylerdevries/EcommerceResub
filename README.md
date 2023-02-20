# From Nepal to Ireland

This is the final resubmission of this project.

This repository houses an augmented version with changes made to failed criteria. 

No changes were made to passed criteria. 

The goal of this site is to advertise and sell products stocked in Nepal.

Users of this site will be able to register for site. Once registered they can add items to their cart and buy items through a checkout with a third party payment processor. 

The site is targeting towards use for individuals who are from nepal and living in Ireland (the currency bring used is Rs) or users looking buy items at a discount as their are coming from nepalese suppliers.

![home page](https://user-images.githubusercontent.com/93283135/220038835-1f0921d4-718f-44da-8422-f9a69009a41a.PNG)




## Features:


### General Navigation:

I Designed the site with UX in mind.

Users are initially directed to the home page where they can browse the items being sold.

They can access more information in regards to each item by clicking on the names of the products.

Users can add items from cart without going into the detail.

Users can access the categories, cart, account tabs from here.


![login](https://user-images.githubusercontent.com/93283135/220040267-c767d2e3-ff5e-46a1-81d7-94c2c2226b91.PNG)
![register](https://user-images.githubusercontent.com/93283135/220040276-8e1e79a1-20a4-43e5-bb03-01be48849dd1.PNG)


![loginview](https://user-images.githubusercontent.com/93283135/220040760-486a9808-2046-4a41-9395-66623a8ada73.PNG)
![regisview](https://user-images.githubusercontent.com/93283135/220040801-0913fc37-2c64-454f-8b14-795baa73b870.PNG)


### The Login and Register Pages:

The login page first appears, if the user doesnt have an account they prompted to register.

It asks the user for a username and password. Djangos built in class for login authorization will validate the information given through the database.

Below the login button, users can register for the app by follow the link titled register. 

A screenshot of the view for this page is shown above. This view is called on within the urls.py file.

When taken to the register page the user can sign up for the app.

Upon sign up completion the user is redirected to the home page.

The view used here is displayed above. This confirms authorisation and adds the user to the database. 

This view is called on within the urls.py.

![search](https://user-images.githubusercontent.com/93283135/220043188-652ff420-8c8c-49d8-9ec4-462dd790a6e5.PNG)

![search result](https://user-images.githubusercontent.com/93283135/220043196-ac86d136-6298-42bc-a59f-c9a0ed142b2f.PNG)


### The Search bar:

The search bar searches through all the products by name and gives a result on a seperate page.

![cart view](https://user-images.githubusercontent.com/93283135/220043492-63dda8ca-9c1b-4eec-b0d3-d01f4694c176.PNG)
![checkout view](https://user-images.githubusercontent.com/93283135/220043517-933ace83-288a-4249-995d-6e8b86c7be76.PNG)
![khalti](https://user-images.githubusercontent.com/93283135/220043528-41fd5dd6-0e23-4b86-b9a8-7901fed96a8c.PNG)
![cart![cart](https://user-images.githubusercontent.com/93283135/220044164-c661dc07-9116-4790-9cfd-ff525bfe5c71.png)
](ht![cart order](https://user-images.githubusercontent.com/93283135/220043621-abef793f-ce90-4ea9-9726-cf9e888ded19.PNG)

Here the user can access the items added to the cart.

They can empty the cart with one button.

They also change individual using CRUD functionality. They add anohter of an item. Take an item away or delete an item entirely from their cart.

They can put in their detail in the order summary to the right and choose either cash on delivery or use the khalti gateway.

When moving to checkout the user can see a total of their order.

Above is the view for the functioning of these pages.

This view is called on within the urls.py file.

![categories](https://user-images.githubusercontent.com/93283135/220044671-b88dd946-c223-4bab-8545-784bcafd7952.PNG)

![categories view](https://user-images.githubusercontent.com/93283135/220044681-cf639a62-2abf-465a-a2f8-59233c61fb99.PNG)


### The Categories Page:

This is the page where all the items are.

The items are categorised here.

Above is the view for the functioning of this page.

![profile](https://user-images.githubusercontent.com/93283135/220045739-956dff2f-f9be-499e-875b-9533f3921a79.PNG)

![profile view](https://user-images.githubusercontent.com/93283135/220045169-01de10b8-1a28-44e5-88fe-2e9fb7af2b5f.PNG)




### Profile: 

The profile page is accessible when the user is logged in.

Here the user can view their unique detailed user information and previous orders.

It shows detailed info in regard to previous orders.

Above is the views for the functioning of these pages.


## Major Errors in Development

### Solved Bugs

An initial issue I ran into with working with the most recent build of django was a crsf token issue when loading the homepage.

I fixed this by amending the setting.py file and adding CSRF_TRUSTED_ORIGINS = [
    (https://fromnepaltoireland.herokuapp.com)
]

I also ran into an issue when deploying my app to heroku. The issue was that the push to heroku main would failed due to using the newest version of pyhton.

I solved this by using a runtime.txt file to change it to an earlier version when deploying.

I also reverted to python-3.9.14 to solve this issue. 

### Unfixed Bugs

No unfixed bugs

## Deployment

The site was deployed through Heroku. 

I used the following steps to deploy my page:
1. Installed Psycopg2.
2. I installed gunicorn and dj-database-url.
3. I logged into my installed heroku within the repo terminal.
4. I created a new heroku app linking the repo to my heroku account.
5. I created a new ElephantSQL Database and linked it and cloudinary to my repo for use.
6. I pushed all these changes to github and made my first deployment to heroku
7. Created the Environment Variables within setting.py and env.py, gitpod workspaces and heroku.
8. Hid the SECRET_KEY

The livelink can be found here https://fromnepaltoireland.herokuapp.com/

## Credits

The prior walkthrough in this module of the course. 

I used the following sites as sources and tutorials for django components.

https://stackoverflow.com/

https://ccbv.co.uk/projects/Django/4.0/

