
# DuckWiki
A Wikipedia-like online encyclopedia.


![Alt text](https://res.cloudinary.com/ddhxwfbaj/image/upload/v1711272037/Duckwiki1.png)

![Alt text](https://res.cloudinary.com/ddhxwfbaj/image/upload/v1711271987/Duckwiki2.png)


## Specifications

1.  **Entry Page:** Ensure that visiting "/wiki/TITLE" displays the content of the corresponding encyclopedia entry. Utilize the appropriate function to retrieve entry content. Display an error page if the requested entry does not exist.
2.  **Index Page:** Update "index.html" to allow users to click on entry names and be directed to the respective entry pages.
3.  **Search:** Implement a search feature in the sidebar, enabling users to search for encyclopedia entries. If a query matches an entry name, redirect the user to that entry page. If not, display a search results page listing entries containing the query substring.
4.  **New Page:** Enable users to create new encyclopedia entries by clicking "Create New Page" in the sidebar. Users should provide a title and Markdown content for the new page. Display an error message if an entry with the same title already exists. Otherwise, save the new entry and redirect the user to its page.
5.  **Edit Page:** Allow users to edit existing entry content by providing a link on each entry page. Display the existing content in a textarea for editing. Upon saving changes, redirect the user back to the entry page.
6.  **Random Page:** Implement a "Random Page" feature in the sidebar, redirecting users to a random encyclopedia entry.
7.  **Markdown to HTML Conversion:** Convert Markdown content to HTML before displaying it on each entry page. Use the python-markdown2 package for conversion or implement conversion without external libraries, supporting headings, boldface text, unordered lists, links, and paragraphs.



## Requirements to run the code

* Install python and pip.

* After pip was installed, run

``` python -m pip install Django ``` 
``` pip3 install markdown2``` 

* In the root folder, execute

``` python manage.py runserver``` 



## Demo Link

https://www.youtube.com/watch?v=3O1qVW5HYmE
