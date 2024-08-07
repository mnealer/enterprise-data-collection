# Admin Console

All Tortoise Model classes have a method called describe, which lists the
data classes and their types.

I think I could override the __str__ to have a default on each record, but I think not. I think
the display field format should be defined when registered.

for use with an Admin panel, Admin needs to know about all the models. They will need to be imported and marked as
an admin object. When an admin page is called, it will import the Admin object with the models and use this object to
build tables. It will only be using the classes until such time as it goes into a given model.

The side menu, create new pages etc can be cached using the lru if the are fetched from a function

ok, we need to build pages, but we can't cache whole pages. The Side menu is one we can cache. So would
the header and footer sections. Create object pages can also be cached though they won't be used that much.
that leaves the main table view, object view and edit view. We can have functions that will create the templates
for these and have them cached. That way we can call the function and get the prebuild template, rather than having
to build the template from model formats.

Ok, need to stop and think about Mako and caching templates. We can grab templates within functions and cache
them using lru

* get the admin object and all the relevant models
* render the main page
* part of the render, render the side bar with the admin object
* part of the render, render the header
* part of the render, render the footer

* when a model is clicked.
* get the model from the Admin object
* Get a count of the number of objects in the database
* get the id and display fields for the first page
* Add in the action dropdown for delete, edit, view
* use limit() and offset() options for getting records
* First itteration, no filter or sort options
* create components for each of the field types
* pages are created by calling the components in order and passing values if required
* need read and write component
