# Infograins

Task -

- 1. The product can have the following fields --> name, product code,
price, category, manufacture date, expiry date, product owner

- Include Basic user registration and login functionality

- 2. Category can be a subcategory of other categories & possibly number
of depth.

- 3. Create a basic UI for superuser to perform CRUD on Product- with
search and filter by category or any other product attribute

- 4. Create a basic UI for superuser to perform CRUD for Category- with
search and filter category name and

- 5. Create Basic UI to list out all the Products and Categories for
end-user (Separate Menus for Product and Category)

- The only owner of the product can update/delete the product
if other users try to update show proper message

- Owners can only change the price of the product Once per day
before 11:00 AM (show proper validation message)

- Admin should be able to know when the product is created and
when it is updated (date and time) - only for the Django admin panel

- In the admin Panel add a filter and search with all details
in the display

- 6. You have to use Django rest framework for writing API for Category
and Product both (send postman collection link)

# Completed Task
1 . Create Models for Product Where i have used Many to Many field for Category

2 . Basic Registration and login functionality where i have manage the url(to not go back to same /registration or /login when you are already logged in) after login using decorators

3 . For Category Model i have used Category and owner field

4 . Created CRUD for product and categories and use js datatable for showing the data in table tag and there is one more button below table tag you can explore the django-filter also

5 . Seperate the section(sidebar) of product and categories to show all data and add a basic paginator for both section

6 . Only Owner can change the value of their product and manage return HttpResponse(You can't access this page because that object is created by other superuser)

7 . After 11AM i have showed the message above table(YOU CAN'T CHANGE THE PRICE OF PRODUCT AFTER 11AM)

8 . Django admin panel : I have used Monitorlog on admin file to manage logs

9 . Add search and filters functionality on admin section

10 . Created API Using DRF I have used APIView Class


